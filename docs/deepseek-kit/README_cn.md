# deepseek-kit

> 轻量级 Agent 框架，原生级 DeepSeek 适配 — 思维模式精准工具调用 · 可靠结构化输出 · 最大缓存命中率

**源代码**：[https://github.com/FliPPeDround/deepseek-kit](https://github.com/FliPPeDround/deepseek-kit)

**文档**：[https://deepseek-kit.netlify.app](https://deepseek-kit.netlify.app)

**npm**：[deepseek-kit](https://npmx.dev/package/deepseek-kit)

deepseek-kit 是一个专为 DeepSeek API 打造的 TypeScript Agent 框架，解决了 LangChain.js 和 AI SDK 等通用框架无法正确处理的关键问题。

## 为什么选择 deepseek-kit？

### 🧠 思维模式精准工具调用

DeepSeek 的思维模式会在最终回答前输出思维链（`reasoning_content`）。当模型在思维过程中发起工具调用时，**所有后续请求必须包含完整的 `reasoning_content`**——否则 API 会返回 400 错误。

通用框架无法区分"有工具调用"和"无工具调用"场景下 `reasoning_content` 的不同处理要求，导致多轮工具调用频繁失败。

**deepseek-kit** 在 Agent 循环中自动追踪并重新发送 `reasoning_content`，根据是否发生工具调用应用差异化策略，默认启用思维模式——零配置即可使用。

### 💾 最大缓存命中率

DeepSeek API 默认启用上下文硬盘缓存。当后续请求的**前缀与之前的请求完全匹配**时，重复部分将从缓存中提供，显著降低延迟和成本。

通用框架经常注入动态元数据（时间戳、请求 ID）或以非确定性顺序排列消息，破坏前缀一致性，导致缓存命中率骤降。

**deepseek-kit** 发送零冗余请求体，采用确定性消息构建，确保相同输入始终产生相同的请求前缀。

### 📋 可靠结构化输出

结构化输出对 Agent 应用至关重要，但在 DeepSeek 思维模式下，通用框架的结构化输出方案经常与 `reasoning_content` 管理冲突，导致输出格式不可靠。

**deepseek-kit** 提供基于 Zod Schema 的结构化输出，具备智能重试和格式化错误反馈，完全兼容思维模式。

## 快速开始

```bash
pnpm add deepseek-kit
```

```ts
import { createAgent, createModel, tool } from 'deepseek-kit'
import { z } from 'zod'

const model = createModel({ model: 'deepseek-v4-flash' })

const weatherTool = tool({
  name: 'get_weather',
  description: '获取城市天气信息',
  parameters: z.object({
    city: z.string().describe('城市名称'),
  }),
  execute: async ({ city }) => `${city}: 晴天，25°C`,
})

const agent = createAgent({ model, tools: [weatherTool] })

const result = await agent.generate({
  prompt: '重庆今天天气怎么样？',
})

console.log(result.text)
```

## 核心特性

- 🧠 **思维模式适配** — 自动 `reasoning_content` 管理，零配置工具调用链
- 💾 **缓存命中率优化** — 零冗余请求体 + 确定性消息构建
- 📋 **结构化输出** — Zod Schema 驱动，智能重试，兼容思维模式
- 🤖 **Agent 系统** — 构建具有工具调用和多步执行的智能体
- 🌿 **子智能体** — 将 Agent 封装为工具进行委托，支持隔离上下文和并行执行
- 💬 **流式输出** — 文本、思维链和工具调用的流式事件
- 🔧 **工具调用** — 内置工具定义、参数校验、超时和重试
- ✍️ **FIM 补全** — Fill-in-the-Middle 代码补全支持
- 🪝 **Hook 系统** — 在生成步骤前后插入自定义逻辑
- 🔄 **自动重试** — 带指数退避和抖动的智能重试策略
- 🌲 **Tree-shakable** — 纯 ESM，`sideEffects: false`
- 🔒 **类型安全** — 完整的 TypeScript 类型定义
