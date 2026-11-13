<div style="font-size: 64px">❄️</div>

# [Permafrost](https://github.com/jianzhichun/permafrost)

冻结 Claude Code 的提示词前缀,让 DeepSeek 的自动上下文缓存每轮都命中。
Permafrost 是一个零依赖的透传代理(同时也是 Claude Code 插件),位于 Claude Code
与 DeepSeek 的 Anthropic 兼容端点之间,重写每条请求中与缓存相关的字节——工具确定性
排序、易变环境块冻结、每请求随机数固定、规范化序列化——使 `tools + system` 前缀逐轮
字节级一致,以未命中价约 2% 的成本从 DeepSeek 缓存读取。

在真实 Claude Code 流量上对线上 API 实测:多轮 agent 任务 **缓存命中率 66%、成本降低
64%**。还支持并行子代理扇出合并(leader 暖缓存、follower 等待后读取,实测 0% → 73%
命中)以及可选的空闲保温(回放命中 99.9%)。

## 界面

```
$ permafrost status
mode=aggressive  upstream=https://api.deepseek.com/anthropic  requests=4
cache hit rate : 66.2%  (41,728 hit / 21,339 miss tokens)
cost so far    : $0.0032  ($0.0057 saved, 64% vs all-miss)
prefix resets  : 0
```

## 接入 DeepSeek API

在 <https://platform.deepseek.com/api_keys> 获取 API key,然后:

```bash
git clone https://github.com/jianzhichun/permafrost && cd permafrost
export ANTHROPIC_API_KEY=YOUR_DEEPSEEK_API_KEY
./cli/permafrost wrap          # 启动代理并让 Claude Code 经由它访问 DeepSeek
```

`wrap` 会把 Claude Code 指向本地代理(`ANTHROPIC_BASE_URL=http://127.0.0.1:8787`、
`ENABLE_TOOL_SEARCH=true`),代理转发到 `https://api.deepseek.com/anthropic`。
用 `./cli/permafrost status` 查看实时省钱数据,用 `./cli/permafrost doctor` 诊断缓存失效原因。

Claude Code 用户也可以作为插件安装:

```
/plugin marketplace add jianzhichun/permafrost
/plugin install permafrost@permafrost
```
