# Agent Gateway — LLM Router with DeepSeek Support

[Agent Gateway](https://agent-gateway-kappa.vercel.app) is a free, unified API gateway that routes LLM requests to multiple providers including **DeepSeek**, OpenAI, Anthropic, Google Gemini, Groq, and Together AI through a single OpenAI-compatible endpoint.

## DeepSeek Integration

Agent Gateway supports DeepSeek models via the `/v1/chat/completions` endpoint:

```bash
curl -X POST "https://agent-gateway-kappa.vercel.app/v1/agent-llm/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "Explain quantum computing in 3 sentences"}]
  }'
```

## Features

- **OpenAI-compatible endpoint** — drop-in replacement, works with any OpenAI SDK
- **6 providers** — DeepSeek, OpenAI, Anthropic, Google Gemini, Groq, Together AI
- **24+ models** — including DeepSeek Chat and DeepSeek Coder
- **Response caching** — 5-minute TTL, reduces redundant API calls
- **Auto retries** — automatic failover on provider errors
- **No signup required** — free tier with 30 requests/minute

## Links

- [API Documentation](https://agent-gateway-kappa.vercel.app/docs)
- [LLM Gateway Tutorial](https://api-catalog-three.vercel.app/blog/free-llm-api)
- [All 39+ APIs](https://api-catalog-three.vercel.app/blog/best-free-apis-for-developers)
