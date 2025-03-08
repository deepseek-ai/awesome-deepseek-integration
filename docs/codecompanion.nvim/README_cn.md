# [codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim)

> AI 驱动的编码，在 Neovim 中无缝集成

**codecompanion.nvim** 是一个提高生产力的工具，它简化了在 Neovim 中使用大型语言模型（LLM）进行开发的方式。

## 特性

- :speech_balloon: 在 Neovim 中，[Copilot Chat](https://github.com/features/copilot) 与 [Zed AI](https://zed.dev/blog/zed-ai) 的结合
- :electric_plug: 支持 Anthropic、Copilot、Gemini、Ollama、OpenAI、Azure OpenAI、HuggingFace 和 xAI LLM（或自定义 LLM！）
- :rocket: 内联变换、代码生成与重构
- :robot: 通过变量、斜杠命令、代理/工具和工作流改善 LLM 输出
- :sparkles: 内置常用任务的提示词，例如 LSP 错误的建议和代码解释
- :building_construction: 创建自定义提示、变量和斜杠命令
- :books: 同时打开多个对话
- :muscle: 异步执行，提供快速的性能

## 安装

首先，导航到 Neovim 配置文件夹（默认情况下，Linux 上的路径是 `~/.config/nvim`）。

### 通过 `lazy.nvim` 安装

然后进入 `lua/plugins` 文件夹。创建一个名为 `init.lua` 的文件，并添加以下内容：

```lua
return {
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
  },
  config = function()
    require("codecompanion").setup({
      adapters = {
        deepseek = function()
          return require("codecompanion.adapters").extend("deepseek", {
            env = {
              api_key = "YOUR_API_KEY",
            },
          })
        end,
      },
      strategies = {
        chat = { adapter = "deepseek", },
        inline = { adapter = "deepseek" },
        agent = { adapter = "deepseek" },
      },
    })
  end
}
```
重新启动 Neovim，`lazy.nvim` 应该会自动下载并安装 `codecompanion.nvim` 插件及其依赖项。

### 通过 `mini.deps` 安装

将以下内容添加到你的 `init.lua` 中

```lua
local add, later = MiniDeps.add, MiniDeps.later

later(function()
  add({
    source = "olimorris/codecompanion.nvim",
    depends = {
      "nvim-lua/plenary.nvim",
      "nvim-treesitter/nvim-treesitter",
    },
  })
  require("codecompanion").setup({
    adapters = {
      deepseek = function()
        return require("codecompanion.adapters").extend("deepseek", {
          env = {
              api_key = "YOUR_API_KEY",
          },
        })
      end,
    },
    strategies = {
      chat = { adapter = "deepseek", },
      inline = { adapter = "deepseek" },
      agent = { adapter = "deepseek" },
    },
  })
end)
```

重新启动 Neovim，`mini.deps` 应该会自动下载并安装 `codecompanion.nvim` 插件。


### 其他安装方法
https://codecompanion.olimorris.dev/installation.html

## 使用
https://codecompanion.olimorris.dev/usage/introduction.html
