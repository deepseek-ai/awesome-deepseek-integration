# DeepSeek CLI (`deepseek`)

[DeepSeek CLI](https://github.com/surf1k/deepseek-cli) 是一个使用纯 Rust 编写的极速、轻量级 DeepSeek-V3 和 DeepSeek-R1 命令行终端客户端与代码助手。

## 特性

- **超快启动**: 纯 Rust 编写，毫秒级即时启动，极低内存占用。
- **DeepThink / R1 思考过程实时流式显示**: 在输出最终答案前，独立格式化展示推理思维链。
- **交互式 REPL**: 支持多轮对话、持久历史记录、多行输入及会话导出（`/save`）。
- **Unix 管道支持**: 轻松结合终端工作流（`git diff | deepseek "编写提交信息"`）。
- **多文件上下文注入**: 使用 `-f <file>` 快速加载本地代码文件。
- **开箱即用**: 支持通过 `deepseek config set-key <KEY>` 或 `DEEPSEEK_API_KEY` 环境变量配置。

## 快速使用

```bash
cargo install --git https://github.com/surf1k/deepseek-cli
export DEEPSEEK_API_KEY="your-api-key"
deepseek "解释一下 Rust 中 Arc 和 Rc 的区别"
```

🔗 **项目地址**: https://github.com/surf1k/deepseek-cli
