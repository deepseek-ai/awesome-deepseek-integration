# YoMo Framework - Deepseek Provider

YoMo is an open-source LLM Function Calling Framework for building Geo-distributed AI agents. Built atop QUIC Transport Protocol and Strongly-typed Stateful Serverless architecture, makes your AI agents low-latency, reliable, secure, and easy.

## 🚀 Getting Started

Let's implement a function calling serverless `sfn-get-ip-latency`:

### Step 1. Install CLI

```bash
curl -fsSL https://get.yomo.run | sh
```

### Step 2. Start the server

Prepare the configuration as `my-agent.yaml`

```yaml
name: ai-zipper
host: 0.0.0.0
port: 9000

auth:
  type: token
  token: SECRET_TOKEN

bridge:
  ai:
    server:
      addr: 0.0.0.0:9000 ## Restful API endpoint
      provider: deepseek ## LLM API Service we will use

    providers:
      deepseek:
        api_key: <DEEPSEEK_API_KEY>
        model: deepseek-reasoner
```

Start the server:

```sh
YOMO_LOG_LEVEL=debug yomo serve -c my-agent.yaml
```

### Step 3. Write the function

First, let's define what this function do and how's the parameters required, these will be combined to prompt when invoking LLM.

```golang
type Parameter struct {
	Domain string `json:"domain" jsonschema:"description=Domain of the website,example=example.com"`
}

func Description() string {
	return `if user asks ip or network latency of a domain, you should return the result of the giving domain. try your best to dissect user expressions to infer the right domain names`
}

func InputSchema() any {
	return &Parameter{}
}
```

Create a Stateful Serverless Function to get the IP and Latency of a domain:

```golang
func Handler(ctx serverless.Context) {
	var msg Parameter
	ctx.ReadLLMArguments(&msg)

	// get ip of the domain
	ips, _ := net.LookupIP(msg.Domain)

	// get ip[0] ping latency
	pinger, _ := ping.NewPinger(ips[0].String())
	pinger.Count = 3
	pinger.Run()
	stats := pinger.Statistics()

	val := fmt.Sprintf("domain %s has ip %s with average latency %s", msg.Domain, ips[0], stats.AvgRtt)
	ctx.WriteLLMResult(val)
}

```

Finally, let's run it

```bash
$ yomo run app.go

time=2025-01-29T21:43:30.583+08:00 level=INFO msg="connected to zipper" component=StreamFunction sfn_id=B0ttNSEKLSgMjXidB11K1 sfn_name=fn-get-ip-from-domain zipper_addr=localhost:9000
time=2025-01-29T21:43:30.584+08:00 level=INFO msg="register ai function success" component=StreamFunction sfn_id=B0ttNSEKLSgMjXidB11K1 sfn_name=fn-get-ip-from-domain zipper_addr=localhost:9000 name=fn-get-ip-from-domain tag=16
```

### Done, let's have a try

```sh
$ curl -i http://127.0.0.1:9000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Compare website speed between Nike and Puma"
    }
  ],
  "stream": false
}'

HTTP/1.1 200 OK
Content-Length: 944
Connection: keep-alive
Content-Type: application/json
Date: Wed, 29 Jan 2025 13:30:14 GMT
Keep-Alive: timeout=4
Proxy-Connection: keep-alive

{
  "Content": "Based on the data provided for the domains nike.com and puma.com which include IP addresses and average latencies, we can infer the following about their website speeds:
  - Nike.com has an IP address of 13.225.183.84 with an average latency of 65.568333 milliseconds.
  - Puma.com has an IP address of 151.101.194.132 with an average latency of 54.563666 milliseconds.
  
  Comparing these latencies, Puma.com is faster than Nike.com as it has a lower average latency. 
  
  Please be aware, however, that website speed can be influenced by many factors beyond latency, such as server processing time, content size, and delivery networks among others. To get a more comprehensive understanding of website speed, you would need to consider additional metrics and possibly conductreal-time speed tests.",
  "FinishReason": "stop"
}
```

### Full Example Code

[Full LLM Function Calling Codes](https://github.com/yomorun/llm-function-calling-examples)

## 🎯 Focuses on Geo-distributed AI Inference Infra

It’s no secret that today’s users want instant AI inference, every AI 
application is more powerful when it response quickly. But, currently, when we
talk about `distribution`, it represents **distribution in data center**. The AI model is
far away from their users from all over the world.

If an application can be deployed anywhere close to their end users, solve the
problem, this is **Geo-distributed System Architecture**:

<img width="580" alt="yomo geo-distributed system" src="https://user-images.githubusercontent.com/65603/162367572-5a0417fa-e2b2-4d35-8c92-2c95d461706d.png">
