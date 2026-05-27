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

**FateStar** is a DeepSeek-powered AI fortune-telling platform that unifies three traditions in one place: **Zi Wei Dou Shu (Purple Star Astrology, San He school)**, **BaZi (Four Pillars of Destiny)**, and **Western astrology**. A dual-track Gan Zhi (heavenly stem / earthly branch) engine and classical-text grounding (e.g., *Tai Wei Fu*, *Zi Wei Dou Shu Quan Shu*) produce readings that are cited, auditable, and reproducible.

Website: <https://fatestar.top>

## Features

- **Three schools, one chart**: Zi Wei (San He lineage), BaZi four pillars, and Western astrology in a single workspace.
- **Dual-track Gan Zhi**: real lunisolar calendar Gan Zhi and Zi Wei palace-numbering Gan Zhi are strictly separated to avoid the common "calendar/palace mixup" bug.
- **Classical-text grounding**: every interpretation cites primary sources from Chinese metaphysics canon — no hallucinated "ancient wisdom".
- **DeepSeek inference**: DeepSeek V3 / R1 handles long-context reasoning across structured chart data, classical Chinese, and modern explanation.
- **Reversibility-proven engine**: 7-dimensional bijection (annual / monthly / daily / hourly / Dou Jun / Major Limit / Minor Limit) verified across 500+ randomized test cases.
- **Privacy-first**: birth data is encrypted at rest; charts can be exported locally; no signup required for a basic reading.

## How DeepSeek is used

1. **Chart-to-language**: turns 144 stars × 12 palaces of structured chart data into a reading the user can actually read.
2. **Cross-source verification**: DeepSeek R1's long context window lets the model read classical Chinese text, the chart, and the user question simultaneously to produce a grounded answer.
3. **Multi-step luck-cycle reasoning**: chain-of-thought transformations (stem-revealing → Hua Lu/Hua Ji → self-transformation → Lai Yin palace) executed step by step by DeepSeek.

## Try it

Open <https://fatestar.top>, enter a birth time, get a chart. No signup required.

## Screenshot

<p align="center">
  <img src="./assets/screenshot.png" alt="FateStar chart screenshot" width="640" />
</p>

## Contact

- Website: <https://fatestar.top>
- Email: hello@fatestar.top
