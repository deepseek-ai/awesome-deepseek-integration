# Minuet AI

Minuet AI：在您的代码中翩翩起舞，挥洒智能 💃。

`Minuet-ai` 将小步舞曲的优雅与和谐带入您的编码流程。正如舞者在小步舞曲中舞动一样。

# 特性

- 基于 AI 的代码补全，提供双重模式：
  - 针对代码补全任务，为基于聊天的 LLMs 提供专门的提示和各种增强功能。
  - 针对兼容的模型（DeepSeek、Codestral、Qwen 等）提供中间填充 (FIM) 补全。
- 支持多种 AI 提供商（OpenAI、Claude、Gemini、Codestral、Ollama 和兼容 OpenAI 的服务）。
- 可自定义配置选项。
- 支持流式传输，即使使用较慢的 LLMs 也能实现补全的交付。
- 支持 `nvim-cmp`、`blink-cmp`、`virtual text` 前端。

# 要求

- Neovim 0.10+。
- [plenary.nvim](https://github.com/nvim-lua/plenary.nvim)
- 可选： [nvim-cmp](https://github.com/hrsh7th/nvim-cmp)
- 可选： [blink.cmp](https://github.com/Saghen/blink.cmp)
- 至少一个受支持的 AI 提供商的 API 密钥

# 安装

**Lazy.nvim：**

```lua
specs = {
    {
        'milanglacier/minuet-ai.nvim',
        config = function()
            require('minuet').setup {
                -- 在此处配置您的选项
            }
        end,
    },
    { 'nvim-lua/plenary.nvim' },
    -- 可选，如果您使用 virtual-text 前端，则不需要 nvim-cmp。
    { 'hrsh7th/nvim-cmp' },
    -- 可选，如果您使用 virtual-text 前端，则不需要 blink。
    { 'Saghen/blink.cmp' },
}
```

**Rocks.nvim：**

`Minuet` 可在 luarocks.org 上获取。只需运行 `Rocks install minuet-ai.nvim` 即可像安装其他 luarocks 包一样安装它。

**使用 virtual text 进行设置：**

```lua
require('minuet').setup {
    virtualtext = {
        auto_trigger_ft = {},
        keymap = {
            -- 接受完整补全
            accept = '<A-A>',
            -- 接受一行
            accept_line = '<A-a>',
            -- 接受 n 行（提示输入数字）
            -- 例如，“A-z 2 CR”将接受 2 行
            accept_n_lines = '<A-z>',
            -- 切换到上一个补全项，或手动调用补全
            prev = '<A-[>',
            -- 切换到下一个补全项，或手动调用补全
            next = '<A-]>',
            dismiss = '<A-e>',
        },
    },
}
```

**使用 nvim-cmp 进行设置：**

<details>

```lua
require('cmp').setup {
    sources = {
        {
             -- 包含 minuet 作为源以启用自动补全
            { name = 'minuet' },
            -- 和您的其他来源
        }
    },
    performance = {
        -- 建议增加超时时间，因为与其他补全来源相比，LLMs 的响应速度通常较慢。如果您只需要手动补全，则不需要此设置。
        fetching_timeout = 2000,
    },
}


-- 如果你希望手动调用补全，
-- 以下配置将 `A-y` 键绑定到手动调用配置。
require('cmp').setup {
    mapping = {
        ["<A-y>"] = require('minuet').make_cmp_map()
        -- 和您的其他键映射
    },
}
```

</details>

**使用 blink-cmp 进行设置：**

<details>

```lua
require('blink-cmp').setup {
    keymap = {
        -- 手动调用 minuet 补全。
        ['<A-y>'] = require('minuet').make_blink_map(),
    },
    sources = {
         -- 启用 minuet 进行自动补全
        default = { 'lsp', 'path', 'buffer', 'snippets', 'minuet' },
        -- 仅对于手动补全，从默认值中删除 'minuet'
        providers = {
            minuet = {
                name = 'minuet',
                module = 'minuet.blink',
                score_offset = 8, -- 在建议中赋予 minuet 更高的优先级
            },
        },
    },
    -- 建议避免不必要的请求
    completion = { trigger = { prefetch_on_insert = false } },
}
```

</details>

**LLM 提供商示例：**

**Deepseek：**

```lua
-- 你可以使用 openai_fim_compatible 或 openai_compatible 提供商来使用 deepseek
require('minuet').setup {
    provider = 'openai_fim_compatible',
    provider_options = {
        openai_fim_compatible = {
            api_key = 'DEEPSEEK_API_KEY',
            name = 'deepseek',
            optional = {
                max_tokens = 256,
                top_p = 0.9,
            },
        },
    },
}


-- 或者
require('minuet').setup {
    provider = 'openai_compatible',
    provider_options = {
        openai_compatible = {
            end_point = 'https://api.deepseek.com/v1/chat/completions',
            api_key = 'DEEPSEEK_API_KEY',
            name = 'deepseek',
            optional = {
                max_tokens = 256,
                top_p = 0.9,
            },
        },
    },
}
```
