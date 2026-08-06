# OpenMinis

<div align="center">
<img src="assets/logo.png" alt="OpenMinis" width="96" height="auto" />

**你的私有端侧 AI Agent —— 不只是聊天，它会真正动手做事**

</div>

[GitHub](https://github.com/OpenMinis/OpenMinis) · [官网](https://openminis.app) · [App Store](https://apps.apple.com/) · [Telegram 社区](https://t.me/openminis)

---

## 这是什么

OpenMinis 是一款**完全免费、完全开源（GPL-3.0）**的跨平台 AI Agent 应用，覆盖 **iOS、iPadOS、macOS、Android**（及 visionOS），GitHub 上已收获 **3.3k+ stars**。

它的理念与普通 AI 聊天应用截然不同：不只是把大模型封装进一个对话框，而是给模型**一台真正的电脑**——设备本地运行着完整的 Linux 环境，模型可以安装软件包、执行脚本、读写文件、操作浏览器、调用系统能力，真正替你完成任务。

## 核心特性

| 特性 | 说明 |
|------|------|
| 🤖 自带模型（BYO Model） | 接入 Anthropic Claude、OpenAI GPT、Google Gemini、OpenRouter，以及 **DeepSeek 等任意 OpenAI 兼容 API**，按对话自由切换 |
| 🐚 内置 Linux Shell | 设备端运行沙箱化 Alpine Linux（iOS 基于 iSH / Android 基于 PRoot），可 `apk add` 装包、跑脚本、处理真实文件，无需服务器 |
| 📱 深度系统集成 | HealthKit、日历、提醒事项、通讯录、HomeKit、蓝牙、剪贴板、媒体、闹钟等原生能力以工具形式开放给 Agent |
| 🌐 浏览器自动化 | Agent 可替你浏览网页、填写表单、提取内容、截图 |
| 🛠️ 技能系统（Skills） | 开放 SKILL.md 格式，可导入/创建技能扩展能力；兼容 Claude、Codex、OpenClaw 等生态技能，即装即用 |
| 🧠 持久记忆 | 跨会话记忆，越用越懂你 |
| 📂 Workspaces | 按任务组织独立上下文，通过 `minis://workspace/` 寻址 |
| 🔒 隐私优先 | API Key 存于系统钥匙串（Keychain），无数据收集、无第三方分析，对话只属于你 |

## 技术架构

仓库结构（Swift 51% / Kotlin 41% / Objective-C 6%）：

```
src/ios/          iOS 应用（Swift/SwiftUI）+ Share、Widget、文件提供器扩展
src/android/      Android 应用（Kotlin/Compose）+ JNI 原生代码
src/shared/       双平台共享资源
deps/             原生依赖构建脚本（iSH、PRoot、FFmpeg、LAME）
docs/specs/       架构与接口规范
scripts/          Rootfs 准备与开发者工具
```

关键依赖：**iSH**（iOS 的 Linux 用户态模拟，ARM64 fork）、**PRoot**（Android 沙箱的用户态 chroot）、**Alpine Linux**（沙箱系统）、FFmpeg、LAME 等，均从源码构建而非提交二进制。

## 真实使用场景

- 📸 拍一张餐食照片，识别菜品、估算热量并写入 Apple Health
- ⏰ 用快捷指令触发：拉取 X 时间线 → 生成摘要 → 语音合成 → 作为闹钟叫你起床
- 💬 从 Telegram 群聊中提取 Bug 与待办事项，去重后归档进 Apple Reminders
- 📓 挂载 Obsidian 仓库，研究、整理并直接写回 Markdown 笔记
- 📅 通过 iOS 分享面板把网页/消息一键变成带时间地点的日历事件

## 媒体报道

> "the most impressive indie app I've seen in a while"
> —— Federico Viticci, MacStories（2026-07）

> "在很大程度上实现甚至局部超越了 Apple Intelligence"
> —— 知乎（2026-06）

> "可能是 iOS 端最强 AI Agent"
> —— 小众软件 / Appinn（2026-03）

## 开源生态

OpenMinis 组织（github.com/OpenMinis）下还有：

- **[MinisSkills](https://github.com/OpenMinis/MinisSkills)**（354⭐）—— 官方技能集合，40+ 个 SKILL.md 技能：GitHub 趋势、Twitter/X、Bilibili、睡眠健康分析、PPT 生成、qBittorrent、12306 购票、豆包 TTS 等
- **[AwesomeMinis](https://github.com/OpenMinis/AwesomeMinis)**（190⭐）—— 社区真实用例合集（健康、效率、研究、金融、开发者工具）
- **ish-arm64 / proot** —— iSH 与 PRoot 的定制 fork

## 许可证

GPL-3.0。应用链接了 GPL 组件（iSH、PRoot），因此整体以 GPLv3 分发。仓库为私有开发树的镜像，不接受 PR，欢迎通过 Issues 反馈与共建。
