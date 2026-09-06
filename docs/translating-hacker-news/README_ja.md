<img src="https://aidoge.ai/resource/TranslatingHackerNewsIcon.jpg" width="64" height="auto" />

# Translating Hacker News

セットアップとライブデモ：[https://aidoge.ai/ja/translating_hacker_news_intro.html](https://aidoge.ai/ja/translating_hacker_news_intro.html)

**Translating Hacker News** は、ストーリー、コメント、リンク先の記事をその場で翻訳する iOS 向け Hacker News リーダーです。公式 **DeepSeek API**（BYOK）を使うのは、高速・低コストで、HN の議論に合うように翻訳プロンプトを編集できるからです。

## UI

<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/5e/82/ea/5e82ea84-ad70-6785-8e6e-e56ea962df2d/iPhone_16_Pro_Max-01-app-launched.png/686x1024bb.jpg" width="280" alt="フィードのその場翻訳" />
<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/d5/5b/7a/d55b7a61-80de-7f23-5e2d-265b55a3feb0/iPhone_16_Pro_Max-04-agent-configuration.png/686x1024bb.jpg" width="280" alt="DeepSeek エージェント設定" />

## なぜ DeepSeek か

- **高速**：デフォルトの `deepseek-v4-flash` なら、スクロールしながらタイトルとコメントツリーを翻訳し続けられます。
- **低コスト**：BYOK なら、フィードとスレッドを継続的に翻訳しても費用を抑えられます。
- **カスタムプロンプト**：翻訳プロンプト（および temperature / Top P）を編集して、HN の技術的な議論に合うトーンにできます。

## DeepSeek API の連携

**設定 → AI Agent** で DeepSeek を選び、[DeepSeek Open Platform](https://platform.deepseek.com/api_keys) のキーを保存します。
