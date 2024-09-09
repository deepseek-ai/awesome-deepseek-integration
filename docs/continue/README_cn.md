<img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/e4d082de-6f64-44b9-beaa-0de55d70cfab" width="64" height="auto" /> 

# [Continue](https://continue.dev/)

开源 IDE 插件，使用 LLM 做你的编程助手.

## UI

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)


## 接入 DeepSeek API

### Tab 补全

    config.json

```json
{
  "completionOptions": {
    "BaseCompletionOptions": {
        "temperature": 0.0,
        "maxTokens": 256
    }
  },
  "models": [
    {
      "title": "DeepSeek",
      "model": "deepseek-chat",
      "contextLength": 128000,
      "apiKey": "REDACTED",
      "provider": "openai",
      "apiBase": "https://api.deepseek.com/beta"
    }
  ],
  "tabAutocompleteModel": {
    "title": "DeepSeek",
    "model": "deepseek-chat",
    "apiKey": "REDACTED",
    "provider": "openai",
    "apiBase": "https://api.deepseek.com/beta"
  },
...
```

![image](https://github.com/user-attachments/assets/30aca5ee-b1bc-4c01-a007-45bb229283dd)

