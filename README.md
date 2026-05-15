# Booksmith — Automated Book Pipeline

## Overview

Booksmith is a fully automated book creation pipeline that transforms five comprehensive research reports into a polished manuscript. The pipeline handles planning, drafting, review, supplementary writing, and final assembly — with human intervention only at the chapter quality gate.

## Architecture

```
Phase 1: Planning     → outline, book bible, chapter prompts
Phase 2: Drafting     → serial chapter drafts + self-review (Claude Opus 4.7)
Phase 2b: Review Gate → human feedback on flagged chapters (3-day timeout)
Phase 3: Manuscript   → full manuscript review (Claude Sonnet 4.6)
Phase 4: Logues       → foreword, intro, prologue, epilogue, glossary
Phase 5: Finalizing   → stitch all parts into final manuscript
```

## Models Used

| Phase | Model | Role |
|-------|-------|------|
| Planning | Claude Sonnet 4 | Outline, book bible, chapter prompts |
| Drafting | Claude Opus 4.7 | Chapter drafts (primary generation) |
| Self-Review | Claude Sonnet 4.6 | Per-chapter quality gate |
| Manuscript Review | Claude Sonnet 4.6 | Full manuscript review |
| Logues | Claude Opus 4.7 | Supplementary material |

## Estimated Cost

~$55–70 per book (drafting dominates at ~85% of cost). Prompt caching can reduce this by 30-50%.

## Directory Structure

```
booksmith/                          ← project root (git-tracked)
├── config.yaml                     ← pipeline configuration
├── README.md                       ← this file
├── .gitignore                      ← git ignore rules
├── pipeline/                       ← automation code & templates
│   ├── templates/                  ← prompt templates
│   └── ...                         ← orchestrator scripts (future)
├── books/                          ← per-book monorepo subdirectories
│   └── <book-name>/                ← each book's working directory
│       ├── planning/               ← Phase 1 output
│       ├── chapters/               ← Phase 2 output
│       ├── review/                 ← Phase 3 output
│       ├── logues/                 ← Phase 4 output
│       └── manuscript/             ← Phase 5 output
└── logs/                           ← execution logs per run
```

## Usage

### Starting a New Book

1. Create a new directory under `books/`: `mkdir books/<book-name>`
2. Place the five research report markdown files in `books/<book-name>/reports/`
3. Trigger the pipeline (via Hermes: "run booksmith pipeline for <book-name>")

### Pipeline Execution

The pipeline runs as an on-demand task through Hermes. It:
1. Pulls the latest state from git
2. Executes each phase sequentially
3. Pauses at Phase 2b for human review feedback
4. Pushes all changes back to git

## Configuration

Edit `config.yaml` to customize:
- GitHub repo URL
- Model selections per phase
- Timeout settings
- Which logues to generate

## Git Workflow

The entire `booksmith/` directory is a single git repository (monorepo). Each book lives as a subdirectory under `books/`. This means:
- One push/pull for all books
- Shared templates and config across books
- Simple backup and version control

Per-book commits are made during pipeline execution (e.g., one commit per drafted chapter).

## Human Intervention Points

1. **Phase 2b — Chapter Review Gate** (after all ~20 chapters drafted)
   - You receive a review report via Telegram
   - Options: approve all, specify fixes, or handle manually
   - Timeout: 3 days → auto-fixes applied if no response

That's the only human gate. Everything else is fully automated.
