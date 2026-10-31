# [mlx-stream-moe](https://github.com/martianacademy/mlx-stream-moe)

适用于 Apple Silicon (Metal) 的高性能混合专家模型 (MoE) 磁盘流式推理引擎，专为 **DeepSeek-V3**、**DeepSeek-V4.1-Flash** 及 **DeepSeek-R1 (671B)** 打造。

通常运行 671B 模型需要 400GB+ 显存。`mlx-stream-moe` 利用 MoE 稀疏激活特性（每个 token 仅激活 8/256 个专家），通过 Apple Silicon 高速 NVMe SSD 进行零拷贝流式分页加载，使消费级 **16GB/24GB 内存的 Mac** 也能在本地零成本运行前沿大模型。

---

## 🚀 核心特性

* **极低显存占用:** 在 16GB/24GB Mac 上运行 500B–671B DeepSeek 大模型，内存占用降低 90% 以上。
* **Apple Silicon Metal 原生优化:** 基于 MLX 深度优化，统一内存零拷贝与双缓冲异步预读取。
* **OpenAI 兼容网关:** 内置 FastAPI 服务与 SSE 实时流式响应 (`/v1/chat/completions`)。
* **100% 开源免费:** 采用 MIT 开源协议。

---

## ⚡ 快速使用

```bash
git clone https://github.com/martianacademy/mlx-stream-moe.git
cd mlx-stream-moe
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .

# 启动兼容 API 服务
mlx-stream-moe serve \
  --model path/to/DeepSeek-V3-or-R1 \
  --port 8080
```

🔗 **项目地址:** [https://github.com/martianacademy/mlx-stream-moe](https://github.com/martianacademy/mlx-stream-moe)
