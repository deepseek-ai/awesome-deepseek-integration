# [OfoxAI](https://ofox.ai)

OfoxAI is a unified LLM API gateway that provides access to DeepSeek R1, V3 and 50+ other leading models (GPT, Claude, Gemini, Qwen, Kimi, etc.) through a single OpenAI-compatible API.

## Key Features

- **50+ Models, One API** — Access DeepSeek, OpenAI, Anthropic, Google, and more through unified endpoints
- **Three Native Protocols** — OpenAI, Anthropic, and Gemini SDK compatible, zero code changes to migrate
- **Automatic Failover** — Smart provider routing with automatic fallback to backup models
- **Prompt Caching** — Reduce cost and latency with built-in prompt caching support
- **China Direct Connect** — Low-latency access from China via HK express routes, no VPN needed
- **99.9% SLA** — Enterprise-grade reliability with multi-region deployment
- **Pay-as-you-go** — No monthly fees, token-level billing with 10+ free models

## Quick Start

### OpenAI Compatible

```bash
export OPENAI_BASE_URL=https://api.ofox.ai/v1
export OPENAI_API_KEY=<your-ofoxai-key>
```

### Anthropic Compatible

```bash
export ANTHROPIC_BASE_URL=https://api.ofox.ai/anthropic
export ANTHROPIC_AUTH_TOKEN=<your-ofoxai-key>
```

### Gemini Compatible

```bash
export GEMINI_API_KEY=<your-ofoxai-key>
# Base URL: https://api.ofox.ai/gemini
```

## DeepSeek Integration

OfoxAI fully supports DeepSeek models including:

- **DeepSeek-R1** — Reasoning model with chain-of-thought capabilities
- **DeepSeek-V3** — High-performance chat model
- **DeepSeek-Coder** — Code generation specialist

Simply use `deepseek-r1`, `deepseek-v3`, or `deepseek-coder` as the model ID in your API calls.

## Compatible Tools

OfoxAI works with all major AI development tools:

Claude Code, Cursor, Cline, Cherry Studio, Zed, OpenClaw, Codex CLI, Gemini CLI, OpenCode, Windsurf, Aider, and any tool supporting custom OpenAI/Anthropic/Gemini base URLs.

## Links

- **Website:** [https://ofox.ai](https://ofox.ai)
- **Documentation:** [https://docs.ofox.ai](https://docs.ofox.ai)
- **Console:** [https://app.ofox.ai](https://app.ofox.ai)
- **GitHub:** [https://github.com/ofoxai](https://github.com/ofoxai)
