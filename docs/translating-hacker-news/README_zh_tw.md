<img src="https://aidoge.ai/resource/TranslatingHackerNewsIcon.jpg" width="64" height="auto" />

# 黑客新聞翻譯

使用說明與現場演示：[https://aidoge.ai/zh-hant/translating_hacker_news_intro.html](https://aidoge.ai/zh-hant/translating_hacker_news_intro.html)

**黑客新聞翻譯（Translating Hacker News）** 是一款 iOS 上的 Hacker News 閱讀器，可將故事、評論和外鏈文章就地翻譯。App 接入 **DeepSeek 官方 API**（自備 Key），因為 DeepSeek 回應快、成本低，並且允許你改寫適合 HN 討論的提示詞。

## 介面預覽

<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/28/1d/ce/281dce89-5095-8eae-096f-19b8d89b775c/iPhone_16_Pro_Max-01-app-launched.png/686x1024bb.jpg" width="280" alt="就地資訊流翻譯" />
<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/05/bb/62/05bb6242-d4cd-a2a8-49d7-25671285f60c/iPhone_16_Pro_Max-04-agent-configuration.png/686x1024bb.jpg" width="280" alt="DeepSeek 引擎設定" />

## 為什麼用 DeepSeek

- **快**：預設 `deepseek-v4-flash`，刷資訊流和展開評論樹時都能跟上閱讀節奏。
- **便宜**：自備 Key，持續翻譯標題和長討論的成本更低。
- **可改提示詞**：可編輯翻譯提示詞（以及 Temperature / Top P），讓譯文更貼合 HN 的技術討論語氣。

## 接入 DeepSeek API

在 App 內打開 **設定 → AI Agent**，選擇 DeepSeek，填入 [DeepSeek 開放平台](https://platform.deepseek.com/api_keys) 的 API Key 即可。
