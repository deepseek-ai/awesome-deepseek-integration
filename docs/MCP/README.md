<p align="center">
  <img src="https://raw.githubusercontent.com/arikusi/deepseek-mcp-server/main/icon.png" alt="DeepSeek MCP Server" width="120" />
</p>

<h1 align="center">DeepSeek MCP Server</h1>

<p align="center">
  MCP server for DeepSeek AI with chat, reasoning, multi-turn sessions, function calling, thinking mode, and cost tracking.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@arikusi/deepseek-mcp-server"><img src="https://img.shields.io/npm/v/@arikusi/deepseek-mcp-server.svg" alt="npm version" /></a>
  <a href="https://www.npmjs.com/package/@arikusi/deepseek-mcp-server"><img src="https://img.shields.io/npm/dm/@arikusi/deepseek-mcp-server.svg" alt="npm downloads" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/node/v/@arikusi/deepseek-mcp-server.svg" alt="Node.js Version" /></a>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-5.7-blue.svg" alt="TypeScript" /></a>
  <a href="https://github.com/arikusi/deepseek-mcp-server/actions"><img src="https://github.com/arikusi/deepseek-mcp-server/workflows/CI/badge.svg" alt="Build Status" /></a>
</p>

<p align="center">
  Compatible with Claude Code, Gemini CLI, Cursor, Windsurf, and any MCP-compatible client.<br />
  Officially listed on the <a href="https://registry.modelcontextprotocol.io/?q=io.github.arikusi"><strong>MCP Registry</strong></a>, <a href="https://smithery.ai/servers/arikusi/deepseek-mcp-server">Smithery</a>, <a href="https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server">Glama</a>, and <a href="https://lobehub.com/mcp/arikusi-deepseek-mcp-server">LobeHub</a>.
</p>

<p align="center">
  <a href="https://registry.modelcontextprotocol.io/?q=io.github.arikusi"><img src="https://img.shields.io/badge/Official_MCP_Registry-active-brightgreen" alt="Official MCP Registry" /></a>
  <a href="https://smithery.ai/servers/arikusi/deepseek-mcp-server"><img src="https://smithery.ai/badge/@arikusi/deepseek-mcp-server" alt="Smithery" /></a>
  <a href="https://lobehub.com/mcp/arikusi-deepseek-mcp-server"><img src="https://lobehub.com/badge/mcp/arikusi-deepseek-mcp-server" alt="LobeHub" /></a>
</p>

<p align="center">
  <a href="https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server">
    <img width="380" height="200" src="https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server/badge" alt="Glama Badge" />
  </a>
</p>

## Quick Start

### Remote (No Install)

Use the hosted endpoint directly — no npm install, no Node.js required. Bring your own DeepSeek API key:

**Claude Code:**
```bash
claude mcp add --transport http deepseek \
  https://deepseek-mcp.tahirl.com/mcp \
  --header "Authorization: Bearer YOUR_DEEPSEEK_API_KEY"
```

**Cursor / Windsurf / VS Code:**
```json
{
  "mcpServers": {
    "deepseek": {
      "url": "https://deepseek-mcp.tahirl.com/mcp",
      "headers": {
        "Authorization": "Bearer ${DEEPSEEK_API_KEY}"
      }
    }
  }
}
```

### Local (stdio)

**Claude Code:**
```bash
claude mcp add -s user deepseek npx @arikusi/deepseek-mcp-server -e DEEPSEEK_API_KEY=your-key-here
```

**Gemini CLI:**
```bash
gemini mcp add deepseek npx @arikusi/deepseek-mcp-server -e DEEPSEEK_API_KEY=your-key-here
```

**Scope options** (Claude Code):
- `-s user`: Available in all your projects (recommended)
- `-s local`: Only in current project (default)
- `-s project`: Project-specific `.mcp.json` file

**Get your API key:** [https://platform.deepseek.com](https://platform.deepseek.com)

---

## Features

- **DeepSeek V3.2**: Both models now run DeepSeek-V3.2 (since Sept 2025)
- **Multi-Turn Sessions**: Conversation context preserved across requests via `session_id` parameter
- **Model Fallback & Circuit Breaker**: Automatic fallback between models with circuit breaker protection against cascading failures
- **MCP Resources**: `deepseek://models`, `deepseek://config`, `deepseek://usage` — query model info, config, and usage stats
- **Thinking Mode**: Enable thinking on deepseek-chat with `thinking: {type: "enabled"}`
- **JSON Output Mode**: Structured JSON responses with `json_mode: true`
- **Function Calling**: OpenAI-compatible tool use with up to 128 tool definitions
- **Cache-Aware Cost Tracking**: Automatic cost calculation with cache hit/miss breakdown
- **Session Management Tool**: List, delete, and clear sessions via `deepseek_sessions` tool
- **Configurable**: Environment-based configuration with validation
- **12 Prompt Templates**: Templates for debugging, code review, function calling, and more
- **Streaming Support**: Real-time response generation
- **Multimodal Ready**: Content part types for text + image input (enable with `ENABLE_MULTIMODAL=true`)
- **Remote Endpoint**: Hosted at `deepseek-mcp.tahirl.com/mcp` — BYOK (Bring Your Own Key), no install needed
- **HTTP Transport**: Self-hosted remote access via Streamable HTTP with `TRANSPORT=http`
- **Docker Ready**: Multi-stage Dockerfile with health checks for containerized deployment
- **Tested**: 253 tests with 90%+ code coverage
- **Type-Safe**: Full TypeScript implementation
- **MCP Compatible**: Works with any MCP-compatible CLI (Claude Code, Gemini CLI, etc.)

## Installation

### Prerequisites

- Node.js 18+
- A DeepSeek API key (get one at [https://platform.deepseek.com](https://platform.deepseek.com))

### Manual Installation

If you prefer to install manually:

```bash
npm install -g @arikusi/deepseek-mcp-server
```

### From Source

1. **Clone the repository**

```bash
git clone https://github.com/arikusi/deepseek-mcp-server.git
cd deepseek-mcp-server
```

2. **Install dependencies**

```bash
npm install
```

3. **Build the project**

```bash
npm run build
```

## Usage

Once configured, your MCP client will have access to `deepseek_chat` and `deepseek_sessions` tools, plus 3 MCP resources.

**Example prompts:**
```
"Use DeepSeek to explain quantum computing"
"Ask DeepSeek Reasoner to solve: If I have 10 apples and buy 5 more..."
```

Your MCP client will automatically call the `deepseek_chat` tool.

### Manual Configuration (Advanced)

If your MCP client doesn't support the `add` command, manually add to your config file:

```json
{
  "mcpServers": {
    "deepseek": {
      "command": "npx",
      "args": ["@arikusi/deepseek-mcp-server"],
      "env": {
        "DEEPSEEK_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Config file locations:**
- **Claude Code**: `~/.claude.json` (add to `projects["your-project-path"].mcpServers` section)
- **Other MCP clients**: Check your client's documentation for config file location

## Available Tools

### `deepseek_chat`

Chat with DeepSeek AI models with automatic cost tracking and function calling support.

**Parameters:**

- `messages` (required): Array of conversation messages
  - `role`: "system" | "user" | "assistant" | "tool"
  - `content`: Message text
  - `tool_call_id` (optional): Required for tool role messages
- `model` (optional): "deepseek-chat" (default) or "deepseek-reasoner"
- `temperature` (optional): 0-2, controls randomness (default: 1.0). Ignored when thinking mode is enabled.
- `max_tokens` (optional): Maximum tokens to generate (deepseek-chat: max 8192, deepseek-reasoner: max 65536)
- `stream` (optional): Enable streaming mode (default: false)
- `tools` (optional): Array of tool definitions for function calling (max 128)
- `tool_choice` (optional): "auto" | "none" | "required" | `{type: "function", function: {name: "..."}}`
- `thinking` (optional): Enable thinking mode `{type: "enabled"}`
- `json_mode` (optional): Enable JSON output mode (supported by both models)
- `session_id` (optional): Session ID for multi-turn conversations. Previous context is automatically prepended.

**Response includes:**
- Content with formatting
- Function call results (if tools were used)
- Request information (tokens, model, cost in USD)
- Structured data with `cost_usd` and `tool_calls` fields

**Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Explain the theory of relativity in simple terms"
    }
  ],
  "model": "deepseek-chat",
  "temperature": 0.7,
  "max_tokens": 1000
}
```

**DeepSeek Reasoner Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "If I have 10 apples and eat 3, then buy 5 more, how many do I have?"
    }
  ],
  "model": "deepseek-reasoner"
}
```

The reasoner model will show its thinking process in `<thinking>` tags followed by the final answer.

**Function Calling Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "What's the weather in Istanbul?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name"
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}
```

When the model decides to call a function, the response includes `tool_calls` with the function name and arguments. You can then send the result back using a `tool` role message with the matching `tool_call_id`.

**Thinking Mode Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Analyze the time complexity of quicksort"
    }
  ],
  "model": "deepseek-chat",
  "thinking": { "type": "enabled" }
}
```

When thinking mode is enabled, `temperature`, `top_p`, `frequency_penalty`, and `presence_penalty` are automatically ignored.

**JSON Output Mode Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Return a json object with name, age, and city fields for a sample user"
    }
  ],
  "model": "deepseek-chat",
  "json_mode": true
}
```

JSON mode ensures the model outputs valid JSON. Include the word "json" in your prompt for best results. Supported by both `deepseek-chat` and `deepseek-reasoner`.

**Multi-Turn Session Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ],
  "session_id": "my-session-1"
}
```

Use the same `session_id` across requests to maintain conversation context. The server stores messages in memory and automatically prepends history to each request.

### `deepseek_sessions`

Manage conversation sessions.

**Parameters:**
- `action` (required): "list" | "clear" | "delete"
- `session_id` (optional): Required when action is "delete"

**Examples:**
```json
{"action": "list"}
{"action": "delete", "session_id": "my-session-1"}
{"action": "clear"}
```

## Available Resources

MCP Resources provide read-only data about the server:

| Resource URI | Description |
|-------------|-------------|
| `deepseek://models` | Available models with capabilities, context limits, and pricing |
| `deepseek://config` | Current server configuration (API key masked) |
| `deepseek://usage` | Real-time usage statistics (requests, tokens, costs, sessions) |

## Model Fallback & Circuit Breaker

When a model fails with a retryable error (429, 503, timeout), the server automatically falls back to the other model:
- `deepseek-chat` fails → tries `deepseek-reasoner`
- `deepseek-reasoner` fails → tries `deepseek-chat`

The circuit breaker protects against cascading failures:
- After `CIRCUIT_BREAKER_THRESHOLD` consecutive failures (default: 5), the circuit **opens** (fast-fail mode)
- After `CIRCUIT_BREAKER_RESET_TIMEOUT` ms (default: 30000), it enters **half-open** state and sends a probe request
- If the probe succeeds, the circuit **closes** and normal operation resumes

Fallback can be disabled with `FALLBACK_ENABLED=false`.

## Available Prompts

Prompt templates (12 total):

### Core Reasoning
- **debug_with_reasoning**: Debug code with step-by-step analysis
- **code_review_deep**: Comprehensive code review (security, performance, quality)
- **research_synthesis**: Research topics and create structured reports
- **strategic_planning**: Create strategic plans with reasoning
- **explain_like_im_five**: Explain complex topics in simple terms

### Advanced
- **mathematical_proof**: Prove mathematical statements rigorously
- **argument_validation**: Analyze arguments for logical fallacies
- **creative_ideation**: Generate creative ideas with feasibility analysis
- **cost_comparison**: Compare LLM costs for tasks
- **pair_programming**: Interactive coding with explanations

### Function Calling
- **function_call_debug**: Debug function calling issues with tool definitions and messages
- **create_function_schema**: Generate JSON Schema for function calling from natural language

Each prompt is optimized for the DeepSeek Reasoner model to provide detailed reasoning.

## Models

Both models run **DeepSeek-V3.2** with unified pricing.

### deepseek-chat

- **Best for**: General conversations, coding, content generation
- **Speed**: Fast
- **Context**: 128K tokens
- **Max Output**: 8K tokens (default 4K)
- **Mode**: Non-thinking (can enable thinking via parameter)
- **Features**: Thinking mode, JSON mode, function calling, FIM completion
- **Pricing**: $0.028/1M cache hit, $0.28/1M cache miss, $0.42/1M output

### deepseek-reasoner

- **Best for**: Complex reasoning, math, logic problems, multi-step tasks
- **Speed**: Slower (shows thinking process)
- **Context**: 128K tokens
- **Max Output**: 64K tokens (default 32K)
- **Mode**: Thinking (always active, chain-of-thought reasoning)
- **Features**: JSON mode, function calling
- **Output**: Both reasoning process and final answer
- **Pricing**: $0.028/1M cache hit, $0.28/1M cache miss, $0.42/1M output

## Configuration

The server is configured via environment variables. All settings except `DEEPSEEK_API_KEY` are optional.

| Variable | Default | Description |
|----------|---------|-------------|
| `DEEPSEEK_API_KEY` | (required) | Your DeepSeek API key |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | Custom API endpoint |
| `DEFAULT_MODEL` | `deepseek-chat` | Default model for requests |
| `SHOW_COST_INFO` | `true` | Show cost info in responses |
| `REQUEST_TIMEOUT` | `60000` | Request timeout in milliseconds |
| `MAX_RETRIES` | `2` | Maximum retry count for failed requests |
| `SKIP_CONNECTION_TEST` | `false` | Skip startup API connection test |
| `MAX_MESSAGE_LENGTH` | `100000` | Maximum message content length (characters) |
| `SESSION_TTL_MINUTES` | `30` | Session time-to-live in minutes |
| `MAX_SESSIONS` | `100` | Maximum number of concurrent sessions |
| `FALLBACK_ENABLED` | `true` | Enable automatic model fallback on errors |
| `CIRCUIT_BREAKER_THRESHOLD` | `5` | Consecutive failures before circuit opens |
| `CIRCUIT_BREAKER_RESET_TIMEOUT` | `30000` | Milliseconds before circuit half-opens |
| `MAX_SESSION_MESSAGES` | `200` | Max messages per session (sliding window) |
| `ENABLE_MULTIMODAL` | `false` | Enable multimodal (image) input support |
| `TRANSPORT` | `stdio` | Transport mode: `stdio` or `http` |
| `HTTP_PORT` | `3000` | HTTP server port (when TRANSPORT=http) |

**Example with custom config:**
```bash
claude mcp add -s user deepseek npx @arikusi/deepseek-mcp-server \
  -e DEEPSEEK_API_KEY=your-key \
  -e SHOW_COST_INFO=false \
  -e REQUEST_TIMEOUT=30000
```

## Development

### Project Structure

```
deepseek-mcp-server/
├── worker/                  # Cloudflare Worker (remote BYOK endpoint)
│   ├── src/index.ts         # Worker entry point
│   ├── wrangler.toml        # Cloudflare config
│   └── package.json
├── src/
│   ├── index.ts              # Entry point, bootstrap
│   ├── server.ts             # McpServer factory (auto-version)
│   ├── deepseek-client.ts    # DeepSeek API wrapper (circuit breaker + fallback)
│   ├── config.ts             # Centralized config with Zod validation
│   ├── cost.ts               # Cost calculation and formatting
│   ├── schemas.ts            # Zod input validation schemas
│   ├── types.ts              # TypeScript types + type guards
│   ├── errors.ts             # Custom error classes
│   ├── session.ts            # In-memory session store (multi-turn)
│   ├── circuit-breaker.ts    # Circuit breaker pattern
│   ├── usage-tracker.ts      # Usage statistics tracker
│   ├── transport-http.ts     # Streamable HTTP transport (Express)
│   ├── tools/
│   │   ├── deepseek-chat.ts  # deepseek_chat tool (sessions + fallback)
│   │   ├── deepseek-sessions.ts # deepseek_sessions tool
│   │   └── index.ts          # Tool registration aggregator
│   ├── resources/
│   │   ├── models.ts         # deepseek://models resource
│   │   ├── config.ts         # deepseek://config resource
│   │   ├── usage.ts          # deepseek://usage resource
│   │   └── index.ts          # Resource registration aggregator
│   └── prompts/
│       ├── core.ts           # 5 core reasoning prompts
│       ├── advanced.ts       # 5 advanced prompts
│       ├── function-calling.ts # 2 function calling prompts
│       └── index.ts          # Prompt registration aggregator
├── dist/                     # Compiled JavaScript
├── llms.txt                  # AI discoverability index
├── llms-full.txt             # Full docs for LLM context
├── vitest.config.ts          # Test configuration
├── package.json
├── tsconfig.json
└── README.md
```

### Building

```bash
npm run build
```

### Watch Mode (for development)

```bash
npm run watch
```

### Testing

```bash
# Run all tests
npm test

# Watch mode
npm run test:watch

# With coverage report
npm run test:coverage
```

### Testing Locally

```bash
# Set API key
export DEEPSEEK_API_KEY="your-key"

# Run the server
npm start
```

The server will start and wait for MCP client connections via stdio.

### Remote Endpoint (Hosted)

A hosted BYOK (Bring Your Own Key) endpoint is available at:

```
https://deepseek-mcp.tahirl.com/mcp
```

Send your DeepSeek API key as `Authorization: Bearer <key>`. No server-side API key stored — your key is used directly per request. Powered by Cloudflare Workers (global edge, zero cold start).

> **Note:** The `deepseek-reasoner` model may take over 30 seconds for complex queries. Some MCP clients (e.g. Claude Code) have built-in tool call timeouts that may interrupt long-running requests. For complex tasks, `deepseek-chat` is recommended.

```bash
# Test health
curl https://deepseek-mcp.tahirl.com/health

# Test MCP (requires auth)
curl -X POST https://deepseek-mcp.tahirl.com/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"capabilities":{}},"id":1}'
```

### HTTP Transport (Self-Hosted)

Run your own HTTP endpoint:

```bash
TRANSPORT=http HTTP_PORT=3000 DEEPSEEK_API_KEY=your-key node dist/index.js
```

Test the health endpoint:
```bash
curl http://localhost:3000/health
```

The MCP endpoint is available at `POST /mcp` (Streamable HTTP protocol).

### Docker

```bash
# Build
docker build -t deepseek-mcp-server .

# Run
docker run -d -p 3000:3000 -e DEEPSEEK_API_KEY=your-key deepseek-mcp-server

# Or use docker-compose
DEEPSEEK_API_KEY=your-key docker compose up -d
```

The Docker image defaults to HTTP transport on port 3000 with a built-in health check.

## Troubleshooting

### "DEEPSEEK_API_KEY environment variable is not set"

**Option 1: Use the correct installation command**
```bash
# Make sure to include -e flag with your API key
claude mcp add deepseek npx @arikusi/deepseek-mcp-server -e DEEPSEEK_API_KEY=your-key-here
```

**Option 2: Manually edit the config file**

If you already installed without the API key, edit your config file:

1. **For Claude Code**: Open `~/.claude.json` (Windows: `C:\Users\USERNAME\.claude.json`)
2. Find the `"mcpServers"` section under your project path
3. Add the `env` field with your API key:
```json
"deepseek": {
  "type": "stdio",
  "command": "npx",
  "args": ["@arikusi/deepseek-mcp-server"],
  "env": {
    "DEEPSEEK_API_KEY": "your-api-key-here"
  }
}
```
4. Save and restart Claude Code

### "Failed to connect to DeepSeek API"

1. Check your API key is valid
2. Verify you have internet connection
3. Check DeepSeek API status at [https://status.deepseek.com](https://status.deepseek.com)

### Server not appearing in your MCP client

1. Verify the path to `dist/index.js` is correct
2. Make sure you ran `npm run build`
3. Check your MCP client's logs for errors
4. Restart your MCP client completely

### Permission Denied on macOS/Linux

Make the file executable:

```bash
chmod +x dist/index.js
```

## Publishing to npm

To share this MCP server with others:

1. Run `npm login`
2. Run `npm publish --access public`

Users can then install with:

```bash
npm install -g @arikusi/deepseek-mcp-server
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting PRs.

### Reporting Issues

Found a bug or have a feature request? Please [open an issue](https://github.com/arikusi/deepseek-mcp-server/issues/new/choose) using our templates.

### Development

```bash
# Clone the repo
git clone https://github.com/arikusi/deepseek-mcp-server.git
cd deepseek-mcp-server

# Install dependencies
npm install

# Build in watch mode
npm run watch

# Run tests
npm test

# Lint
npm run lint
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

MIT License - see [LICENSE](LICENSE) file for details

## Support

- [Documentation](https://github.com/arikusi/deepseek-mcp-server#readme)
- [Bug Reports](https://github.com/arikusi/deepseek-mcp-server/issues)
- [Discussions](https://github.com/arikusi/deepseek-mcp-server/discussions)
- Contact: [GitHub Issues](https://github.com/arikusi/deepseek-mcp-server/issues)

## Resources

- [DeepSeek Platform](https://platform.deepseek.com) - Get your API key
- [Model Context Protocol](https://modelcontextprotocol.io) - MCP specification
- [DeepSeek API Documentation](https://api-docs.deepseek.com) - API reference

## Acknowledgments

- Built with [Model Context Protocol SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- Uses [OpenAI SDK](https://github.com/openai/openai-node) for API compatibility
- Created for the MCP community

---

**Made by [@arikusi](https://github.com/arikusi)**

