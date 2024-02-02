<img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/huixiangdou.jpg" width="64" height="auto" />

# [HuixiangDou](https://github.com/InternLM/HuixiangDou)
"HuixiangDou" is a domain knowledge assistant based on LLM. Features:

1. Handles complex scenarios such as group chat and handle answer user questions without flooding messages.
2. Proposes a solution for technical issues through an algorithm pipeline.
3. Low cost, see [arxiv2401.08772](https://arxiv.org/abs/2401.08772)

# Demonstration
HuixiangDou is a **assistant**
* Says it doesn't know in response to halluciations
* Personal Wechat supported
* Feishu supported

<img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/demo0.jpg" width="400">

HuixiangDou is a **group** assistant
* Ignores idle talk
* Only interacts with those who need help

<img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/inside-mmpose.jpg" width="400">

HuixiangDou is a **domain knowledge** group assistant
* Relies on an algorithm pipeline + LLM instead of training
* Has faced thousands of users, and has been "teased" over 20,000 times in half a year

<img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/inside-middleware.png" width="400">

# Configuring deepseek API
**STEP1.** Apply for a token at deepseek open platform

**STEP2.** Follow the HuixiangDou Advanced Configuration and fill in the config.ini with your token

```ini
# config.ini
[llm]
enable_local = 0
enable_remote = 1
..
[llm.server]
..
remote_type = "deepseek"
remote_api_key = "YOUR-API-KEY"
remote_llm_max_text_length = 16000
remote_llm_model = "deepseek-chat"
```

**STEP3.** Run

```shell
python3 -m huixiangdou.main --standalone
```