# `Reasonix`

> ⚡ A DeepSeek-native agent framework for TypeScript. Opinionated defaults squeeze every drop of value from DeepSeek's unique economic and behavioural profile.

**Reasonix Source Code**: [https://github.com/esengine/reasonix](https://github.com/esengine/reasonix)

**npm**: [https://www.npmjs.com/package/reasonix](https://www.npmjs.com/package/reasonix)

Reasonix is built exclusively for DeepSeek (no generic multi-provider abstraction). Every design decision leans into a DeepSeek-specific property — automatic prefix caching, `reasoning_content` from R1, and the economic window opened by DeepSeek being ~20× cheaper than Claude.

## 🚀 Quick Start

```bash
npm install -g reasonix
reasonix chat
```

On first launch the TUI prompts for your DeepSeek API key and saves it to `~/.reasonix/config.json`. Sessions auto-persist — next launch resumes where you left off.

## ✨ Core Design — Three Pillars

### Pillar 1 — Cache-First Loop

DeepSeek bills cached input tokens at ~10% of the miss rate, but the cache only hits when the byte prefix of the request is identical to the previous one. Most agent frameworks rebuild prompts each turn, so the cache rarely fires.

Reasonix partitions the context into three regions with strict invariants:

```
┌─────────────────────────────────────────┐
│ IMMUTABLE PREFIX                        │ ← fixed for the session
│   system + tool_specs + few_shots       │   cache hit target
├─────────────────────────────────────────┤
│ APPEND-ONLY LOG                         │ ← grows monotonically
│   [assistant₁][tool₁][assistant₂]...    │   preserves prior-turn prefix
├─────────────────────────────────────────┤
│ VOLATILE SCRATCH                        │ ← reset each turn
│   R1 reasoning, transient plan state    │   never sent upstream
└─────────────────────────────────────────┘
```

**Measured**: 85–95% prefix cache hit rate on real multi-turn sessions.

### Pillar 2 — R1 Thought Harvesting

R1's `reasoning_content` contains a plan, not just trivia to display. Reasonix pipes it through a cheap secondary V3 call in JSON mode and extracts a typed plan state:

```typescript
{
  subgoals: string[],      // concrete intermediate objectives
  hypotheses: string[],    // candidate approaches being weighed
  uncertainties: string[], // facts flagged as unclear
  rejectedPaths: string[]  // approaches the trace considered and abandoned
}
```

The TUI renders this as a magenta block above the answer. The orchestrator can branch on it — e.g. sample more when `uncertainties.length > 2`.

### Pillar 3 — Tool-Call Repair

R1/V3 have known quirks: dropping arguments on deep/wide schemas, leaking tool calls into `<think>`, truncating JSON at `max_tokens`, call-storm loops. Reasonix ships four always-on repair passes:

1. **scavenge** — regex + JSON parser sweeps `reasoning_content` for missed tool calls
2. **flatten** — schemas with >10 leaf params or depth >2 auto-flattened to dot notation, args re-nested on dispatch
3. **truncation recovery** — detect unbalanced JSON and close braces, trim trailing commas, fill dangling keys
4. **storm breaker** — identical `(tool, args)` tuples within a sliding window are suppressed

## 🎯 Bonus: Self-Consistency Branching

Because DeepSeek is ~20× cheaper than Claude, running N=3 R1 samples per turn is still cheaper than a single Claude call. `/preset max` enables it. The default selector picks the sample with fewest flagged uncertainties (Occam tie-break on shorter answers).

## 📊 Validated Numbers

Measured against live DeepSeek API:

| scenario | model | turns | cache hit | cost | Claude Sonnet 4.6 equivalent | savings |
|---|---|---|---|---|---|---|
| Chinese multi-turn chat | `deepseek-chat` | 5 | **85.2%** | $0.000923 | $0.015174 | **93.9%** |
| Tool-use (calculator) | `deepseek-chat` | 2 | **94.9%** | $0.000142 | $0.003351 | **95.8%** |
| R1 math + harvest | `deepseek-reasoner` | 1 | 72.7% | $0.006478 | $0.044484 | 85.4% |

## 🛠️ Usage

### CLI

```bash
reasonix chat                # auto-saves to session 'default'; resumes next time
reasonix chat --session work # use a different named session
reasonix chat --no-session   # ephemeral — nothing persisted
reasonix run "ask anything"  # one-shot, streams to stdout
```

### Inside the TUI — slash commands

```
/preset fast|smart|max   one-tap config (fast is default)
/model <id>              deepseek-chat or deepseek-reasoner
/harvest [on|off]        Pillar 2 toggle
/branch <N|off>          N parallel samples per turn (>=2)
/sessions                list saved sessions
/forget                  delete the current session
/help                    full command list
```

### Library

```typescript
import { CacheFirstLoop, DeepSeekClient, ImmutablePrefix, ToolRegistry } from "reasonix";

const client = new DeepSeekClient(); // reads DEEPSEEK_API_KEY
const tools = new ToolRegistry();

tools.register({
  name: "add",
  parameters: {
    type: "object",
    properties: { a: { type: "integer" }, b: { type: "integer" } },
    required: ["a", "b"],
  },
  fn: ({ a, b }: { a: number; b: number }) => a + b,
});

const loop = new CacheFirstLoop({
  client,
  tools,
  prefix: new ImmutablePrefix({
    system: "You are a math helper.",
    toolSpecs: tools.specs(),
  }),
  harvest: true,
  branch: 3,
  session: "my-session",
});

for await (const ev of loop.step("What is 17 + 25?")) {
  if (ev.role === "assistant_final") console.log(ev.content);
}
```

## 🎯 Explicit Non-Goals

- Multi-agent orchestration (use LangGraph)
- RAG / vector retrieval (use LlamaIndex)
- Multi-provider abstraction (use LiteLLM)
- Web UI / SaaS

Reasonix does DeepSeek, deeply.

## 🔗 Links

- GitHub: [https://github.com/esengine/reasonix](https://github.com/esengine/reasonix)
- npm: [https://www.npmjs.com/package/reasonix](https://www.npmjs.com/package/reasonix)
- License: MIT
