# zenfeed 与 DeepSeek 集成

zenfeed 支持通过在其配置文件的 `llms` 部分进行设置，来使用 DeepSeek 模型执行摘要、语义分析等任务。

## 配置方法

要使用 DeepSeek，请在你的配置文件中的 `llms` 列表下添加一个条目。以下是一个示例：

```yaml
llms:
  - name: my-deepseek-chat  # 为此配置指定一个唯一的名称
    provider: deepseek        # 指定提供商为 deepseek
    api_key: sk-xxxxxxxxxxx # 替换为你的 DeepSeek API 密钥
    model: deepseek-chat      # 指定所需的 DeepSeek 模型（例如：deepseek-chat, deepseek-coder）
```