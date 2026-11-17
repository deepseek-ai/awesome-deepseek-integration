# DGrid AI Gateway

[DGrid AI Gateway](https://dgrid.ai/) provides a single, unified API to access 200+ leading AI models — including the full suite of the latest DeepSeek models. Built on a decentralized AI inference network that is open, low-cost, and community-powered, DGrid dramatically reduces integration complexity and operational costs. Users can directly plug their DGrid API key into tools like Claude Code, Codex, and Cursor, and freely switch between hundreds of models through one standardized endpoint.

## Supported DeepSeek Models

DGrid hosts the complete DeepSeek lineup with zero additional configuration. Models follow the `[provider]/[model-name]` naming format:

| Model ID | Description |
|---|---|
| `deepseek/deepseek-v4-pro` | DeepSeek V4 Pro — flagship reasoning & coding model |
| `deepseek/deepseek-v4-flash` | DeepSeek V4 Flash — fast, cost-efficient variant |
| `deepseek/deepseek-r1-0528` | DeepSeek-R1 (May 2025 release) |
| `deepseek/deepseek-r1` | DeepSeek-R1 — advanced reasoning model |
| `deepseek/deepseek-v3.2` | DeepSeek V3.2 |
| `deepseek/deepseek-v3.2-exp` | DeepSeek V3.2 Experimental |
| `deepseek/deepseek-v3.1-terminus` | DeepSeek V3.1 Terminus |
| `deepseek/deepseek-chat-v3.1` | DeepSeek Chat V3.1 |
| `deepseek/deepseek-chat-v3-0324` | DeepSeek Chat V3 (March 2024) |
| `deepseek/deepseek-r1-distill-qwen-32b:free` | DeepSeek-R1 Qwen-32B distill — free tier |

## Quick Start

### Prerequisites

- A valid `DGRID_API_KEY` — obtain one from [dgrid.ai](https://dgrid.ai/)
- Network access to `https://api.dgrid.ai/v1`
- For SDK usage: the OpenAI SDK installed in your project

### Direct API Request via cURL

```bash
curl https://api.dgrid.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DGRID_API_KEY" \
  -d '{
    "model": "deepseek/deepseek-v4-pro",
    "messages": [
      {"role": "user", "content": "What are the key innovations in DeepSeek-V4?"}
    ]
  }'
```

### Using the OpenAI SDK (DGrid Compatible)

DGrid AI Gateway is fully compatible with the OpenAI SDK. You only need to change the `baseURL` to migrate or integrate.

**Install the SDK**

```bash
# TypeScript / Node.js
npm install openai

# Python
pip install openai
```

**TypeScript**

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://api.dgrid.ai/v1',   // DGrid AI Gateway endpoint
  apiKey: '<DGRID_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>',  // Optional: your application URL
    'X-Title': '<YOUR_SITE_NAME>',      // Optional: your application name
  },
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'deepseek/deepseek-v4-pro',
    messages: [
      { role: 'user', content: 'What are the key innovations in DeepSeek-V4?' },
    ],
  });
  console.log(completion.choices[0].message);
}

main();
```

**Python**

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.dgrid.ai/v1",  # DGrid AI Gateway endpoint
    api_key="<DGRID_API_KEY>",
)

completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: your application URL
        "X-Title": "<YOUR_SITE_NAME>",      # Optional: your application name
    },
    model="deepseek/deepseek-v4-pro",
    messages=[
        {"role": "user", "content": "What are the key innovations in DeepSeek-V4?"}
    ],
)

print(completion.choices[0].message.content)
```

> **Note:** The `HTTP-Referer` and `X-Title` headers are optional, but providing them helps DGrid better identify your application and deliver optimized service support.

## Key Features

- **OpenAI-compatible API** — drop-in replacement for any OpenAI SDK or toolchain; no code rewrite required
- **200+ models, one key** — access DeepSeek alongside leading models from OpenAI, Anthropic, Google, and more through a single endpoint
- **Direct tool integration** — plug your API key directly into Claude Code, Codex, Cursor, and other AI-native tools
- **Decentralized inference network** — open, low-cost, community-powered infrastructure
- **Automatic fallback** — define a priority list of models; DGrid retries seamlessly on failure
- **Built-in observability** — request logging, latency tracking, and usage analytics from the dashboard
- **Rate-limit management** — per-key and per-team controls to prevent runaway costs
- **Web3-ready** — native support for decentralized application teams
- **Pay per token** — no monthly subscription; only pay for what you use

## Resources

- [Official Website](https://dgrid.ai/)
- [AI Gateway Documentation](https://docs.dgrid.ai/AI-Gateway)
- [Model API Reference](https://docs.dgrid.ai/Model-API)
- [Integration Tutorials](https://docs.dgrid.ai/AI-Gateway-Integrations)
- [GitHub Organization](https://github.com/dgridai)
