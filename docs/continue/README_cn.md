<img src="https://github.com/continuedev/continue/blob/main/docs/static/img/logo.png?raw=true" width="64" height="auto" />

# [Continue](https://continue.dev/)

开源 IDE 插件，使用 LLM 做你的编程助手.

## UI

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)

## 接入 DeepSeek API

修改 `config.yaml` 文件，添加 `DeepSeek` 模型配置，将 `YOUR_DEEPSEEK_API_KEY` 替换为你的 DeepSeek API Key。

* `~/.continue/config.yaml` (MacOS/Linux)
* `%USERPROFILE%\.continue\config.yaml` (Windows)

```yaml
name: Local Assistant
version: 1.0.0
schema: v1
models:
  - name: DeepSeek
    provider: deepseek
    model: deepseek-chat
    apiKey: YOUR_DEEPSEEK_API_KEY
    apiBase: https://api.deepseek.com/
    roles:
      - chat
      - edit
      - apply
      - summarize
      - autocomplete
    contextLength: 128000
    defaultCompletionOptions:
      temperature: 0.0
      maxTokens: 256
context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase
```

## 修改continue插件的设置
将超时时间改为3000ms
<img width="589" height="888" alt="image" src="https://github.com/user-attachments/assets/17fa5925-b8e1-4384-a748-d839c3aff48e" />
