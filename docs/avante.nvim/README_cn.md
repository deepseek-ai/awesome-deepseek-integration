# [avante.nvim](https://github.com/yetone/avante.nvim)

**avante.nvim** 是一个旨在模拟 [Cursor](https://www.cursor.com) AI IDE 的行为的 Neovim 插件。它为用户提供 AI 驱动的代码建议，并能够以最小的努力将这些建议直接应用于他们的源文件。

## 功能

 - **AI 驱动的代码辅助**：与 AI 聊天以询问有关您当前代码文件的问题，并接收改进或修改的智能建议。
 - **一键应用**：使用单个命令快速将 AI 建议的更改应用于您的源代码，简化编辑过程并节省时间。

> [!IMPORTANT]
>
> 该项目处于快速迭代状态，本指南更新于2024.10.19，在此日期之后的安装配置方法可能会发生变更，请以原项目README.md为准。


## 安装

### 通过 `lazy.nvim` 安装

转到nvim的配置文件夹下（linux 默认是`~/.config/nvim`）的 `lua/plugins` 文件夹，创建一个名为 `avante.lua` 的文件，并在其中添加以下内容：   
```lua
return {
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    lazy = false,
    version = false, -- set this if you want to always pull the latest change
    opts = {
      provider = "deepseek",
      vendors = {
        deepseek = {
          __inherited_from = "openai",
          api_key_name = "DEEPSEEK_API_KEY",
          endpoint = "https://api.deepseek.com",
          model = "deepseek-coder",
        },
      },
    },
    -- if you want to build from source then do `make BUILD_FROM_SOURCE=true`
    build = "make",
    -- build = "powershell -ExecutionPolicy Bypass -File Build.ps1 -BuildFromSource false" -- for windows
    dependencies = {
      "nvim-treesitter/nvim-treesitter",
      "stevearc/dressing.nvim",
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      --- The below dependencies are optional,
      "nvim-tree/nvim-web-devicons", -- or echasnovski/mini.icons
      "zbirenbaum/copilot.lua", -- for providers='copilot'
      {
        -- support for image pasting
        "HakonHarnes/img-clip.nvim",
        event = "VeryLazy",
        opts = {
          -- recommended settings
          default = {
            embed_image_as_base64 = false,
            prompt_for_file_name = false,
            drag_and_drop = {
              insert_mode = true,
            },
            -- required for Windows users
            use_absolute_path = true,
          },
        },
      },
      {
        -- Make sure to set this up properly if you have lazy=true
        'MeanderingProgrammer/render-markdown.nvim',
        opts = {
          file_types = { "markdown", "Avante" },
        },
        ft = { "markdown", "Avante" },
      },
    },
  },
}
```

重启 nvim，此时`lazy.nvim`应该会根据上述文件帮你下载安装好 avante.nvim 插件及其依赖项。

### 其他安装方式

https://github.com/yetone/avante.nvim?tab=readme-ov-file#installation

## 使用

https://github.com/yetone/avante.nvim?tab=readme-ov-file#usage
