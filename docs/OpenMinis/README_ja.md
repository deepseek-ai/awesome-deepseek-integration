# OpenMinis

<div align="center">
<img src="assets/logo.png" alt="OpenMinis" width="96" height="auto" />

**あなたのプライベートなオンデバイス AI エージェント —— チャットだけでなく、実際に行動します**

</div>

[GitHub](https://github.com/OpenMinis/OpenMinis) · [公式サイト](https://openminis.app) · [App Store](https://apps.apple.com/) · [Telegram コミュニティ](https://t.me/openminis)

---

## これは何か

OpenMinis は、**完全無料・完全オープンソース（GPL-3.0）**のクロスプラットフォーム AI エージェントアプリで、**iOS、iPadOS、macOS、Android**（および visionOS）に対応し、GitHub で **3.3k+ スター**を獲得しています。

その理念は一般の AI チャットアプリとは根本的に異なります。大モデルを単にチャットボックスに閉じ込めるのではなく、モデルに**本物のコンピューター**を与えます——デバイス上で完全な Linux 環境が動作し、モデルはパッケージのインストール、スクリプトの実行、ファイルの読み書き、ブラウザ操作、システム機能の呼び出しまで行い、本当にあなたの代わりにタスクを完了します。

## 主な機能

| 機能 | 説明 |
|------|------|
| 🤖 Bring Your Own Model | Anthropic Claude、OpenAI GPT、Google Gemini、OpenRouter に加え、**DeepSeek や任意の OpenAI 互換 API** に対応。会話ごとにモデルを自由に切り替え |
| 🐚 内蔵 Linux Shell | デバイス上でサンドボックス化された Alpine Linux が動作（iOS は iSH / Android は PRoot）。`apk add` でパッケージ導入、スクリプト実行、実ファイルの処理が可能。サーバー不要 |
| 📱 深いシステム統合 | HealthKit、カレンダー、リマインダー、連絡先、HomeKit、Bluetooth、クリップボード、メディア、アラームなどのネイティブ機能をツールとして Agent に開放 |
| 🌐 ブラウザ自動化 | Agent があなたの代わりに Web 閲覧、フォーム入力、コンテンツ抽出、スクリーンショットを実行 |
| 🛠️ スキルシステム | オープンな SKILL.md 形式。スキルのインポート/作成で機能拡張。Claude、Codex、OpenClaw などのエコシステムとも互換 |
| 🧠 永続メモリ | セッションをまたぐ記憶。使い込むほどあなたを理解 |
| 📂 Workspaces | タスクごとに独立したコンテキストを整理。`minis://workspace/` でアクセス |
| 🔒 プライバシー最優先 | API キーはシステムのキーチェーンに保存。データ収集なし、第三者分析なし。会話はあなたのもの |

## 技術アーキテクチャ

リポジトリ構成（Swift 51% / Kotlin 41% / Objective-C 6%）：

```
src/ios/          iOS アプリ（Swift/SwiftUI）+ Share・Widget・ファイルプロバイダ拡張
src/android/      Android アプリ（Kotlin/Compose）+ JNI ネイティブコード
src/shared/       両プラットフォーム共通アセット
deps/             ネイティブ依存ビルドスクリプト（iSH、PRoot、FFmpeg、LAME）
docs/specs/       アーキテクチャ・インターフェース仕様
scripts/          Rootfs 準備と開発者ツール
```

主要依存：**iSH**（iOS 向け Linux ユーザーモードエミュレーション、ARM64 fork）、**PRoot**（Android サンドボックス用ユーザースペース chroot）、**Alpine Linux**（サンドボックス起動用 minirootfs）、FFmpeg、LAME など。いずれもバイナリをコミットせずソースからビルドします。

## 実際のユースケース

- 📸 食事を撮影して栄養を記録——料理を識別し、カロリーとマクロを推定して Apple Health に書き込み
- ⏰ タイムラインで目覚める——ショートカットで X のタイムライン取得 → 要約 → 音声合成 → アラームとして再生
- 💬 グループの雑談をタスクに——Telegram グループからメッセージを取得し、バグとタスクを抽出・重複排除して Apple Reminders に登録
- 📓 Obsidian ボルトをマウント——調査・整理し、Markdown ノートをボルトに直接書き戻し
- 📅 あらゆるものをカレンダーイベントに——iOS 共有シートから、日時と場所付きでイベントを作成

## メディア掲載

> "the most impressive indie app I've seen in a while"
> —— Federico Viticci, MacStories（2026-07）

> "在很大程度上实现甚至局部超越了 Apple Intelligence"
> —— 知乎（2026-06）

> "可能是 iOS 端最强 AI Agent"
> —— 小众软件 / Appinn（2026-03）

## オープンソースエコシステム

OpenMinis 組織（github.com/OpenMinis）配下のリポジトリ：

- **[MinisSkills](https://github.com/OpenMinis/MinisSkills)**（354⭐）—— 公式スキルコレクション、40+ の SKILL.md スキル：GitHub トレンド、Twitter/X、Bilibili、睡眠健康分析、PPT 生成、qBittorrent、12306 切符、豆包 TTS など
- **[AwesomeMinis](https://github.com/OpenMinis/AwesomeMinis)**（190⭐）—— コミュニティ投稿の実用例集（健康、生産性、研究、金融、開発者ツール）
- **ish-arm64 / proot** —— iSH と PRoot のカスタムフォーク

## ライセンス

GPL-3.0。アプリは GPL コンポーネント（iSH、PRoot）にリンクしているため、結合成果物は GPLv3 で配布されます。このリポジトリはプライベート開発ツリーのミラーであり、PR は受け付けていません。Issues でのフィードバックと共創をお願いします。
