# CodeGate: secure AI code generation

CodeGate is a **local gateway** that makes AI agents and coding assistants safer. It
ensures AI-generated recommendations adhere to best practices while safeguarding
your code's integrity and protecting your privacy. With CodeGate, you can
confidently leverage AI in your development workflow without sacrificing
security or productivity.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/stacklok/codegate/main/static/diagram-dark.png">
  <img alt="CodeGate dashboard" src="https://github.com/stacklok/codegate/raw/main/static/diagram-light.png" width="1100px" style="max-width: 100%;">
</picture>

---
## ✨ Why choose CodeGate?

AI coding assistants are powerful, but they can inadvertently introduce risks.
CodeGate protects your development process by:

- 🔒 Preventing accidental exposure of secrets and sensitive data
- 🛡️ Ensuring AI suggestions follow secure coding practices
- ⚠️ Blocking recommendations of known malicious or deprecated libraries
- 🔍 Providing real-time security analysis of AI suggestions

---
## 🚀 Quickstart with 🐋 Deepseek!

### Prerequisites

CodeGate is distributed as a Docker container. You need a container runtime like
Docker Desktop or Docker Engine. Podman and Podman Desktop are also supported.
CodeGate works on Windows, macOS, and Linux operating systems with x86_64 and
arm64 (ARM and Apple Silicon) CPU architectures.

These instructions assume the `docker` CLI is available. If you use Podman,
replace `docker` with `podman` in all commands.

### Installation

To start CodeGate, run this simple command (making sure to pass in the
deepseek.com URL as the `CODEGATE_PROVIDER_OPENAI_URL` environment variable):

```bash
docker run --name codegate -d -p 8989:8989 -p 9090:9090 -p 8990:8990 \
  -e CODEGATE_PROVIDER_OPENAI_URL=https://api.deepseek.com \
  --mount type=volume,src=codegate_volume,dst=/app/codegate_volume \
  --restart unless-stopped ghcr.io/stacklok/codegate:latest
```

That’s it! CodeGate is now running locally. 

### Using CodeGate and 🐋 Deepseek within Continue

To use Continue with CodeGate, open the Continue settings and add
the following configuration:

```json
{
    "title": "Deepseek-r1",
    "provider": "openai",
    "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    "apiKey": "YOUR_DEEPSEEK_API_KEY",
    "apiBase": "http://localhost:8989/openai",
}
```

Just use Continue as normal, and you know longer have to worry about security
or privacy concerns!

![continue-image](https://github.com/deepseek/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/continue-screen.png)


### Using CodeGate and 🐋 Deepseek with Cline

To use Cline with CodeGate, open the Cline settings and add
the following configuration:

![cline-settings](https://github.com/deepseek/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/cline-settings.png)

Just use Cline as normal, and you know longer have to worry about security
or privacy concerns!

![cline-image](https://github.com/deepseek/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/cline-screen.png)

---
## 🖥️ Dashboard

CodeGate includes a web dashboard that provides:

- A view of **security risks** detected by CodeGate
- A **history of interactions** between your AI coding assistant and your LLM

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/dashboard-dark.webp">
  <img alt="CodeGate dashboard" src="./static/dashboard-light.webp" width="1200px" style="max-width: 100%;">
</picture>

### Accessing the dashboard

Open [http://localhost:9090](http://localhost:9090) in your web browser to
access the dashboard.

To learn more, visit the
[CodeGate Dashboard documentation](https://docs.codegate.ai/how-to/dashboard).

---
## 🔐 Features

### Secrets encryption

CodeGate helps you protect sensitive information from being accidentally exposed
to AI models and third-party AI provider systems by redacting detected secrets
from your prompts using encryption.
[Learn more](https://docs.codegate.ai/features/secrets-encryption)

### Dependency risk awareness

LLMs’ knowledge cutoff date is often months or even years in the past. They
might suggest outdated, vulnerable, or non-existent packages (hallucinations),
exposing you and your users to security risks.

CodeGate scans direct, transitive, and development dependencies in your package
definition files, installation scripts, and source code imports that you supply
as context to an LLM.
[Learn more](https://docs.codegate.ai/features/dependency-risk)

### Security reviews

CodeGate performs security-centric code reviews, identifying insecure patterns
or potential vulnerabilities to help you adopt more secure coding practices.
[Learn more](https://docs.codegate.ai/features/security-reviews)

---
## 🛡️ Privacy first

Unlike other tools, with CodeGate **your code never leaves your machine**.
CodeGate is built with privacy at its core:

- 🏠 **Everything stays local**
- 🚫 **No external data collection**
- 🔐 **No calling home or telemetry**
- 💪 **Complete control over your data**

---
## 🛠️ Development

Are you a developer looking to contribute? Dive into our technical resources:

- [Development guide](https://github.com/stacklok/codegate/blob/main/docs/development.md)
- [CLI commands and flags](https://github.com/stacklok/codegate/blob/main/docs/cli.md)
- [Configuration system](https://github.com/stacklok/codegate/blob/main/docs/configuration.md)
- [Logging system](https://github.com/stacklok/codegate/blob/main/docs/logging.md)

---
## 📜 License

CodeGate is licensed under the terms specified in the
[LICENSE file](https://github.com/stacklok/codegate/blob/main/LICENSE).
