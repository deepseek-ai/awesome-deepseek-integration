# deepseek-kit

> A lightweight Agent framework with native-level DeepSeek adaptation — Precise tool calling in thinking mode · Reliable structured output · Maximum cache hit rate.

**Source Code**: [https://github.com/FliPPeDround/deepseek-kit](https://github.com/FliPPeDround/deepseek-kit)

**Documentation**: [https://deepseek-kit.netlify.app](https://deepseek-kit.netlify.app)

**npm**: [deepseek-kit](https://npmx.dev/package/deepseek-kit)

deepseek-kit is a TypeScript Agent framework purpose-built for the DeepSeek API, solving critical issues that general-purpose frameworks like LangChain.js and AI SDK cannot properly handle.

## Why deepseek-kit?

### 🧠 Precise Tool Calling in Thinking Mode

DeepSeek's thinking mode outputs a chain of thought (`reasoning_content`) before the final answer. When the model makes tool calls during thinking, **all subsequent requests must include the full `reasoning_content`** — otherwise the API returns a 400 error.

General-purpose frameworks cannot distinguish between the different handling requirements for `reasoning_content` in "with tool call" vs "without tool call" scenarios, causing multi-turn tool calling to fail frequently.

**deepseek-kit** automatically tracks and re-sends `reasoning_content` in the agent loop, applies differentiated strategies based on whether tool calls occurred, and enables thinking mode by default — zero configuration needed.

### 💾 Maximum Cache Hit Rate

DeepSeek API enables context hard disk caching by default. When subsequent requests have a **prefix that exactly matches** a previous request, the repeated portion is served from cache, significantly reducing latency and cost.

General-purpose frameworks often inject dynamic metadata (timestamps, request IDs) or arrange messages in non-deterministic order, breaking prefix consistency and causing cache hit rates to plummet.

**deepseek-kit** sends zero-redundancy request bodies with deterministic message construction, ensuring the same input always produces the same request prefix.

### 📋 Reliable Structured Output

Structured output is essential for agent applications, but under DeepSeek's thinking mode, general-purpose frameworks' structured output solutions often conflict with `reasoning_content` management, resulting in unreliable output formats.

**deepseek-kit** provides Zod Schema-driven structured output with smart retry and formatted error feedback, fully compatible with thinking mode.

## Quick Start

```bash
pnpm add deepseek-kit
```

```ts
import { createAgent, createModel, tool } from 'deepseek-kit'
import { z } from 'zod'

const model = createModel({ model: 'deepseek-v4-flash' })

const weatherTool = tool({
  name: 'get_weather',
  description: 'Get weather information for a city',
  parameters: z.object({
    city: z.string().describe('City name'),
  }),
  execute: async ({ city }) => `${city}: Sunny, 25°C`,
})

const agent = createAgent({ model, tools: [weatherTool] })

const result = await agent.generate({
  prompt: 'How\'s the weather in Chongqing today?',
})

console.log(result.text)
```

## Key Features

- 🧠 **Thinking Mode Adaptation** — Automatic `reasoning_content` management, zero-config tool calling chains
- 💾 **Cache Hit Rate Optimization** — Zero-redundancy request body + deterministic message construction
- 📋 **Structured Output** — Zod Schema-driven, smart retry, thinking mode compatible
- 🤖 **Agent System** — Build intelligent agents with tool calling and multi-step execution
- 🌿 **Subagents** — Encapsulate agents as tools for delegation, with isolated context and parallel execution
- 💬 **Streaming** — Streaming events for text, chain-of-thought, and tool calls
- 🔧 **Tool Calling** — Built-in tool definition, parameter validation, timeout, and retry
- ✍️ **FIM Completion** — Fill-in-the-Middle code completion support
- 🪝 **Hook System** — Insert custom logic before and after generation steps
- 🔄 **Auto Retry** — Smart retry strategy with exponential backoff and jitter
- 🌲 **Tree-shakable** — Pure ESM, `sideEffects: false`
- 🔒 **Type Safe** — Complete TypeScript type definitions
