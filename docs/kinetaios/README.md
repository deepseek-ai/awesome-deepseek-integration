# `KinetAios`

> 🤖 A local-first multi-engine AI agent dashboard for Windows & macOS — run Claude Code, Codex, DeepSeek, and a built-in ReAct engine side by side in one window.

**KinetAios Source Code**: [https://github.com/phinn/KinetAios](https://github.com/phinn/KinetAios)

**Website**: [https://phinn.github.io/KinetAios/](https://phinn.github.io/KinetAios/)

KinetAios connects to DeepSeek (and any OpenAI-compatible API) as a first-class engine provider: configure a DeepSeek API key and the agent loop streams reasoning + tool calls entirely on your machine.

## 🤖 Introduction

`KinetAios` is an open-source (GPL-3.0) desktop AI agent dashboard built with Electron + TypeScript. It is local-first: conversations, long-term memory, and tool outputs live in a local SQLite database — no account, no relay server, no cloud storage.

### ✨ Key Features

1. **Multi-Engine, One Window**:
   Run Claude Code, Codex, and the built-in "Direct" ReAct engine side by side. Switch engines per conversation; each engine gets the same project rules, memory, and tools. DeepSeek (OpenAI-compatible API), GLM, Anthropic, and other providers are all supported out of the box.

2. **Cross-Engine Long-Term Memory**:
   A shared memory layer (SQLite + FTS5 full-text search) is extracted from every turn and injected into the next — works across engine switches, so your agent remembers context no matter which engine you use.

3. **MCP Client + Server**:
   Connect any MCP server for extra tools, or expose KinetAios's own 40+ tools (shell, files, web fetch, screenshot, memory search) to other MCP clients through its built-in MCP server.

4. **Agent Toolchain**:
   Shell with approval gating, file read/write, web search + fetch, computer use (screenshot/click/type), multi-agent team dispatch, cron-scheduled tasks, and a plugin system with 27+ built-in plugins.

5. **Project Rules Injection**:
   `KINET.md` / `KinetAios.md` in your project root are automatically loaded into every engine's system prompt — the same "project memory" pattern as Claude Code's CLAUDE.md, but engine-agnostic.

### 🖥️ Platforms

Windows 10/11 and macOS (Apple Silicon & Intel).
