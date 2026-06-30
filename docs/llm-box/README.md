# [llm-box](https://github.com/alib8b8/llm-box)

llm-box is a **terminal-first AI workflow engine** built with Go. It lets you compose AI-powered automations using simple YAML workflows, with native support for DeepSeek API.

## Features

- **YAML Workflows** - Define multi-step AI pipelines in simple YAML format
- **Natural Language Creation** - Generate workflows from plain English descriptions
- **DeepSeek Native** - First-class support for DeepSeek-V4 and DeepSeek-R1 models
- **20+ Built-in Nodes** - fetch_url, file_read/write, json_parse, template_render, execute, http_request, and more
- **Single Binary** - No dependencies, just download and run
- **Multi-LLM Support** - Works with DeepSeek, Qwen, Kimi, GLM, Ollama, Mistral, and 15+ other providers
- **Terminal UI** - Beautiful TUI with progress tracking and live output

## UI

![llm-box demo](https://github.com/alib8b8/llm-box/raw/main/assets/demo.gif)

## Quick Start

### 1. Install

```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/alib8b8/llm-box/main/install.sh | bash

# Or download from GitHub Releases
# https://github.com/alib8b8/llm-box/releases
```

### 2. Set your DeepSeek API key

```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

### 3. Run your first workflow

```bash
# Create a workflow from natural language
llm-box create "fetch example.com and summarize it using deepseek"

# Or run a pre-built example
llm-box run https://raw.githubusercontent.com/alib8b8/llm-box/main/examples/deepseek_summary.yaml
```

## Configure DeepSeek

The `deepseek` node is built-in and uses the OpenAI-compatible API format.

**Example workflow:**

```yaml
name: "DeepSeek Summary"
description: "Fetch a webpage and summarize it using DeepSeek"

steps:
  - node: fetch_url
    params:
      url: "https://example.com"

  - node: deepseek
    params:
      model: "deepseek-chat"
      system: "You are a helpful assistant that summarizes text concisely."

  - node: file_write
    params:
      path: "summary.txt"
```

**Parameters:**

| Parameter | Description | Default |
|-----------|-------------|---------|
| `model` | Model name | `deepseek-chat` |
| `api_key` | DeepSeek API key | `DEEPSEEK_API_KEY` env var |
| `endpoint` | API base URL | `https://api.deepseek.com/v1` |
| `system` | System prompt | _(optional)_ |
| `temperature` | Sampling temperature | `0.7` |

**Supported models:**

- `deepseek-chat` (V4 Flash - fast, cost-effective)
- `deepseek-reasoner` (R1 - strong reasoning)

## Resources

- **GitHub:** https://github.com/alib8b8/llm-box
- **Documentation:** https://github.com/alib8b8/llm-box#readme
- **Examples:** https://github.com/alib8b8/llm-box/tree/main/examples
- **DeepSeek API:** https://platform.deepseek.com/
