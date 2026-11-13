# rss-pod integration with DeepSeek

[rss-pod](https://github.com/synrise25/rss-pod) is a self-hosted RSS-to-podcast app. It can use DeepSeek through its OpenAI-compatible API to turn RSS content into multi-speaker dialogue scripts, which are then synthesized into audio using Edge TTS or Azure Speech.

## DeepSeek configuration

1. Follow the [rss-pod setup guide](https://github.com/synrise25/rss-pod#quick-start) to prepare PostgreSQL and S3-compatible storage, and copy `.env.example` to `.env` and `config.example.yaml` to `config.yaml`.
2. Set these entries in `.env` (replace the placeholder with your own DeepSeek API key):

```dotenv
LLM_DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
LLM_DEEPSEEK_API_KEY=YOUR_DEEPSEEK_API_KEY
LLM_DEEPSEEK_MODEL=deepseek-chat
```

3. In `config.yaml`, keep the existing `services.llm.deepseek` service and select it for dialogue generation:

```yaml
defaults:
  llm:
    - deepseek
```

4. Configure at least one RSS source, then follow the repository's [check, migration, and startup instructions](https://github.com/synrise25/rss-pod#quick-start). Edge TTS can be used without an Azure Speech key.

DeepSeek is used for script generation, and may also be selected for optional content screening (`defaults.screening.services: [llm.deepseek]`). The application also supports other OpenAI-compatible providers.

**Demo:** [English sample audio and web player](https://github.com/synrise25/rss-pod#audio-demo) · [Chinese sample](https://github.com/synrise25/rss-pod/blob/main/README.zh-CN.md#播客试听)
