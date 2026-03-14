<img src="./assets/logo.png" width="64" height="auto" />

# [AhaKnow Chat](https://github.com/IHKYoung/AhaKnowChat)

AhaKnow Chat は、任意の OpenAI-compatible API を通じて DeepSeek を利用できる、ローカルファーストの AI チャットワークスペースです。トピックベースのスレッド、再利用可能なロール、マルチロールのブレインストーミング、ブラウザローカル保存をサポートしています。

## UI

<img src="./assets/home.png" />

## 使用例

<img src="./assets/usage.png" />

## 設定画面

<img src="./assets/settings.png" />

## DeepSeek API との統合

AhaKnow Chat は OpenAI-compatible API を前提に設計されているため、DeepSeek を追加のバックエンド実装なしで直接統合できます。

### 設定手順

1. `Settings` を開き、`AI Provider` タブに移動します。
2. `Base URL` に `https://api.deepseek.com` を設定します。
3. `API Key` フィールドに自分の DeepSeek API Key を貼り付けます。
4. `Test Connection` をクリックして接続確認とモデル一覧の取得を行います。
5. デフォルトモデルを選択します。
   - `deepseek-chat`: 一般的なチャット用途
   - `deepseek-reasoner`: より強い推論タスク向け
6. 設定を保存し、トピックとスレッドを作成して DeepSeek との対話を開始します。

### 補足

- Web 版では設定情報はブラウザローカルに保存されます。
- Vercel に Web 版をデプロイする場合、DeepSeek 側のエンドポイントがブラウザアクセスと CORS を許可している必要があります。
- OpenAI-compatible API を提供していれば、DeepSeek 互換のゲートウェイやプロキシ経由でも接続できます。
