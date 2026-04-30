# [open-multi-agent](https://github.com/JackChen-me/open-multi-agent)

<img src="https://raw.githubusercontent.com/JackChen-me/open-multi-agent/main/.github/brand/logo-mark-light.svg" alt="open-multi-agent" width="120" />

`open-multi-agent` 是一个 TypeScript 原生的多智能体系统构建框架。其**目标驱动的 Coordinator** 会自动将一个目标拆解为并行任务 DAG、分配给最合适的 agent，并综合各任务结果给出最终输出。DeepSeek 通过专用 adapter 作为一等公民 LLM 提供商接入。

## 核心特性

- **目标 → DAG，自动化**：Coordinator agent 将目标拆解为带类型的任务图；无依赖的任务并行执行，有依赖的任务自动等待。
- **DeepSeek 一等公民支持**：`deepseek-chat`（DeepSeek-V3）适合快速编码与工具调用，`deepseek-reasoner` 适合思考模式推理。
- **共享记忆 & MCP**：跨 agent 的命名空间共享记忆；通过 `open-multi-agent/mcp` 子路径懒加载 Model Context Protocol 集成。
- **内置工具**：`bash`、`file_read`、`file_write`、`file_edit`、`grep`、`glob`，以及可选的 `delegate_to_agent` 用于子 agent 调用。
- **三个运行时依赖**：`@anthropic-ai/sdk`、`openai`、`zod`。其他 provider 与 MCP 均懒加载，只为实际使用的能力付费。

## 接入 DeepSeek API

安装：

```bash
npm install open-multi-agent
export DEEPSEEK_API_KEY=sk-...
```

### 单 agent

```typescript
import { OpenMultiAgent } from 'open-multi-agent'

const oma = new OpenMultiAgent({
  defaultProvider: 'deepseek',
  defaultModel: 'deepseek-chat', // 或使用 'deepseek-reasoner' 切换到思考模式
})

const result = await oma.runAgent(
  {
    name: 'researcher',
    systemPrompt: '你是一个严谨的研究助理。',
  },
  '用 5 个 bullet 概括 DeepSeek-V3 的核心思路。'
)

console.log(result.output)
```

### 多 agent 团队（目标驱动）

```typescript
const team = oma.createTeam('api-team', {
  name: 'api-team',
  sharedMemory: true,
  agents: [
    { name: 'architect', provider: 'deepseek', model: 'deepseek-reasoner', systemPrompt: '你负责设计清晰的 API 契约。' },
    { name: 'developer', provider: 'deepseek', model: 'deepseek-chat',     systemPrompt: '你按 architect 的设计实现代码。', tools: ['bash', 'file_write', 'file_edit'] },
    { name: 'reviewer',  provider: 'deepseek', model: 'deepseek-chat',     systemPrompt: '你审查代码的正确性与清晰度。', tools: ['file_read', 'grep'] },
  ],
})

const teamResult = await oma.runTeam(team, '搭建一个最小 Express REST API，包含 /health 与 /users 接口。')
console.log(teamResult.success, teamResult.totalTokenUsage)
```

完整可运行示例：[`examples/providers/deepseek.ts`](https://github.com/JackChen-me/open-multi-agent/blob/main/examples/providers/deepseek.ts)。

## 相关资源

- GitHub：https://github.com/JackChen-me/open-multi-agent
- 示例集合：https://github.com/JackChen-me/open-multi-agent/tree/main/examples
- CLI 文档：https://github.com/JackChen-me/open-multi-agent/blob/main/docs/cli.md
