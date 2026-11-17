# DGrid AI Gateway

[DGrid AI Gateway](https://dgrid.ai/) 提供统一的单一 API，访问 200+ 主流 AI 模型，其中包括 DeepSeek 最新全系列。基于去中心化 AI 推理网络构建，开放、低成本、社区驱动，大幅降低多供应商集成的复杂性与运营成本。用户可将 DGrid API Key 直接接入 Claude Code、Codex、Cursor 等 AI 工具，通过统一端点自由切换数百个模型，无需任何兼容性适配。

## 支持的 DeepSeek 模型

通过 DGrid，无需额外配置即可使用完整 DeepSeek 模型阵列。模型采用 `[提供商]/[模型名]` 格式：

| 模型 ID | 说明 |
|---|---|
| `deepseek/deepseek-v4-pro` | DeepSeek V4 Pro —— 旗舰推理与代码模型 |
| `deepseek/deepseek-v4-flash` | DeepSeek V4 Flash —— 高速低成本变体 |
| `deepseek/deepseek-r1-0528` | DeepSeek-R1（2025 年 5 月版） |
| `deepseek/deepseek-r1` | DeepSeek-R1 —— 高级推理模型 |
| `deepseek/deepseek-v3.2` | DeepSeek V3.2 |
| `deepseek/deepseek-v3.2-exp` | DeepSeek V3.2 实验版 |
| `deepseek/deepseek-v3.1-terminus` | DeepSeek V3.1 Terminus |
| `deepseek/deepseek-chat-v3.1` | DeepSeek Chat V3.1 |
| `deepseek/deepseek-chat-v3-0324` | DeepSeek Chat V3（2024 年 3 月） |
| `deepseek/deepseek-r1-distill-qwen-32b:free` | DeepSeek-R1 Qwen-32B 蒸馏版 —— 免费额度 |

## 快速开始

### 前置条件

- 有效的 `DGRID_API_KEY` —— 在 [dgrid.ai](https://dgrid.ai/) 注册获取
- 可访问 `https://api.dgrid.ai/v1`
- SDK 使用时：在项目中安装 OpenAI SDK

### 通过 cURL 直接请求

```bash
curl https://api.dgrid.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DGRID_API_KEY" \
  -d '{
    "model": "deepseek/deepseek-v4-pro",
    "messages": [
      {"role": "user", "content": "介绍一下 DeepSeek-V4 的核心创新。"}
    ]
  }'
```

### 使用 OpenAI SDK（DGrid 兼容）

DGrid AI Gateway 完全兼容 OpenAI SDK 规范，只需修改 `baseURL` 即可快速迁移或集成。

**安装 SDK**

```bash
# TypeScript / Node.js
npm install openai

# Python
pip install openai
```

**TypeScript**

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://api.dgrid.ai/v1',   // DGrid AI Gateway 端点
  apiKey: '<DGRID_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>',  // 可选：您的应用 URL
    'X-Title': '<YOUR_SITE_NAME>',      // 可选：您的应用名称
  },
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'deepseek/deepseek-v4-pro',
    messages: [
      { role: 'user', content: '介绍一下 DeepSeek-V4 的核心创新。' },
    ],
  });
  console.log(completion.choices[0].message);
}

main();
```

**Python**

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.dgrid.ai/v1",  # DGrid AI Gateway 端点
    api_key="<DGRID_API_KEY>",
)

completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>",  # 可选：您的应用 URL
        "X-Title": "<YOUR_SITE_NAME>",      # 可选：您的应用名称
    },
    model="deepseek/deepseek-v4-pro",
    messages=[
        {"role": "user", "content": "介绍一下 DeepSeek-V4 的核心创新。"}
    ],
)

print(completion.choices[0].message.content)
```

> **说明：** `HTTP-Referer` 和 `X-Title` 为可选请求头，填写后有助于 DGrid 更好地识别您的应用并提供优化服务支持。

## 核心特性

- **OpenAI 兼容接口** —— 直接复用现有 OpenAI SDK 或工具链，零改造成本
- **200+ 模型，一个 Key** —— 通过单一端点访问 DeepSeek 及 OpenAI、Anthropic、Google 等主流供应商模型
- **直连 AI 工具** —— API Key 可直接接入 Claude Code、Codex、Cursor 等主流 AI 开发工具
- **去中心化推理网络** —— 开放、低成本、社区驱动的基础设施
- **自动故障转移** —— 配置优先级模型列表，失败时 DGrid 无缝重试
- **内置可观测性** —— 控制台提供请求日志、延迟追踪和用量分析
- **限流管理** —— 支持 Key 级别和团队级别精细化限流，防止费用失控
- **Web3 友好** —— 原生支持去中心化应用团队
- **按 Token 计费** —— 无月度订阅，用多少付多少

## 相关链接

- [官方网站](https://dgrid.ai/)
- [AI Gateway 文档](https://docs.dgrid.ai/AI-Gateway)
- [Model API 参考](https://docs.dgrid.ai/Model-API)
- [集成教程](https://docs.dgrid.ai/AI-Gateway-Integrations)
- [GitHub 组织](https://github.com/dgridai)
