# [falsify](https://github.com/263311487-ux/falsify)

The scientific thinking protocol for AI agents. **Falsify before you believe.**

falsify is a single-Markdown skill that installs a 5-stage scientific thinking protocol on any AI agent — DeepSeek Harness, Codex, Claude Code, Cursor, Gemini CLI and 20+ more. It stops agents from giving confident answers they cannot falsify.

## Key Features

1. **5-stage protocol**: Axioms → Hypothesis → Adversarial test → Evidence → Calibrated verdict
2. **The Iron Law**: no verdict without a falsifiable hypothesis (没有可证伪的假设，就没有结论)
3. **Evidence calibration**: every verdict carries a confidence grade and explicit uncertainty markers
4. **28 built-in eval cases**: `evals/cases.md` verifies the skill actually changes agent behavior
5. **Zero dependencies**: one Markdown file; installs via skills.sh or npm in seconds

## Integrate with DeepSeek

falsify works out of the box with **DeepSeek Harness (DSH)** — the companion project [dsh-verify](https://github.com/263311487-ux/dsh-verify) is an installable DSH (Cordis) plugin that runs falsify's verification passes inside DSH sessions.

### Install with skills.sh

```bash
npx skills add 263311487-ux/falsify
```

### Install with npm

```bash
npx falsify-skill
```

Or copy `SKILL.md` into your agent's skills directory — that's it.
