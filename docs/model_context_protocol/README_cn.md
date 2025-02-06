# DeepSeek MCP 服务器

这是一个适用于 DeepSeek API 的 Model Context Protocol (MCP) 服务器，可与 Claude Desktop 等兼容 MCP 的应用程序无缝集成，从而利用 DeepSeek 强大的语言模型。

## *匿名* 使用 DeepSeek API —— 另一端只会看到代理

<a href="https://glama.ai/mcp/servers/asht4rqltn"><img width="380" height="200" src="https://glama.ai/mcp/servers/asht4rqltn/badge" alt="DeepSeek MCP Server" /></a>
<a href="https://smithery.ai/server/@dmontgomery40/deepseek-mcp-server"><img alt="Smithery Badge" src="https://smithery.ai/badge/@dmontgomery40/deepseek-mcp-server"></a>

[![npm version](https://img.shields.io/npm/v/deepseek-mcp-server)](https://www.npmjs.com/package/deepseek-mcp-server)
[![npm downloads](https://img.shields.io/npm/dm/deepseek-mcp-server)](https://www.npmjs.com/package/deepseek-mcp-server)
[![GitHub issues](https://img.shields.io/github/issues/DMontgomery40/deepseek-mcp-server)](https://github.com/DMontgomery40/deepseek-mcp-server/issues)
[![GitHub forks](https://img.shields.io/github/forks/DMontgomery40/deepseek-mcp-server)](https://github.com/DMontgomery40/deepseek-mcp-server/network)
[![GitHub stars](https://img.shields.io/github/stars/DMontgomery40/deepseek-mcp-server)](https://github.com/DMontgomery40/deepseek-mcp-server/stargazers)
[![GitHub license](https://img.shields.io/github/license/DMontgomery40/deepseek-mcp-server?color=blue)](https://github.com/DMontgomery40/deepseek-mcp-server/blob/main/LICENSE)

## 安装

### 通过 Smithery 安装

要使用 Smithery 在 Claude Desktop 上自动安装 DeepSeek MCP Server，请执行以下命令（请确保已安装 `@smithery/cli`）：

`bash
npx -y @smithery/cli install @dmontgomery40/deepseek-mcp-server --client claude
`

### 手动安装

`bash
npm install -g deepseek-mcp-server
`

### 在 Claude Desktop 中使用

在你的 `claude_desktop_config.json` 中添加：

`json
{
  "mcpServers": {
    "deepseek": {
      "command": "npx",
      "args": [
        "-y",
        "deepseek-mcp-server"
      ],
      "env": {
        "DEEPSEEK_API_KEY": "your-api-key"
      }
    }
  }
}
`

## 功能简介

> 注意：该服务器能够根据自然语言请求智能地将其映射到相应的配置更改。你也可以查询当前设置和可用模型：

- 用户：“有哪些可用的模型？”
  - 响应：通过 models 资源列出可用模型及其功能。
- 用户：“我有哪些配置选项？”
  - 响应：通过 model-config 资源列出所有可用的配置选项。
- 用户：“当前的温度（temperature）设置是多少？”
  - 响应：显示当前温度设置。
- 用户：“开始一个多轮对话。使用如下设置：model: 'deepseek-chat'，创意度不要太高，并且允许 8000 个 token。”
  - 响应：使用指定设置启动一个多轮对话。

### 当 R1 出现故障时自动回退到其他模型

- 如果主模型（R1，服务器中称为 `deepseek-reasoner`）出现故障，服务器会自动尝试使用 v3（服务器中称为 `deepseek-chat`）
- 你也可以随时在对话中切换，只需在对话中输入提示并说“使用 `deepseek-reasoner`”或“使用 `deepseek-chat`”
- v3 更适用于通用场景；R1 更适用于处理较为复杂的技术性问题，主要得益于速度和 token 使用的优化

### 资源发现：可用的模型和配置

- 自定义模型选择
- 温度控制（0.0 - 2.0）
- 最大 token 限制
- Top P 采样（0.0 - 1.0）
- 存在惩罚（presence penalty）（-2.0 - 2.0）
- 频率惩罚（frequency penalty）（-2.0 - 2.0）

## 增强的对话功能

**多轮对话支持：**
- 在多轮交互过程中维护完整的消息历史和上下文
- 在对话过程中保留配置设置
- 自动处理复杂的对话逻辑和后续请求

这一功能在以下两个主要场景中特别有价值：

1. **训练 & 微调：**
   - 由于 DeepSeek 是开源的，很多用户正在训练自己的版本。多轮对话支持能够提供格式正确的对话数据，这对于训练高质量对话模型至关重要。

2. **复杂场景交互：**
   - 在生产环境中，这种功能有助于管理需要保留上下文的更长对话，例如：
     * 多步骤推理问题
     * 交互式故障排查
     * 详尽的技术讨论
     * 任何需要利用早期消息上下文来影响后续响应的场景

该功能在幕后自动处理所有上下文管理和消息格式，你只需关注对话本身，无需担心维护对话状态的技术细节。

## 使用 MCP Inspector 进行测试

你可以使用 MCP Inspector 工具在本地测试服务器：

1. 构建服务器：  
   `bash
   npm run build
   `

2. 使用 MCP Inspector 启动服务器：  
   `bash
   npx @modelcontextprotocol/inspector node ./build/index.js
   `

MCP Inspector 将在你的浏览器中打开，并通过 stdio 传输连接到该服务器。你可以：

- 查看可用工具
- 使用不同参数测试对话补全
- 调试服务器响应
- 监控服务器性能

注意：服务器默认使用 DeepSeek 的 R1 模型（`deepseek-reasoner`），它在推理和通用任务方面具有最先进的性能。

## 许可证

MIT
