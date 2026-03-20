<p align="center">
  <img src="https://raw.githubusercontent.com/arikusi/deepseek-mcp-server/main/icon.png" alt="DeepSeek MCP Server" width="120" />
</p>

<h1 align="center">DeepSeek MCP Server (Remote)</h1>

<p align="center">
  支持聊天、推理、多轮会话、函数调用、思考模式和费用追踪的 DeepSeek AI MCP 服务器。
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@arikusi/deepseek-mcp-server"><img src="https://img.shields.io/npm/v/@arikusi/deepseek-mcp-server.svg" alt="npm 版本" /></a>
  <a href="https://www.npmjs.com/package/@arikusi/deepseek-mcp-server"><img src="https://img.shields.io/npm/dm/@arikusi/deepseek-mcp-server.svg" alt="npm 下载量" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="许可证: MIT" /></a>
</p>

<p align="center">
  兼容 Claude Code、Gemini CLI、Cursor、Windsurf 及所有 MCP 兼容客户端。<br />
  已收录于 <a href="https://registry.modelcontextprotocol.io/?q=io.github.arikusi"><strong>MCP 官方注册表</strong></a>、<a href="https://smithery.ai/servers/arikusi/deepseek-mcp-server">Smithery</a>、<a href="https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server">Glama</a> 和 <a href="https://lobehub.com/mcp/arikusi-deepseek-mcp-server">LobeHub</a>。
</p>

## 快速开始

### 远程使用（无需安装）

直接使用托管端点，无需 npm 安装或 Node.js，只需携带您自己的 DeepSeek API 密钥：

**Claude Code:**
```bash
claude mcp add --transport http deepseek \
  https://deepseek-mcp.tahirl.com/mcp \
  --header "Authorization: Bearer YOUR_DEEPSEEK_API_KEY"
```

**Cursor / Windsurf / VS Code:**
```json
{
  "mcpServers": {
    "deepseek": {
      "url": "https://deepseek-mcp.tahirl.com/mcp",
      "headers": {
        "Authorization": "Bearer ${DEEPSEEK_API_KEY}"
      }
    }
  }
}
```

### 本地使用（stdio）

**Claude Code:**
```bash
claude mcp add -s user deepseek npx @arikusi/deepseek-mcp-server -e DEEPSEEK_API_KEY=your-key-here
```

**Gemini CLI:**
```bash
gemini mcp add deepseek npx @arikusi/deepseek-mcp-server -e DEEPSEEK_API_KEY=your-key-here
```

**获取 API 密钥：** [https://platform.deepseek.com](https://platform.deepseek.com)

---

## 主要功能

- **DeepSeek V3.2**: 两个模型均运行 DeepSeek-V3.2
- **多轮会话**: 通过 `session_id` 参数在请求间保持对话上下文
- **模型回退与熔断器**: 自动在模型间切换，具备熔断保护
- **MCP 资源**: `deepseek://models`、`deepseek://config`、`deepseek://usage`
- **思考模式**: 通过 `thinking: {type: "enabled"}` 启用 deepseek-chat 思考模式
- **JSON 输出模式**: 通过 `json_mode: true` 获取结构化 JSON 响应
- **函数调用**: 兼容 OpenAI 的工具调用，最多支持 128 个工具定义
- **费用追踪**: 自动计算费用，含缓存命中/未命中明细
- **12 个提示模板**: 调试、代码审查、函数调用等场景的模板
- **远程端点**: 托管于 `deepseek-mcp.tahirl.com/mcp`，BYOK（自带密钥），无需安装
- **Docker 支持**: 多阶段 Dockerfile，含健康检查
- **全面测试**: 253 个测试，代码覆盖率 90%+

## 模型

两个模型均运行 **DeepSeek-V3.2**，统一定价。

### deepseek-chat

- **适用场景**: 通用对话、编程、内容生成
- **上下文**: 128K tokens
- **最大输出**: 8K tokens
- **特性**: 思考模式、JSON 模式、函数调用
- **定价**: $0.028/1M 缓存命中，$0.28/1M 缓存未命中，$0.42/1M 输出

### deepseek-reasoner

- **适用场景**: 复杂推理、数学、逻辑问题
- **上下文**: 128K tokens
- **最大输出**: 64K tokens
- **特性**: 展示思考过程，JSON 模式，函数调用
- **定价**: $0.028/1M 缓存命中，$0.28/1M 缓存未命中，$0.42/1M 输出

## 链接

- [GitHub 仓库](https://github.com/arikusi/deepseek-mcp-server)
- [npm 包](https://www.npmjs.com/package/@arikusi/deepseek-mcp-server)
- [在线文档](https://mcp.tahirl.com)
- [问题反馈](https://github.com/arikusi/deepseek-mcp-server/issues)

## 许可证

MIT License

---

**由 [@arikusi](https://github.com/arikusi) 创建**

