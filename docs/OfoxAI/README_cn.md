# [OfoxAI](https://ofox.ai)

OfoxAI 是统一的大模型 API 网关，通过一个 OpenAI 兼容的 API 即可接入 DeepSeek R1、V3 及 50+ 其他主流模型（GPT、Claude、Gemini、Qwen、Kimi 等）。

## 核心特性

- **50+ 模型，一个 API** — 通过统一端点接入 DeepSeek、OpenAI、Anthropic、Google 等
- **三大原生协议** — 兼容 OpenAI、Anthropic、Gemini SDK，零代码改动即可迁移
- **自动故障转移** — 智能供应商路由，自动回退到备选模型
- **提示缓存** — 内置 Prompt Caching 支持，降低成本和延迟
- **国内直连** — 通过香港快速节点低延迟访问，无需科学上网
- **99.9% SLA** — 企业级稳定性，多区域部署
- **按量付费** — 无月费，Token 级计费，10+ 免费模型可用

## 快速开始

### OpenAI 兼容

```bash
export OPENAI_BASE_URL=https://api.ofox.ai/v1
export OPENAI_API_KEY=<你的 OfoxAI API Key>
```

### Anthropic 兼容

```bash
export ANTHROPIC_BASE_URL=https://api.ofox.ai/anthropic
export ANTHROPIC_AUTH_TOKEN=<你的 OfoxAI API Key>
```

### Gemini 兼容

```bash
export GEMINI_API_KEY=<你的 OfoxAI API Key>
# Base URL: https://api.ofox.ai/gemini
```

## DeepSeek 集成

OfoxAI 完整支持 DeepSeek 系列模型：

- **DeepSeek-R1** — 推理模型，支持思维链
- **DeepSeek-V3** — 高性能对话模型
- **DeepSeek-Coder** — 代码生成专用模型

在 API 调用中使用 `deepseek-r1`、`deepseek-v3` 或 `deepseek-coder` 作为模型 ID 即可。

## 兼容工具

OfoxAI 适配所有主流 AI 开发工具：

Claude Code、Cursor、Cline、Cherry Studio、Zed、OpenClaw、Codex CLI、Gemini CLI、OpenCode、Windsurf、Aider，以及任何支持自定义 OpenAI/Anthropic/Gemini base URL 的工具。

## 链接

- **官网：** [https://ofox.ai](https://ofox.ai)
- **文档：** [https://docs.ofox.ai](https://docs.ofox.ai)
- **控制台：** [https://app.ofox.ai](https://app.ofox.ai)
- **GitHub：** [https://github.com/ofoxai](https://github.com/ofoxai)
