# [Memdoor](https://github.com/guregodevo/memdoor)

Memdoor is an open-source coding agent for the terminal that runs on your own API key, DeepSeek's included. You describe a job in steps and it runs them as a checked, resumable workflow: one task file per step, a step done when its output exists or its command exits 0, a gate where you approve, resume at the failed step.

## Use with DeepSeek

```bash
curl -fsSL https://memdoor.ai/install.sh | bash
export DEEPSEEK_API_KEY=sk-...
cd your-project && memdoor tui
```

`/model` lists the DeepSeek models on your key with their prices and pins one for the conversation. Inference is billed by DeepSeek to your account; nothing passes through memdoor.ai.

## Key features

1. **Your own key, any provider**: DeepSeek, OpenRouter, Anthropic, OpenAI, Gemini, Groq, xAI, Baseten, or a company AI gateway.
2. **Workflows**: say the steps; the coder writes one YAML per step and runs them as a graph, in parallel where independent, drawn live in the terminal.
3. **Done means the target exists**: a file written or a command exiting 0, never the model's word.
4. **A gate**: a step only you can complete; the run stops and shows the diff.
5. **Resume**: a failed run starts again at the failed step.
6. **A decision model** in front of the chat model keeps what it reads to what the task needs: 26–49% fewer input tokens on measured runs.
7. **One static binary** for macOS, Linux and Windows; no Docker, no Python.

Site: https://memdoor.ai · Docs: https://memdoor.ai/docs/getting-started · Apache 2.0
