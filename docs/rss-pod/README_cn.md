# rss-pod 与 DeepSeek 集成

[rss-pod](https://github.com/synrise25/rss-pod) 是一款自托管的 RSS 转播客工具。它支持通过兼容 OpenAI 的接口调用 DeepSeek，将 RSS 内容改写为多人对话脚本，再使用 Edge TTS 或 Azure Speech 生成音频。

## DeepSeek 配置

1. 按照 [rss-pod 部署文档](https://github.com/synrise25/rss-pod/blob/main/README.zh-CN.md#快速开始) 准备 PostgreSQL、S3 兼容对象存储，复制 `.env.example` 为 `.env`，复制 `config.example.yaml` 为 `config.yaml`。
2. 在 `.env` 中配置 DeepSeek（将占位内容替换成自己的 API Key）：

```dotenv
LLM_DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
LLM_DEEPSEEK_API_KEY=YOUR_DEEPSEEK_API_KEY
LLM_DEEPSEEK_MODEL=deepseek-chat
```

3. 保留 `config.yaml` 里的 `services.llm.deepseek` 服务，并选择 DeepSeek 生成对话脚本：

```yaml
defaults:
  llm:
    - deepseek
```

4. 配置至少一个 RSS 来源，再按项目文档执行检查、数据库迁移及启动命令。使用 Edge TTS 不需要配置 Azure Speech Key。

DeepSeek 可用于脚本生成，也可选用于内容筛选（`defaults.screening.services: [llm.deepseek]`）；项目同样支持其他兼容 OpenAI API 的模型服务。

**效果演示：** [中文音频试听与播放器](https://github.com/synrise25/rss-pod/blob/main/README.zh-CN.md#播客试听) · [英文试听](https://github.com/synrise25/rss-pod#audio-demo)
