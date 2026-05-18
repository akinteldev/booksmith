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
3.  **Do Not Overwrite Existing Work:** If `books/<book-name>/` already exists and contains any non-`.gitkeep` files, STOP and ask the user to choose a new book slug or explicitly approve reuse. Never overwrite existing reports, planning files, chapters, logues, reviews, or manuscripts silently.
4.  **Create Structure:** If not, create the full directory tree with `.gitkeep` files:
    ```
    books/<book-name>/
    ├── reports/          ← where research reports go
    ├── planning/         ← Book Bible + Chapter Prompts (Phase 1)
    ├── chapters/         ← Drafted chapters (Phase 2)
    ├── review/           ← Manuscript review notes (Phase 3)
    ├── logues/           ← Foreword, intro, etc. (Phase 4)
    └── manuscript/       ← Final stitched book (Phase 5)
    ```
5.  **Commit Structure:** Run `git add -A && git commit -m "Initialize book directory: <book-name>"`.
6.  **Notify User:** Send a message via Telegram:
    > "**Booksmith Setup Complete**\nDirectory created at `books/<book-name>/reports/`. Drop your 5 production research reports there and reply 'ready' when done."
7.  **Wait for Confirmation:** Pause execution until the user replies confirming they've placed their reports.
8.  **Production Preflight Validation:** Before creating Kanban tasks, validate the reports directory:
    * exactly 5 markdown files (`*.md`), excluding `.gitkeep`
    * no empty files
    * no duplicate files by checksum
    * each report has a detectable title or top-level heading
    * each report has meaningful length (flag suspiciously short reports)
    * filenames and extracted titles are recorded for the Book Bible Report Mapping
    If validation fails, STOP and report the exact issue to the user before proceeding.
9.  **Archive Old Tasks:** Archive ALL existing tasks on the `booksmith` board from previous runs (not just completed ones — blocked and todo tasks also need clearing):
    ```bash
    hermes kanban --board booksmith list --json | python3 -c "import sys,json; [print(t['id']) for t in json.load(sys.stdin)]"
    ```
    Then archive them: `hermes kanban --board booksmith archive <task_ids...>`
10. **Create Kanban Tasks:** Create all pipeline tasks with parent-child linking (capture each task ID and pass it as a parent to the next):

```python
t1 = kanban_create(
    title="Phase 1: Planning - Generate Book Bible & Prompts",
    assignee="booksmith-planner",
    body=f"""Analyze the five research reports in books/{book_name}/reports/. Generate a comprehensive Book Bible and individual Chapter Prompts following templates/book_bible_template.md and templates/chapter_prompt_template.md.

CRITICAL: At the top of the Book Bible, include an explicit 'Report Mapping' section that lists each report number (1-5) alongside its exact filename, source authorities, and core topic. This crosswalk prevents confusion in later phases about which report covers what subject matter.

For every chapter in the Book Bible's Chapter Sequence & Arc and in every chapter prompt, include exact repo-relative Required Source Files for that chapter (for example: `books/{book_name}/reports/<exact_filename>.md`). Do not list all five reports by default. Select only the reports directly needed for that chapter, while preserving enough source grounding for high-quality drafting.

Derive both a **Title** and a **Subtitle** for the book from the reports. The title should be punchy and memorable; the subtitle should clarify the book's scope (e.g., "How Cybercriminal Organizations Became the Internet's Most Efficient Enterprise"). Populate both fields in the Book Bible header.

IMPORTANT FORMATTING RULES:
- NO horizontal rules (`---`) anywhere in output — these break docx conversion for Kindle Create.
- Use section headers (##, ###) instead of separators to divide content.
- Italics only for emphasis where genuinely needed; do not use for chapter titles or decorative purposes.

Save output to books/{book_name}/planning/.

After saving, commit this phase output:
`git add books/{book_name}/planning && git commit -m "Phase 1: Plan {book_name}"`""",
)[task_id]

t2 = kanban_create(
    title="Phase 2: Drafting - Serial Chapter Generation & Self-Review",
    assignee="booksmith-author",
    body=f"""Draft all chapters serially from prompts in books/{book_name}/planning/chapter_prompts/. For each chapter: read the prompt + book bible, extract the Required Source Files list from the chapter prompt, read those exact report files before drafting, draft the chapter, save a brief source-use sidecar note listing files read and main facts used, self-review against templates/self_review_template.md, then automatically revise once to fix all issues found by the self-review before moving to the next chapter. Save drafts, source-use notes, and self-review notes to books/{book_name}/chapters/.

Do not use unrelated reports for a chapter unless the Book Bible or chapter prompt explicitly requires them. The source-use sidecar should make routing auditable by listing the exact files read and the main facts used from each file.

COMPREHENSIVE OUTPUT FORMATTING RULES (apply to ALL chapters and logues):
- ONLY `# Chapter N: Title` as headings — NO `##`, `###`, or any subheadings within chapter text. Subheadings bloat the Kindle TOC and break clean reading flow.
- NO horizontal rules (`---`) anywhere in output — these break docx conversion for Kindle Create. Use blank lines between paragraphs/sections only.
- NO italic subtitle line after the chapter title. The `# Chapter N: Title` is sufficient; do not add `*Subtitle text*` beneath it.
- Cross-chapter references: maximum ONE per chapter, and only when genuinely necessary. Do NOT write "Chapter 4 explains..." or "As discussed in Chapter X" repeatedly. If a concept naturally connects to another chapter, weave the connection into the prose without explicit chapter-number calls.
- Bold/italics in body prose: use SPARINGLY. Italics for genuine emphasis only (one per page at most). No bold text in body prose — it reads as shouting.
- No citation markers like [1], [Author Year], etc. The Book Bible's 'No Hallucination' rule means facts come from reports without attribution notation in the text.

The final output should read like a professionally published non-fiction book: clean headings (h1 only), persistent flowing prose, minimal formatting decoration.

If any chapter still has critical or unresolved issues after the automatic revision pass, compile a summary and block this task with the issues using kanban_block(). Wait for user feedback via /unblock before proceeding.

After all chapters pass self-review, commit this phase output:
`git add books/{book_name}/chapters && git commit -m "Phase 2: Draft chapters for {book_name}"`""",
    parents=[t1],
)[task_id]

t3 = kanban_create(
    title="Phase 3: Manuscript Review - Full Text Analysis",
    assignee="booksmith-author",
    body=f"""Review the complete manuscript in books/{book_name}/chapters/. Check for pacing, cross-chapter continuity, and redundancy. Save notes to books/{book_name}/review/manuscript_review.md.

IMPORTANT: During review, flag any formatting issues that must be cleaned before final assembly: horizontal rules (`---`), subheadings (`##`, `###`) within chapter text, italic subtitle lines after chapter titles, excessive cross-chapter references ("Chapter X explains..."), and overuse of bold/italics in body prose. Note these for Phase 5 cleanup.

After saving the manuscript review, commit this phase output:
`git add books/{book_name}/review && git commit -m "Phase 3: Review manuscript for {book_name}"`""",
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

Logues should be written in this reading order: Foreword → Introduction → Prologue → Epilogue → Glossary. Glossary is back matter and must be assembled after the Epilogue.

After saving logues, commit this phase output:
`git add books/{book_name}/logues && git commit -m "Phase 4: Write logues for {book_name}"`""",
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
8. Glossary (if enabled)

CRITICAL: Do NOT assemble logues alphabetically — alphabetical sorting puts 'Epilogue' before 'Foreword' and 'Introduction'. Use the explicit reading order above.

CLEANUP BEFORE ASSEMBLY (mandatory):
- Remove ALL horizontal rules (`---`) from every file. These break docx conversion for Kindle Create. Replace with no separator or a blank line between sections only.
- Remove ALL subheadings (`##`, `###`) within chapter text and logues — keep ONLY the top-level `# Chapter N: Title` heading per chapter. Subheadings bloat the Kindle TOC.
- Remove any italic subtitle lines that appear directly after chapter titles (e.g., `*How Crime Became a Platform*`). The `# Chapter N: Title` is sufficient.
- Ensure consistent spacing: exactly one blank line between sections, no double or triple blank lines.

Add Title Page and Copyright Notice at the top. Save to books/{book_name}/manuscript/final_manuscript.md.

Commit and push the final manuscript:
`git add books/{book_name}/chapters books/{book_name}/logues books/{book_name}/manuscript && git commit -m "Phase 5: Assemble final manuscript for {book_name}" && git push origin main`

After push succeeds, send a Telegram completion notification to the user containing: book name, final manuscript path, approximate word count, latest commit hash, and any cleanup warnings or skipped optional logues.""",
    parents=[t4],
)[task_id]
```

11. **Report Back:** Tell the user: "All 5 phases queued on Kanban board. Dispatcher will execute sequentially — you'll see progress as each task moves from ready → done."

### Phase Execution Notes (Dispatcher Handles This)

The dispatcher manages execution automatically via parent-child links. No manual intervention needed between phases unless human review is triggered.

**Phase 2 Review Gate:** Phase 2 must self-review each chapter and perform one automatic revision pass for all fixable issues. Only if critical or unresolved issues remain after that revision should it call `kanban_block()` with a concise issue summary. The user provides feedback via `/unblock <task_id>`, then the worker resumes and revises based on that feedback.

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
*   **Missing/Invalid Reports:** Production preflight must find exactly 5 non-empty, non-duplicate markdown reports with detectable headings/titles. If validation fails, stop and ask the user to fix the reports before creating Kanban tasks.
*   **Profile Errors:** If a task fails, check the gateway is running for that profile and retry with clearer instructions.
*   **Kanban Task Stuck:** If a task stays in `todo` too long, verify parent completed successfully and gateway is active. Use `hermes kanban show <task_id>` to inspect.
*   **Unknown Assignee:** The dispatcher silently drops tasks assigned to non-existent profiles. Always assign to `booksmith-planner`, `booksmith-author`, or `default`.
