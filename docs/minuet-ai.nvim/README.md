
# Minuet AI

Minuet AI: Dance with Intelligence in Your Code 💃.

`Minuet-ai` brings the grace and harmony of a minuet to your coding process.
Just as dancers move during a minuet.

# Features

- AI-powered code completion with dual modes:
  - Specialized prompts and various enhancements for chat-based LLMs on code completion tasks.
  - Fill-in-the-middle (FIM) completion for compatible models (DeepSeek,
    Codestral, Qwen, and others).
- Support for multiple AI providers (OpenAI, Claude, Gemini, Codestral, Ollama, and
  OpenAI-compatible services).
- Customizable configuration options.
- Streaming support to enable completion delivery even with slower LLMs.
- Support `nvim-cmp`, `blink-cmp`, `virtual text` frontend.

# Requirements

- Neovim 0.10+.
- [plenary.nvim](https://github.com/nvim-lua/plenary.nvim)
- optional: [nvim-cmp](https://github.com/hrsh7th/nvim-cmp)
- optional: [blink.cmp](https://github.com/Saghen/blink.cmp)
- An API key for at least one of the supported AI providers

# Installation

**Lazy.nvim**:

```lua
specs = {
    {
        'milanglacier/minuet-ai.nvim',
        config = function()
            require('minuet').setup {
                -- Your configuration options here
            }
        end,
    },
    { 'nvim-lua/plenary.nvim' },
    -- optional, if you are using virtual-text frontend, nvim-cmp is not
    -- required.
    { 'hrsh7th/nvim-cmp' },
    -- optional, if you are using virtual-text frontend, blink is not required.
    { 'Saghen/blink.cmp' },
}
```

**Rocks.nvim**:

`Minuet` is available on luarocks.org. Simply run `Rocks install
minuet-ai.nvim` to install it like any other luarocks package.

**Setting up with virtual text**:

```lua
require('minuet').setup {
    virtualtext = {
        auto_trigger_ft = {},
        keymap = {
            -- accept whole completion
            accept = '<A-A>',
            -- accept one line
            accept_line = '<A-a>',
            -- accept n lines (prompts for number)
            -- e.g. "A-z 2 CR" will accept 2 lines
            accept_n_lines = '<A-z>',
            -- Cycle to prev completion item, or manually invoke completion
            prev = '<A-[>',
            -- Cycle to next completion item, or manually invoke completion
            next = '<A-]>',
            dismiss = '<A-e>',
        },
    },
}
```

**Setting up with nvim-cmp**:

<details>

```lua
require('cmp').setup {
    sources = {
        {
             -- Include minuet as a source to enable autocompletion
            { name = 'minuet' },
            -- and your other sources
        }
    },
    performance = {
        -- It is recommended to increase the timeout duration due to
        -- the typically slower response speed of LLMs compared to
        -- other completion sources. This is not needed when you only
        -- need manual completion.
        fetching_timeout = 2000,
    },
}


-- If you wish to invoke completion manually,
-- The following configuration binds `A-y` key
-- to invoke the configuration manually.
require('cmp').setup {
    mapping = {
        ["<A-y>"] = require('minuet').make_cmp_map()
        -- and your other keymappings
    },
}
```

</details>

**Setting up with blink-cmp**:

<details>

```lua
require('blink-cmp').setup {
    keymap = {
        -- Manually invoke minuet completion.
        ['<A-y>'] = require('minuet').make_blink_map(),
    },
    sources = {
         -- Enable minuet for autocomplete
        default = { 'lsp', 'path', 'buffer', 'snippets', 'minuet' },
        -- For manual completion only, remove 'minuet' from default
        providers = {
            minuet = {
                name = 'minuet',
                module = 'minuet.blink',
                score_offset = 8, -- Gives minuet higher priority among suggestions
            },
        },
    },
    -- Recommended to avoid unnecessary request
    completion = { trigger = { prefetch_on_insert = false } },
}
```

</details>

**LLM Provider Examples**:

**Deepseek**:

```lua
-- you can use deepseek with both openai_fim_compatible or openai_compatible provider
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


-- or
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
