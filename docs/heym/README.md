# Use DeepSeek in Heym

[Heym](https://github.com/heymrun/heym) is a self-hosted runtime for agent workflows. Its Custom credential connects OpenAI-compatible model endpoints to LLM and Agent nodes. Heym is source-available under [MIT with the Commons Clause condition](https://github.com/heymrun/heym/blob/main/COMMONS-CLAUSE.md).

## Start Heym

Install Bun, Python 3.11+, uv, and Docker, then follow the [quick start](https://github.com/heymrun/heym#-quick-start):

```bash
git clone https://github.com/heymrun/heym.git
cd heym
./run.sh
```

Open `http://localhost:4017` and create an account. The launcher starts PostgreSQL, the backend, and the frontend. Infrastructure and model-provider usage have separate costs.

## Add a DeepSeek credential

Get your API key from the [DeepSeek platform](https://platform.deepseek.com/). In Heym, open **Settings > Credentials**, add a **Custom** credential, and save:

| Field | Value |
|---|---|
| Name | `DeepSeek` |
| API key | Your DeepSeek API key |
| Base URL | `https://api.deepseek.com/v1` |

Enter the key in the credential form. Keep it out of workflow prompts, node outputs, and exported configuration.

## Make a text request

1. Create a workflow and add an **LLM** node.
2. Select the `DeepSeek` credential and model `deepseek-flash`.
3. Keep text output selected, batch mode off, and **Use Responses API** off.
4. Set the user message to `Say hello in one sentence.`
5. Enable **Send extra request body** and enter:

```json
{
  "thinking": {
    "type": "disabled"
  }
}
```

Run the workflow and inspect the node's `text` output and the Traces tab. Model names and availability can change; confirm them in the [DeepSeek API documentation](https://api-docs.deepseek.com/). This example uses non-thinking Chat Completions. See the [thinking-mode guide](https://api-docs.deepseek.com/guides/thinking_mode/) before adapting it to reasoning or tool-calling workflows.

## Validation and limits

The credential path, model field, extra body, and `/v1/chat/completions` request were checked through Heym's LLM service with mocked HTTP responses. An unauthenticated request to that route returned HTTP 401. Live authenticated model inference was not run for this contribution.

This walkthrough covers one text request. Test tool calls, structured output, reasoning history, and provider-specific APIs separately before extending it.

## References

- [Heym Custom credentials](https://github.com/heymrun/heym/blob/main/frontend/src/docs/content/reference/integrations.md#llm-providers-openai-google-custom-cohere)
- [Heym LLM node and extra request body](https://github.com/heymrun/heym/blob/main/frontend/src/docs/content/nodes/llm-node.md#extra-body)
- [Heym Agent architecture and approval checkpoints](https://github.com/heymrun/heym/blob/main/frontend/src/docs/content/reference/agent-architecture.md)
