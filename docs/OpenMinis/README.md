# OpenMinis

<div align="center">
<img src="assets/logo.png" alt="OpenMinis" width="96" height="auto" />

**Your private on-device AI agent — it doesn't just chat, it takes action**

</div>

[GitHub](https://github.com/OpenMinis/OpenMinis) · [Website](https://openminis.app) · [App Store](https://apps.apple.com/) · [Telegram Community](https://t.me/openminis)

---

## What is it

OpenMinis is a **free, fully open-source (GPL-3.0)** cross-platform AI agent for **iOS, iPadOS, macOS, Android** (and visionOS), with **3.3k+ stars** on GitHub.

Its philosophy is fundamentally different from ordinary AI chat apps: instead of wrapping a model in a chat window, it gives the model **a real computer** — a complete Linux environment running locally on your device, where the model can install packages, execute scripts, read and write files, drive a browser, and call native system capabilities to actually get things done for you.

## Key Features

| Feature | Description |
|---------|-------------|
| 🤖 Bring Your Own Model | Connect to Anthropic Claude, OpenAI GPT, Google Gemini, OpenRouter, and **DeepSeek or any OpenAI-compatible API**, with per-conversation model switching |
| 🐚 Built-in Linux Shell | Sandboxed Alpine Linux runs on-device (iSH on iOS / PRoot on Android) — `apk add` packages, run scripts, process real files, no server needed |
| 📱 Deep System Integration | HealthKit, Calendar, Reminders, Contacts, HomeKit, Bluetooth, Clipboard, Media, Alarms and more exposed to the agent as tools |
| 🌐 Browser Automation | The agent browses the web, fills forms, extracts content, and takes screenshots on your behalf |
| 🛠️ Skills Ecosystem | Open SKILL.md format — import or create skills; compatible with Claude, Codex, OpenClaw and other skill ecosystems |
| 🧠 Persistent Memory | Cross-session memory that gets to know you better over time |
| 📂 Workspaces | Organize work into separate contexts, addressable via `minis://workspace/` |
| 🔒 Privacy by Design | API keys stored in the system Keychain. No data collection. No third-party analytics. Your conversations are yours |

## Technical Architecture

Repository layout (Swift 51% / Kotlin 41% / Objective-C 6%):

```
src/ios/          iOS app (Swift/SwiftUI) + share, widget and file-provider extensions
src/android/      Android app (Kotlin/Compose) + JNI native code
src/shared/       Assets shared by both platforms
deps/             Native dependency build scripts (iSH, PRoot, FFmpeg, LAME)
docs/specs/       Architecture and interface specifications
scripts/          Rootfs preparation and developer tooling
```

Key dependencies: **iSH** (Linux usermode emulation on iOS, ARM64 fork), **PRoot** (user-space chroot for the Android sandbox), **Alpine Linux** (the minirootfs the sandbox boots), FFmpeg, LAME — all built from source rather than committed as binaries.

## Real-World Use Cases

- 📸 Photograph a meal, log the nutrition — identifies dishes, estimates calories and macros, writes them to Apple Health
- ⏰ Wake up to your timeline — Shortcuts triggers Minis to fetch your X timeline, summarise it, synthesise speech, and play it as your alarm
- 💬 Turn group chatter into tasks — pull messages from a Telegram group, extract bugs and action items, deduplicate them, file them into Apple Reminders
- 📓 Mount your Obsidian vault — research, clean up and write Markdown notes back into the vault
- 📅 Share anything into a calendar event — via the iOS Share Sheet, with time and place included

## Press

> "the most impressive indie app I've seen in a while"
> —— Federico Viticci, MacStories (July 2026)

> "在很大程度上实现甚至局部超越了 Apple Intelligence"
> —— Zhihu (June 2026)

> "可能是 iOS 端最强 AI Agent"
> —— Appinn (March 2026)

## Open-Source Ecosystem

Under the OpenMinis organization (github.com/OpenMinis):

- **[MinisSkills](https://github.com/OpenMinis/MinisSkills)** (354⭐) — official skills collection, 40+ SKILL.md skills: GitHub Trending, Twitter/X, Bilibili, sleep health analysis, PPT generation, qBittorrent, 12306 tickets, Doubao TTS and more
- **[AwesomeMinis](https://github.com/OpenMinis/AwesomeMinis)** (190⭐) — community-curated real-world use cases (health, productivity, research, finance, developer tooling)
- **ish-arm64 / proot** — customized forks of iSH and PRoot

## License

GPL-3.0. The app links GPL-licensed components (iSH, PRoot), so the combined work is distributed under GPLv3. The repository is a mirror of a private development tree — it does not accept pull requests; Issues are the way to shape the product.
