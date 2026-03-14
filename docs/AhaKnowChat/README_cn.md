<img src="./assets/logo.png" width="64" height="auto" />

# [AhaKnow Chat](https://github.com/IHKYoung/AhaKnowChat)

AhaKnow Chat 是一个本地优先的 AI 对话工作台，可通过任何 OpenAI-compatible API 直接接入 DeepSeek。它支持按话题和线程组织对话、复用角色、多角色同时对话，并将数据保存在浏览器本地。

## 界面

<img src="./assets/home.png" />

## 使用过程

<img src="./assets/usage.png" />

## 设置界面

<img src="./assets/settings.png" />

## 配置 DeepSeek API

由于 AhaKnow Chat 基于 OpenAI-compatible API 设计，所以接入 DeepSeek 不需要额外的后端代码。

### 配置步骤

1. 打开 `Settings`，进入 `AI 提供商` 标签页。
2. 将 `Base URL` 设置为 `https://api.deepseek.com`。
3. 在 `API Key` 中填入你自己的 DeepSeek API Key。
4. 点击 `测试连接`，验证接口可用并拉取模型列表。
5. 选择默认模型：
   - `deepseek-chat` 适合日常对话和通用使用
   - `deepseek-reasoner` 适合更强的推理类任务
6. 保存配置后，新建话题与线程，即可开始使用 DeepSeek 对话。

### 补充说明

- Web 版会将配置保存在浏览器本地。
- 如果将 Web 版部署到 Vercel，目标 DeepSeek 接口需要允许浏览器请求和 CORS。
- 只要提供 OpenAI-compatible API，也可以通过兼容网关或代理接入 DeepSeek。
