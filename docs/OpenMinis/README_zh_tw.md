# OpenMinis

<div align="center">
<img src="assets/logo.png" alt="OpenMinis" width="96" height="auto" />

**你的私有端側 AI Agent —— 不只是聊天，它會真正動手做事**

</div>

[GitHub](https://github.com/OpenMinis/OpenMinis) · [官網](https://openminis.app) · [App Store](https://apps.apple.com/) · [Telegram 社群](https://t.me/openminis)

---

## 這是什麼

OpenMinis 是一款**完全免費、完全開源（GPL-3.0）**的跨平台 AI Agent 應用，覆蓋 **iOS、iPadOS、macOS、Android**（及 visionOS），GitHub 上已收穫 **3.3k+ stars**。

它的理念與一般 AI 聊天應用截然不同：不只是把大模型封裝進一個對話框，而是給模型**一台真正的電腦**——裝置本地運行著完整的 Linux 環境，模型可以安裝套件、執行腳本、讀寫檔案、操作瀏覽器、呼叫系統能力，真正替你完成任務。

## 核心特性

| 特性 | 說明 |
|------|------|
| 🤖 自帶模型（BYO Model） | 接入 Anthropic Claude、OpenAI GPT、Google Gemini、OpenRouter，以及 **DeepSeek 等任意 OpenAI 相容 API**，依對話自由切換 |
| 🐚 內建 Linux Shell | 裝置端運行沙箱化 Alpine Linux（iOS 基於 iSH / Android 基於 PRoot），可 `apk add` 安裝套件、跑腳本、處理真實檔案，無需伺服器 |
| 📱 深度系統整合 | HealthKit、行事曆、提醒事項、通訊錄、HomeKit、藍牙、剪貼簿、媒體、鬧鐘等原生能力以工具形式開放給 Agent |
| 🌐 瀏覽器自動化 | Agent 可替你瀏覽網頁、填寫表單、提取內容、截圖 |
| 🛠️ 技能系統（Skills） | 開放 SKILL.md 格式，可匯入/建立技能擴充能力；相容 Claude、Codex、OpenClaw 等生態技能，即裝即用 |
| 🧠 持久記憶 | 跨會話記憶，越用越懂你 |
| 📂 Workspaces | 依任務組織獨立上下文，透過 `minis://workspace/` 定址 |
| 🔒 隱私優先 | API Key 存於系統鑰匙圈（Keychain），無資料收集、無第三方分析，對話只屬於你 |

## 技術架構

倉庫結構（Swift 51% / Kotlin 41% / Objective-C 6%）：

```
src/ios/          iOS 應用（Swift/SwiftUI）+ Share、Widget、檔案提供器擴充
src/android/      Android 應用（Kotlin/Compose）+ JNI 原生程式碼
src/shared/       雙平台共享資源
deps/             原生依賴建置腳本（iSH、PRoot、FFmpeg、LAME）
docs/specs/       架構與介面規範
scripts/          Rootfs 準備與開發者工具
```

關鍵依賴：**iSH**（iOS 的 Linux 使用者態模擬，ARM64 fork）、**PRoot**（Android 沙箱的使用者態 chroot）、**Alpine Linux**（沙箱系統）、FFmpeg、LAME 等，均從原始碼建置而非提交二進位。

## 真實使用場景

- 📸 拍一張餐食照片，辨識菜色、估算熱量並寫入 Apple Health
- ⏰ 用捷徑觸發：拉取 X 時間軸 → 產生摘要 → 語音合成 → 作為鬧鐘叫你起床
- 💬 從 Telegram 群聊中提取 Bug 與待辦事項，去重後歸檔進 Apple Reminders
- 📓 掛載 Obsidian 倉庫，研究、整理並直接寫回 Markdown 筆記
- 📅 透過 iOS 分享面板把網頁/訊息一鍵變成附時間地點的行事曆事件

## 媒體報導

> "the most impressive indie app I've seen in a while"
> —— Federico Viticci, MacStories（2026-07）

> "在很大程度上實現甚至局部超越了 Apple Intelligence"
> —— 知乎（2026-06）

> "可能是 iOS 端最強 AI Agent"
> —— 小众软件 / Appinn（2026-03）

## 開源生態

OpenMinis 組織（github.com/OpenMinis）下還有：

- **[MinisSkills](https://github.com/OpenMinis/MinisSkills)**（354⭐）—— 官方技能集合，40+ 個 SKILL.md 技能：GitHub 趨勢、Twitter/X、Bilibili、睡眠健康分析、PPT 產生、qBittorrent、12306 購票、豆包 TTS 等
- **[AwesomeMinis](https://github.com/OpenMinis/AwesomeMinis)**（190⭐）—— 社群真實用例合集（健康、效率、研究、金融、開發者工具）
- **ish-arm64 / proot** —— iSH 與 PRoot 的客製 fork

## 授權

GPL-3.0。應用連結了 GPL 元件（iSH、PRoot），因此整體以 GPLv3 散佈。倉庫為私有開發樹的鏡像，不接受 PR，歡迎透過 Issues 回饋與共建。
