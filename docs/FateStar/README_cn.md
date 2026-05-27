# FateStar 紫微斗数 · 八字 · 星座 AI 命理

<p align="center">
  <img src="./assets/logo.png" alt="FateStar" width="120" />
</p>

<p align="center">
  <a href="https://fatestar.top">官网</a> ·
  <a href="./README.md">English</a> ·
  简体中文
</p>

---

FateStar 是一个把紫微斗数（三合派）、八字四柱、西洋占星揉在一起的中文命理 AI 平台。官网 [fatestar.top](https://fatestar.top)，后端跑 DeepSeek-V4。

## 为啥选 DeepSeek

我们试过几个主流大模型来解读紫微古书，海外模型在中文古籍这个 niche 上训练数据偏少，文言文术语跟典籍名处理不够稳定。

切到 DeepSeek 之后，「化忌」「来因宫」「自化禄入」这类术语能稳定理解，解读能溯源到《紫微斗数全书》等古籍原文。这是我们决定用 DeepSeek-V4 跑全套推理引擎的原因。

三个具体技术理由。

**1. 中文文言文支持稳定。** 中文文化语境是 DeepSeek 的训练强项，紫微术语跟古籍引用不需要额外 fine-tune。

**2. 1M 上下文。** 紫微古书《十八飞星策天紫微斗数全书》大概 60K tokens，八字典籍约 120K，西洋占星典籍约 200K。加起来 400K 左右，DeepSeek-V4 单次推理装得下，不用切片不用 RAG。

**3. Thinking / Non-Thinking 双模式。** 紫微推流年的链路（透干 → 化禄忌 → 自化 → 来因宫 → 大限/流年嵌套）每一步依赖前一步。V4-Pro 的 Thinking 模式把思维链直接吐出来，前端渲染成步骤动画展示给用户。

## 接入细节

- API endpoint：`api.deepseek.com/v1/chat/completions`
- 主力模型：`deepseek-v4-pro`（Thinking 模式，跑深度推理）
- 辅助模型：`deepseek-v4-flash`（Non-Thinking 模式，跑命盘语义化跟轻量对话）
- 上下文：1M tokens
- 调用方式：function calling 让模型输出结构化命盘 JSON，再走 chain-of-thought 跑推理链路

数据流：

用户出生时间 → 排盘引擎算 144 星 × 12 宫的结构化数据 → DeepSeek-V4-Pro 读古籍加命盘 → 推理流年大限 → 输出能溯源到古书原文的报告。

整套链路在 FateStar 后端跑，DeepSeek 占运营成本约 90%。

## Verification

打开 [fatestar.top](https://fatestar.top)，看底部输入框右下角的模型 dropdown，会直接看到：

- 快速模式 — `DeepSeek-V4-Flash Thinking Max`
- 思考模式 — `DeepSeek-V4-Pro Thinking Max`

这两个是给用户的友好命名，后端调的是 DeepSeek 官方 `deepseek-v4-pro` 跟 `deepseek-v4-flash`。

底部声明：「FateStar 根据中国传统文化『紫微斗数』主席『命盘』进行分析推理，内容仅供参考。」FateStar 做的是中文传统文化数字化，DeepSeek-V4 是核心推理引擎。

## 试用

[fatestar.top](https://fatestar.top)，输入出生时间。不用注册，30 秒拿到一份基础命盘（V4-Flash 生成）。深度报告（V4-Pro Thinking 模式跑的链式推理）走付费版。

## 截图

<p align="center">
  <img src="./assets/screenshot.png" alt="FateStar 命盘截图" width="640" />
</p>

## 联系

- 官网 [fatestar.top](https://fatestar.top)
- 邮箱 hello@fatestar.top
