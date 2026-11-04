<img src="assets/logo.png" width="64" height="auto" />

# [My Assistant](https://myassistant.aplusz.app)

My Assistant 是一款自带 API 密钥的大模型聊天客户端。粘贴 DeepSeek 密钥后，每次调用都按 DeepSeek 的特点来：难题（代码、数学、多步推理、对比、长文）才走推理模型，按任务分别调参，对输出下硬性指令约束以保证精确，并采用贴合该 API 的重试策略。任意大小的文件编辑后逐字节原样返回，另有一道检查确认回复覆盖了你消息里的每一个问题。网页版（可安装）、Google Play、Microsoft Store，20 种语言。应用本身 €1.99/月，不抽取你的 token 费用，密钥只发往 DeepSeek。

## 配置 DeepSeek API

1. 打开 https://myassistant.aplusz.app，用邮箱登录。
2. 设置 → **你的 AI** → 粘贴 DeepSeek 密钥。应用自动识别服务商、向 DeepSeek 校验密钥、加密保存，并显示你的 DeepSeek 余额。
3. 点顶栏的 🔑 将其设为作答密钥。日常问题走 `deepseek-chat`，难题自动切换到 `deepseek-reasoner`。

## 界面

回复流式输出，"Thinking it through" 一行取自 DeepSeek 的推理内容；代码面板支持复制与下载；模型编辑过的每个文件都有版本记录。
