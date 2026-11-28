# [多问AI](https://www.duowen.app)

Hosted multi-model AI Q&A product (English brand Askmore). Users do not bring their own API keys; usage is billed in credits.

Official site: https://www.duowen.app

## English

**Features (available in the product today)**

- **Automatic model routing.** In Auto mode, the service chooses a main model for the question and decides whether to ask additional models the same question. Users can also pick a model manually. Auto has preference settings: balanced, quality-first, or save-credits.
- **Multi-model comparison.** The same question can be sent to several models (for example GPT, Claude, Gemini, and DeepSeek) in one place.
- **Agreement and difference analysis.** The product organizes what the models said in common and where they differ, so disagreements are easier to notice.
- **Merge into one answer (optional).** Useful points from the other models can be merged into a single answer, with a record of what was added; the original answers remain available.
- **Web search when needed.** The product can judge whether a question needs fresh sources and search automatically (this can be turned off). Search calls the official DeepSeek Search API.
- **Expandable key points and claim verification.** Each answer can be condensed into expandable key points. Optionally, claims in the answer can be checked against sources.
- Attachments are preprocessed on the server. Clients include the web app plus iOS, Mac, and Android.

**How DeepSeek is used**

- Web search calls the official DeepSeek Search API.
- DeepSeek is available as a catalog chat model (currently DeepSeek v4.1 Flash).
- DeepSeek v4.1 Flash is also the default model for key points and for claim verification.

This is a hosted product: end users do not paste a DeepSeek API key into 多问AI. The service calls the DeepSeek API on their behalf.

## 简体中文

**多问AI**（duowen.app，英文品牌 Askmore）是托管式多模型 AI 问答产品。用户不必自备 API Key，按点数使用。

官网：https://www.duowen.app

**今天产品里可以用的能力**

- **自动选模型。** 在「自动」模式下，系统按题目选择主答模型，并决定要不要一起问其他模型。用户也可以手动指定模型。「自动」可在设置里选择均衡、质量优先或省点数。
- **多模型对比。** 同一个问题可以一次交给多家模型（例如 GPT、Claude、Gemini、DeepSeek），在同一处对照。
- **异同分析。** 系统会整理各家「都这么说」的地方和「不一样的地方」，方便看到补充角度和分歧。
- **融合成一个回答（可选）。** 可以把别家补充得好的地方融合成一个回答，并写明增加了什么；原来的回答都还在，可以切回。
- **需要时联网搜索。** 系统会判断这道题是否需要新资料，需要时自动搜索（也可以关闭）。搜索调用官方 DeepSeek Search API。
- **可展开的要点，以及主张核验。** 回答可以提炼成可展开的要点；也可以把主张逐条对照出处做核验。
- 附件在服务端预处理。提供网页以及 iOS、Mac、安卓客户端。

**如何使用 DeepSeek**

- 联网搜索调用官方 DeepSeek Search API。
- 模型目录中提供 DeepSeek（当前为 DeepSeek v4.1 Flash）。
- 要点提炼和主张核验的默认模型也是 DeepSeek v4.1 Flash。

多问AI 是托管产品：终端用户不需要在产品里填写 DeepSeek API Key，由服务端调用 DeepSeek API。
