---
name: booksmith
description: Automated book creation pipeline orchestrator for cybersecurity non-fiction. Manages planning, drafting, review, and finalizing phases using Kanban board orchestration with specialized Hermes Profiles.
category: productivity
---

# Booksmith Pipeline Skill

## Overview

This skill orchestrates the end-to-end creation of a cybersecurity non-fiction book from five research reports. It uses a **Kanban board** for task management — all work is queued as linked tasks that execute sequentially via the dispatcher, giving full visibility into every phase.

**Domain:** Cybersecurity Non-Fiction (Narrative Style)
**Author Voice:** Veteran investigative journalist ("Information, not ammunition"; calm alarm, translation over sensationalism)

## Prerequisites

1.  **Git Repository:** The `booksmith/` directory must be a git repo with a remote configured (`origin`).
2.  **Hermes Profiles:** Two profiles must exist:
    *   `booksmith-planner`: Uses Sonnet 4.6 for structural planning.
    *   `booksmith-author`: Uses Opus 4.7 for drafting/logues and Sonnet 4.6 for review (or Sonnet 4.6 for all phases during test runs to reduce costs).

## Kanban Architecture

The pipeline uses a Kanban board with parent-child task linking to enforce sequential execution:

```
T1: Planning → T2: Drafting + Review Gate → T3: Manuscript Review → T4: Logues Writing → T5: Finalizing
```

- Tasks are created upfront in Phase 0 with proper parent links.
- The dispatcher auto-promotes child tasks when parents complete (polls every ~60s).
- Human-in-the-loop is handled via `kanban_block()` at the review gate — the task blocks itself, user provides feedback via `/unblock`, then execution resumes.
- All task execution is visible on the Kanban board dashboard.

**Task creation method:** Use the Python API (`kanban_create()`) for parent-child linking. If unavailable, fall back to CLI: `hermes kanban --board booksmith create "Title" --body "Body" --assignee profile`.

## Workflow Phases

### Phase 0: Setup (Automatic)

**Goal:** Create directory structure, notify user where to place reports, verify inputs, then create all Kanban tasks with parent-child linking.

1.  **Extract Book Name:** Parse `<book-name>` from the invocation message (e.g., "Run booksmith for 'Zero Trust'" → `zero-trust`). Normalize: lowercase, hyphens for spaces.
2.  **Check Directory:** Check if `books/<book-name>/` exists in `/home/emkay/projects/booksmith/`.
3.  **Create Structure:** If not, create the full directory tree with `.gitkeep` files:
    ```
    books/<book-name>/
    ├── reports/          ← where research reports go
    ├── planning/         ← Book Bible + Chapter Prompts (Phase 1)
    ├── chapters/         ← Drafted chapters (Phase 2)
    ├── review/           ← Manuscript review notes (Phase 3)
    ├── logues/           ← Foreword, intro, etc. (Phase 4)
    └── manuscript/       ← Final stitched book (Phase 5)
    ```
4.  **Commit Structure:** Run `git add -A && git commit -m "Initialize book directory: <book-name>"`.
5.  **Notify User:** Send a message via Telegram:
    > "**Booksmith Setup Complete**\nDirectory created at `books/<book-name>/reports/`. Drop your 5 research reports there and reply 'ready' when done."
6.  **Wait for Confirmation:** Pause execution until the user replies confirming they've placed their reports.
7.  **Verify Reports:** Check that `books/<book-name>/reports/` contains exactly 5 markdown files. If fewer, ask the user to provide them before proceeding.
8.  **Archive Old Tasks:** Archive ALL existing tasks on the `booksmith` board from previous runs (not just completed ones — blocked and todo tasks also need clearing):
    ```bash
    hermes kanban --board booksmith list --json | python3 -c "import sys,json; [print(t['id']) for t in json.load(sys.stdin)]"
    ```
    Then archive them: `hermes kanban --board booksmith archive <task_ids...>`
9.  **Create Kanban Tasks:** Create all pipeline tasks with parent-child linking (capture each task ID and pass it as a parent to the next):

```python
t1 = kanban_create(
    title="Phase 1: Planning - Generate Book Bible & Prompts",
    assignee="booksmith-planner",
    body=f"""Analyze the five research reports in books/{book_name}/reports/. Generate a comprehensive Book Bible and individual Chapter Prompts following templates/book_bible_template.md and templates/chapter_prompt_template.md.

CRITICAL: At the top of the Book Bible, include an explicit 'Report Mapping' section that lists each report number (1-5) alongside its exact filename, source authorities, and core topic. This crosswalk prevents confusion in later phases about which report covers what subject matter.

Derive both a **Title** and a **Subtitle** for the book from the reports. The title should be punchy and memorable; the subtitle should clarify the book's scope (e.g., "How Cybercriminal Organizations Became the Internet's Most Efficient Enterprise"). Populate both fields in the Book Bible header.

IMPORTANT FORMATTING RULES:
- NO horizontal rules (`---`) anywhere in output — these break docx conversion for Kindle Create.
- Use section headers (##, ###) instead of separators to divide content.
- Italics only for emphasis where genuinely needed; do not use for chapter titles or decorative purposes.

Save output to books/{book_name}/planning/.""",
)[task_id]

t2 = kanban_create(
    title="Phase 2: Drafting - Serial Chapter Generation & Self-Review",
    assignee="booksmith-author",
    body=f"""Draft all chapters serially from prompts in books/{book_name}/planning/chapter_prompts/. For each chapter: read the prompt + book bible, draft the chapter, self-review against templates/self_review_template.md. Save drafts to books/{book_name}/chapters/.

COMPREHENSIVE OUTPUT FORMATTING RULES (apply to ALL chapters and logues):
- ONLY `# Chapter N: Title` as headings — NO `##`, `###`, or any subheadings within chapter text. Subheadings bloat the Kindle TOC and break clean reading flow.
- NO horizontal rules (`---`) anywhere in output — these break docx conversion for Kindle Create. Use blank lines between paragraphs/sections only.
- NO italic subtitle line after the chapter title. The `# Chapter N: Title` is sufficient; do not add `*Subtitle text*` beneath it.
- Cross-chapter references: maximum ONE per chapter, and only when genuinely necessary. Do NOT write "Chapter 4 explains..." or "As discussed in Chapter X" repeatedly. If a concept naturally connects to another chapter, weave the connection into the prose without explicit chapter-number calls.
- Bold/italics in body prose: use SPARINGLY. Italics for genuine emphasis only (one per page at most). No bold text in body prose — it reads as shouting.
- No citation markers like [1], [Author Year], etc. The Book Bible's 'No Hallucination' rule means facts come from reports without attribution notation in the text.

The final output should read like a professionally published non-fiction book: clean headings (h1 only), persistent flowing prose, minimal formatting decoration.

If any chapter is flagged as 'needs_review', compile a summary and block this task with the issues using kanban_block(). Wait for user feedback via /unblock before proceeding.""",
    parents=[t1],
)[task_id]

t3 = kanban_create(
    title="Phase 3: Manuscript Review - Full Text Analysis",
    assignee="booksmith-author",
    body=f"""Review the complete manuscript in books/{book_name}/chapters/. Check for pacing, cross-chapter continuity, and redundancy. Save notes to books/{book_name}/review/manuscript_review.md.

IMPORTANT: During review, flag any formatting issues that must be cleaned before final assembly: horizontal rules (`---`), subheadings (`##`, `###`) within chapter text, italic subtitle lines after chapter titles, excessive cross-chapter references ("Chapter X explains..."), and overuse of bold/italics in body prose. Note these for Phase 5 cleanup.""",
    parents=[t2],
)[task_id]

t4 = kanban_create(
    title="Phase 4: Logues Writing - Foreword, Intro, Epilogue, Glossary",
    assignee="booksmith-author",
    body=f"""Write supplementary material based on the manuscript and book bible. Check config.yaml for which logues are enabled (logues_included). Write each enabled logue type and save to books/{book_name}/logues/.

COMPREHENSIVE OUTPUT FORMATTING RULES (apply to ALL logues):
- NO horizontal rules (`---`) anywhere — these break docx conversion for Kindle Create. Use blank lines between paragraphs/sections only.
- NO subheadings (`##`, `###`) within logue text — keep clean flowing prose with only the top-level heading.
- NO italic subtitle line after the title. The `# Title` is sufficient.
- Italics only for genuine emphasis; do not use for titles or decorative purposes.
- No citation markers like [1], [Author Year], etc.

Logues should be written in this reading order (even though they may be assembled alphabetically later): Foreword → Introduction → Prologue.""",
    parents=[t3],
)[task_id]

t5 = kanban_create(
    title="Phase 5: Finalizing - Stitch & Assemble Manuscript",
    assignee="default",
    body=f"""Assemble all logues and chapters into a final manuscript in this EXACT reading order:
1. Title Page (markdown heading with book title)
2. Copyright Notice
3. Foreword (if enabled in config.yaml)
4. Introduction (if enabled)
5. Prologue (if enabled)
6. Chapters 1 through N (numerical order, files named chapter_XX_*)
7. Epilogue (if enabled)

CRITICAL: Do NOT assemble logues alphabetically — alphabetical sorting puts 'Epilogue' before 'Foreword' and 'Introduction'. Use the explicit reading order above.

CLEANUP BEFORE ASSEMBLY (mandatory):
- Remove ALL horizontal rules (`---`) from every file. These break docx conversion for Kindle Create. Replace with no separator or a blank line between sections only.
- Remove ALL subheadings (`##`, `###`) within chapter text and logues — keep ONLY the top-level `# Chapter N: Title` heading per chapter. Subheadings bloat the Kindle TOC.
- Remove any italic subtitle lines that appear directly after chapter titles (e.g., `*How Crime Became a Platform*`). The `# Chapter N: Title` is sufficient.
- Ensure consistent spacing: exactly one blank line between sections, no double or triple blank lines.

Add Title Page and Copyright Notice at the top. Save to books/{book_name}/manuscript/final_manuscript.md. Commit and push to remote.""",
    parents=[t4],
)[task_id]
```

10. **Report Back:** Tell the user: "All 5 phases queued on Kanban board. Dispatcher will execute sequentially — you'll see progress as each task moves from ready → done."

### Phase Execution Notes (Dispatcher Handles This)

The dispatcher manages execution automatically via parent-child links. No manual intervention needed between phases unless human review is triggered.

**Phase 2 Review Gate:** If the drafting task blocks itself with flagged chapters, it calls `kanban_block()` with a summary of issues. The user provides feedback via `/unblock <task_id>`. The worker resumes and revises based on feedback.

## Templates Reference

All templates are located in `templates/` (project root):
*   `book_bible_template.md` — includes mandatory Report Mapping table; no `---` separators
*   `chapter_prompt_template.md`
*   `self_review_template.md`
*   `manuscript_review_template.md`
*   `logues_template.md`

## Test Runs

Before committing to frontier model costs (~$55-70/book), validate the pipeline with local models and shorter reports. See `references/test-run-strategy.md`.

For known pitfalls discovered during test runs (separator issues, assembly order, report mapping), see `references/test-run-pitfalls.md`.

## Kanban Reference

For detailed task graph structure, review gate patterns, and pitfall avoidance, see `references/kanban-patterns.md`.

## Error Handling

*   **Git Failures:** If push fails, check if the remote is configured correctly.
*   **Missing Reports:** Verify 5 markdown files in reports/ before creating Kanban tasks.
*   **Profile Errors:** If a task fails, check the gateway is running for that profile and retry with clearer instructions.
*   **Kanban Task Stuck:** If a task stays in `todo` too long, verify parent completed successfully and gateway is active. Use `hermes kanban show <task_id>` to inspect.
*   **Unknown Assignee:** The dispatcher silently drops tasks assigned to non-existent profiles. Always assign to `booksmith-planner`, `booksmith-author`, or `default`.
