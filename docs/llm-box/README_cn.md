# [llm-box](https://github.com/alib8b8/llm-box)

llm-box 是一个**终端优先的 AI 工作流引擎**，使用 Go 语言开发。通过简单的 YAML 工作流编排 AI 自动化任务，原生支持 DeepSeek API。

## 功能特性

- **YAML 工作流** - 用简单的 YAML 格式定义多步骤 AI 流水线
- **自然语言创建** - 用中文描述即可自动生成工作流
- **DeepSeek 原生支持** - 完美支持 DeepSeek-V4 和 DeepSeek-R1 模型
- **20+ 内置节点** - fetch_url、file_read/write、json_parse、template_render、execute、http_request 等
- **单二进制** - 零依赖，下载即用
- **多模型支持** - 支持 DeepSeek、Qwen、Kimi、GLM、Ollama、Mistral 等 15+ 模型
- **终端 UI** - 精美的 TUI 界面，实时进度追踪

## 界面预览

![llm-box demo](https://github.com/alib8b8/llm-box/raw/main/assets/demo.gif)

## 快速开始

### 1. 安装

```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/alib8b8/llm-box/main/install.sh | bash

# 或从 GitHub Releases 下载
# https://github.com/alib8b8/llm-box/releases
```

### 2. 设置 DeepSeek API 密钥

```bash
export DEEPSEEK_API_KEY="你的-deepseek-api-key"
```

### 3. 运行第一个工作流

```bash
# 用自然语言创建工作流
llm-box create "抓取 example.com 并用 deepseek 总结内容"

# 或运行预置示例
llm-box run https://raw.githubusercontent.com/alib8b8/llm-box/main/examples/deepseek_summary.yaml
```

## 配置 DeepSeek

`deepseek` 节点已内置，使用 OpenAI 兼容的 API 格式。

**示例工作流：**

```yaml
name: "DeepSeek 总结"
description: "抓取网页并用 DeepSeek 总结内容"

steps:
  - node: fetch_url
    params:
      url: "https://example.com"

  - node: deepseek
    params:
      model: "deepseek-chat"
      system: "你是一个乐于助人的助手，用简洁的语言总结文本。"

  - node: file_write
    params:
      path: "summary.txt"
```

**参数说明：**

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `model` | 模型名称 | `deepseek-chat` |
| `api_key` | DeepSeek API 密钥 | `DEEPSEEK_API_KEY` 环境变量 |
| `endpoint` | API 基础地址 | `https://api.deepseek.com/v1` |
| `system` | 系统提示词 | _(可选)_ |
| `temperature` | 采样温度 | `0.7` |

**支持的模型：**

- `deepseek-chat`（V4 Flash - 快速、性价比高）
- `deepseek-reasoner`（R1 - 强推理能力）

## 相关资源

- **GitHub 仓库：** https://github.com/alib8b8/llm-box
- **使用文档：** https://github.com/alib8b8/llm-box#readme
- **示例工作流：** https://github.com/alib8b8/llm-box/tree/main/examples
- **DeepSeek 开放平台：** https://platform.deepseek.com/
