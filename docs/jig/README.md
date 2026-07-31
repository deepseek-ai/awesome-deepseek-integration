# Jig

Jig is a Python multi-agent orchestration framework with **pre-execution safety gates** (Agent Firewall), 4-layer memory architecture, and a hard-constraint Harness layer. It's optimized for DeepSeek V4's API — SHA-256 prefix caching, flash-first cost routing, and automatic tool-call repair.

## Why Jig?

Most agent frameworks "trust the LLM" and rely on prompt-level constraints. Jig inverts this: every tool call passes through a code-level **Agent Firewall** (whitelist + blacklist + PreToolUse hooks) before execution. This makes agent autonomy safe by construction, not by prompting.

## Features

- 🛡️ **Pre-execution Agent Firewall** — tool whitelist/blacklist enforced in code, not prompt
- 🧠 **DeepSeek-Native Optimizations** — SHA-256 prefix caching, flash-first CostAwareRouter, Tool-Call Repair
- 🤖 **11 Preset Agents** — PM, Spec, Coding, Acceptance, Security, TDD, DevOps, Secretary, Mentor, etc.
- 🌐 **Multi-Model + Streaming** — DeepSeek + OpenAI providers, SSE streaming
- 🔄 **Loop Engineering** — convergence detection, quality validation, retry + escalate
- 🗄️ **4-Layer Memory** — append-only, working, compressed, consolidated
- 🧩 **Graph Orchestration** — complex queries route through graph pipelines
- 🛡️ **Human-in-the-Loop** — `requires_approval` nodes pause for manual approve/reject

## Installation

```bash
pip install jig-toolguard
```

## Quick Start

```python
from jig import Jig

app = Jig(skills_dir="./skills")
result = app.run("帮我分析这个需求并拆解任务")
print(result)
```

## DeepSeek Integration

Set your API key:

```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```

All agents default to `deepseek-v4-flash` for cost efficiency. Short queries stay on Flash; complex tasks auto-upgrade to `deepseek-v4-pro`. Token budgets prevent runaway costs.

| Model | Cost / 1K tokens |
|-------|-----------------|
| deepseek-v4-pro | $0.435 in / $0.87 out |
| deepseek-v4-flash | $0.14 in / $0.28 out |
| Cache hit | 2% of base price |

## Links

- GitHub: https://github.com/luyi14-bits/jig
- PyPI: https://pypi.org/project/jig-toolguard/
