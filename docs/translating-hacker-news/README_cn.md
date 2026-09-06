<img src="https://aidoge.ai/resource/TranslatingHackerNewsIcon.jpg" width="64" height="auto" />

# 黑客新闻翻译

使用说明与现场演示：[https://aidoge.ai/zh/translating_hacker_news_intro.html](https://aidoge.ai/zh/translating_hacker_news_intro.html)

**黑客新闻翻译（Translating Hacker News）** 是一款 iOS 上的 Hacker News 阅读器，可将故事、评论和外链文章就地翻译。App 接入 **DeepSeek 官方 API**（自备 Key），因为 DeepSeek 响应快、成本低，并且允许你改写适合 HN 讨论的提示词。

## 界面预览

<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/28/1d/ce/281dce89-5095-8eae-096f-19b8d89b775c/iPhone_16_Pro_Max-01-app-launched.png/686x1024bb.jpg" width="280" alt="就地信息流翻译" />
<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/05/bb/62/05bb6242-d4cd-a2a8-49d7-25671285f60c/iPhone_16_Pro_Max-04-agent-configuration.png/686x1024bb.jpg" width="280" alt="DeepSeek 引擎配置" />

## 为什么用 DeepSeek

- **快**：默认 `deepseek-v4-flash`，刷信息流和展开评论树时都能跟上阅读节奏。
- **便宜**：自备 Key，持续翻译标题和长讨论的成本更低。
- **可改提示词**：可编辑翻译提示词（以及 Temperature / Top P），让译文更贴合 HN 的技术讨论语气。

## 接入 DeepSeek API

在 App 内打开 **设置 → AI Agent**，选择 DeepSeek，填入 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 的 API Key 即可。
