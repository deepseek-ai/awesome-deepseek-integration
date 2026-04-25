# CodeGate:安全的 AI 代码生成

CodeGate 是一个**本地代理**,可以让 AI 代理和编码助手更加安全。它确保 AI 生成的建议遵循最佳实践,同时保护您的代码完整性和隐私。使用 CodeGate,您可以在开发工作流程中自信地利用 AI,而不会牺牲安全性或生产力。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/stacklok/codegate/main/static/diagram-dark.png">
  <img alt="CodeGate dashboard" src="https://github.com/stacklok/codegate/raw/main/static/diagram-light.png" width="1100px" style="max-width: 100%;">
</picture>

---
## ✨ 为什么选择 CodeGate?

AI 编码助手功能强大,但可能会无意中带来风险。CodeGate 通过以下方式保护您的开发过程:

- 🔒 防止意外泄露机密和敏感数据
- 🛡️ 确保 AI 建议遵循安全编码实践
- ⚠️ 阻止推荐已知的恶意或已弃用的库
- 🔍 提供 AI 建议的实时安全分析

---
## 🚀 使用 🐋 Deepseek 快速开始!

### 前提条件

CodeGate 以 Docker 容器的形式分发。您需要一个容器运行时,如 Docker Desktop 或 Docker Engine。同时也支持 Podman 和 Podman Desktop。CodeGate 可在 Windows、macOS 和 Linux 操作系统上运行,支持 x86_64 和 arm64(ARM 和 Apple Silicon)CPU 架构。

以下说明基于 `docker` CLI 可用的前提。如果您使用 Podman,请在所有命令中将 `docker` 替换为 `podman`。

### 安装

要启动 CodeGate,运行这个简单的命令(确保将 deepseek.com URL 作为 `CODEGATE_PROVIDER_OPENAI_URL` 环境变量传入):

```bash
docker run --name codegate -d -p 8989:8989 -p 9090:9090 -p 8990:8990 \
  -e CODEGATE_PROVIDER_OPENAI_URL=https://api.deepseek.com \
  --mount type=volume,src=codegate_volume,dst=/app/codegate_volume \
  --restart unless-stopped ghcr.io/stacklok/codegate:latest
```

就是这样!CodeGate 现在在本地运行了。

### 在 Continue 中使用 CodeGate 和 🐋 Deepseek

要在 Continue 中使用 CodeGate,打开 Continue 设置并添加以下配置:

```json
{
    "title": "Deepseek-v4-pro",
    "provider": "openai",
    "model": "deepseek-v4-pro",
    "apiKey": "YOUR_DEEPSEEK_API_KEY",
    "apiBase": "http://localhost:8989/openai",
}
```

像往常一样使用 Continue,您不再需要担心安全或隐私问题!

![continue-image](](https://github.com/deepseek/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/continue-screen.png))

### 在 Cline 中使用 CodeGate 和 🐋 Deepseek

要在 Cline 中使用 CodeGate,打开 Cline 设置并添加以下配置:

![cline-settings](https://github.com/deepseek/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/cline-settings.png)

像往常一样使用 Cline,您不再需要担心安全或隐私问题!

![cline-image](https://github.com/deepseek/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/cline-screen.png)

---
## 🖥️ 仪表板

CodeGate 包含一个 Web 仪表板,提供:

- CodeGate 检测到的**安全风险**视图
- AI 编码助手与 LLM 之间的**交互历史**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/dashboard-dark.webp">
  <img alt="CodeGate dashboard" src="./static/dashboard-light.webp" width="1200px" style="max-width: 100%;">
</picture>

### 访问仪表板

在您的网络浏览器中打开 [http://localhost:9090](http://localhost:9090) 以访问仪表板。

要了解更多信息,请访问 [CodeGate 仪表板文档](https://docs.codegate.ai/how-to/dashboard)。

---
## 🔐 功能

### 机密加密

CodeGate 通过使用加密对检测到的机密进行编辑,帮助您防止敏感信息意外暴露给 AI 模型和第三方 AI 提供商系统。
[了解更多](https://docs.codegate.ai/features/secrets-encryption)

### 依赖风险意识

LLM 的知识截止日期通常是几个月甚至几年前。它们可能会建议过时的、易受攻击的或不存在的包(幻觉),使您和您的用户面临安全风险。

CodeGate 扫描您作为上下文提供给 LLM 的包定义文件、安装脚本和源代码导入中的直接依赖、传递依赖和开发依赖。
[了解更多](https://docs.codegate.ai/features/dependency-risk)

### 安全审查

CodeGate 执行以安全为中心的代码审查,识别不安全的模式或潜在的漏洞,帮助您采用更安全的编码实践。
[了解更多](https://docs.codegate.ai/features/security-reviews)

---
## 🛡️ 隐私优先

与其他工具不同,使用 CodeGate **您的代码永远不会离开您的机器**。CodeGate 以隐私为核心构建:

- 🏠 **所有数据均本地存储**
- 🚫 **没有外部数据收集**
- 🔐 **没有回传或遥测**
- 💪 **完全控制您的数据**

---
## 🛠️ 开发

您是想要贡献的开发者吗?深入了解我们的技术资源:

- [开发指南](https://github.com/stacklok/codegate/blob/main/docs/development.md)
- [CLI 命令和标志](https://github.com/stacklok/codegate/blob/main/docs/cli.md)
- [配置系统](https://github.com/stacklok/codegate/blob/main/docs/configuration.md)
- [日志系统](https://github.com/stacklok/codegate/blob/main/docs/logging.md)

---
## 📜 许可证

CodeGate 根据 [LICENSE 文件](https://github.com/stacklok/codegate/blob/main/LICENSE) 中指定的条款获得许可。
