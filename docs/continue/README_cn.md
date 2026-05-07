<img src="https://github.com/continuedev/continue/blob/main/docs/logo/light.svg?raw=true" width="64" height="auto" />

# [Continue](https://continue.dev/)

开源 IDE 插件，使用 LLM 做你的编程助手.

## UI

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)

## 接入 DeepSeek API

修改 `config.yaml` 文件，添加 `DeepSeek` 模型配置，将 `YOUR_DEEPSEEK_API_KEY` 替换为你的 DeepSeek API Key。

* `~/.continue/config.yaml` (MacOS/Linux)
* `%USERPROFILE%\.continue\config.yaml` (Windows)

下面的示例把对话模型和补全模型分开：

* `DeepSeek-V4-Flash` 和 `DeepSeek-V4-Pro` 用于 chat、edit、apply、summarize，可以在 Continue 里按需切换。
* `DeepSeek FIM` 用于 autocomplete，适合快速、稳定的行内补全。

```yaml
name: Local Assistant
version: 1.0.0
schema: v1
models:
  - name: DeepSeek-V4-Flash
    provider: deepseek
    model: deepseek-v4-flash
    apiKey: YOUR_DEEPSEEK_API_KEY
    apiBase: https://api.deepseek.com/
    roles:
      - chat
      - edit
      - apply
      - summarize
    contextLength: 1000000
    defaultCompletionOptions:
      temperature: 0.2
      maxTokens: 4096

  - name: DeepSeek-V4-Pro
    provider: deepseek
    model: deepseek-v4-pro
    apiKey: YOUR_DEEPSEEK_API_KEY
    apiBase: https://api.deepseek.com/
    roles:
      - chat
      - edit
      - apply
      - summarize
    contextLength: 1000000
    defaultCompletionOptions:
      temperature: 0.2
      maxTokens: 8192

  - name: DeepSeek FIM
    provider: deepseek
    model: deepseek-v4-flash
    apiKey: YOUR_DEEPSEEK_API_KEY
    apiBase: https://api.deepseek.com/
    roles:
      - autocomplete
    defaultCompletionOptions:
      temperature: 0.0
      maxTokens: 128
    autocompleteOptions:
      disable: false
      maxPromptTokens: 2048
      debounceDelay: 300
      modelTimeout: 5000
      maxSuffixPercentage: 0.3
      prefixPercentage: 0.7
      useCache: true
      useImports: true
      useRecentlyEdited: true
      onlyMyCode: false

context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase
```
