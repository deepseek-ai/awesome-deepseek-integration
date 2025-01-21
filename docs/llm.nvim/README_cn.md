> [!IMPORTANT]
> 免费的大语言模型插件，让你在Neovim中与大模型交互
>
> 主要功能包括但不限于:
>
> - AI对话
> - 划词翻译
> - 解释代码
> - 优化代码
> - 生成测试用例
> - AI翻译
> - 生成git commit信息
> - 生成docstring

链接: [Github:Kurama622/llm.nvim](https://github.com/Kurama622/llm.nvim)

# 安装

- lazy.nvim

```lua
return {
  {
    "Kurama622/llm.nvim",
    dependencies = { "nvim-lua/plenary.nvim", "MunifTanjim/nui.nvim" },
    cmd = { "LLMSessionToggle", "LLMSelectedTextHandler", "LLMAppHandler" },
    config = function()
      require("llm").setup({
        url = "https://api.deepseek.com/chat/completions",
        model = "deepseek-chat",
        api_type = "openai",
        max_tokens = 4096,
        temperature = 0.3,
        top_p = 0.7,

        prompt = "You are a helpful Chinese assistant.",

        prefix = {
          user = { text = "  ", hl = "Title" },
          assistant = { text = "  ", hl = "Added" },
        },

        -- history_path = "/tmp/llm-history",
        save_session = true,
        max_history = 15,
        max_history_name_length = 20,

        -- stylua: ignore
        keys = {
          -- The keyboard mapping for the input window.
          ["Input:Submit"]      = { mode = "n", key = "<cr>" },
          ["Input:Cancel"]      = { mode = {"n", "i"}, key = "<C-c>" },
          ["Input:Resend"]      = { mode = {"n", "i"}, key = "<C-r>" },

          -- only works when "save_session = true"
          ["Input:HistoryNext"] = { mode = {"n", "i"}, key = "<C-j>" },
          ["Input:HistoryPrev"] = { mode = {"n", "i"}, key = "<C-k>" },

          -- The keyboard mapping for the output window in "split" style.
          ["Output:Ask"]        = { mode = "n", key = "i" },
          ["Output:Cancel"]     = { mode = "n", key = "<C-c>" },
          ["Output:Resend"]     = { mode = "n", key = "<C-r>" },

          -- The keyboard mapping for the output and input windows in "float" style.
          ["Session:Toggle"]    = { mode = "n", key = "<leader>ac" },
          ["Session:Close"]     = { mode = "n", key = {"<esc>", "Q"} },
        },
      })
    end,
    keys = {
      { "<leader>ac", mode = "n", "<cmd>LLMSessionToggle<cr>" },
      { "<leader>ae", mode = "v", "<cmd>LLMSelectedTextHandler 请解释下面这段代码<cr>" },
      { "<leader>ts", mode = "x", "<cmd>LLMSelectedTextHandler 英译汉<cr>" },
    },
  },
}
```

