<img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/huixiangdou.jpg" width="64" height="auto" /> 

# [茴香豆](https://github.com/InternLM/HuixiangDou)

“茴香豆”是一个基于 LLM 的领域知识助手。特点：

1. 应对群聊这类复杂场景，解答用户问题的同时，不会消息泛滥
2. 提出一套解答技术问题的算法 pipeline
3. 部署成本低，见[技术报告 arxiv2401.08772](https://arxiv.org/abs/2401.08772)


## 效果展示

1. 它是个**机器人**

    * 面对幻觉会说不知道
    * 支持微信
    * 支持飞书

    <img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/demo0.jpg" width="400">

2. 它是个**群组**机器人

    * 不会搭理闲聊
    * 只找需要帮助的人

    <img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/inside-mmpose.jpg" width="400">

2. 它是个**领域知识**群组机器人

    * 不依赖训练，依靠算法 pipeline + LLM
    * 已经面对数千用户，半年被“调戏”了 2w 次以上

    <img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/inside-middleware.png" width="400">

## 配置 deepseek API

**STEP1.** 打开 [deepseek 开放平台](https://platform.deepseek.com) 申请 token

**STEP2.** 参照 [HuixiangDou 高级配置](https://github.com/InternLM/HuixiangDou?tab=readme-ov-file#step4-advanced-version-optional)，把 token 填入 `config.ini`

```ini
# config.ini
[llm]
enable_local = 0
enable_remote = 1
..
[llm.server]
..
remote_type = "deepseek"
remote_api_key = "YOUR-API-KEY"
remote_llm_max_text_length = 16000
remote_llm_model = "deepseek-chat"
```

**STEP3.** 运行
```shell
python3 -m huixiangdou.main --standalone
```