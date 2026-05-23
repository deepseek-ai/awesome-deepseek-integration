<img src="assets/logo.svg" width="64" height="auto" />

# [LeAgent](https://github.com/vixues/LeAgent)

LeAgent is an open-source desktop AI agent that combines multi-turn chat, a visual workflow builder, 100+ built-in tools, Agent Skills, MCP, and a declarative rule engine — all in a single self-hostable stack.

## Features

- **Agent runtime** — multi-turn sessions with streaming, tool execution, tiered model routing, layered prompts, and cognitive memory (episodic / semantic / procedural)
- **100+ offline tools** — documents, web, data, code execution, databases, generative UI, and more
- **Visual workflows** — ReactFlow editor with YAML export, templates, and every tool as a typed node
- **Agent Skills** — Agent Skills v1.0 SKILL.md bundles with progressive disclosure and on-demand loading
- **MCP support** — Model Context Protocol integration
- **Multi-provider LLM** — DeepSeek, DashScope (Qwen), OpenAI, Anthropic, Ollama, vLLM, and more

## Integrate with DeepSeek API

LeAgent natively supports DeepSeek as a first-class LLM provider. DeepSeek is the most thoroughly validated provider and is recommended for first use.

Configure in Settings → Provider Management → add DeepSeek with your API key.

## Screenshot

<img src="https://i.imgur.com/rcNFnFd.png" width="720" />

## Download & Get Started

- Homepage: https://github.com/vixues/LeAgent
- Releases: https://github.com/vixues/LeAgent/releases
- Quick start:
  ```bash
  git clone https://github.com/vixues/LeAgent.git
  cd LeAgent
  ./start.sh
  ```
