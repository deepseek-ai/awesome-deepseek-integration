<img src="assets/logo.png" width="64" height="auto" alt="ClariRec" />

# [ClariRec](https://clarirec.com/)

ClariRec 是一款原生 macOS OCR 与翻译工具。默认用系统 Vision 在本地完成截图 / 剪贴板 / 文件 OCR，并可选用你自己的 API Key（含 DeepSeek）做翻译。

## 功能亮点

- 截图 OCR（`⌥S`）、剪贴板 OCR（`⌥V`）、文件 OCR
- 默认本地 OCR，无需注册 ClariRec 账号
- BYOK 翻译支持 DeepSeek 等引擎（API Key 保存在本机）
- 可选本地离线翻译模型与 macOS 系统翻译
- 结果窗口支持复制 / 导出、Smart Cleanup、Markdown 表格
- 快捷指令与 `clarirec://` URL Scheme 自动化

## UI

![ClariRec 结果窗口](assets/ui-result.png)

![ClariRec DeepSeek 引擎配置](assets/ui-provider.png)

## 接入 DeepSeek API

1. 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
2. 打开 **ClariRec → 设置 → 引擎**。
3. 在列表中选择 **DeepSeek**。
4. 在 **API 密钥** 中粘贴你的 Key。
5. 点击 **测试连接** 验证是否可用。
6. 将 **翻译引擎** 设为 **DeepSeek**（在引擎页或结果窗口均可）。

内置默认（无需自行填写端点）：

- 端点：`https://api.deepseek.com/chat/completions`
- 默认模型：`deepseek-v4-flash`

API Key 保存在 macOS 钥匙串中。ClariRec 直连 DeepSeek 官方 API，不经过任何代理或中间服务器。

## 使用

1. 通过截图 OCR（`⌥S`）、剪贴板 OCR（`⌥V`）或文件 OCR 取得文本。
2. 在结果窗口执行翻译（或开启自动翻译）。
3. 也可在 DeepSeek 为当前翻译引擎时，通过 macOS 服务 / 剪贴板热键（`⌥T`）翻译文本。

## 获取

[官网](https://clarirec.com/) · [Mac App Store](https://apps.apple.com/cn/app/clarirec/id6757385283?mt=12) · 需要 macOS 14.0+

> ClariRec 与 DeepSeek 无关联、未获背书或赞助。「DeepSeek」仅用于标明支持的 BYOK 翻译引擎。
