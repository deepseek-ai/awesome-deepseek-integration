
# APRO-COM/ATTPs-framework

Foundation framework that enables advanced agent based on DeepSeek interactions, data verification, and price queries with [ATTPs Protocol](https://docs.apro.com/attps) . It streamlines agent creation, verification processes, and provides a flexible framework for building robust agent-based solutions.

For more details about ATTPs, you can see the [whitepaper here](https://www.apro.com/attps.pdf)

## Overview

The ATTPs framework bridges agent-based logic with the DeepSeek. It handles agent registration, data verification, and price queries, empowering both automated and user-driven workflows.

## Features

### Agent Operations
- **Agent Creation**: Deploy new agents with custom settings
- **Registration**: Register agents on-chain or via standardized processes
- **Multi-Signer Framework**: Supports threshold-based approval flows

### Data Verification
- **Chain Validation**: Verify data authenticity on-chain
- **Transaction Execution**: Handle verification logic with built-in security checks
- **Auto-Hashing**: Convert raw data to hashed formats when needed
- **Metadata Parsing**: Validate content type, encoding, and compression

### Price Queries
- **Live Price Data**: Fetch price information for various pairs
- **Format Validation**: Normalize user query inputs to standard trading-pair formats
- **APIs Integration**: Retrieve real-time or near-real-time pricing information

## Security Features

### Access Control
- **Private Key Management**: Safe usage of private keys for transaction signing
- **Environment Variables**: Secure injection of credentials
- **On-Chain Validation**: Leverage on-chain contract checks

### Verification
- **Input Validation**: Strict schema checks before on-chain operations
- **Transaction Receipts**: Provide verifiable transaction details
- **Error Handling**: Detailed error logs for quick debugging

## Performance Optimization

1. **Cache Management**
   - Implement caching for frequent queries
   - Monitor retrieval times and cache hits

2. **Network Efficiency**
   - Batch requests where possible
   - Validate response parsing to reduce overhead

## System Requirements
- Node.js 16.x or higher
- Sufficient network access to on-chain endpoints
- Basic configuration of environment variables
- Minimum 4GB RAM recommended

## Troubleshooting

1. **Invalid Agent Settings**
   - Ensure signers and threshold are correct
   - Validate agentHeader for proper UUIDs and numeric values

2. **Verification Failures**
   - Check the input data formats
   - Confirm environment variables are set

3. **Price Query Errors**
   - Verify the trading pair format
   - Check external API availability

## Safety & Security

1. **Credential Management**
   - Store private keys securely
   - Do not commit secrets to version control

2. **Transaction Limits**
   - Configure thresholds to mitigate abuse
   - Log transaction attempts and failures

3. **Monitoring & Logging**
   - Track unusual activity
   - Maintain detailed audit logs


# Usage with js

## Installation

```bash
npm install ai-agent-sdk-js
```

## Configuration

Configure the plugin by setting environment variables or runtime settings:
- APRO_RPC_URL
- APRO_PROXY_ADDRESS
- APRO_PRIVATE_KEY
- APRO_CONVERTER_ADDRESS
- APRO_AUTO_HASH_DATA

## Usage with js sdk

To use the AI Agent SDK, import the library and create an instance of the `Agent` class:

```typescript
import { AgentSDK } from 'ai-agent-sdk-js'

const agent = new AgentSDK({
  rpcUrl: 'https://bsc-testnet-rpc.publicnode.com',
  privateKey: '',
  proxyAddress: '',
})

// if you want the SDK to hash the data automatically
const autoHashAgent = new AgentSDK({
  rpcUrl: 'https://bsc-testnet-rpc.publicnode.com',
  privateKey: '',
  proxyAddress: '',
  autoHashData: true,
  converterAddress: '',
})
```

To create a new agent, call the `createAndRegisterAgent` method:

```typescript
import type { AgentSettings, TransactionOptions } from 'ai-agent-sdk-js'
import { randomUUID } from 'node:crypto'
import { parseUnits } from 'ethers'

// prepare the agent settings
const agentSettings: AgentSettings = {
  signers: [],
  threshold: 3,
  converterAddress: '',
  agentHeader: {
    messageId: randomUUID(),
    sourceAgentId: randomUUID(),
    sourceAgentName: 'AI Agent SDK JS',
    targetAgentId: '',
    timestamp: Math.floor(Date.now() / 1000),
    messageType: 0,
    priority: 1,
    ttl: 3600,
  },
}

// prepare the transaction options
const nonce = await agent.getNextNonce()
const transactionOptions: TransactionOptions = {
  nonce,
  gasPrice: parseUnits('1', 'gwei'),
  gasLimit: BigInt(2000000),
}

const tx = await agent.createAndRegisterAgent({ agentSettings, transactionOptions })

// or you can leave the transaction options empty, the SDK will use the auto-generated values
// const tx = await agent.createAndRegisterAgent({ agentSettings })
```

The SDK also provides the tool to extract the new agent address from the transaction receipt:

```typescript
import { parseNewAgentAddress } from 'ai-agent-sdk-js'

const receipt = await tx.wait()
const agentAddress = parseNewAgentAddress(receipt)
```

To verify the data integrity, call the `verify` method:

```typescript
import type { MessagePayload } from 'ai-agent-sdk-js'
import { hexlify, keccak256, toUtf8Bytes } from 'ethers'

// prepare the payload
const data = hexlify(toUtf8Bytes('Hello World!'))
const dataHash = keccak256(data)
const payload: MessagePayload = {
  data,
  dataHash,
  signatures: [
    {
      r: '',
      s: '',
      v: 1, // 1, 0, 27, 28 are allowed
    },
    // ...
  ],
  metadata: {
    contentType: '',
    encoding: '',
    compression: '',
  },
}

const tx = await agent.verify({ payload, agent: '', digest: '' })
```

If the data is obtained from the APRO DATA pull service, you can use the auto-hash feature:

```typescript
import type { MessagePayload } from 'ai-agent-sdk-js'

const payload: MessagePayload = {
  data: '0x...',
  signatures: [
    {
      r: '',
      s: '',
      v: 1, // 1, 0, 27, 28 are allowed
    },
    // ...
  ],
  metadata: {
    contentType: '',
    encoding: '',
    compression: '',
  },
}

// When
const tx = await autoHashAgent.verify({ payload, agent: '', digest: '' })
```

For more examples, see the [test](https://github.com/APRO-com/ai-agent-sdk-js/tree/main/test) cases.



# Usage with Python

## Installation

```bash
$ pip3 install ai-agent-sdk

```

## Usage with Python SDK

### Initialize AgentSDK

```python
from ai_agent.agent import AgentSDK

AGENT_PROXY_ADDRESS = "0x07771A3026E60776deC8C1C61106FB9623521394"
NETWORK_RPC = "https://testnet-rpc.bitlayer.org"

agent = AgentSDK(endpoint_uri=NETWORK_RPC, proxy_address=AGENT_PROXY_ADDRESS)
```

To create a new agent, call the createAndRegisterAgent method:

```python
import time
from ai_agent.entities import (
    AgentSettings,
    AgentHeader,
    MessageType,
    Priority
)
from ai_agent.utils import (
    generate_uuid_v4
)

AGENT_SETTINGS = AgentSettings(
    signers=[
        "0x4b1056f504f32c678227b5Ae812936249c40AfBF",
        "0xB973476e0cF88a3693014b99f230CEB5A01ac686",
        "0x6cF0803D049a4e8DC01da726A5a212BCB9FAC1a1",
        "0x9D46daa26342e9E9e586A6AdCEDaD667f985567B",
        "0x33AF673aBcE193E20Ee94D6fBEb30fEf0cA7015b",
        "0x868D2dE4a0378450BC62A7596463b30Dc4e3897E",
        "0xD4E157c36E7299bB40800e4aE7909DDcA8097f67",
        "0xA3866A07ABEf3fD0643BD7e1c32600520F465ca8",
        "0x62f642Ae0Ed7F12Bc40F2a9Bf82ccD0a3F3b7531"
    ],
    threshold=2,
    converter_address="0xaB303EF87774D9D259d1098E9aA4dD6c07F69240",
    agent_header=AgentHeader(
        version="1.0",
        message_id="d4d0813f-ceb7-4ce1-8988-12899b26c4b6",
        source_agent_id="da70f6b3-e580-470f-b88b-caa5369e7778",
        source_agent_name="APRO Pull Mode Agent",
        target_agent_id="",
        timestamp=int(time.time()),
        message_type=MessageType.Event,
        priority=Priority.Low,
        ttl=60 * 60
    )
)

dynamic_setting = AGENT_SETTINGS
dynamic_setting.agent_header.source_agent_id = generate_uuid_v4()
dynamic_setting.agent_header.target_agent_id = generate_uuid_v4()
dynamic_setting.agent_header.message_id = generate_uuid_v4()
user_owner = agent.add_account("0x_user_private_key")
result = agent.create_and_register_agent(
    transmitter="",
    nonce=None,
    settings=AGENT_SETTINGS)
print("created agent:", result)

```
To verify the data integrity, call the verify method:

```python
from ai_agent.entities import (
    AgentMessagePayload,
    Proofs,
    AgentMetadata,
)

AGENT_CONTRACT = "0xA1903361Ee8Ec35acC7c8951b4008dbE8D12C155"
AGENT_SETTING_DIGEST = "0x010038164dba6abffb84eb5cb538850d9bc5d8f815149a371069b3255fd177a4"
AGENT_PAYLOAD = AgentMessagePayload(
    data="0x0006e706cf7ab41fa599311eb3de68be869198ce62aef1cd079475ca50e5b3f60000000000000000000000000000000000000000000000000000000002b1bf0e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000022000000000000000000000000000000000000000000000000000000000000002a0000101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001200003665949c883f9e0f6f002eac32e00bd59dfe6c34e92a91c37d6a8322d6489000000000000000000000000000000000000000000000000000000006762677d000000000000000000000000000000000000000000000000000000006762677d000000000000000000000000000000000000000000000000000003128629ec0800000000000000000000000000000000000000000000000004db732547630000000000000000000000000000000000000000000000000000000000006763b8fd0000000000000000000000000000000000000000000015f0f60671beb95cc0000000000000000000000000000000000000000000000015f083baa654a7b900000000000000000000000000000000000000000000000015f103ec7cb057ea80000000000000000000000000000000000000000000000000000000000000000003b64f7e72208147bb898e8b215d0997967bef0219263726c76995d8a19107d6ba5306a176474f9ccdb1bc5841f97e0592013e404e15b0de0839b81d0efb26179f222e0191269a8560ebd9096707d225bc606d61466b85d8568d7620a3b59a73e800000000000000000000000000000000000000000000000000000000000000037cae0f05c1bf8353eb5db27635f02b40a534d4192099de445764891198231c597a303cd15f302dafbb1263eb6e8e19cbacea985c66c6fed3231fd84a84ebe0276f69f481fe7808c339a04ceb905bb49980846c8ceb89a27b1c09713cb356f773",
    data_hash="0x53d9f133f1265bd4391fcdf89b63424cbcfd316c8448f76cc515647267ac0a8e",
    proofs=Proofs(
        zk_proof="0x",
        merkle_proof="0x",
        signature_proof="0x000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000001600000000000000000000000000000000000000000000000000000000000000003b64f7e72208147bb898e8b215d0997967bef0219263726c76995d8a19107d6ba5306a176474f9ccdb1bc5841f97e0592013e404e15b0de0839b81d0efb26179f222e0191269a8560ebd9096707d225bc606d61466b85d8568d7620a3b59a73e800000000000000000000000000000000000000000000000000000000000000037cae0f05c1bf8353eb5db27635f02b40a534d4192099de445764891198231c597a303cd15f302dafbb1263eb6e8e19cbacea985c66c6fed3231fd84a84ebe0276f69f481fe7808c339a04ceb905bb49980846c8ceb89a27b1c09713cb356f7730000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001",
    ),
    meta_data=AgentMetadata(
        content_type="0x",
        encoding="0x",
        compression="0x"
    )
)
user_owner = agent.add_account("0x_user_private_key")
result = agent.verify(
    transmitter=user_owner,
    nonce=None,
    agent_contract=AGENT_CONTRACT,
    settings_digest=AGENT_SETTING_DIGEST,
    payload=AGENT_PAYLOAD
)
print("verify:", result)
```
For more examples, see the [test cases](https://github.com/APRO-com/ai-agent-sdk-python/tree/main/tests).


# Other SDKs

JAVA: https://github.com/APRO-com/ai-agent-sdk-java

RUST: https://github.com/APRO-com/ai-agent-sdk-rust

GOLANG: https://github.com/APRO-com/ai-agent-sdk-go

# Support

For issues or feature requests:
1. Check existing documentation
2. Submit a GitHub issue with relevant details
3. Include transaction logs and system info if applicable

# Contributing

We welcome pull requests! Refer to the project’s CONTRIBUTING.md and open discussions to coordinate efforts.

# Credits

- [APRO](https://www.apro.com/) - Plugin sponsor and partner
- [ai-agent-sdk-js](https://github.com/APRO-com/ai-agent-sdk-js) - Underlying agent SDK
- [ethers.js](https://docs.ethers.io/) - Transaction and contract interaction
- Community contributors for feedback and testing

For more information about Apro plugin capabilities:

- [Apro Documentation](https://docs.apro.com/en)

# License

This plugin is part of the Eliza project. Refer to the main project repository for licensing details.