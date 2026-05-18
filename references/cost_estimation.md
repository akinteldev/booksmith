# Cost Estimation Breakdown

## Per-Book Cost: $55–70 (Standard Pricing)

### Token Assumptions
* 5 reports × ~250KB ≈ 350K tokens total (Opus 4.7 tokenizer: +35% overhead → ~460K effective)
* Book bible + prompts ≈ 10-20K tokens
* Chapter draft output ≈ 3-5K tokens each

### Detailed Breakdown

| Phase | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| **Planning** (outline, bible, prompts) | Opus 4.7 | ~480K | ~15K | ~$2.55 |
| **Drafting** × 20 chapters | Opus 4.7 | ~9.6M | ~80K | ~$50.50 |
| **Self-review** × 20 chapters | Sonnet 4.6 | ~160K | ~3K | ~$0.50 |
| **Manuscript review** (full) | Opus 4.7 | ~100K | ~10K | ~$0.55 |
| **Logues writing** (~5 pieces) | Opus 4.7 | ~250K | ~30K | ~$1.40 |
| **Finalizing** (stitching, minor LLM) | Sonnet 4.6 | ~150K | ~5K | ~$0.50 |

### Cost Optimization: Prompt Caching

If prompt caching is effective (reusing the same reports across chapters), input costs could drop **30-50%**, bringing total to **~$40-50/book**.

**Caching strategy:** Use `cache_control` at the top of prompts for report content that stays constant across chapter drafts.

### Model Pricing Reference (Anthropic API)

| Model | Input | Output |
|-------|-------|--------|
| Opus 4.7 | $5/MTok | $25/MTok |
| Sonnet 4.6 | $3/MTok | $15/MTok |

*MTok = Million tokens*
