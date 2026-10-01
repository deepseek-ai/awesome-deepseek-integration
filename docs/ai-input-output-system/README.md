# [AI Input/Output System](https://github.com/1person280/ai-input-output-system)

A local-first AI request router for VS Code. Simple prompts are answered on-device by a 4B INT8 model served through `llama.cpp`; only genuinely complex requests are forwarded to an OpenAI-compatible cloud endpoint such as DeepSeek.

## Why route at all

Every keystroke-sized AI question ("format this", "add a docstring", "rename this variable") costs a cloud round-trip. A 4B INT8 model with a 64K context window handles those comfortably on-device, so paid cloud tokens can be reserved for the requests that actually need them.

## How routing works

1. **Classify** — a token estimate (CJK-aware), multi/cross-file detection and complex/simple intent keywords produce a `complexity` score in `[0, 1]`.
2. **Decide** — below `aiio.routingThreshold` the request stays local; above it, it goes to the cloud.
3. **Execute** — local requests hit a running `llama-server`; failures fall back to the cloud so an answer is always returned.
4. **Measure** — every decision is appended to a ledger that feeds a status bar and a savings dashboard.

## Integrate with DeepSeek API

Point the cloud endpoint at DeepSeek through the OpenAI-compatible settings:

| Setting | Value |
| --- | --- |
| `aiio.cloudBaseUrl` | `https://api.deepseek.com` |
| `aiio.cloudModel` | `deepseek-chat` |
| `aiio.cloudApiKey` | your DeepSeek API key |

Only requests classified as complex reach DeepSeek; everything else is answered locally.

## Features

- Local 4B model for simple prompts, cloud fallback for everything else
- Savings dashboard: cloud calls avoided, token savings ratio, estimated cost avoided
- Adaptive routing from in-editor feedback
- Autonomous file creation from a natural-language requirement (local → cloud → offline heuristic)

## Links

- Repository: <https://github.com/1person280/ai-input-output-system>
- License: MIT