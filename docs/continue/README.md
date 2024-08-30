<img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/e4d082de-6f64-44b9-beaa-0de55d70cfab" width="64" height="auto" /> 

# [Continue](https://continue.dev/)

An open-source autopilot in your IDE.
Continue will generate, refactor, and explain entire sections of code with LLMs.

## UI
![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)


## Integrate with DeepSeek API

### Tab Completion

    config.json

```json
{
  "completionOptions": {
    "temperature": 1.0,
    "maxTokens": 4096
  },
  "models": [{
    "title": "DeepSeek",
    "provider": "openai",
    "model": "deepseek-coder",
    "apiBase": "https://api.deepseek.com/beta",
    "apiKey": REDACTED,
    "contextLength": 8192
  }],
  "tabAutocompleteOptions": {
    "maxPromptTokens": 4096
  },
  "tabAutocompleteModel": {
    "title": "DeepSeek-V2",
    "model": "deepseek-coder",
    "apiKey": REDACTED,
    "contextLength": 8192,
    "apiBase": "https://api.deepseek.com/beta",
    "completionOptions": {
      "maxTokens": 4096,
      "temperature": 1.0,
      "topP": 1,
      "presencePenalty": 0,
      "frequencyPenalty": 0
    },
    "provider": "openai"
  }
}
```

### Chat with model

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/13600976/7114a8ef-c20a-4f06-91b3-2399c6b77b2d)
