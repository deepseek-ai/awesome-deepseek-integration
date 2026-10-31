# [mlx-stream-moe](https://github.com/martianacademy/mlx-stream-moe)

High-performance Apple Silicon (Metal) disk-streaming inference engine for massive Mixture-of-Experts models (**DeepSeek-V3**, **DeepSeek-V4.1-Flash**, and **DeepSeek-R1 671B**).

Traditionally, running a 671B MoE requires 400GB+ VRAM or costly cloud API subscriptions. `mlx-stream-moe` exploits MoE sparsity — where only ~8 out of 256 experts activate per token — streaming active expert weights directly from Apple Silicon NVMe SSDs into unified memory, enabling consumer **16GB/24GB Macs** to run frontier models at zero cost.

---

## 🚀 Key Features

* **Zero-RAM Exhaustion:** Runs 500B–671B DeepSeek models on consumer Apple Silicon hardware with >90% RAM reduction.
* **Apple Silicon Metal Optimization:** Custom MLX kernels, zero-copy unified memory buffers, and asynchronous lookahead prefetching.
* **OpenAI-Compatible API Gateway:** Built-in FastAPI server with SSE streaming (`/v1/chat/completions`) for seamless drop-in integration.
* **100% Free & Open-Source:** MIT licensed.

---

## ⚡ Quick Start

```bash
# Clone and install
git clone https://github.com/martianacademy/mlx-stream-moe.git
cd mlx-stream-moe
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .

# Launch OpenAI-compatible API gateway
mlx-stream-moe serve \
  --model path/to/DeepSeek-V3-or-R1 \
  --port 8080 \
  --cache-capacity 32
```

---

## 🔌 Cursor & Continue.dev Integration

Connect Cursor, Continue.dev, or Cline to your local DeepSeek engine:

```json
{
  "models": [
    {
      "title": "Local DeepSeek MoE",
      "provider": "openai",
      "model": "deepseek-reasoner",
      "apiBase": "http://127.0.0.1:8080/v1",
      "apiKey": "free-forever"
    }
  ]
}
```

🔗 **Repository:** [https://github.com/martianacademy/mlx-stream-moe](https://github.com/martianacademy/mlx-stream-moe)
