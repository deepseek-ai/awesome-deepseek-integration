<img src="./assets/logo.png" width="64" height="auto" />

# [ByeType](https://github.com/lixiaojie001/byetype)

**告别打字，用说的。**

ByeType 是一款由 Markdown 提示词驱动的 AI 语音输入与图像文字提取工具。通过编辑 Markdown 格式的提示词，你可以自定义专有词汇、识别规则和文本优化策略，让输出最大限度匹配你的行业术语和个人写作习惯。

ByeType 通过标准 API 调用 AI 模型，支持 DeepSeek 及多种多模态模型 —— 使用你自己的 API Key，语音和截图直接发送到你选择的服务商，ByeType 本身不收费、不经手数据。

## 功能特性

- 🎙️ **语音转文字** —— 按下快捷键，开口说，转写后自动粘贴到任何输入框
- 🖼️ **图像文字提取** —— 按 F6 截图选区，AI 识别文字后复制到剪贴板。能智能合并终端/PDF 截图中因窗口宽度产生的硬换行，还能还原被行号、分屏切碎的终端代码
- 📝 **Markdown 驱动提示词** —— 词汇、格式化规则、输出风格都是可编辑的 Markdown 文件。不同快捷键配不同风格（口语化、正式书写、翻译、邮件润色等），一键切换
- 🌐 **跨平台** —— macOS、Windows，以及 iPhone / iPad（通过 iOS 快捷指令）
- 🪶 **轻量** —— 安装包约 8 MB，无需本地模型文件

## 演示

![录音 → 转写 → 优化 → 自动粘贴](./assets/demo.gif)

## 配置 DeepSeek

在「设置 → 模型管理」中添加 DeepSeek 模型，填入从 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取的 API Key。内置预设包含 `deepseek-v4-flash` 和 `deepseek-v4-pro`，适合快速、低成本的文本优化。

语音转写和截图识别同样支持 Qwen Omni、Gemini、LongCat 等多模态模型，以及任何 OpenAI 兼容接口，配置方式相同。

## 链接

- GitHub：<https://github.com/lixiaojie001/byetype>
- 下载：<https://github.com/lixiaojie001/byetype/releases>
- 许可证：MIT
