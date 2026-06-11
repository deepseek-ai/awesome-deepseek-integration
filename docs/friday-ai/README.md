# Friday AI

<div align="center">
<img src="./assets/logo-wordmark.svg" width="320" alt="Friday AI Logo">
</div>

## English

> **Turn requirements into reviewable Pull Requests — automatically.**

**[Friday AI](https://github.com/friday-ai-codes/friday-ai)** is an open-source, self-hosted AI development automation platform. It takes requirements from Feishu (Lark) Project and turns them into reviewable code PRs: the platform reads the requirement, researches your codebase, drafts a technical design for the team to confirm, then lets AI coding agents write the code in isolated containers and open the PR — syncing progress back to Feishu at every step. Humans review, Friday does the legwork.

**Features:**

- **Requirement → PR pipeline**: From Feishu (Lark) Project requirement to branch, commits, and PR/MR — fully orchestrated and observable.
- **Workflow engine**: Visual DAG-based workflow editor with pluggable nodes (AI, Git, control flow, Feishu integrations).
- **Containerized coding agents**: AI agents run in isolated Docker/Kubernetes containers, scheduled by a dedicated runner.
- **Graph RAG code intelligence**: Combines code knowledge graph (tree-sitter + LSP) with vector retrieval for accurate codebase understanding.
- **Self-hosted**: Deploy with Docker Compose or Kubernetes; credentials encrypted at rest.

**Integrate with DeepSeek API:**

Friday AI ships with **DeepSeek as a built-in model provider preset**. In the setup wizard (or *Settings → Model Providers*), select **DeepSeek**, which uses DeepSeek's official Anthropic-compatible endpoint:

| Field | Value |
|---|---|
| Base URL | `https://api.deepseek.com/anthropic` |
| API Key | Get one from [DeepSeek Open Platform](https://platform.deepseek.com/api_keys) |

Once configured, DeepSeek models power Friday's chat, technical design generation, workflow AI nodes, and the coding agents that produce PRs.

- Website / Repo: <https://github.com/friday-ai-codes/friday-ai>
- Docs: <https://friday-ai-codes.github.io/friday-ai/>

---

## 简体中文

> **把需求自动变成可审查的代码 PR。**

**[Friday AI](https://github.com/friday-ai-codes/friday-ai)** 是一个开源、可自托管的 AI 开发自动化平台。它把飞书项目中的需求自动转化为可审查的代码 PR：需求进来后，Friday 会先读懂它、检索代码库、生成技术方案；团队确认后，再由 AI 编码代理在隔离容器中编写代码、自动建分支并提交 PR，每一步进度都会同步回飞书。人负责把关，Friday 负责跑腿。

**核心特性：**

- **需求 → PR 全链路**：从飞书项目需求到分支、提交、PR/MR，全程可编排、可观测。
- **工作流引擎**：可视化 DAG 流程编辑器，AI / Git / 控制流 / 飞书集成等节点即插即用。
- **容器化编码代理**：AI 代理在隔离的 Docker / Kubernetes 容器中运行，由独立 Runner 调度。
- **Graph RAG 代码智能**：代码知识图谱（tree-sitter + LSP）结合向量检索，更精准地理解代码库。
- **自托管部署**：支持 Docker Compose / Kubernetes，凭证全程加密存储。

**接入 DeepSeek API：**

Friday AI 内置 **DeepSeek 供应商预设**。在初始化向导（或「设置 → 模型供应商」）中选择 **DeepSeek**，即使用 DeepSeek 官方 Anthropic 兼容端点：

| 配置项 | 值 |
|---|---|
| Base URL | `https://api.deepseek.com/anthropic` |
| API Key | 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 |

配置完成后，DeepSeek 模型即可驱动 Friday 的对话、技术方案生成、工作流 AI 节点，以及最终产出 PR 的编码代理。

- 项目地址：<https://github.com/friday-ai-codes/friday-ai>
- 文档：<https://friday-ai-codes.github.io/friday-ai/>
