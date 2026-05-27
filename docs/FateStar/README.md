# FateStar — Zi Wei Dou Shu, BaZi & Western Astrology AI

<p align="center">
  <img src="./assets/logo.png" alt="FateStar" width="120" />
</p>

<p align="center">
  <a href="https://fatestar.top">Website</a> ·
  English ·
  <a href="./README_cn.md">简体中文</a>
</p>

---

Last year we tried feeding *Zi Wei Dou Shu Quan Shu*, the foundational text of Chinese Purple Star metaphysics, to several major LLMs.

The results were rough.

Classical Chinese terms came back as nonsense English. Classical text titles got mistaken for people's names. One model insisted Zi Wei Dou Shu is "just a variant of Western astrology" and started explaining Aries.

That's when we knew. To actually understand classical Chinese metaphysics, we needed a model raised on Chinese culture.

Then we tried DeepSeek.

It quoted the San He four-transformations doctrine verbatim: 「Hua Lu, Hua Quan, Hua Ke, Hua Ji are the Four Transformations, derived from the Ten Heavenly Stems. The San He school assigns Hua Ke to Tian Tong and Hua Ji to Tai Yin for the Geng stem — this is the orthodox transmission.」

That's textbook accurate. DeepSeek wasn't guessing. It actually knew.

---

That's when we decided. FateStar's entire metaphysics inference engine runs on DeepSeek.

FateStar ([fatestar.top](https://fatestar.top)) is a Chinese metaphysics AI platform unifying **Zi Wei Dou Shu (San He school)**, **BaZi (Four Pillars)**, and **Western astrology** in one place.

We don't think of it as a 「fortune-telling app.」

We think of it as a **long-context classical Chinese NLP benchmark** that happens to ship to real users.

144 stars, 12 palaces, 500+ classical text passages, 100k lines of algorithm code, and DeepSeek doing all the heavy reasoning underneath.

I know some reviewers will frown at the word 「metaphysics.」 Fair enough — divination apps have a reputation problem.

But Zi Wei Dou Shu, at its core, is a thousand-year-old artificial structured data system. 144 stars arranged into 12 palaces by deterministic rules. Every star-palace interaction annotated by classical texts.

It's literally a **classical Chinese text grounding + structured multi-step reasoning** benchmark hiding in plain sight.

And the only model that hits this benchmark, as of today, is DeepSeek.

## Why DeepSeek

We're not on DeepSeek's payroll. We honestly wish we were.

We tried every major LLM. Only DeepSeek made the full pipeline work end-to-end.

Four reasons, ranked by how much each one made us go 「huh, that's actually wild.」

**1. Classical Chinese — DeepSeek is the home-turf model.**

Terms like 「Hua Ji,」 「Lai Yin Gong,」 「self-transformation Lu」 — DeepSeek understands them out of the box.

We didn't run a rigorous benchmark, but the gap is obvious from daily use. Hand the same *Tai Wei Fu* passage to DeepSeek-V4 and it returns the San He doctrine verbatim, with palace numbering and stem-transformation references intact.

Models trained primarily on English-dominant corpora struggle with this niche — they're starved of classical Chinese training data.

DeepSeek is a Chinese model. This is its home turf.

**2. 1M context — the entire Chinese metaphysics canon fits in one prompt.**

After the April 2026 DeepSeek-V4 release, the single-pass context window jumped to **1,000,000 tokens**.

For perspective:

- *Shi Ba Fei Xing Ce Tian Zi Wei Dou Shu Quan Shu* (Zi Wei canon) ≈ 60K tokens
- *Di Tian Sui* + *Qiong Tong Bao Jian* (BaZi classics) ≈ 120K tokens combined
- William Lilly's *Christian Astrology* ≈ 200K tokens

Total: under 400K. DeepSeek-V4's 1M context fits all three traditions in a single prompt, with 60% headroom.

Our approach: user asks a question, we stuff the entire canonical library plus the user's chart plus the question into one prompt, V4 infers in one pass.

No chunking. No RAG. No vector database.

Less plumbing. Less cost. More accurate.

**3. Thinking / Non-Thinking dual mode — maps directly to user intent.**

DeepSeek-V4 natively supports switching between Thinking and Non-Thinking modes.

In FateStar we expose both to the end user.

- **Fast Mode** = `deepseek-v4-flash` Non-Thinking, 30 seconds for a basic chart
- **Thinking Mode** = `deepseek-v4-pro` Thinking, ~3 minutes for a deep reading with full reasoning chain visible

A Zi Wei luck-cycle inference looks like this: stem-revealing → Hua Lu/Hua Ji → self-transformation → Lai Yin palace → Major Limit / annual / monthly nesting. Each step depends on the previous one.

V4-Pro's Thinking mode streams the entire reasoning chain. We render it on the frontend as a step-by-step animation.

Users see exactly how the model derived the conclusion. Not a black box.

For metaphysics, a domain where credibility *is* the product, this is a killer feature.

**4. Economics that let metaphysics AI reach ordinary users.**

DeepSeek's pricing makes a heavy-context, heavy-call product like ours actually viable.

Our metaphysics inferences are long. Single calls easily hit 300k+ tokens (canon plus chart loaded into 1M context).

Running the same reading on a closed-source frontier model from a US lab would cost at least 10× what we pay DeepSeek-V4.

What does 10× cheaper actually mean here?

It means we can make the **basic chart free** for everyone, and only charge for deep readings.

It means regular people can afford AI-driven metaphysics.

It means this can finally become a viable business.

## How we use DeepSeek

Concrete integration details, in case you want to verify.

We call `api.deepseek.com/v1/chat/completions`. Primary model is `deepseek-v4-pro` (Thinking mode) for deep reasoning. Secondary is `deepseek-v4-flash` (Non-Thinking) for fast chart generation and conversational fallback.

Context window 1M, stuffed with the canonical library plus chart plus user question in a single pass.

We use function calling to make DeepSeek-V4 emit structured chart JSON, then Thinking mode runs the inference pipeline.

The data flow:

User birth time arrives → astrology engine computes the 144-star × 12-palace structured chart → DeepSeek-V4-Pro reads canon + chart → Thinking mode infers Major Limit / annual cycles → outputs an interpretation with citations back to the original classical text.

The entire pipeline runs on FateStar's backend. DeepSeek accounts for about 90% of our infrastructure cost (the rest is DB, CDN, astrology engine).

Without DeepSeek-V4, this product doesn't exist.

I'm serious.

## Verification (please verify yourself)

Open [fatestar.top](https://fatestar.top), enter a birth time.

In the bottom-right of the input box, there's a model selector dropdown. You'll see two options:

- Fast Mode  `DeepSeek-V4-Flash Thinking Max`
- Thinking Mode  `DeepSeek-V4-Pro Thinking Max`

Those are the user-facing names. Under the hood we call DeepSeek's official `deepseek-v4-pro` and `deepseek-v4-flash`.

We didn't hide it. We made DeepSeek the headline feature.

The footer also includes a disclosure: 「FateStar performs analysis and inference based on Chinese traditional culture, Zi Wei Dou Shu, and the chart. Content is for reference only.」

We're building Chinese cultural digitization. DeepSeek-V4 is the engine that makes it possible.

## Try it

Open [fatestar.top](https://fatestar.top), enter a birth time.

No signup. No payment. You get a basic chart in 30 seconds (V4-Flash).

If you want a deep reading (V4-Pro Thinking mode with chain-of-thought), sign up for the paid version.

We have a small following in Taiwan's metaphysics community, primarily because our readings cite back to canonical text rather than hallucinating wisdom. That capability comes from DeepSeek. We couldn't build it without V4.

## Screenshot

<p align="center">
  <img src="./assets/screenshot.png" alt="FateStar chart screenshot" width="640" />
</p>

## Contact

- Website: [fatestar.top](https://fatestar.top)
- Email: hello@fatestar.top

---

A note to the DeepSeek team, if you're reading this.

You gave small, niche products like FateStar a path to exist.

Classical Chinese text grounding + 1M long context + Thinking-mode chain-of-thought reasoning — over the past six months, DeepSeek-V4 is the only model that ships all three at production quality.

We built FateStar to digitize traditional Chinese metaphysics and make it affordable for ordinary people.

We'd love to be in the awesome list, so more DeepSeek users can see that Chinese cultural niches are V4's home turf too.

> / Louis Lin, founder of FateStar
