# Mind Network FHE Rust SDK
`mind_sdk_deepseek` is a **Native Rust SDK** by [Mind Network](https://www.mindnetwork.xyz/) to enable FHE function for DeepSeek. DeepSeek will assist user as an AI Agent to think and predict, and then encrypted by FHE and submit to Mind Network for model consensus. 

[![mind_sdk_deepseek on crates.io](https://img.shields.io/crates/v/mind_sdk_deepseek)](https://crates.io/crates/mind_sdk_deepseek)
[![Documentation on docs.rs](https://img.shields.io/badge/docs-docs.rs-blue)](https://docs.rs/mind_sdk_deepseek)
[![Licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Github](https://img.shields.io/badge/source-github.com-blue.svg)](https://github.com/mind-network/mind-sdk-deepseek-rust)
[![Github](https://img.shields.io/badge/build-pass-green.svg)](https://github.com/mind-network/mind-sdk-deepseek-rust)


## Usage 
```rust
// call deepseek to predict, you can change to other prompt as you wish
let prompt = "Please predict BTC price in next 7 days, return must be a positive integer".to_string()
let client = deepseek_rs::DeepSeekClient::default().unwrap();
let request = deepseek_rs::client::chat_completions::request::RequestBody::new_messages(vec![
        deepseek_rs::client::chat_completions::request::Message::new_user_message(prompt)
    ]).with_model(deepseek_rs::client::chat_completions::request::Model::DeepSeekReasoner);
let response = client.chat_completions(request).await.unwrap();
//println!("Reasoning: {}", response.choices[0].message.reasoning_content.unwrap());
//println!("Answer: {}", response.choices[0].message.content.unwrap());

// convert deepseek prediction to int type
let deepseek_prediction = match response.choices[0].clone().message.content.unwrap().parse::<u128>() {
    Ok(prediction) => prediction,
    Err(_) => 0,
};
        
// fhe encrypt
let fhe: mind_sdk_fhe::FheInt = mind_sdk_fhe::FheInt::new_from_public_key_local(&fhe_public_key_fp);
let ciphertext = mind_sdk_fhe::fhe_client::encrypt(&fhe, "u8", deepseek_prediction.clone());
let ciphertext_str: String = mind_sdk_fhe::io::serialize_base64(ciphertext)?;

// submit ciphertext onchain
let result: alloy::rpc::types::TransactionReceipt = self.submit_fhe_encrypted(ciphertext_str).await?;
```

## Quick Start

## Source
```bash
git clone https://github.com/mind-network/mind-sdk-deepseek-rust.git
cd mind-sdk-deepseek-rust
```

### Install 
```toml
[dependencies]
mind_sdk_deepseek = "*
```

### build 
```bash
cargo build --debug
cargo build --release
```

### run
``` bash
cd msn
cargo build && ./target/debug/mind_sdk_deepseek --log-level=info check-hot-wallet-address

cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn.toml register 0x06eF5C5ba427434bf36469B877e4ea9044D1b735
cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn_1.toml register 0x2F8aCe76a34e50943573826A326a8Eb8DC854f84
cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn_2.toml register 0x3df4b66E1895E68aB000f1086e9393ca1937Cd8b

cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn.toml deepseek-fhe-vote 
cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn_1.toml deepseek-fhe-vote
cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn_2.toml deepseek-fhe-vote

cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn.toml check-registration
cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn_1.toml check-registration
cargo build && ./target/debug/mind_sdk_deepseek --log-level=debug --node-config-file=./config/config_fvn_2.toml check-registration
```



## CLI Help
``` bash
# ./bin/deepseek --help

FHE Randen Voter Node Cli

Usage: fvn [OPTIONS] <COMMAND>

Commands:
  deepseek-fhe-vote         let deepseek think and predict, and then encrypted by FHE and submit to Mind Network for model consensus
  check-hot-wallet-address  check hot wallet address, by default will use ./config/config_fvn.toml
  check-gas-balance         check hot wallet gas balance, need gas fee to vote
  check-registration        check if hot wallet has registered with a particular voter wallet
  register                  register voter address
  check-vote-rewards        check voting rewards
  check-vote                check voting tx history on the explore
  help                      Print this message or the help of the given subcommand(s)

Options:
      --node-config-file <NODE_CONFIG_FILE>
          fvn config file, contains all the config to run fvn [default: ./config/config_fvn.toml]
      --log-level <LOG_LEVEL>
          control level of print, useful for debug, default is info [default: info] [possible values: debug, info, warn, error]
      --hot-wallet-private-key <HOT_WALLET_PRIVATE_KEY>
          fvn wallet private key is needed if to load a different wallet from config_fvn.toml to sign the message onchain, by default load from ./config/config_fvn.toml
  -h, --help
          Print help
  -V, --version
          Print version
```

## CLI Example
``` bash
## command
./bin/deepseek --log-level=info deepseek-fhe-vote 
{
  "app": "deepseek",
  "command": "deepseek-fhe-vote",
  "arg": "deekseek predicted BTC price: 95833, hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "status": true,
  "result": "0x42d78185e4779dd3105598ac4f2786998c5059f8381a55daec12e4ffcc952a56",
  "note": "deekseek predicted BTC price: 95833, gas_sued: 304749, block_number: 26373, tx_hash: 0x42d78185e4779dd3105598ac4f2786998c5059f8381a55daec12e4ffcc952a56"
}

## command
./bin/deepseek --log-level=info check-hot-wallet-address
{
  "app": "deepseek",
  "command": "check-hot-wallet-address",
  "arg": "",
  "status": true,
  "result": "0x64FF17078669A507D0c831D9E844AF1C967604Dd",
  "note": ""
}

## command
./bin/deepseek --log-level=info check-gas-balance
{
  "app": "deepseek",
  "command": "check-gas-balance",
  "arg": "hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "status": true,
  "result": "197015375000000",
  "note": ""
}

## command
./bin/deepseek --log-level=info check-registration
{
  "app": "deepseek",
  "command": "check-registration",
  "arg": "0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "status": false,
  "result": "",
  "note": "hot wallet is not registered with any voter wallet"
}

## command
./bin/deepseek --log-level=info check-vote-rewards
{
  "app": "deepseek",
  "command": "check-vote-rewards",
  "arg": "hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "status": false,
  "result": "0",
  "note": "hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd, voter_wallet: , vote_rewards: 0"
}

## command
./bin/deepseek --log-level=info register 0x06eF5C5ba427434bf36469B877e4ea9044D1b735
{
  "app": "deepseek",
  "command": "register",
  "arg": "hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd, voter_wallet: 0x06eF5C5ba427434bf36469B877e4ea9044D1b735",
  "status": true,
  "result": "registration successful !",
  "note": "is_registered: true, hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd, voter_wallet: 0x06eF5C5ba427434bf36469B877e4ea9044D1b735"
}


## command
./bin/deepseek --log-level=info check-vote-rewards
{
  "app": "deepseek",
  "command": "check-vote-rewards",
  "arg": "hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "status": true,
  "result": "206095238095238095",
  "note": "hot_wallet: 0x6224F72f1439E76803e063262a7e1c03e86c6Dbd, voter_wallet: 0x06eF5C5ba427434bf36469B877e4ea9044D1b735, vote_rewards: 206095238095238095"
}

## command
./bin/deepseek --log-level=info check-vote
{
  "app": "deepseek",
  "command": "check-vote",
  "arg": "0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "status": true,
  "result": "check on the explore: testnet: https://explorer-testnet.mindnetwork.xyz/address/0x6224F72f1439E76803e063262a7e1c03e86c6Dbd, mainnet: https://explorer.mindnetwork.xyz/address/0x6224F72f1439E76803e063262a7e1c03e86c6Dbd",
  "note": ""
}

```

## **License**

This project is licensed under the **MIT License**.

## **Contact**

For questions or support, please contact [Mind Network Official Channels](https://mindnetwork.xyz/).


