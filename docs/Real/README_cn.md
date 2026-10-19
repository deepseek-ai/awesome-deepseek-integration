___
<img src="assets/logo.png" width="auto" height="auto" />

___

# [Real](https://github.com/Azzrenz/Real)

Real 是一个跑在 Windows 上的本地 AI Agent 工作台。给它一个项目文件夹和一句话需求，它会在那个目录里读文件、改文件、跑命令、看报错，一轮一轮改到真正交付为止。文件都在本机处理，只有对话内容会发给模型接口。

技术栈 Rust + Tauri 2 + React，MIT 开源。

## 它和聊天窗有什么区别

- **收敛循环，不是聊天。** 每一轮要么真的改了文件，要么记为无改动；只说"改好了"但没动文件的那一轮不算数。
- **每一步可审计。** 工具调用、文件写入、命令输出都留成卡片，可以点开回看。
- **危险操作有确认门。** 删除文件、执行 shell 命令会先问你。
- **模型可切换。** DeepSeek 与智谱 GLM 可同时配置，换模型不用重启。

## 接入 DeepSeek API

Real 走标准 OpenAI 兼容接口，配置大约 30 秒：

1. 打开 **Settings → Model & credentials**
2. **API key (DeepSeek)**：粘贴 [platform.deepseek.com](https://platform.deepseek.com/api_keys) 申请的 Key
3. **API Base URL**：`https://api.deepseek.com`
4. **Model name**：`deepseek-flash`
5. 点 **Test connection**，再点 **Save settings**

不需要重启，下一轮就直接用 DeepSeek。

也可以在 `real-client.exe` 同目录的 `.env` 里设置 `DEEPSEEK_API_KEY`，适合脚本化安装。

## 常见用法

- 按日期或内容批量重命名、归档文件
- 搭一条视频流水线：抓素材 → 去字幕 → 改文案 → 配音 → 合成
- 用自然语言提需求（"加一个深色主题"），让它自己改完整个项目
- 任何原本要你手动点几百下的重复活

## 链接

- 源码：https://github.com/Azzrenz/Real
- 下载（Windows 便携版 12MB）：https://github.com/Azzrenz/Real/releases
- 协议：MIT
