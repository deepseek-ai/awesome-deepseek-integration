# [VSCode BYOK](https://code.visualstudio.com/docs/copilot/customization/language-models#_bring-your-own-language-model-key)

[English](README.md)

[Bring your own language model API key (BYOK)](https://code.visualstudio.com/docs/copilot/customization/language-models#_bring-your-own-language-model-key) 是 VSCode 中新增的一项功能，允许用户在 GitHub Copilot 中使用第三方语言模型提供商的 API 密钥。通过 BYOK，用户可以将自己喜欢的语言模型集成到 Copilot 中，以获得更个性化和定制化的代码建议。

## ✨ 功能亮点

- 支持多种自定义模型服务商，如 DeepSeek
- 允许用户配置多个模型，并在 Copilot 中轻松切换
- 在 VSCode 中提供和 GitHub Copilot 官方模型相同的使用体验和界面
- 无需安装额外的插件，直接在 Copilot 设置中配置即可使用

## ⚡ 如何使用

1. 准备好第三方语言模型提供商的 API 密钥（例如 DeepSeek）
2. `Ctrl + Shift + P` 打开命令面板，输入 `Chat: Manage Language Models` 并选择它
    ![image](add_endpoint.png)
3. 选择添加模型，输入模型服务商名称（例如 DeepSeek）、 API 密钥、选择 `chat-completions` 模式
4. 在弹出的 `chatLanguageModels.json` 文件中，添加以下配置：

   ```json
   {
      "name": "DeepSeek",
      "vendor": "customendpoint",
      "apiKey": "<这里是刚刚输入的 API KEY 的存储名，每次不同>",
      "apiType": "chat-completions",
      "models": [
         {
             "id": "deepseek-v4-flash",
             "name": "DeepSeek V4 Flash",
             "url": "https://api.deepseek.com",
             "supportsReasoningEffort": [
                 "high",
                 "max"
             ],
             "toolCalling": true,
             "vision": false,
             "thinking": true,
             "maxInputTokens": 800000,
             "maxOutputTokens": 393216
         },
         {
             "id": "deepseek-v4-pro",
             "name": "DeepSeek V4 Pro",
             "url": "https://api.deepseek.com",
             "supportsReasoningEffort": [
                 "high",
                 "max"
             ],
             "toolCalling": true,
             "vision": false,
             "thinking": true,
             "maxInputTokens": 800000,
             "maxOutputTokens": 393216
         }
      ],
      "settings": {
         "deepseek-v4-pro": {
             "reasoningEffort": "max"
         },
         "deepseek-v4-flash": {
             "reasoningEffort": "max"
         }
      }
   }
   ```

5. 保存文件后，重新打开 Copilot Chat 界面，在模型选择器中就可以看到并选择刚刚添加的 DeepSeek 模型了
6. `chatLanguageModels.json` 文件也可以通过 VSCode 设置中的 `Chat: Open Language Models (JSON)` 打开