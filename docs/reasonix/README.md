# Reasonix

> An open-source coding agent built around DeepSeek.

**Source**: [github.com/esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) · **Website**: [reasonix.io](https://reasonix.io) · **License**: MIT

Reasonix is a single Go binary with four front ends on one engine: a terminal UI,
a desktop app, a browser UI (`reasonix web`), and the Agent Client Protocol
(`reasonix acp`) for Zed, JetBrains IDEs and other ACP editors.

## Why DeepSeek

DeepSeek bills a cached input token at a small fraction of a cache miss, and the
cache only hits when the request prefix is byte-identical to an earlier one.
Reasonix keeps the system prompt, tool list and standing instructions
byte-stable for the whole session and carries everything that changes in the
turn tail, so long sessions stay on the cached price. Cache hits and cost are
shown per turn.

DeepSeek is the default; any OpenAI- or Anthropic-compatible endpoint can be
configured as well.

## Features

- Plan mode, per-tool permissions and a workspace sandbox (macOS and Linux)
- Per-turn checkpoints with rewind of code, conversation or both
- MCP servers (stdio, SSE, streamable HTTP, OAuth)
- [Agent Skills](https://agentskills.io) from `.reasonix/`, `.agents/` and `.claude/` skill folders
- Hooks, slash commands, subagents and plugin packages
- `AGENTS.md` / `CLAUDE.md` standing instructions
- SSH remote workspaces, with API keys kept on the local machine

## Quick start

```bash
npm install -g reasonix
reasonix setup   # choose a provider and enter a DeepSeek API key
reasonix
```

Desktop builds are on
[reasonix.io](https://reasonix.io).
