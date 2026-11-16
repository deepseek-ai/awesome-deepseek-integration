<img src="https://github.com/JohnnyZ93/oai-compatible-copilot/blob/main/assets/logo.png?raw=true" width="64" height="auto" />

# [OAI Compatible Provider for Copilot](https://marketplace.visualstudio.com/items?itemName=johnny-zhao.oai-compatible-copilot)

开源的 VS Code 扩展，可在 GitHub Copilot 中使用 OpenAI 兼容的推理提供商。

[源代码](https://github.com/JohnnyZ93/oai-compatible-copilot)

[VS Code Chat Provider API](https://code.visualstudio.com/api/extension-guides/ai/language-model-chat-provider)

## ✨ 特性
- 支持几乎所有 OpenAI 兼容的提供商，如 ModelScope、DeepSeek...
- 支持视觉模型
- 为聊天请求提供额外的配置选项
- 支持在聊天界面中控制模型的思考和推理内容显示
- 支持同时配置来自多个提供商的模型，自动管理 API 密钥而无需重复切换
- 支持为同一模型 ID 定义具有不同设置的多个配置（例如 GLM-4.6 的思考启用/禁用）

## 要求
- VS Code 1.104.0 或更高版本
- DeepSeek API 密钥

## ⚡ 与 DeepSeek API 集成
1. 安装 OAI Compatible Provider for Copilot 扩展 [此处](https://marketplace.visualstudio.com/items?itemName=johnny-zhao.oai-compatible-copilot)
2. 打开 VS Code 设置并配置 `oaicopilot.baseUrl` 和 `oaicopilot.models`
3. 打开 GitHub Copilot Chat 界面
4. 点击模型选择器并选择 "Manage Models..."
5. 选择 "OAI Compatible" 提供商
6. 输入您的 API 密钥 — 它将保存在本地
7. 选择您配置的 DeepSeek 模型

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
