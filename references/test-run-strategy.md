# Test Run Strategy

## Low-cost pipeline validation

Before running the full booksmith pipeline on frontier models (which costs ~$55-70 per book), validate the entire workflow with minimal cost:

### Approach
1. **Use local model** for both `booksmith-planner` and `booksmith-author` profiles temporarily.
2. **Generate shorter reports** via GPT-Researcher (or any source) — 2-5 short markdown files instead of full-length ones.
3. **Run the full pipeline** to verify:
   - Git operations work correctly
   - Kanban board flow is correct (dependencies, status transitions)
   - File I/O and template rendering produce valid output
   - Directory creation with `.gitkeep` works

### Cost comparison
| Run type | Model | Reports | Estimated cost |
|----------|-------|---------|----------------|
| Full production | Opus 4.7 + Sonnet 4.6 | 5 × ~250KB | $55-70 |
| Test validation | Local model | 5 × short (~10KB) | ~$0 (local compute only) |

### When to switch to production models
Once the test run produces a complete manuscript (even if quality is lower), you know:
- The pipeline logic is sound
- All file paths and Git operations work
- Kanban dependencies are correct
- Templates render correctly

Then re-run with frontier models for final quality.
