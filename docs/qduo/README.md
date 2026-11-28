<div align="center">
  <img src="./assets/logo.png" alt="QDuo" width="96" />
  <h1>QDuo</h1>
  <p>
    <a href="https://github.com/XueshiQiao/qduo">GitHub</a> ·
    <b>English</b> ·
    <a href="./README_cn.md">简体中文</a>
  </p>
</div>

**QDuo** is an open-source (GPL v3.0), native macOS (macOS 13+) selection action and AI popup app. Select text in any Mac app, and your actions appear right at the cursor — translate, polish with diff-before-replace, explain, summarize, read aloud, run local text transforms, or ask an LLM — and put the result straight back in place.

<div align="center">
  <img src="./assets/popup-ring-en.jpg" width="800" alt="QDuo selection popup ring" />
</div>

## Key Features

- **Cursor Popup Styles**: Choose between **Liquid Glass** (ring), **3D Glass** (tilting ring), and **Capsule** (horizontal bar), with support for nested action groups.
- **Built-in AI Actions & Per-Action Models**: Ships with Translate, Polish, and Explain, plus templates for Summarize, Fix Grammar, Change Tone, Break Down Sentence, Explain Code, and custom prompts. Each action can use its own model.
- **Diff-Before-Replace**: Review word-level additions and deletions directly in the popup before writing changes back to the active input field.
- **Screen OCR & Local Tools**: Capture text from images or videos (`⌘⇧S`), run 22 offline text transformations, or trigger Shortcuts and shell scripts.
- **History & Privacy**: Full local action history stored on your Mac. API keys are stored exclusively in the macOS Keychain, never in the JSON config file.

## Installation

Install via Homebrew:

```bash
brew install --cask XueshiQiao/tap/qduo
```

Or download `QDuo.dmg` from [GitHub Releases](https://github.com/XueshiQiao/qduo/releases).

## Using QDuo with DeepSeek

1. Launch **QDuo** — **DeepSeek** is built in as the default AI provider, preconfigured with `https://api.deepseek.com`.
2. In the onboarding guide or **Settings → AI Models**, make sure **DeepSeek** is selected, paste your API key from the [DeepSeek Open Platform](https://platform.deepseek.com/), and click **Test**.
3. Select text in any app and click **Translate**, **Polish**, **Explain**, or any custom AI prompt action to run it with DeepSeek right at your cursor.
