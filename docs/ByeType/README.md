<img src="./assets/logo.png" width="64" height="auto" />

# [ByeType](https://github.com/lixiaojie001/byetype)

**Stop typing. Just speak.**

ByeType is an AI-powered voice input and image text extraction tool driven by editable Markdown prompts. By customizing the prompts, you can teach the AI your industry jargon, proper nouns, and personal writing style — so the output matches the way you actually work.

ByeType talks to AI providers via standard APIs and supports DeepSeek alongside other multimodal models — bring your own API key, your audio and screenshots go straight from your machine to the provider you choose.

## Features

- 🎙️ **Voice to text** — press a hotkey, speak, get clean text auto-pasted into any app
- 🖼️ **Image text extraction** — press F6 to capture a region, AI reads the text and copies it to your clipboard. Smart enough to merge hard line breaks in terminal/PDF screenshots and reconstruct code blocks split by line numbers
- 📝 **Markdown-driven prompts** — vocabulary, formatting rules, and tone are all editable Markdown files. Switch between styles (casual, formal, translation, email polish, etc.) with different hotkeys
- 🌐 **Cross-platform** — macOS, Windows, and iPhone / iPad via iOS Shortcuts
- 🪶 **Lightweight** — ~8 MB install, no local model files

## Demo

![Record → Transcribe → Polish → Auto-paste](./assets/demo.gif)

## Configure DeepSeek

In **Settings → Model Management**, add a DeepSeek model with your API key from [DeepSeek Open Platform](https://platform.deepseek.com/). Built-in presets include `deepseek-v4-flash` and `deepseek-v4-pro` for fast, low-cost text polishing.

For voice and screenshot capture, ByeType also supports multimodal models such as Qwen Omni, Gemini, LongCat, and any OpenAI-compatible endpoint — all configured the same way.

## Links

- GitHub: <https://github.com/lixiaojie001/byetype>
- Releases: <https://github.com/lixiaojie001/byetype/releases>
- License: MIT
