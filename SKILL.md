---
name: booksmith
description: Automated book creation pipeline orchestrator for cybersecurity non-fiction. Manages planning, drafting, review, and finalizing phases using delegated Hermes profiles.
category: productivity
---

# Booksmith Pipeline Skill

## Overview

This skill orchestrates the end-to-end creation of a cybersecurity non-fiction book from five research reports. It manages the workflow across 5 phases, delegating creative work to specialized Hermes Profiles (`booksmith-planner` and `booksmith-author`) while handling file I/O and Git operations directly.

**Domain:** Cybersecurity Non-Fiction (Narrative Style)
**Author Voice:** Elite investigative journalist ("Information, not ammunition")

## Prerequisites

1.  **Git Repository:** The `booksmith/` directory must be a git repo with a remote configured (`origin`).
2.  **Hermes Profiles:** Two profiles must exist:
    *   `booksmith-planner`: Uses Sonnet 4.6 for structural planning.
    *   `booksmith-author`: Uses Opus 4.7 for drafting/logues and Sonnet 4.6 for review.
3.  **Book Directory:** A directory exists under `books/<book-name>/` containing a `reports/` folder with the 5 source markdown files.

## Workflow Phases

### Phase 1: Planning (Delegated)

**Goal:** Create the Book Bible and Chapter Prompts.

1.  **Load Context:** Read all `.md` files from `books/<book-name>/reports/`.
2.  **Delegate to Planner:** Use `delegate_task` to send the reports to the `booksmith-planner` profile with this instruction:
    > "Analyze these five research reports and generate a comprehensive Book Bible and individual Chapter Prompts for each chapter. Follow the structure defined in `pipeline/templates/book_bible_template.md` and `pipeline/templates/chapter_prompt_template.md`. Save the output to `books/<book-name>/planning/`."
3.  **Verify:** Ensure `book_bible.md` and `chapter_prompts/` directory are created with content.

### Phase 2: Drafting (Delegated, Serial)

**Goal:** Write all chapters one by one with self-review.

1.  **Iterate Chapters:** For each chapter prompt in `books/<book-name>/planning/chapter_prompts/`:
    *   **Load Context:** Read the specific chapter prompt and the Book Bible (`books/<book-name>/planning/book_bible.md`).
    *   **Delegate to Author:** Use `delegate_task` to send the data to the `booksmith-author` profile with this instruction:
        > "Draft Chapter {{number}} using the provided prompt and book bible. Follow the 'No Hallucination' rule strictly. After drafting, perform a self-review against the checklist in `pipeline/templates/self_review_template.md`. Save the draft to `books/<book-name>/chapters/ch{{number}}_draft.md`."
    *   **Commit:** Run `git add -A && git commit -m "Draft chapter {{number}}"` after each successful draft.

### Phase 2b: Review Gate (Human Intervention)

**Goal:** Human review of flagged chapters before proceeding.

1.  **Compile Report:** Check all drafts in `books/<book-name>/chapters/`. Identify any that were marked as "needs_review" during self-review or show obvious quality issues.
2.  **Send to User:** Send a summary via Telegram:
    > "**Booksmith Review Gate**\nTotal Chapters: {{total}}\nApproved: {{approved}}\nFlagged: {{flagged}}\n\nIssues:\n- Ch X: [Issue description]\n..."
3.  **Wait:** Pause execution for up to 3 days waiting for user feedback.
4.  **Handle Feedback:**
    *   If user provides specific fixes, delegate revision tasks to `booksmith-author`.
    *   If no response after 3 days, auto-fix all flagged chapters using `booksmith-author`.

### Phase 3: Manuscript Review (Delegated)

**Goal:** Full manuscript review for macro-level issues.

1.  **Load Context:** Read the full assembled text (all chapters).
2.  **Delegate to Author:** Use `delegate_task` with `booksmith-author`:
    > "Review the complete manuscript in `books/<book-name>/chapters/`. Check for pacing, cross-chapter continuity, and redundancy. Save notes to `books/<book-name>/review/manuscript_review.md`."

### Phase 4: Logues Writing (Delegated)

**Goal:** Write supplementary material (Foreword, Intro, etc.).

1.  **Check Config:** Read `config.yaml` to see which logues are enabled (`logues_included`).
2.  **Delegate to Author:** For each enabled logue type:
    > "Write the {{logue_type}} for this book based on the manuscript and bible. Save to `books/<book-name>/logues/{{logue_type}}.md`."

### Phase 5: Finalizing (Direct Execution)

**Goal:** Stitch everything into a final manuscript.

1.  **Assemble:** Read all files in order:
    *   Logues (alphabetical)
    *   Chapters (numerical)
2.  **Add Front Matter:** Prepend Title Page and Copyright Notice.
3.  **Save:** Write the result to `books/<book-name>/manuscript/final_manuscript.md`.
4.  **Final Commit:** Run `git add -A && git commit -m "Final manuscript assembled"` and push to remote.

## Templates Reference

All templates are located in `pipeline/templates/`:
*   `SOUL_planner.md` / `SOUL_author.md` (Loaded by Profiles, not passed here)
*   `book_bible_template.md`
*   `chapter_prompt_template.md`
*   `self_review_template.md`
*   `manuscript_review_template.md`
*   `logues_template.md`

## Error Handling

*   **Git Failures:** If push fails, check if the remote is configured correctly.
*   **Missing Reports:** Verify `books/<book-name>/reports/` exists before starting Phase 1.
*   **Profile Errors:** If a delegation fails, retry once with a clearer instruction or simplified context.
