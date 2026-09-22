<img src="./assets/icon.png" width="64" height="auto" />

# [DeepSeeker-Code](https://github.com/xknk/deepseeker-code)

DeepSeeker-Code is a local-first AI coding assistant powered by the DeepSeek API. It is built around one self-developed agentic engine with three interchangeable entries — VS Code extension, terminal CLI (React Ink), and a local HTTP API — all sharing the same core, toolchain, and session store, so sessions can be continued across entries in the same project.

## Installation

**VS Code extension**: install the `.vsix` from the repo releases, set `deepseekerCode.apiKey` in Settings, then run the command palette command `DeepSeeker-Code: Open Chat` (or press `Ctrl+Esc`). The extension is self-contained — the engine is bundled in, no separate CLI install needed.

**Terminal CLI**:

```bash
npm install -g deepseeker-code
export DEEP_SEEK_API_KEY=sk-***
cd your-project && deepseeker-code
```

## Key Features

1. **Agentic coding engine**: a streaming agent main loop with a complete toolchain — read/write/edit/move/delete files with AST symbol outlines, run commands (foreground and background processes), ripgrep content search + glob file search, git operations, web fetch/search, a full HTTP client for local API testing, TypeScript/JS code navigation with type diagnostics, Word/PDF/Excel document reading, git worktree management, and sub-agent orchestration.

2. **Approval gateway**: read-only tools run freely, while file mutations and dangerous operations require explicit user approval. "Always allow" decisions are persisted as glob permission rules.

3. **Context compaction with recall**: automatic conversation compaction tuned for long tasks, with a lossless entity index; archived messages and oversized tool outputs remain retrievable on demand through the built-in `recall` tool, so details survive long sessions without re-running tools.

4. **Two-phase plan mode**: read-only research first, then an implementation plan presented for your approval before any code is written.

5. **Diff review for every change**: file edits are shown as diffs — red/green inline in the CLI, side-by-side in the VS Code panel, or in the native `vscode.diff` editor.

6. **Multimodal input**: paste images into chat (up to 8 MB each) and ask questions about them when vision mode is enabled.

7. **MCP / Hooks / Skills / Sub-agents**: four extension mechanisms — external tools via MCP, declarative lifecycle hooks, on-demand skill loading, and workflow sub-agents.

## Integrate with DeepSeek API

DeepSeeker-Code talks to the DeepSeek API directly; set your key and optionally override the endpoint or model:

```bash
export DEEP_SEEK_API_KEY=sk-***                     # required
export DEEP_SEEK_API_URL=https://api.deepseek.com   # optional
export DEEP_SEEK_MODEL=deepseek-chat                # optional
```

In the VS Code extension, set `deepseekerCode.apiKey` in Settings instead. Both entries keep configuration and sessions under `~/.deepseeker-code/`.

## Best practices

1. **Keep the approval gateway on** when running with the DeepSeek API, especially for write operations — approve per-action or grant glob rules only for paths you trust.

2. **Use plan mode for non-trivial tasks**: let the agent research read-only first and agree on a plan before it starts editing.
