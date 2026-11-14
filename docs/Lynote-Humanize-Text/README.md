# Lynote Humanize Text with DeepSeek

[Project](https://github.com/lynote-ai/humanize-text) | [Configuration reference](https://github.com/lynote-ai/humanize-text/blob/main/docs/configuration.md)

Lynote Humanize Text is an MIT-licensed text rewriting toolkit. Its runnable translation-chain reference uses DeepSeek for two rewrite stages and then Google and Niutrans for cross-engine translation. The second LLM stage receives the previous stage as context.

## Setup

Use Python 3.10 or later. Obtain a DeepSeek API key from [DeepSeek Open Platform](https://platform.deepseek.com/) and a Niutrans API key for the final translation stage.

```bash
git clone https://github.com/lynote-ai/humanize-text.git
cd humanize-text
pip install -r requirements.txt
cp config/config.example.toml config/config.toml
```

Set these values in the copied configuration file, keeping the other settings:

```toml
[api_keys]
deepseek_api_key = "YOUR_DEEPSEEK_API_KEY"
niutrans_api_key = "YOUR_NIUTRANS_API_KEY"

[llm]
provider = "deepseek"
model = "deepseek-chat"
temperature = 1.3
```

```bash
python -m src.standard.pipeline --input "Your draft text here"
```

The default client uses https://api.deepseek.com/chat/completions. Keep keys out of version control. API usage is billed according to the providers' terms; the MIT source license does not include free API credits.

## Workflow and Current Research

- [n8n workflow](https://github.com/lynote-ai/humanize-text/blob/main/n8n/humanize_standard.json) for automation.
- [Step-by-step examples](https://github.com/lynote-ai/humanize-text/tree/main/examples/showcase) of the translation-chain reference.
- [Training-data pipeline](https://github.com/lynote-ai/humanize-text/tree/main/training-data-pipeline) documenting the current structure-first SFT/KTO data method. This is data preparation code, not released model weights.

Round-trip translation can alter terminology or nuance. Review the result; detector classifications are probabilistic and are not guaranteed.
