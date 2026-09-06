<img src="https://aidoge.ai/resource/TranslatingHackerNewsIcon.jpg" width="64" height="auto" />

# Translating Hacker News

Setup and live demo: [https://aidoge.ai/translating_hacker_news_intro.html](https://aidoge.ai/translating_hacker_news_intro.html)

**Translating Hacker News** is an iOS Hacker News reader that translates stories, comments, and linked articles in place. It uses the official **DeepSeek API** (BYOK) because DeepSeek is fast, low-cost, and lets you edit the translation prompt to fit HN discussions.

## UI

<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/5e/82/ea/5e82ea84-ad70-6785-8e6e-e56ea962df2d/iPhone_16_Pro_Max-01-app-launched.png/686x1024bb.jpg" width="280" alt="In-place feed translation" />
<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/d5/5b/7a/d55b7a61-80de-7f23-5e2d-265b55a3feb0/iPhone_16_Pro_Max-04-agent-configuration.png/686x1024bb.jpg" width="280" alt="DeepSeek agent configuration" />

## Why DeepSeek

- **Fast**: Default `deepseek-v4-flash` keeps titles and comment trees translating as you scroll.
- **Low cost**: BYOK pricing stays cheap enough for continuous feed and thread translation.
- **Custom prompts**: Edit the translation prompt (and temperature / Top P) so the tone matches technical HN discussions.

## Integrate with DeepSeek API

Open **Settings → AI Agent**, choose DeepSeek, and save your key from [DeepSeek Open Platform](https://platform.deepseek.com/api_keys).
