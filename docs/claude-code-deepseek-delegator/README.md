<img src="https://cdn.jsdelivr.net/npm/simple-icons@14/icons/deepseek.svg" width="64" height="auto" alt="DeepSeek" />

# Claude Code DeepSeek Delegator

[![npm](https://img.shields.io/npm/v/claude-code-deepseek-delegator?color=cb3837&logo=npm)](https://www.npmjs.com/package/claude-code-deepseek-delegator)
[![downloads](https://img.shields.io/npm/dm/claude-code-deepseek-delegator?color=cb3837)](https://www.npmjs.com/package/claude-code-deepseek-delegator)
![dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)
![license](https://img.shields.io/npm/l/claude-code-deepseek-delegator?color=blue)

MCP server that lets **Claude Code** delegate heavy-token tasks to **DeepSeek**. Claude orchestrates; DeepSeek does the heavy lifting. Zero dependencies.

> Unlike the standard DeepSeek + Claude Code setup (which replaces Claude's backend entirely), this keeps Claude in the driver's seat and offloads only the expensive work — file audits, large generations, deep reasoning — to DeepSeek at roughly 1/16th the cost.

## How it works

```
> This task analyzes ~800 lines across 4 files.
> Delegate to DeepSeek? (y/n)  y

◆ delegated to DeepSeek (v4-pro)
  Claude hands the heavy compute to DeepSeek, then synthesizes the
  answer for you — same conversation, a fraction of the token spend.
```

Claude calls the `deepseek()` tool like any other. The MCP server reads files off disk (via `files[]`) and forwards bytes straight to DeepSeek — large codebases never touch Claude's context window.

## Install

```bash
npx claude-code-deepseek-delegator init
```

`init` wires everything into Claude Code in one shot: MCP server registration, CLAUDE.md rules, and PreToolUse hooks for the automatic delegation prompt.

Get a DeepSeek API key at [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys) and set:

```bash
export DEEPSEEK_API_KEY=sk-your-key-here
```

## Pricing comparison (per 1M tokens)

| | Input | Output |
|---|---|---|
| DeepSeek V4 Pro | $0.435 | $0.87 |
| Claude Opus 4.8 | $5.00 | $25.00 |

The `files[]` trick saves further: file bytes go directly to DeepSeek, never billed at Claude's input rate.

## License

MIT &middot; [GitHub](https://github.com/12122J/claude-delegator-deepseek-mcp) &middot; [npm](https://www.npmjs.com/package/claude-code-deepseek-delegator)
