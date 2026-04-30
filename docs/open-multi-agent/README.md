# [open-multi-agent](https://github.com/JackChen-me/open-multi-agent)

<img src="https://raw.githubusercontent.com/JackChen-me/open-multi-agent/main/.github/brand/logo-mark-light.svg" alt="open-multi-agent" width="120" />

`open-multi-agent` is a TypeScript-native framework for building multi-agent systems. Its **goal-driven Coordinator** automatically decomposes a single goal into a parallel task DAG, dispatches tasks to the best-fit agents, and synthesizes a final answer. DeepSeek is supported as a first-class LLM provider through a dedicated adapter.

## Key Features

- **Goal → DAG, automatically.** A coordinator agent decomposes a goal into a typed task graph; independent tasks run in parallel, dependent tasks wait.
- **First-class DeepSeek support.** `deepseek-chat` (DeepSeek-V3) for fast coding and tool use, `deepseek-reasoner` for thinking-mode reasoning.
- **Shared memory & MCP.** Namespaced shared memory across agents; lazy-loaded Model Context Protocol integration via the `open-multi-agent/mcp` subpath.
- **Built-in tools.** `bash`, `file_read`, `file_write`, `file_edit`, `grep`, `glob`, plus opt-in `delegate_to_agent` for sub-agent calls.
- **Three runtime dependencies.** `@anthropic-ai/sdk`, `openai`, `zod`. Other providers and MCP load lazily so you only pay for what you use.

## Integrate with the DeepSeek API

Install:

```bash
npm install open-multi-agent
export DEEPSEEK_API_KEY=sk-...
```

### Single agent

```typescript
import { OpenMultiAgent } from 'open-multi-agent'

const oma = new OpenMultiAgent({
  defaultProvider: 'deepseek',
  defaultModel: 'deepseek-chat', // or 'deepseek-reasoner' for thinking mode
})

const result = await oma.runAgent(
  {
    name: 'researcher',
    systemPrompt: 'You are a careful research assistant.',
  },
  'Summarize the key ideas of DeepSeek-V3 in 5 bullets.'
)

console.log(result.output)
```

### Multi-agent team (goal-driven)

```typescript
const team = oma.createTeam('api-team', {
  name: 'api-team',
  sharedMemory: true,
  agents: [
    { name: 'architect', provider: 'deepseek', model: 'deepseek-reasoner', systemPrompt: 'You design clear API contracts.' },
    { name: 'developer', provider: 'deepseek', model: 'deepseek-chat',     systemPrompt: 'You implement what the architect specifies.', tools: ['bash', 'file_write', 'file_edit'] },
    { name: 'reviewer',  provider: 'deepseek', model: 'deepseek-chat',     systemPrompt: 'You review code for correctness and clarity.', tools: ['file_read', 'grep'] },
  ],
})

const teamResult = await oma.runTeam(team, 'Build a minimal Express REST API with /health and /users endpoints.')
console.log(teamResult.success, teamResult.totalTokenUsage)
```

A complete runnable example lives at [`examples/providers/deepseek.ts`](https://github.com/JackChen-me/open-multi-agent/blob/main/examples/providers/deepseek.ts).

## Resources

- GitHub: https://github.com/JackChen-me/open-multi-agent
- Examples: https://github.com/JackChen-me/open-multi-agent/tree/main/examples
- CLI docs: https://github.com/JackChen-me/open-multi-agent/blob/main/docs/cli.md
