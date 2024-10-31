# DeepSpace

DeepSpace（深度空间）是一款用于调试 DeepSeek API 的工具，由社区制作，灵感来源于 [MoonPalace](https://github.com/MoonshotAI/moonpalace?tab=readme-ov-file)。

[Read this in English](README.md)

## 特性

- **全平台支持：**
  - [x] Mac
  - [x] Windows
  - [x] Linux
- **简单易用**：启动后只需将 `base_url` 替换为 `http://localhost:9988` 即可开始调试。
- **捕获完整请求**，包括网络错误时的“事故现场”。
- **快速检索**：通过 `request_id`、`chatcmpl_id` 快速检索、查看请求信息。
- **一键导出 BadCase 结构化上报数据**，帮助 DeepSeek 完善模型能力。

**推荐在代码编写和调试阶段使用 DeepSpace 作为你的 API “供应商”，以便能快速发现和定位关于 API 调用和代码编写过程中的各种问题。对于 DeepSeek 大模型各种不符合预期的输出，你也可以通过 DeepSpace 导出请求详情并提交给 DeepSeek 以改进 DeepSeek 的大模型。**

## 安装方式

### 使用 `go` 命令安装

如果你已经安装了 `go` 工具链，可以执行以下命令来安装：

```shell
$ go install github.com/2404589803/deepspace@latest
```

上述命令会在你的 `$GOPATH/bin/` 目录中安装编译后的二进制文件。运行 `deepspace` 命令来检查是否成功安装：

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

*如果你仍然无法检索到 `deepspace` 二进制文件，请尝试将 `$GOPATH/bin/` 目录添加到你的 `$PATH` 环境变量中。*

### 从 Releases 页面下载二进制（可执行）文件

你也可以从 [Releases](https://github.com/2404589803/deepspace/releases) 页面下载编译好的二进制文件：

- deepspace-linux
- deepspace-macos-amd64 => 对应 Intel 版本的 Mac
- deepspace-macos-arm64 => 对应 Apple Silicon 版本的 Mac
- deepspace-windows.exe

## 使用方式

### 启动服务

使用以下命令启动 DeepSpace 代理服务器：

```shell
$ deepspace start --port <PORT>
```

DeepSpace 会在本地启动一个 HTTP 服务器，`--port` 参数指定 DeepSpace 监听的本地端口，默认值为 `9988`。当 DeepSpace 启动成功时，会输出：

```shell
[DeepSpace] 2024/08/26 12:12:26 DeepSpace Starts => change base_url to "http://127.0.0.1:9988/v1"
```

你可以将导出的文件投递至以下邮箱：

[api-service@deepseek.com](mailto:api-service@deepseek.com)