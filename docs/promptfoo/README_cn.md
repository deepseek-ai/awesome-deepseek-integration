# promptfoo

[promptfoo](https://promptfoo.dev) 是一个开源框架，用于测试和评估 LLM 输出。它可以帮助您将 DeepSeek 模型与其他 LLM（如 o1、GPT-4o、Claude 3.5、Llama 3.3 和 Gemini）进行比较，并测试 LLM 及其应用的安全漏洞。您可以：

- 对不同模型进行并排比较
- 检查输出质量和一致性
- 生成测试报告

## 安装设置

1. 安装 promptfoo：

```bash
npm install -g promptfoo
# 或者使用 brew
brew install promptfoo
```

2. 配置 API 密钥：

```bash
export DEEPSEEK_API_KEY=your_api_key
# 根据需要添加其他 API 密钥
```

## 快速开始

创建配置文件 `promptfooconfig.yaml`：

```yaml
providers:
  - deepseek:deepseek-reasoner # DeepSeek-R1
  - openai:o1

prompts:
  - '请逐步解决这个问题：{{math_problem}}'

tests:
  - vars:
      math_problem: '求 x^3 + 2x 对 x 的导数'
    assert:
      - type: contains
        value: '3x^2' # 检查正确答案
      - type: llm-rubric
        value: '回答需要展示清晰的步骤'
      - type: cost
        threshold: 0.05 # 每次请求的最大成本
```

运行测试：

```bash
promptfoo eval
```

在浏览器中查看结果：

```bash
promptfoo view
```

## 示例项目

查看我们的[示例](https://github.com/promptfoo/promptfoo/tree/main/examples/deepseek-r1-vs-openai-o1)，展示了 r1 和 o1 在 MMLU 上的比较。

## 资源

- [文档](https://promptfoo.dev/docs/providers/deepseek)
- [GitHub 仓库](https://github.com/promptfoo/promptfoo)
- [社区 Discord](https://discord.gg/promptfoo)
