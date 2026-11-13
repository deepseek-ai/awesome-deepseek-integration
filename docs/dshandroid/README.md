# [DShAndroid](https://github.com/kekejiang114514/deepseek-harness-android)

DeepSeek Harness for Android — an Android agent client that runs DeepSeek **on the phone itself**. No Termux, no root, no PC: the APK bundles the agent loop, the tool runtime and the UI.

![Icon](assets/logo.png)

## Features

- **Tool calling** — deepseek's native `tools` / `tool_calls` protocol drives a shell, file I/O, a browser and screen automation.
- **Screen control via AccessibilityService** — read the view tree, tap, type, swipe, so the model can operate other apps on the device.
- **Automatic context compaction** — when history passes ~24k tokens the client compacts older turns and keeps the current task in focus, so long sessions do not hit the window limit.
- **Six-level thinking effort** — sent as `reasoning_effort` (`low` / `high` / `max`, per the Thinking Mode doc); the `off` level sends `thinking: {"type": "disabled"}`.
- **Model list read at runtime** — the picker queries `/models`, so `deepseek-flash` and `deepseek-v4-pro` appear without a client update.
- **Installable plugins**, prompt presets, an on-device terminal, a step-by-step virtual machine panel and a token usage panel.

## Integrate with the DeepSeek API

1. Get an API key from the [DeepSeek platform](https://platform.deepseek.com/api_keys).
2. Install the APK from the [Releases page](https://github.com/kekejiang114514/deepseek-harness-android/releases/latest) and open it.
3. Open **Settings → Model**, enter the API key. The base URL defaults to `https://api.deepseek.com` and only needs changing for a self-hosted gateway.
4. Tap the model pill above the input; the list is fetched from `/models`. Pick `deepseek-v4-pro` for reasoning-heavy work or `deepseek-flash` for speed.
5. Set the effort level next to the model name — this is the thinking depth actually sent to the API.

## Notes

- Screen automation needs the accessibility service enabled manually in system settings. Some Android skins delete a package's accessibility record when they force-stop the app; the client detects this on launch and offers a one-tap path back to the setting.
- Minimum Android 10 (API 29), arm64.
