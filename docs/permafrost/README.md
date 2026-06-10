<div style="font-size: 64px">❄️</div>

# [Permafrost](https://github.com/jianzhichun/permafrost)

Freeze Claude Code's prompt prefix so DeepSeek's automatic context cache always
hits. Permafrost is a zero-dependency passthrough proxy (plus a Claude Code
plugin) that sits between Claude Code and DeepSeek's Anthropic-compatible
endpoint and rewrites the cache-relevant bytes of every request — deterministic
tool ordering, volatile env-block freezing, per-request nonce stabilization,
canonical serialization — so the `tools + system` prefix stays byte-identical
turn after turn and is served from DeepSeek's cache at ~2% of the miss price.

Measured on real Claude Code traffic against the live API: **66% cache hit rate,
64% lower cost** on a multi-turn agentic task. It also coalesces parallel
subagent fan-out (one leader warms the cache, followers wait and read it:
0% → 73% hit measured live) and can keep the prefix warm through idle gaps with
an opt-in keepalive (99.9% hit on replay).

## UI

```
$ permafrost status
mode=aggressive  upstream=https://api.deepseek.com/anthropic  requests=4
cache hit rate : 66.2%  (41,728 hit / 21,339 miss tokens)
cost so far    : $0.0032  ($0.0057 saved, 64% vs all-miss)
prefix resets  : 0
```

## Integrate with DeepSeek API

Get a DeepSeek API key from <https://platform.deepseek.com/api_keys>, then:

```bash
git clone https://github.com/jianzhichun/permafrost && cd permafrost
export ANTHROPIC_API_KEY=YOUR_DEEPSEEK_API_KEY
./cli/permafrost wrap          # starts the proxy and launches Claude Code through it
```

`wrap` points Claude Code at the local proxy (`ANTHROPIC_BASE_URL=http://127.0.0.1:8787`,
`ENABLE_TOOL_SEARCH=true`) and the proxy forwards to
`https://api.deepseek.com/anthropic`. Watch live savings with
`./cli/permafrost status`, or diagnose cache busts with `./cli/permafrost doctor`.

Claude Code users can also install it as a plugin:

```
/plugin marketplace add jianzhichun/permafrost
/plugin install permafrost@permafrost
```
