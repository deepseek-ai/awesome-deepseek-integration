# 轻译 (LightTranslate)

[English](README.md)

轻译是一款 MIT 开源的 Windows 划词翻译与英语查词工具，默认将文本译为简体中文。

- 项目与完整源码：https://github.com/shanghaiyangming/lighttranslate
- Windows 安装包 / 便携 EXE：https://github.com/shanghaiyangming/lighttranslate/releases/latest

## 配置 DeepSeek

1. 下载 Windows x64 安装包并安装，或直接运行便携 EXE。
2. 首次启动在设置中填写自己的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
3. 保留接口 `https://api.deepseek.com`、模型 `deepseek-flash`，点击保存。
4. 在其他应用中选中可复制的文字，按 **Ctrl+Alt+Q** 后松开按键。

译文在鼠标旁的小浮窗中逐步显示。英文单词和短语可查看 IPA、含义、用法、例句与词源。支持常见 Markdown 格式、复制、取消、重试、粘贴翻译、自定义快捷键和可选开机启动。

## API 接入与隐私

程序直接调用 DeepSeek 的 `/chat/completions`，使用用户自己的 Bearer 密钥认证，发送 `stream: true` 和 `thinking.type: disabled`。密钥通过 Windows 当前用户 DPAPI 加密保存在本机，不保存翻译历史；原文与提示词会发送至用户设置的 API 服务商。

软件免费，API 由服务商向用户账号按用量计费。要求 Windows 10/11 x64、.NET Framework 4.8、可访问 API 的网络和可用额度。音标与词源由模型生成，可能有误；不支持图片 OCR。
