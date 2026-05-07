<img src="https://github.com/continuedev/continue/blob/main/docs/logo/light.svg?raw=true" width="64" height="auto" />

# [Continue](https://continue.dev/)

An open-source autopilot in your IDE.
Continue will generate, refactor, and explain entire sections of code with LLMs.

## UI

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)

## Integrate with DeepSeek API

Modify the `config.yaml` file to add the `DeepSeek` model configuration, replacing `YOUR_DEEPSEEK_API_KEY` with your DeepSeek API Key.

* `~/.continue/config.yaml` (MacOS/Linux)
* `%USERPROFILE%\.continue\config.yaml` (Windows)

This example keeps chat models and autocomplete separate:

* `DeepSeek-V4-Flash` and `DeepSeek-V4-Pro` are used for chat, edit, apply, and summarize. You can switch between them in Continue.
* `DeepSeek FIM` is used for autocomplete. It keeps inline completion fast and focused.

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
