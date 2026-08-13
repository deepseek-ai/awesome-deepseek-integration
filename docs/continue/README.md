<img width="440" height="496" alt="image" src="https://github.com/user-attachments/assets/fa41c95c-e98d-4234-bfeb-760966cf818b" /><img src="https://github.com/continuedev/continue/blob/main/docs/static/img/logo.png?raw=true" width="64" height="auto" />

# [Continue](https://continue.dev/)

An open-source autopilot in your IDE.
Continue will generate, refactor, and explain entire sections of code with LLMs.

## UI

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)

## Integrate with DeepSeek API

Modify the `config.yaml` file to add the `DeepSeek` model configuration, replacing `YOUR_DEEPSEEK_API_KEY` with your DeepSeek API Key.

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

## Modify the settings of the Continue plugin
Change the timeout to '3000ms'
<img width="589" height="888" alt="image" src="https://github.com/user-attachments/assets/bad9a829-34f2-44b1-bcc9-d6b804615158" />
