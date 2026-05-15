# Booksmith — Automated Book Pipeline

## Overview

Booksmith is a fully automated book creation pipeline that transforms five comprehensive research reports into a polished manuscript. The pipeline handles planning, drafting, review, supplementary writing, and final assembly — with human intervention only at the chapter quality gate.

**Domain:** Cybersecurity Non-Fiction (Narrative Style)
**Author Voice:** Elite investigative journalist ("Information, not ammunition")

## Architecture

The pipeline is managed by a **Hermes Skill**. It runs as an on-demand task through Hermes and acts as a Project Manager:

1.  **Loads Context:** Reads reports and templates from disk.
2.  **Delegates Work:** Sends creative tasks to specialized Hermes Profiles (`booksmith-planner` and `booksmith-author`).
3.  **Manages State:** Handles Git operations (pull/push) and file management directly using terminal tools.
4.  **Human Gate:** Pauses at Phase 2b for review feedback via Telegram before proceeding.

### Workflow Phases

*   **Phase 1: Planning** → Outline, Book Bible, Chapter Prompts (Delegated to Planner)
*   **Phase 2: Drafting** → Serial chapter drafts + self-review (Delegated to Author)
*   **Phase 2b: Review Gate** → Human feedback on flagged chapters (3-day timeout → auto-fix)
*   **Phase 3: Manuscript** → Full manuscript review (Delegated to Author)
*   **Phase 4: Logues** → Foreword, intro, prologue, epilogue, glossary (Delegated to Author)
*   **Phase 5: Finalizing** → Stitch all parts into final manuscript

## Models Used

| Phase | Model | Role |
|-------|-------|------|
| Planning | Claude Sonnet 4.6 | Outline, book bible, chapter prompts |
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
├── templates/                      ← prompt templates used by the Skill
│   ├── book_bible_template.md      ← Phase 1 output template
│   ├── chapter_prompt_template.md  ← per-chapter prompt template
│   ├── self_review_template.md     ← Phase 2 quality gate checklist
│   ├── manuscript_review_template.md← Phase 3 full review format
│   └── logues_template.md          ← Phase 4 supplementary writing guide
├── books/                          ← per-book monorepo subdirectories
│   └── <book-name>/                ← each book's working directory
│       ├── reports/                ← Your 5 research reports go here
│       ├── planning/               ← Phase 1 output (bible, prompts)
│       ├── chapters/               ← Phase 2 output (drafted chapters)
│       ├── review/                 ← Phase 3 output (manuscript review)
│       ├── logues/                 ← Phase 4 output (foreword, intro, etc.)
│       └── manuscript/             ← Phase 5 output (final stitched book)
└── logs/                           ← execution logs per run
```

## Usage

### Starting a New Book

1. Trigger the pipeline via Hermes: "run booksmith for <book-name>"
2. The pipeline automatically creates the full directory structure and commits it to Git
3. Drop your five research report markdown files into `books/<book-name>/reports/`

### Pipeline Execution

The pipeline is managed by the **Booksmith Skill** (installed at `~/.hermes/skills/booksmith/SKILL.md`). When triggered, I will:
1. Load the skill to understand the workflow.
2. Delegate creative work to your Hermes Profiles (`booksmith-planner` and `booksmith-author`).
3. Handle Git operations and file management directly.

## Configuration

Edit `config.yaml` to customize:
*   GitHub repo URL
*   Model selections per phase
*   Timeout settings
*   Which logues to generate

## Git Workflow

The entire `booksmith/` directory is a single git repository (monorepo). Each book lives as a subdirectory under `books/`. This means:
*   One push/pull for all books
*   Shared templates and config across books
*   Simple backup and version control

Per-book commits are made during pipeline execution (e.g., one commit per drafted chapter).

## Human Intervention Points

1.  **Phase 2b — Chapter Review Gate** (after all ~20 chapters drafted)
    *   You receive a review report via Telegram
    *   Options: approve all, specify fixes, or handle manually
    *   Timeout: 3 days → auto-fixes applied if no response

That's the only human gate. Everything else is fully automated.
