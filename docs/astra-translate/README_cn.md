<div align="center">
  <img src="assets/icon.png" alt="Astra Translate" width="96" />

# Astra Translate

轻量、优雅、供应商中立的浏览器翻译扩展。

[GitHub](https://github.com/avaritiachaos/astra-translate-extension) · [Releases](https://github.com/avaritiachaos/astra-translate-extension/releases) · [English](README.md)

</div>

## 简介

Astra Translate 是一个开源（MIT）的 Chrome 扩展（Manifest V3），可将任意 OpenAI 兼容的 LLM API 变成快速、细致的网页翻译器。内置 **DeepSeek 预设**——填入 API Key 即可开箱即用。

## 功能特性

- **整页翻译，视口优先** —— 先翻译可见区域，滚动到哪翻到哪；可切换整页全量模式。流式批量应用，模型每译完一段立即上屏。
- **块级分组** —— 同一段落的多个片段合并为完整语境一起翻译，保留行内标记。
- **划词翻译与词典模式** —— 选中即译；单词自动展示词典卡片（释义、发音、例句）。URL、代码、路径、哈希等自动保护不翻译。
- **即时 UI 词表** —— 内置词表 + 按站点学习的词汇表，常见按钮/标签在再次访问时零 API 延迟直接渲染。
- **高负载下的稳健性** —— 自适应并发配合 429/5xx 退避（尊重 `Retry-After`）、翻译缓存、诚实的错误上报。
- **三语界面** —— 简体中文 / English / 日本語。

## 接入 DeepSeek API

1. 在 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取 API Key。
2. 安装 Astra Translate（从 [Releases](https://github.com/avaritiachaos/astra-translate-extension/releases) 下载后，在 `chrome://extensions` 开启开发者模式 → 加载已解压的扩展程序）。
3. 打开扩展**设置**页 —— DeepSeek 是默认供应商预设（`https://api.deepseek.com`）。
4. 粘贴 API Key，选择模型（如 `deepseek-chat`），点击**测试**。
5. 开始翻译：弹窗中点击**翻译当前页面**、在任意页面划词，或选中文字后按 `Alt+T`。

DeepSeek 专属适配：设置页提供 DeepSeek 的思考开关，页面翻译时可关闭推理输出，更快更省。
