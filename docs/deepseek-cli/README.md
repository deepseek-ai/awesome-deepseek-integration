# DeepSeek CLI (`deepseek`)

[DeepSeek CLI](https://github.com/surf1k/deepseek-cli) is a blazing-fast, open-source autonomous coding agent, terminal assistant, and Git workflow tool for DeepSeek-V3 and DeepSeek-R1 reasoning models written in pure Rust.

It brings the **full Claude Code & OpenCode experience** to the terminal, powered by DeepSeek API and local LLMs.

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/surf1k/deepseek-cli/main/install.sh | bash
```

## Key Features

- 🤖 **Autonomous Coding Agent (`deepseek agent`)**: Replicates the Claude Code agentic loop. Autonomously reads files, performs surgical string edits, runs shell commands, searches code, and iterates until the task is solved.
- 👥 **Multi-Agent Delegation (`spawn_subagent`)**: Primary agent can launch focused subagents (Researcher, Test Runner, Auditor) in separate sandboxed contexts.
- 🎨 **Visual Diff Engine**: Surgical file edits are previewed in color-coded unified diff format (`+`/`-`) before applying.
- 💰 **Real-Time Cost & Claude Savings (`/cost`)**: Calculates exact API cost in dollars ($) and displays real-time savings compared to Claude 3.5 Sonnet.
- 🗜️ **Context Compaction (`/compact`)**: Automatic and manual conversation summarization to free up context window tokens.
- 💾 **Session Persistence (`deepseek --continue`)**: Resume prior tasks and chat sessions seamlessly.
- 🛡️ **Interactive Safety & Permissions**: Read-only tools run safely; mutating actions (`edit_file`, `write_file`, `bash`) require approval (`[y/n/a]`), with an `--auto` flag for background tasks.
- 🧠 **Project Memory**: Automatically detects and reads `DEEPSEEK.md`, `CLAUDE.md`, or `AGENTS.md` instructions from your repository.
- ⚡ **Blazing Fast**: Starts in milliseconds (<10ms) with zero runtime dependencies.
- 💭 **DeepThink / R1 Reasoning Stream**: Live visualization of inner reasoning tokens with timer and token count.
- 🛠️ **Git Assistant**: Automated Conventional Commits (`deepseek commit`) and deep diff reviews (`deepseek review`).
- 🐚 **Natural Language Shell**: Convert prompt to executable shell commands (`deepseek sh "find large files"`).

🔗 **Repository**: https://github.com/surf1k/deepseek-cli
