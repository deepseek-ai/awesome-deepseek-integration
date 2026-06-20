# AFK

[AFK](https://afk.mooglest.com) is a browser-based command center for persistent coding-agent sessions. It supports DeepSeek as a built-in LLM connection, so you can bring your DeepSeek API key, choose a DeepSeek model per session, and supervise agent work from the web UI.

## Setup

1. Create or sign in to [AFK](https://afk.mooglest.com).
2. Install and connect an AFK daemon on the machine that has access to your project files.
3. Open **Account → LLM** in AFK.
4. Add a **DeepSeek** connection and paste your DeepSeek API key.
5. Leave **Base URL** blank unless you use a custom proxy or gateway.
6. Start a new AFK session, choose the DeepSeek connection, and select or type a DeepSeek model name such as `deepseek-v4-pro` or `deepseek-v4-flash`.

AFK uses DeepSeek's default OpenAI-compatible endpoint automatically for the built-in DeepSeek provider.

## Resources

- [AFK](https://afk.mooglest.com)
- [AFK DeepSeek setup docs](https://docs.mooglest.com/providers#deepseek)
- [DeepSeek Open Platform](https://platform.deepseek.com/)
