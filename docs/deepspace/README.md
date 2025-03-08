# DeepSpace

DeepSpace is a tool for debugging the DeepSeek API, developed by the community and inspired by [MoonPalace](https://github.com/MoonshotAI/moonpalace?tab=readme-ov-file).

[简体中文](README_cn.md)

## Features

- **Cross-platform Support:**
  - [x] Mac
  - [x] Windows
  - [x] Linux
- **User-friendly**: Simply replace `base_url` with `http://localhost:9988` after starting the service to begin debugging.
- **Complete Request Capture**, including error details in case of network failures.
- **Fast Retrieval**: Quickly search and view request information using `request_id` or `chatcmpl_id`.
- **One-click Export of Structured BadCase Reports**, aiding DeepSeek in enhancing model capabilities.

**It is recommended to use DeepSpace as your API “provider” during code development and debugging stages. This allows you to quickly identify and resolve issues related to API calls and code implementation. For any unexpected outputs from the DeepSeek large model, you can also export request details via DeepSpace and submit them to DeepSeek to help improve the model.**

## Installation

### Install using the `go` command

If you have the `go` toolchain installed, you can install DeepSpace by executing the following command:

```shell
$ go install github.com/2404589803/deepspace@latest
```

This command will install the compiled binary in your `$GOPATH/bin/` directory. To verify the installation, run the following command:

```shell
$ deepspace
DeepSpace is a command-line tool for debugging the DeepSeek AI HTTP API

Usage:
  deepspace [command]

Available Commands:
  cleanup     Cleanup DeepSeek AI requests
  completion  Generate the autocompletion script for the specified shell
  export      Export a DeepSeek AI request
  help        Help about any command
  inspect     Inspect the specific content of a DeepSeek AI request
  list        Query DeepSeek AI requests based on conditions
  start       Start the DeepSpace proxy server

Flags:
  -h, --help      help for deepspace
  -v, --version   version for deepspace

Use "deepspace [command] --help" for more information about a command.
```

*If the `deepspace` binary is not found, try adding the `$GOPATH/bin/` directory to your `$PATH` environment variable.*

### Download Executable from the Releases Page

Alternatively, you can download the precompiled binary from the [Releases](https://github.com/2404589803/deepspace/releases) page:

- deepspace-linux
- deepspace-macos-amd64 => for Intel-based Macs
- deepspace-macos-arm64 => for Apple Silicon-based Macs
- deepspace-windows.exe

## Usage

### Starting the Service

Use the following command to start the DeepSpace proxy server:

```shell
$ deepspace start --port <PORT>
```

DeepSpace will start a local HTTP server. The `--port` parameter specifies the local port that DeepSpace listens to, with a default value of `9988`. Upon successful startup, the following message will be displayed:

```shell
[DeepSpace] 2024/08/26 12:12:26 DeepSpace Starts => change base_url to "http://127.0.0.1:9988/v1"
```

You can submit the exported files to the following email:

[api-service@deepseek.com](mailto:api-service@deepseek.com)
