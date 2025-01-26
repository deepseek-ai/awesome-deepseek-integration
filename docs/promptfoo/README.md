# promptfoo

[promptfoo](https://promptfoo.dev) is an open-source framework for testing and evaluating LLM outputs. It helps you compare DeepSeek models with other LLMs (like o1, GPT-4o, Claude 3.5, Llama3.3, and Gemini) and test LLMs and LLM applications for security vulnerabilities. You can:

- Run side-by-side comparisons between models
- Check output quality and consistency
- Generate test reports

## Setup

1. Install promptfoo:

```bash
npm install -g promptfoo
# or
brew install promptfoo
```

2. Configure API keys:

```bash
export DEEPSEEK_API_KEY=your_api_key
# Add other API keys as needed
```

## Quick Start

Create a configuration file `promptfooconfig.yaml`:

```yaml
providers:
  - deepseek:deepseek-reasoner # DeepSeek-R1
  - openai:o1

prompts:
  - 'Solve this step by step: {{math_problem}}'

tests:
  - vars:
      math_problem: 'What is the derivative of x^3 + 2x with respect to x?'
    assert:
      - type: contains
        value: '3x^2' # Check for correct answer
      - type: llm-rubric
        value: 'Response shows clear steps'
      - type: cost
        threshold: 0.05 # Maximum cost per request
```

Run tests:

```bash
promptfoo eval
```

View results in your browser:

```bash
promptfoo view
```

## Example Project

Check out our [example](https://github.com/promptfoo/promptfoo/tree/main/examples/deepseek-r1-vs-openai-o1) that compares r1 and o1 on MMLU.

## Resources

- [Documentation](https://promptfoo.dev/docs/providers/deepseek)
- [GitHub Repository](https://github.com/promptfoo/promptfoo)
- [Community Discord](https://discord.gg/promptfoo)
