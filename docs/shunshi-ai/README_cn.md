<img src="assets/logo.png" width="64" height="auto" style="border-radius: 15px" />

# [顺时 AI (Shunshi.AI)](https://shunshi.ai)

顺时 AI 是一个对话式中国命理助手：根据用户的出生信息计算出八字（四柱 / 四柱推命 / 사주팔자）命盘，然后围绕这张已经算好的命盘回答人生规划、事业、感情等问题。对话推理层由 DeepSeek API 驱动。支持中文 / English / 日本語 / 한국어 多语言界面与回复。

## 与 DeepSeek API 的集成方式

顺时 AI 当前在问答层使用 `deepseek-chat`，未来会切换到 `deepseek-reasoner`，对复杂命盘做更深入的多步推理。

系统会把计算好的八字命盘（天干、地支、四柱，以及经过真太阳时修正的准确时刻）拼入 system context，这样大模型的回答是基于已经核算过的天文数据来推演，而不是自己去臆测。

## 开源排盘引擎

顺时 AI 所使用的底层排盘引擎同时以开源 MCP server 的形式提供，可以直接嵌进 Claude Desktop / Cursor / Cline 本地使用：

- GitHub: https://github.com/shunshi-ai/bazi-reader-mcp
- npm: `npm i shunshi-bazi-mcp`

## 主页

- Web 应用: https://shunshi.ai
