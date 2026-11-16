
# DeepSeek MCP Server

A Model Context Protocol (MCP) server for the DeepSeek API, allowing seamless integration of DeepSeek's powerful language models with MCP-compatible applications like Claude Desktop.

## *Anonymously*  use DeepSeek API  --  Only a proxy is seen on the other side 

<a href="https://glama.ai/mcp/servers/asht4rqltn"><img width="380" height="200" src="https://glama.ai/mcp/servers/asht4rqltn/badge" alt="DeepSeek Server MCP server" /></a>
<a href="https://smithery.ai/server/@dmontgomery40/deepseek-mcp-server"><img alt="Smithery Badge" src="https://smithery.ai/badge/@dmontgomery40/deepseek-mcp-server"></a>


[![npm version](https://img.shields.io/npm/v/deepseek-mcp-server)](https://www.npmjs.com/package/deepseek-mcp-server)
[![npm downloads](https://img.shields.io/npm/dm/deepseek-mcp-server)](https://www.npmjs.com/package/deepseek-mcp-server)
[![GitHub issues](https://img.shields.io/github/issues/DMontgomery40/deepseek-mcp-server)](https://github.com/DMontgomery40/deepseek-mcp-server/issues)
[![GitHub forks](https://img.shields.io/github/forks/DMontgomery40/deepseek-mcp-server)](https://github.com/DMontgomery40/deepseek-mcp-server/network)
[![GitHub stars](https://img.shields.io/github/stars/DMontgomery40/deepseek-mcp-server)](https://github.com/DMontgomery40/deepseek-mcp-server/stargazers)
[![GitHub license](https://img.shields.io/github/license/DMontgomery40/deepseek-mcp-server?color=blue)](https://github.com/DMontgomery40/deepseek-mcp-server/blob/main/LICENSE)

## Installation

### Installing via Smithery

To install DeepSeek MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@dmontgomery40/deepseek-mcp-server):

```bash
npx -y @smithery/cli install @dmontgomery40/deepseek-mcp-server --client claude
```

### Manual Installation
```bash
npm install -g deepseek-mcp-server
```
### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "deepseek": {
      "command": "npx",
      "args": [
        "-y",
        "deepseek-mcp-server"
      ],
      "env": {
        "DEEPSEEK_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Features

> Note: The server intelligently handles these natural language requests by mapping them to appropriate configuration changes. You can also query the current settings and available models:

- User: "What models are available?"
  - Response: Shows list of available models and their capabilities via the models resource.
- User: "What configuration options do I have?"
  - Response: Lists all available configuration options via the model-config resource.
- User: "What is the current temperature setting?"
  - Response: Displays the current temperature setting.
- User: "Start a multi-turn conversation. With the following settings: model: 'deepseek-chat', make it not too creative, and 
   allow 8000 tokens."
  - Response: *Starts a multi-turn conversation with the specified settings.*

### Automatic Model Fallback if R1 is down

- If the primary model (R1) is down (called `deepseek-reasoner` in the server), the server will automatically attempt to try with v3 (called `deepseek-chat` in the server) 
> Note: You can switch back and forth anytime as well, by just giving your prompt and saying "use `deepseek-reasoner`" or "use `deepseek-chat`"
- V3 is recommended for general purpose use, while R1 is recommended for more technical and complex queries, primarily due to speed and token useage

###  Resource discovery for available models and configurations:
   * Custom model selection
   * Temperature control (0.0 - 2.0)
   * Max tokens limit
   * Top P sampling (0.0 - 1.0)
   * Presence penalty (-2.0 - 2.0)
   * Frequency penalty (-2.0 - 2.0)

## Enhanced Conversation Features

**Multi-turn conversation support:**
* Maintains complete message history and context across exchanges
* Preserves configuration settings throughout the conversation
* Handles complex dialogue flows and follow-up chains automatically

This feature is particularly valuable for two key use cases:

1. **Training & Fine-tuning:**
   Since DeepSeek is open source, many users are training their own versions. The multi-turn support provides properly formatted conversation data that's essential for training high-quality dialogue models.

2. **Complex Interactions:**
   For production use, this helps manage longer conversations where context is crucial:
   * Multi-step reasoning problems
   * Interactive troubleshooting sessions
   * Detailed technical discussions
   * Any scenario where context from earlier messages impacts later responses

The implementation handles all context management and message formatting behind the scenes, letting you focus on the actual interaction rather than the technical details of maintaining conversation state.




## Testing with MCP Inspector

You can test the server locally using the MCP Inspector tool:

1. Build the server:
   ```bash
   npm run build
   ```

2. Run the server with MCP Inspector:
   ```bash
   # Make sure to specify the full path to the built server
   npx @modelcontextprotocol/inspector node ./build/index.js
   ```

The inspector will open in your browser and connect to the server via stdio transport. You can:
- View available tools
- Test chat completions with different parameters
- Debug server responses
- Monitor server performance

Note: The server uses DeepSeek's R1 model (deepseek-reasoner) by default, which provides state-of-the-art performance for reasoning and general tasks.

## License

MIT
