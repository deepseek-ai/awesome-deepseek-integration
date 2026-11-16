<img src="https://github.com/JohnnyZ93/oai-compatible-copilot/blob/main/assets/logo.png?raw=true" width="64" height="auto" />

# [OAI Compatible Provider for Copilot](https://marketplace.visualstudio.com/items?itemName=johnny-zhao.oai-compatible-copilot)

An open-source VS Code extension to use openai compatible inference providers in GitHub Copilot.

[Source Code](https://github.com/JohnnyZ93/oai-compatible-copilot)

[VS Code Chat Provider API](https://code.visualstudio.com/api/extension-guides/ai/language-model-chat-provider)

## ✨ Features
- Supports almost all OpenAI-compatible providers, such as ModelScope, DeepSeek...
- Supports vision models.
- Offers additional configuration options for chat requests.
- Supports control model thinking and reasoning content show in chat interface.
- Supports configuring models from multiple providers simultaneously, automatically managing API keys without switch them repeatedly.
- Supports defining multiple configurations for the same model ID with different settings (e.g. thinking enable/disable for GLM-4.6).

## Requirements
- VS Code 1.104.0 or higher.
- DeepSeek API key.

## ⚡ Integrate with DeepSeek API
1. Install the OAI Compatible Provider for Copilot extension [here](https://marketplace.visualstudio.com/items?itemName=johnny-zhao.oai-compatible-copilot).
2. Open VS Code Settings and configure `oaicopilot.baseUrl` and `oaicopilot.models`.
3. Open Github Copilot Chat interface.
4. Click the model picker and select "Manage Models...".
5. Choose "OAI Compatible" provider.
6. Enter your API key — it will be saved locally.
7. Select the DeepSeek models by your configuration.

```json
"oaicopilot.baseUrl": "https://api.deepseek.com/v1",
"oaicopilot.models": [
  {
      "id": "deepseek-chat",
      "owned_by": "deepseek",
      "context_length": 128000,
      "max_tokens": 8000
  },
  {
      "id": "deepseek-reasoner",
      "owned_by": "deepseek",
      "context_length": 128000,
      "max_tokens": 16000
  }
]
```
