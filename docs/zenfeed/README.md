# zenfeed Integration with DeepSeek

zenfeed supports using DeepSeek models for tasks like summarization and semantic analysis by configuring it within the `llms` section of your zenfeed configuration file.

## Configuration

To use DeepSeek, add an entry to the `llms` list in your configuration file. Here's an example:

```yaml
llms:
  - name: my-deepseek-chat  # A unique name for this configuration
    provider: deepseek        # Specify the provider as deepseek
    api_key: sk-xxxxxxxxxxx # Replace with your actual DeepSeek API key
    model: deepseek-chat      # Specify the desired DeepSeek model (e.g., deepseek-chat, deepseek-coder)
```