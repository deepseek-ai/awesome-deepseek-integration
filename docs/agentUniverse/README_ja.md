___
<img src="assets/agentUniverse_logo.jpg" width="auto" height="auto" />

___

# [agentUniverse](https://github.com/antgroup/agentUniverse)

agentUniverseは、複雑なビジネスシーン向けに設計されたマルチエージェント協調フレームワークです。迅速で使いやすい大規模モデルのインテリジェントエージェントアプリケーション構築能力を提供し、特にエージェント間の協調スケジューリング、自律的な意思決定、動的なフィードバックなどのメカニズムに重点を置いています。これは、Ant Groupの金融業界における実践的なビジネス経験に基づいて開発されました。agentUniverseは、2024年6月にDeepSeekシリーズモデルのサポートを全面的に統合しました。

## 概念

<img src="https://raw.githubusercontent.com/antgroup/agentUniverse/refs/heads/master/docs/guidebook/_picture/agentuniverse_structure_en.png" />

## Deepseek APIと統合する

### Pythonコードを使って設定する
```python
import os
os.environ['DEEPSEEK_API_KEY'] = 'sk-***'
os.environ['DEEPSEEK_API_BASE'] = 'https://xxxxxx'
```
### 設定ファイルを使って設定する
プロジェクトのconfigディレクトリ内のcustom_key.tomlファイルに、設定を追加します：
```toml
DEEPSEEK_API_KEY="sk-******"
DEEPSEEK_API_BASE="https://xxxxxx"
```

詳細についてはドキュメントを参照してください - [Documentation: DeepSeek Integration](https://github.com/antgroup/agentUniverse/blob/master/docs/guidebook/en/In-Depth_Guides/Components/LLMs/DeepSeek_LLM_Use.md).

