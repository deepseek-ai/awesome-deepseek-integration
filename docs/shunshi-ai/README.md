<img src="assets/logo.png" width="64" height="auto" style="border-radius: 15px" />

# [Shunshi.AI](https://shunshi.ai)

Shunshi.AI is a conversational Chinese-metaphysics assistant: it computes a Bazi (四柱 / 四柱推命 / 사주팔자) chart from the user's birth details and answers life-path, career, and relationship questions grounded in that chart. The reasoning layer is powered by the DeepSeek API. Multilingual — interface and answers available in 中文 / English / 日本語 / 한국어.

## Integrate with DeepSeek API

Shunshi.AI currently uses `deepseek-chat` for the question-answering layer, and is planned to move to `deepseek-reasoner` for deeper multi-step inference on complex charts.

The computed Bazi chart (stems, branches, pillars, and true-solar-time corrected timestamps) is included in the system context so the model can reason against verified astronomical data instead of inventing it.

## Open-source engine

The underlying calculation engine that Shunshi.AI uses is also available as an open-source MCP server, so the same chart math can be run locally inside Claude Desktop / Cursor / Cline:

- GitHub: https://github.com/shunshi-ai/bazi-reader-mcp
- npm: `npm i shunshi-bazi-mcp`

## Homepage

- Web app: https://shunshi.ai
