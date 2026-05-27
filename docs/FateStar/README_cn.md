# FateStar 紫微斗数 · 八字 · 星座 AI 命理

<p align="center">
  <img src="./assets/logo.png" alt="FateStar" width="120" />
</p>

<p align="center">
  <a href="https://fatestar.top">官网</a> ·
  <a href="./README.md">English</a> ·
  简体中文
</p>

---

故事是这样的。

去年我们试着把紫微斗数全书丢给市面上几家主流大模型解读。

效果惨不忍睹。

中文古籍术语被翻得完全跑题。古文典籍名当成了人名。还有的直接告诉我紫微斗数是西方占星的变体。

= =

那一刻我心里咯噔一下，想让大模型真正读懂中文古籍，海外那批不行，得找个真正读过中文文化的。

最后我们试到 DeepSeek。

它直接给出了三合派四化的教科书原文，「化禄、化权、化科、化忌为四化，源自十干，三合派以庚干化科为天同、化忌为太阴，此乃世传」。

我当时就愣住了。

不是说它说的有多惊艳，是因为它说的就是教科书上的原文。

它不是猜，是真的懂。

---

那个时候我们就下定决心，FateStar 全套命理推理引擎绑死 DeepSeek。

FateStar 是一个把**紫微斗数（三合派）**、**八字四柱**、**西洋占星**揉在一起的中文命理 AI 平台，官网在 [fatestar.top](https://fatestar.top)。

我们没把它当成一个「算命 App」在做。

我们是把它当成**中文文言文长上下文 NLP benchmark** 在做。

144 颗星，12 个宫位，500+ 古籍条文，10 万行算法代码，DeepSeek 在后面顶着整套推理链路。

我知道有些朋友看到「命理」两个字会皱眉。我也理解，毕竟「算命」这两个字多少带点土腥气。

但说真的，紫微斗数这套东西，底层是一个 1000 年前的人造结构化数据系统。144 颗星按规则排进 12 个宫，每颗星跟每个宫的组合关系都有古籍条文标注。

它就是一个**中文古籍数字化加结构化推理** 的活靶子场景。

而能打中这个靶的大模型，目前我们只找到 DeepSeek。

## 为啥非得是 DeepSeek

这块我跟你说真的。

我们不是收了 DeepSeek 的钱（我们恨不得 DeepSeek 来收编我们）。

我们试过市面上每一个主流大模型，最后只有 DeepSeek 能跑通整套链路。

四点原因，按惊艳度排。

**1. 中文文言文，DeepSeek 是国产大模型的绝对主场。**

「化忌」「来因宫」「自化禄入」这种术语，DeepSeek 直接懂。

我们没做过严谨的 benchmark，但日常用下来感受很明显。同一段太微赋丢给 DeepSeek 解读，它直接给出三合派的教科书原文，看得我们直接愣住。

海外模型在中文古籍这个 niche 上训练数据吃得太少，目前还差得远。

DeepSeek 是国产大模型，中文文化语境是它的主场。

**2. 1M 上下文，整套术数典籍一锅端。**

2026 年 4 月 DeepSeek-V4 发布之后，单次推理上下文直接拉到 1,000,000 tokens。

啥概念呢。

紫微古书《十八飞星策天紫微斗数全书》大概 60K tokens。八字大典《滴天髓》《穷通宝鉴》加起来 120K tokens。再加西洋占星《Christian Astrology》也才 200K tokens。

加起来不到 400K，DeepSeek-V4 一把全塞进去还剩 60% 富余。

我们的做法是这样，用户问问题进来、把整套术数典籍加上用户命盘加上问题塞进同一个 prompt、V4 一次推理拿结果。

不用切片。不用 RAG。不用向量数据库。

省事，省钱，还准。

**3. Thinking / Non-Thinking 双模式，直接对应用户场景。**

DeepSeek-V4 原生支持 Thinking 模式跟 Non-Thinking 模式切换。

在 FateStar 里我们直接把这两个模式暴露给用户。

- **快速模式** = `deepseek-v4-flash` Non-Thinking，30 秒出基础命盘
- **思考模式** = `deepseek-v4-pro` Thinking，3 分钟出深度推理报告，思维链可见

紫微推流年要走透干 → 化禄忌 → 自化 → 来因宫 → 大限/流年/流月嵌套这套链路，每一步都依赖前一步。

V4-Pro 的 Thinking 模式把整个思维链直接吐出来，我们前端把它渲染成步骤动画给用户看。

用户能看到 AI 是怎么一步一步推出来的，不是黑箱。

这对命理这种需要「信服感」的场景，是核武器。

**4. 成本极其经济，让 AI 命理能普及给普通人。**

DeepSeek 的官方定价让我们这种长上下文重度调用的应用跑得起。

我们做命理这种长上下文推理，单次调用 token 数动辄 30 万起（古籍加命盘塞满 1M context）。

如果用闭源大厂的旗舰模型跑同样的报告，成本至少是 DeepSeek 的 10 倍以上。

10 倍的差距是啥概念呢？

就是说我们能把基础命盘做成**免费** 给用户用，付费的只有深度报告。

就是说普通人能用得起 AI 命理。

就是说这件事终于能做成生意。

## 我们怎么用 DeepSeek

具体的技术接入是这样的。

我们调 `api.deepseek.com/v1/chat/completions`，主力模型 `deepseek-v4-pro`（思考模式）跑深度推理链路，辅助模型 `deepseek-v4-flash`（快速模式）跑基础命盘语义化跟闲聊。

上下文配 1M，单次推理一把塞整套术数典籍加命盘加问题。

调用方式上我们用 function calling 让 V4 输出结构化命盘 JSON，再让 Thinking 模式跑后续的推理链路。

整条数据流是这样跑的。

用户出生时间进来 → 排盘引擎算 144 星 × 12 宫的结构化数据 → DeepSeek-V4-Pro 读古籍加命盘 → Thinking 模式推理出流年大限 → 输出溯源到古书原文的报告。

整套链路在 FateStar 后端跑，DeepSeek 占成本结构的 90%（剩下是数据库加 CDN 加排盘引擎）。

没有 DeepSeek-V4，这事真做不成。

我说真的。

## Verification（你可以自己验证）

打开 [fatestar.top](https://fatestar.top)，输入出生时间。

底部输入框右下角有个模型切换 dropdown，你直接能看到两个选项。

- 快速模式  `DeepSeek-V4-Flash Thinking Max`
- 思考模式  `DeepSeek-V4-Pro Thinking Max`

这两个名字是我们暴露给用户的友好命名。后端调的就是 DeepSeek 官方 `deepseek-v4-pro` 跟 `deepseek-v4-flash`。

我们没藏。我们把 DeepSeek 当卖点。

底部还有一行声明，「FateStar 根据中国传统文化『紫微斗数』主席『命盘』进行分析推理，内容仅供参考」。

我们做的是中国传统文化数字化，DeepSeek-V4 是这件事的核心引擎。

## 你可以这样玩

打开 [fatestar.top](https://fatestar.top)，输入出生时间。

不用注册，不用付费，30 秒拿到一份基础命盘（V4-Flash 跑的）。

想看深度报告（V4-Pro Thinking 模式跑的链式推理），可以注册看付费版。

我们目前在台湾命理圈有点小名气，主要是因为我们的解读真的能溯源到古书原文，不是 AI 瞎掰。

这点是 DeepSeek 给我们的能力。

我们自己做不到。

## 截图

<p align="center">
  <img src="./assets/screenshot.png" alt="FateStar 命盘截图" width="640" />
</p>

## 联系

- 官网 [fatestar.top](https://fatestar.top)
- 邮箱 hello@fatestar.top

---

以上。

如果你是 DeepSeek 团队的兄弟看到这里，我想说一句。

是你们让 FateStar 这种小而美的产品有了活路。

中文古籍加 1M 长上下文加 Thinking 模式链式推理这三件事，过去半年只有 DeepSeek-V4 能同时做到。

我们做 FateStar 是为了把传统术数数字化，让普通人用得起。

希望能进 awesome 清单，让更多 DeepSeek 用户看到中文文化 niche 也是 V4 的主场。

> / 作者：林靖翔（FateStar 创始人）
