___
<img src="assets/logo.png" width="auto" height="auto" />

___

# [Real](https://github.com/Azzrenz/Real)

Real is a local AI agent workbench for Windows. Give it a project folder and a one-line request — it reads the files, edits them, runs commands, checks the errors and keeps iterating until the task is actually delivered. Everything runs on your own machine; only the conversation is sent to the model API.

Built with Rust + Tauri 2 + React. MIT licensed.

## Why it is different

- **Convergence loop, not a chat window.** Every round either changes a real file or is recorded as no-op; a round that says "done" without touching anything does not count.
- **Every step is auditable.** Tool calls, file writes and command output are kept as cards you can reopen.
- **Approval gate for risky actions.** Deleting files or running shell commands asks you first.
- **Model switchable.** DeepSeek and Zhipu GLM are supported side by side; switch model without restarting.

## Integrate with DeepSeek API

Real talks to DeepSeek through the standard OpenAI-compatible endpoint. Setup takes about 30 seconds:

1. Open **Settings → Model & credentials**
2. **API key (DeepSeek)**: paste your key from [platform.deepseek.com](https://platform.deepseek.com/api_keys)
3. **API Base URL**: `https://api.deepseek.com`
4. **Model name**: `deepseek-flash`
5. Click **Test connection**, then **Save settings**

No restart needed — the next round uses DeepSeek immediately.

Optional: set `DEEPSEEK_API_KEY` in the `.env` file next to `real-client.exe` for a fully scripted install.

## What people use it for

- Batch renaming / reorganizing files by date or content
- Building a video pipeline: fetch clips → strip subtitles → rewrite copy → TTS → compose
- Asking for a new feature in plain language ("add a dark theme") and letting it implement across the codebase
- Any repetitive job you would otherwise click through by hand

## Links

- Source: https://github.com/Azzrenz/Real
- Download (Windows, portable 12 MB): https://github.com/Azzrenz/Real/releases
- License: MIT
