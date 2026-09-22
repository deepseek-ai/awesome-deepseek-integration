<img src="./assets/icon.png" width="64" height="auto" />

# [DeepSeeker-Code](https://github.com/xknk/deepseeker-code)

DeepSeeker-Code 是一个由 DeepSeek API 驱动的本地优先 AI 编码助手。自研 agentic 引擎配三种等价入口——VS Code 插件、终端 CLI（React Ink）、本地 HTTP API——共享同一 core、工具链与会话存储，同一项目下会话可跨入口互续。

## 安装

**VS Code 插件**：从仓库 Releases 安装 `.vsix`，在设置里填 `deepseekerCode.apiKey`，命令面板执行 `DeepSeeker-Code: 打开聊天`（或按 `Ctrl+Esc`）。插件自包含——引擎已内联，无需另装 CLI。

**终端 CLI**：

```bash
npm install -g deepseeker-code
export DEEP_SEEK_API_KEY=sk-***
cd 你的项目 && deepseeker-code
```

## 核心特性

1. **Agentic 编码引擎**：流式 agent 主循环 + 完整工具链——文件读/写/编辑/移动/删除（含 AST 符号大纲）、命令执行（前台/后台进程）、ripgrep 内容搜索 + glob 文件搜索、Git 操作、网页抓取与搜索、全方法 HTTP 客户端（本地联调）、TypeScript/JS 代码导航与类型诊断、Word/PDF/Excel 文档阅读、worktree 管理、子 Agent 编排。

2. **审批网关**：只读工具免审执行，文件修改与危险操作需明确审批；「总是允许」会持久化为 glob 权限规则。

3. **上下文压缩与召回**：面向长任务调优的自动对话压缩，实体索引无损；被归档消息与超长工具结果可经内置 `recall` 工具按需取回，长会话细节不丢、免重跑工具。

4. **两阶段计划模式**：先只读调研，再提交实施方案供你审批，批准后才开始写代码。

5. **每次修改都有 diff**：文件编辑以 diff 呈现——CLI 红绿内联、VS Code 左右对比、或原生 `vscode.diff` 编辑器。

6. **多模态输入**：开启视觉模式后可在聊天中直接贴图提问（单张 ≤ 8MB）。

7. **MCP / Hooks / Skills / 子 Agent**：四套扩展机制——MCP 接外部工具、声明式生命周期 Hooks、Skills 按需加载、工作流子 Agent。

## 接入 DeepSeek API

DeepSeeker-Code 直连 DeepSeek API，设置 key 后可选覆盖接入点或模型：

```bash
export DEEP_SEEK_API_KEY=sk-***                     # 必填
export DEEP_SEEK_API_URL=https://api.deepseek.com   # 可选
export DEEP_SEEK_MODEL=deepseek-chat                # 可选
```

VS Code 插件则在设置里填 `deepseekerCode.apiKey`。两个入口的配置与会话都存放在 `~/.deepseeker-code/`。

## 最佳实践

1. **保持审批网关开启**：尤其在写操作上，逐次审批或只对可信路径授予 glob 规则。

2. **非平凡任务先走计划模式**：让 agent 先只读调研、对齐方案，再动手改代码。
