<img src="./assets/logo.png" width="64" height="auto" />

# [AhaKnow Chat](https://github.com/IHKYoung/AhaKnowChat)

AhaKnow Chat 是一個本地優先的 AI 對話工作台，可透過任何 OpenAI-compatible API 直接接入 DeepSeek。它支援以話題與執行緒組織對話、重複使用角色、多角色同時對話，以及瀏覽器本地儲存。

## 介面

<img src="./assets/home.png" />

## 使用過程

<img src="./assets/usage.png" />

## 設定畫面

<img src="./assets/settings.png" />

## 配置 DeepSeek API

由於 AhaKnow Chat 以 OpenAI-compatible API 為基礎設計，因此接入 DeepSeek 不需要額外的後端程式碼。

### 配置步驟

1. 開啟 `Settings`，進入 `AI 提供商` 分頁。
2. 將 `Base URL` 設為 `https://api.deepseek.com`。
3. 在 `API Key` 欄位填入你自己的 DeepSeek API Key。
4. 點擊 `測試連線`，驗證介面可用並抓取模型清單。
5. 選擇預設模型：
   - `deepseek-chat` 適合日常對話與一般用途
   - `deepseek-reasoner` 適合更強的推理任務
6. 儲存設定後，建立話題與執行緒，即可開始使用 DeepSeek 對話。

### 補充說明

- Web 版會將設定保存在瀏覽器本地。
- 若將 Web 版部署到 Vercel，目標 DeepSeek 端點需要允許瀏覽器請求與 CORS。
- 只要提供 OpenAI-compatible API，也可以透過相容的閘道或代理接入 DeepSeek。
