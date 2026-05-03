# Zero-API-Key Web Search

<p align="center">
  <strong>Search infrastructure for AI agents — free by default, MCP-ready, LLM-context aware, production-grade when you opt in.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/zero-api-key-web-search/"><img src="https://img.shields.io/pypi/v/zero-api-key-web-search?label=pypi" alt="PyPI"></a>
  <a href="https://github.com/wd041216-bit/zero-api-key-web-search"><img src="https://img.shields.io/badge/GitHub-repo-blue" alt="GitHub"></a>
  <img src="https://img.shields.io/badge/MCP-Ready-0f766e.svg" alt="MCP Ready">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
</p>

## Integration with DeepSeek

Zero-API-Key Web Search works with DeepSeek models through MCP (Model Context Protocol). Any agent framework that supports MCP can use it alongside DeepSeek for live web search, evidence verification, and citation-ready context.

### Quick Start

```bash
pip install zero-api-key-web-search
```

### MCP Server Configuration

Add to your MCP client configuration (Claude Code, Cursor, Copilot, etc.):

```json
{
  "mcpServers": {
    "zero-api-key-web-search": {
      "command": "zero-mcp"
    }
  }
}
```

### Use with DeepSeek via Function Calling

```python
from zero_api_key_web_search import UltimateSearcher

searcher = UltimateSearcher()

# Search the web
answer = searcher.search("DeepSeek V3 latest release", search_type="text", region="wt-wt")
print(answer.answer)
for source in answer.sources[:5]:
    print(f"  {source.title}: {source.url}")

# Verify a claim
verification = searcher.verify_claim("DeepSeek V3 is open source", include_pages=True)
print(f"Verdict: {verification.verdict} (confidence: {verification.confidence})")

# Build LLM context for DeepSeek to consume
context = searcher.llm_context("DeepSeek R1 reasoning capabilities", max_sources=5)
print(context.context_markdown)
```

### Provider Paths

| Profile | Providers | Best for |
| --- | --- | --- |
| `free` | DuckDuckGo | Zero-setup, no API key |
| `free-verified` | DuckDuckGo + SearXNG | Free cross-validation |
| `production` | Bright Data | Production reliability, 7 SERP engines, geo-targeting |
| `production-unlock` | Bright Data + Web Unlocker | Production SERP + access blocked pages |
| `max-evidence` | All providers | Maximum diversity |

### Key Features

- **Zero-key default**: Works immediately with DuckDuckGo, no API key required
- **MCP-native**: 8 tools including `search_web`, `browse_page`, `verify_claim`, `evidence_report`
- **Multi-engine SERP**: Google, Bing, DuckDuckGo, Yandex, Baidu, Yahoo, Naver (via Bright Data)
- **Web Unlocker**: Access blocked, CAPTCHA-protected, and geo-restricted pages
- **Claim verification**: Evidence-aware heuristic classification (supported/contested/likely false)
- **Citation-ready context**: LLM-optimized Markdown with source attribution
- **7+ agent platforms**: Claude Code, Cursor, Copilot, Codex, Gemini, Continue, Kiro, Manus

### CLI Commands

```bash
zero-search "DeepSeek R1 capabilities" --json
zero-context "DeepSeek V3 architecture" --goggles docs-first
zero-verify "DeepSeek R1 is open source" --deep --json
zero-report "DeepSeek latest models" --deep --json
zero-browse "https://api-docs.deepseek.com/" --json
zero-setup  # Interactive provider configuration
```

### Optional: Production Providers

```bash
# Bright Data for production-grade SERP (5000 free credits)
export ZERO_SEARCH_BRIGHTDATA_API_KEY="your-key"

# Search with specific engines
zero-search "news" --provider brightdata --engine bing --type news --region us-en --json

# Access blocked pages via Web Unlocker
export ZERO_SEARCH_BRIGHTDATA_UNLOCKER_ZONE="web_unlocker1"
zero-browse "https://protected-site.com" --use-unlocker auto --json
```

New Bright Data users: <https://get.brightdata.com/h21j9xz4uxgd>

## Links

- **GitHub**: https://github.com/wd041216-bit/zero-api-key-web-search
- **PyPI**: https://pypi.org/project/zero-api-key-web-search/
- **Documentation**: https://github.com/wd041216-bit/zero-api-key-web-search/tree/main/docs