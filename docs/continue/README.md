<img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/e4d082de-6f64-44b9-beaa-0de55d70cfab" width="64" height="auto" /> 

# [Continue](https://continue.dev/)

An open-source autopilot in your IDE.
Continue will generate, refactor, and explain entire sections of code with LLMs.

## UI
![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/094e9dc8-03d0-493d-95fb-6129a42a35bd)


## Integrate with DeepSeek API

### Tab Completion

Please use the following config before we release official FIM support:

    config.json

```json
{
  "models": [{
    "title": "DeepSeek",
    "provider": "openai",
    "model": "deepseek-coder",
    "apiBase": "https://api.deepseek.com",
    "apiType": "openai",
    "apiKey": REDACTED,
    "useLegacyCompletionsEndpoint": false,
    "contextLength": 8192
  }],
  "tabAutocompleteOptions": {
    "template": "Please teach me what I should write in the `hole` tag, but without any further explanation and code backticks, i.e., as if you are directly outputting to a code editor. It can be codes or comments or strings. Don't provide existing & repetitive codes. If the provided prefix and suffix contain incomplete code and statement, your response should be able to be directly concatenated to the provided prefix and suffix. Also note that I may tell you what I'd like to write inside comments. \n{{{prefix}}}<hole></hole>{{{suffix}}}\n\nPlease be aware of the environment the hole is placed, e.g., inside strings or comments or code blocks, and please don't wrap your response in ```. You should always provide non-empty output.\n",
    "useCache": true,
    "maxPromptTokens": 2048
  },
  "tabAutocompleteModel": {
    "title": "DeepSeek-V2",
    "model": "deepseek-coder",
    "apiKey": REDACTED,
    "contextLength": 8192,
    "apiBase": "https://api.deepseek.com",
    "completionOptions": {
      "maxTokens": 4096,
      "temperature": 0,
      "topP": 1,
      "presencePenalty": 0,
      "frequencyPenalty": 0
    },
    "provider": "openai",
    "useLegacyCompletionsEndpoint": false
  }
}
```

### Chat with model

![image](https://github.com/deepseek-ai/awesome-deepseek-integration/assets/13600976/7114a8ef-c20a-4f06-91b3-2399c6b77b2d)
