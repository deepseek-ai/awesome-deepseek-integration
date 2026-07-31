# Jig

Jig 是一个 Python 多 Agent 编排框架，具备**执行前安全门禁**（Agent Firewall）、4 层记忆架构和硬约束 Harness 层。针对 DeepSeek V4 API 深度优化 — SHA-256 前缀缓存、Flash 优先成本路由、自动 Tool-Call Repair。

## 为什么选择 Jig？

大多数 Agent 框架"信任 LLM"，依赖 prompt 级约束。Jig 反其道而行：每个工具调用在**代码层**先经过 Agent Firewall（白名单 + 黑名单 + PreToolUse 钩子）再执行。Agent 自主性靠架构保证安全，而非提示词。

## 特性

- 🛡️ **执行前 Agent Firewall** — 工具白名单/黑名单在代码层强制，不靠 prompt
- 🧠 **DeepSeek 原生优化** — SHA-256 前缀缓存、Flash 优先 CostAwareRouter、Tool-Call Repair
- 🤖 **11 个预设 Agent** — PM、Spec、Coding、Acceptance、Security、TDD、DevOps、秘书、导师等
- 🌐 **多模型 + 流式** — DeepSeek + OpenAI provider、SSE 流式输出
- 🔄 **Loop Engineering** — 收敛检测、质量校验、重试 + 升级
- 🗄️ **4 层记忆** — append-only、工作区、压缩、整合
- 🧩 **图编排** — 复杂查询走图管道
- 🛡️ **Human-in-the-Loop** — `requires_approval` 节点暂停等待人工审批

## 安装

```bash
pip install jig-toolguard
```

## 快速开始

```python
from jig import Jig

app = Jig(skills_dir="./skills")
result = app.run("帮我分析这个需求并拆解任务")
print(result)
```

## DeepSeek 集成

设置 API Key：

```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```

所有 Agent 默认使用 `deepseek-v4-flash` 控制成本。短查询保持 Flash；复杂任务自动升级到 `deepseek-v4-pro`。Token 预算防止成本失控。

| 模型 | 成本 / 1K tokens |
|-------|-----------------|
| deepseek-v4-pro | $0.435 in / $0.87 out |
| deepseek-v4-flash | $0.14 in / $0.28 out |
| 缓存命中 | 基础价 2% |

## 链接

- GitHub: https://github.com/luyi14-bits/jig
- PyPI: https://pypi.org/project/jig-toolguard/
