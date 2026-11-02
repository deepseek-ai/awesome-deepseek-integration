# 在 Heym 中使用 DeepSeek

[Heym](https://github.com/heymrun/heym) 是可自托管的智能体工作流运行时。Custom 凭据可将兼容 OpenAI 的模型服务接入 LLM 和 Agent 节点。Heym 采用[附带 Commons Clause 条件的 MIT 许可](https://github.com/heymrun/heym/blob/main/COMMONS-CLAUSE.md)，属于源码可用项目。

## 启动 Heym

安装 Bun、Python 3.11+、uv 和 Docker，然后按照[快速开始](https://github.com/heymrun/heym#-quick-start)运行：

```bash
git clone https://github.com/heymrun/heym.git
cd heym
./run.sh
```

打开 `http://localhost:4017` 并创建账号。启动脚本会运行 PostgreSQL、后端和前端。基础设施与模型服务的使用费用需单独承担。

## 添加 DeepSeek 凭据

从 [DeepSeek 开放平台](https://platform.deepseek.com/)获取 API Key。在 Heym 的 **Settings > Credentials** 中新建 **Custom** 凭据：

| 字段 | 值 |
|---|---|
| Name | `DeepSeek` |
| API key | 你的 DeepSeek API Key |
| Base URL | `https://api.deepseek.com/v1` |

仅在凭据表单中填写密钥。不要将密钥写入提示词、节点输出或导出的配置。

## 发起文本请求

1. 创建工作流，添加 **LLM** 节点。
2. 选择 `DeepSeek` 凭据，模型填写 `deepseek-flash`。
3. 使用文本输出，关闭批处理和 **Use Responses API**。
4. 用户消息填写 `Say hello in one sentence.`。
5. 启用 **Send extra request body**，输入：

```json
{
  "thinking": {
    "type": "disabled"
  }
}
```

运行工作流，在节点的 `text` 输出和 Traces 标签页查看结果。模型名称与可用性可能变化，请以 [DeepSeek API 文档](https://api-docs.deepseek.com/)为准。本例使用非思考模式的 Chat Completions。扩展为推理或工具调用流程前，请阅读[思考模式指南](https://api-docs.deepseek.com/guides/thinking_mode/)。

## 验证范围与限制

本次通过 Heym 的 LLM 服务和模拟 HTTP 响应，检查了凭据路径、模型字段、额外请求体和 `/v1/chat/completions` 请求。对该路径的无身份认证请求返回 HTTP 401。本次贡献未执行带真实密钥的模型推理。

本教程仅覆盖一次文本请求。工具调用、结构化输出、推理历史和供应商专属 API 需要另行验证。

## 参考资料

- [Heym Custom 凭据](https://github.com/heymrun/heym/blob/main/frontend/src/docs/content/reference/integrations.md#llm-providers-openai-google-custom-cohere)
- [Heym LLM 节点与额外请求体](https://github.com/heymrun/heym/blob/main/frontend/src/docs/content/nodes/llm-node.md#extra-body)
- [Heym Agent 架构与人工审批](https://github.com/heymrun/heym/blob/main/frontend/src/docs/content/reference/agent-architecture.md)
