# BiliCommentBot

<div align="center">
<img src="https://avatars.githubusercontent.com/u/178089866?v=4" width="128" alt="BiliCommentBot Logo">
</div>

## English

> **Intelligent Bilibili comment replies powered by DeepSeek AI, fully managed through an elegant Web UI.**

**BiliCommentBot** is a Python bot that automatically monitors and replies to new comments on your Bilibili account's videos using the **DeepSeek API**. With an intuitive **Web UI management interface** and **Docker one-click deployment**, you can set up a smart comment assistant in minutes without touching any configuration files.

**Features:**
- **Docker Ultra-Lightweight**: Average memory usage ~50MB, max under 100MB
- **Web UI Dashboard**: Start/stop bot, view real-time logs, browse reply history — all from the browser
- **DeepSeek AI Replies**: Generate intelligent, context-aware responses using DeepSeek API
- **Chain Replies (Nested Comments)**: Monitor and reply to sub-comments on main comments for multi-layer conversations
- **QR Code Login**: Scan to get Bilibili Cookie, no manual extraction needed
- **Cookie Auto-Refresh**: Never worry about login expiration again
- **Smart Rate Limiting**: Exponential backoff, random jitter, and Bilibili error code detection
- **Hot-Reload Config**: Edit settings in Web UI and they take effect immediately — no restart required
- **Video List Caching**: Reduce API calls with automatic caching (12-hour default TTL)
- **Reply History**: Browse all past replies with pagination
- **Real-Time Logs**: WebSocket-powered live log feed with level filtering
- **Password Protection**: Optional login password for the Web UI
- **Docker & Local Deploy**: Run via Docker Compose or directly with Python

---

## 简体中文

> **基于 DeepSeek AI 的 B 站评论智能回复机器人，优雅的 Web UI 全盘掌控。**

**BiliCommentBot** 是一款使用 **DeepSeek API** 自动回复 B 站账号下视频新增评论的 Python 机器人。它配备了完整的 **Web UI 管理界面**，支持 **Docker 一键部署**，让你无需修改配置文件即可轻松上手。

**核心特性：**
- **🐳 Docker 部署超轻量**：内存占用平均仅约 50M，最高不超过 100M
- **🌐 Web UI 管理界面**：启动后浏览器中完成所有配置和操作
- **🤖 自动监控**：自动检测 B 站视频新增评论，智能回复
- **🎯 指定视频回复**：支持只回复某个特定视频下的评论
- **🧠 DeepSeek API 驱动**：生成自然、有温度的智能回复
- **📝 链式回复（楼中楼）**：支持多层子评论的对话互动
- **📱 扫码登录**：B 站 APP 扫码一键获取 Cookie，无需手动提取
- **🔄 Cookie 自动刷新**：彻底告别登录过期问题
- **🛡️ 智能频率控制**：指数退避 + 随机抖动 + 错误码检测，稳定运行
- **⚙️ 配置热更新**：Web UI 修改配置即刻生效，无需重启
- **📚 回复历史**：分页查看所有回复记录
- **📋 实时日志**：WebSocket 推送，按级别过滤，自动滚动
- **🔒 登录保护**：可设置 Web UI 访问密码
- **📦 Docker & 本地运行**：二选一，满足不同部署需求

---

## Quick Start | 快速开始

### Docker (Recommended | 推荐)

```bash
docker run -d \
  --name bilicomment-bot \
  -p 5000:5000 \
  -v $(pwd)/data:/app/data \
  -e TZ=Asia/Shanghai \
  janson20/bilicommentbot:latest
```

Then open `http://localhost:5000` in your browser.

### Local | 本地运行

```bash
# Install dependencies
pip install -r requirements.txt

# Start the bot
python main.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## How It Works | 工作原理

```
┌─────────────────────────────────────────────────────┐
│                    BiliCommentBot                     │
│                                                       │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────┐ │
│  │  Bilibili    │───▶│  Comment     │───▶│  DeepSeek │ │
│  │  API Poller  │    │  Filter      │    │  API      │ │
│  └─────────────┘    └──────────────┘    └──────────┘ │
│         │                                                  │
│         ▼                                                  │
│  ┌─────────────┐                                        │
│  │  Reply &     │                                        │
│  │  Log Result  │                                        │
│  └─────────────┘                                        │
│                                                       │
│  ┌──────────────────────────────────────────────────┐ │
│  │              Web UI (Flask + SocketIO)            │ │
│  │  Config │ Dashboard │ History │ Logs │ Login     │ │
│  └──────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

## Links | 链接

[![GitHub](https://img.shields.io/badge/GitHub-BiliCommentBot-black?logo=github)](https://github.com/Janson20/BiliCommentBot)
[![Docker Hub](https://img.shields.io/badge/Docker-Hub-2496ED?logo=docker)](https://hub.docker.com/r/janson20/bilicommentbot)
[![GHCR](https://img.shields.io/badge/GHCR-Package-181717?logo=github)](https://ghcr.io/janson20/bilicommentbot)
