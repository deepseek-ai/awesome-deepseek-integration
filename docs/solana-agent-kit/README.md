# README

<img src="assets/sendai-logo.png" width="64" height="auto" alt="logo">

---

An open-source toolkit for connecting AI agents to Solana protocols. Now, any agent, using any model can autonomously perform 60+ Solana actions:
‍

## STEP1.

Apply a token from [deepseek open platform](https://platform.deepseek.com/)

## STEP 2

Intialize the DeepSeek LLM

```
import { ChatDeepSeek } from "@langchain/deepseek";

const deepseek = new ChatDeepSeek({
  model: "deepseek-chat",
  temperature: 0,
});
```
‍
## STEP 3

Intialize the Solana Agent Kit with DeepSeek

```typescript
const solanaAgent = new SolanaAgentKit(
  process.env.SOLANA_PRIVATE_KEY!,
  process.env.RPC_URL!,
  {
    OPENAI_API_KEY: process.env.OPENAI_API_KEY!,
    HELIUS_API_KEY: process.env.HELIUS_API_KEY!,
    PERPLEXITY_API_KEY: process.env.PERPLEXITY_API_KEY!,
  },
);

const tools = createSolanaTools(solanaAgent);

const agent = createReactAgent({
  llm: deepseek,
  tools,
  checkpointSaver: memory,
  messageModifier: `
    You are a helpful agent that can interact onchain using the Solana Agent Kit. You are
    empowered to interact onchain using your tools. If you ever need funds, you can request them from the
    faucet. If not, you can provide your wallet details and request funds from the user. If there is a 5XX
    (internal) HTTP error code, ask the user to try again later. If someone asks you to do something you
    can't do with your currently available tools, you must say so, and encourage them to implement it
    themselves using the Solana Agent Kit, recommend they go to https://www.solanaagentkit.xyz for more information. Be
    concise and helpful with your responses. Refrain from restating your tools' descriptions unless it is explicitly requested.
  `,
});

const stream = await agent.stream(
  { messages: [new HumanMessage(userInput)] },
  config,
);
```

More guides can be found in the [Solana Agent Kit](https://docs.solanaagentkit.xyz/v0/introduction)

‍