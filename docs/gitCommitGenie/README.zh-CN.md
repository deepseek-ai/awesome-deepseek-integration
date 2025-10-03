<div align="center">

# Git Commit Genie

English version: [English README](../gitCommitGenie/README.md)

</div>

## 概述

Git Commit Genie 基于已暂存的 Git diff，使用主流大模型（OpenAI / DeepSeek / Anthropic / Gemini）自动生成高质量的 Conventional Commits 风格提交信息。内置仓库智能分析功能，自动理解项目结构和技术栈，为提交信息生成提供更好的上下文。支持可选"链式提示"模式（多步推理）与"用户模板"策略，显著提升结构一致性与团队风格统一。

优势：
- 避免在提交语句格式/措辞上反复纠结。
- 严格符合 Conventional Commits（类型、scope、BREAKING CHANGE）。
- 通过一个简单的模板文件定义 Body / Footers / 语气 / 词汇偏好。
- 支持多模型动态切换，快速选择最适合的提供商与模型。

## Usage
<img src="../gitCommitGenie/demo1.gif" width="300"/>

## 格式

默认生成的提交信息遵循 Conventional Commits 1.0.0 规范，详情见：https://www.conventionalcommits.org/zh-hans/v1.0.0/

基本格式：
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Tips

- 少量 / 轻量级提交：优先选择轻巧快速的模型，生成更快、Token 消耗更低。
- 大型 / 多文件提交：再考虑切换更强的模型，以获得更好的理解与结构质量。
- 可随时通过命令面板运行 "Git Commit Genie: Manage Models" 切换模型。

## 核心特性

| 特性                     | 说明                                                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| 多模型提供商             | 支持 OpenAI、DeepSeek、Anthropic、Gemini等。                                                         |
| 仓库智能分析             | 自动分析项目结构、技术栈和架构，为提交信息生成提供上下文；支持手动刷新、实时更新和手动修改分析报告。 |
| 链式提示模式             | 多步：文件级摘要 → 结构化综合 → 校验修复，显著提升准确度与模板贴合度。                               |
| 用户模板策略             | 内置模板选择和创建功能，支持工作区和用户数据目录，抽取策略影响段落顺序、必填 footers、词汇偏好等。   |
| Conventional Commit 校验 | 头行格式（type(scope)!: desc），长度 ≤ 72，无句号。                                                  |
| Diff 感知                | 仅读取"已暂存"更改；自动推断类型（feat / fix / docs / refactor 等）。                                |
| Token 与速率保护         | 429 自动退避重试；Gemini 软限本地节流；并发可配置。                                                  |
| 状态栏集成               | 显示当前模型和分析状态，点击可访问功能菜单。                                                         |
| 生成取消                 | SCM 标题栏按钮可实时取消正在进行的生成。                                                             |
| 安全存储                 | API Key 使用 VS Code SecretStorage，不写入明文设置。                                                 |
| 国际化支持               | 内置英文、简体中文、繁体中文等多语言支持。                                                           |

## 工作流程

1. 暂存（Stage）你的变更。
2. 执行命令：`Git Commit Genie: AI Generate`（SCM 顶部按钮或命令面板）。
3. 若开启链式模式：
   - 并行生成文件级摘要
   - 综合分析类型与 scope
   - 应用模板策略（若有效）
   - 结构 + 风格自检与最小修复
4. 输出写入仓库提交框，可人工微调后提交。

未开启链式：使用单轮提示 → 更低延迟，但结构与风格细腻度稍弱。

## 安装

1. VS Code 市场搜索 “Git Commit Genie” 安装，或使用打包 `.vsix` 手动安装。
2. 命令面板运行 `Git Commit Genie: Manage Models` 选择 Provider、输入/替换 API Key、选择模型。
3. （可选）使用命令 `Git Commit Genie: Select/Create Template` 选择或创建模板文件。

## 运行要求

| 项       | 说明                        |
| -------- | --------------------------- |
| VS Code  | 版本需满足引擎 `^1.103.0`。 |
| Git 扩展 | 内置 `vscode.git`，需启用。 |
| 网络访问 | 调用所选 LLM 提供商。       |
| API Key  | 使用的每个提供商都需要。    |

## 配置项

所有设置位于：`Git Commit Genie`。

| Setting                                             | 类型    | 默认    | 说明                                                                                                                                         |
| --------------------------------------------------- | ------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `gitCommitGenie.autoStageAllForDiff`                | boolean | false   | 仅当暂存区为空时：临时将所有更改加入暂存用于生成 diff，生成后会自动还原暂存状态。谨慎使用，可能会把无关更改包含进提示。                      |
| `gitCommitGenie.chain.enabled`                      | boolean | false   | 启用链式多步提示生成提交信息（使得生成的提交信息更加详准确，且可以更加贴合用户模版，但将增加延迟与 Token 消耗）                              |
| `gitCommitGenie.chain.maxParallel`                  | number  | 2       | 链式提示并行 LLM 调用最大数量。谨慎增大以避免触发速率限制。                                                                                  |
| `gitCommitGenie.llm.maxRetries`                     | number  | 2       | API请求失败最大重试次数。                                                                                                                    |
| `gitCommitGenie.llm.temperature`                    | number  | 0.2     | Temperature（0–2），默认为 0.2。                                                                                                             |
| `gitCommitGenie.repositoryAnalysis.enabled`         | boolean | true    | 启用仓库分析以提供更好的提交信息生成上下文。                                                                                                 |
| `gitCommitGenie.repositoryAnalysis.excludePatterns` | array   | []      | 仓库分析扫描时要排除的文件模式（gitignore风格）。                                                                                            |
| `gitCommitGenie.repositoryAnalysis.updateThreshold` | number  | 10      | 更新仓库分析的提交次数阈值。                                                                                                                 |
| `gitCommitGenie.repositoryAnalysis.model`           | enum    | general | 用于仓库分析的模型。可选择所有供应商支持的模型，系统将自动切换到该模型所属的服务商；或选择“使用与commit message生成相同的模型”以复用主模型。 |
| `gitCommitGenie.commitLanguage`                     | string  | `auto`  | 生成的提交信息目标语言。选项：`auto`、`en`、`zh-CN`、`zh-TW`、`ja`、`ko`、`de`、`fr`、`es`、`pt`、`ru`、`it`。                               |
| `gitCommitGenie.typingAnimationSpeed`               | number  | 15      | 提交信息框打字动画速度，单位为每字符毫秒。设置 -1 关闭动画。                                                                                 |  |
| `gitCommitGenie.showUsageCost`                      | boolean | true    | 启用后在生成文本时弹出通知，显示本次生成的估计总费用。                                                                                       |



## 命令列表

| Command ID                                   | 标题                        | 作用                                         |
| -------------------------------------------- | --------------------------- | -------------------------------------------- |
| `git-commit-genie.generateCommitMessage`     | AI Generate                 | 基于已暂存更改生成提交信息。                 |
| `git-commit-genie.cancelGeneration`          | Stop                        | 取消当前生成。                               |
| `git-commit-genie.manageModels`              | Manage Models               | 选择提供商 / 输入或更换 API Key / 选择模型。 |
| `git-commit-genie.toggleChainMode`           | Toggle Chain Prompting      | 快速开启/关闭链式模式。                      |
| `git-commit-genie.selectTemplate`            | Select/Create Template      | 选择或新建提交信息模板文件。                 |
| `git-commit-genie.viewRepositoryAnalysis`    | View Repository Analysis    | 快速打开仓库分析报告。                       |
| `git-commit-genie.refreshRepositoryAnalysis` | Refresh Repository Analysis | 手动刷新仓库分析。                           |
| `git-commit-genie.cancelRepositoryAnalysis`  | Stop Repository Analysis    | 停止正在进行的仓库分析。                     |
| `git-commit-genie.genieMenu`                 | Menu                        | 打开Git Commit Genie功能菜单。               |
| `git-commit-genie.showRepositoryCost`        | Show Repository Cost        | 显示当前工作区累计消耗估算。                 |
| `git-commit-genie.resetRepositoryCost`       | Reset Repository Cost       | 重置当前工作区累计消耗估算。                 |

SCM 标题栏：根据状态显示“Generate commit message”或“Stop generate”按钮。

## 模板编写
使用命令 `Git Commit Genie: Select/Create Template` 选择或创建模板文件。

<img src="../gitCommitGenie//demo2.gif" width="600"/>

模版文件存在且非空时，系统尝试抽取“模板策略”。支持：
1. 自然语言偏好描述。
2. markdown模版编写。

完整指南： [English](./user-template-guide.md) | [中文](./user-template-guide.zh-CN.md)

最小示例：
```
Minimal Template
- Always include a body with Summary and Changes.
- Use imperative, no trailing period.
- Always include a `Refs` footer (use `Refs: N/A` when missing).
- Prefer: add, fix, refactor; Avoid: update.
```

## 链式模式 vs 单轮模式

| 模式 | 优点                             | 缺点                 | 适用场景                |
| ---- | -------------------------------- | -------------------- | ----------------------- |
| 链式 | 结构最佳，模板贴合度高，分类更准 | 延迟更高，Token 更多 | 多文件 / 需严格风格统一 |
| 单轮 | 快速，成本低                     | 结构细腻度较低       | 小变更 / 临时修复       |

通过命令或设置切换。

## 安全与隐私

- API Key 使用 SecretStorage，不以明文写入 settings.json， 不会以任何形式上传到互联网，仅保存在本地。
- 仅发送“已暂存 diff”中的文件名与修改上下文；不包括未暂存或未跟踪文件。
- 无遥测 / 分析数据收集。

## 常见问题（Troubleshooting）

| 现象                      | 原因                | 解决                                    |
| ------------------------- | ------------------- | --------------------------------------- |
| "No staged changes found" | 未暂存任何文件      | 使用 Source Control 或 `git add` 暂存。 |
| 生成内容空泛              | 模板不明确          | 尝试编写结构化的模版                    |
| 频繁 429                  | 并行过高 / 模板过大 | 降低 `chain.maxParallel`。              |
| 状态栏无“· Thinking”      | 未启用链式          | 使用命令或设置开启。                    |
| 重复要求输入 API Key      | 秘钥被清除          | 重新运行 Manage Models。                |



## 许可证

MIT

## 致谢

- [Conventional Commits](https://conventionalcommits.org/) - https://github.com/conventional-commits/conventionalcommits.org
- OpenAI / DeepSeek / Anthropic / Gemini 模型生态

---

让提交信息不再痛苦。
