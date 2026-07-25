<div align="center">
  <img src="assets/icon.png" alt="Astra Translate" width="96" />

# Astra Translate

A lightweight, elegant, provider-neutral browser translation extension.

[GitHub](https://github.com/avaritiachaos/astra-translate-extension) · [Releases](https://github.com/avaritiachaos/astra-translate-extension/releases) · [中文文档](README_cn.md)

</div>

## Introduction

Astra Translate is an open-source (MIT) Chrome extension (Manifest V3) that turns any OpenAI-compatible LLM API into a fast, careful webpage translator. It ships with a built-in **DeepSeek preset** — paste your API key and it works out of the box.

## Features

- **Full-page translation, viewport-first** — translates what you can see first, then the rest as you scroll; optional whole-page mode. Streaming batch apply paints each passage as the model emits it.
- **Block-level grouping** — fragments of one paragraph are translated together as a coherent passage, preserving inline markup.
- **Selection translation & dictionary mode** — select text for instant translation; single words get a dictionary card (meanings, pronunciation, examples). URLs, code, paths and hashes are auto-protected from translation.
- **Instant UI lexicons** — a built-in lexicon plus per-site learned glossaries render common buttons/labels with zero API latency on revisits.
- **Robust under load** — adaptive concurrency with 429/5xx backoff that honours `Retry-After`, translation caching, and honest error reporting.
- **Trilingual UI** — Simplified Chinese / English / Japanese.

## Integrate with DeepSeek API

1. Get an API key from the [DeepSeek Open Platform](https://platform.deepseek.com/).
2. Install Astra Translate (download from [Releases](https://github.com/avaritiachaos/astra-translate-extension/releases), then load the unpacked build via `chrome://extensions` → Developer mode → Load unpacked).
3. Open the extension **Settings** page — DeepSeek is the default provider preset (`https://api.deepseek.com`).
4. Paste your API key, pick a model (e.g. `deepseek-chat`), and click **Test**.
5. Translate: click **Translate this page** in the popup, select text on any page, or press `Alt+T` on a selection.

DeepSeek-specific extras: the settings page exposes DeepSeek's thinking toggle, so you can disable reasoning output for faster, cheaper page translation.
