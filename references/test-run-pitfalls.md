# Test Run Pitfalls — Lessons from First Production Run

## What Went Wrong (raas-book test run)

### 1. Horizontal Rules (`---`) Break Docx Conversion
**Symptom:** ~120 `---` lines across manuscript files. These are markdown horizontal rules used as section separators by the LLM. They break docx conversion for Kindle Create and most publishing pipelines.

**Root cause:** The SKILL.md task bodies didn't explicitly prohibit them. LLMs default to using `---` between sections.

**Fix applied:**
- Phase 2/4 task bodies: "NO horizontal rules (`---`) anywhere — use section headers instead"
- Phase 5 task body: "Before assembling, remove ALL horizontal rules from every file"
- Template files: Removed all `---` separators (book_bible_template.md was the worst offender with 5)

**Pitfall for future:** Always explicitly prohibit `---` in task bodies. LLMs will use them by default.

### 2. Manuscript Assembly Order Was Alphabetical, Not Reading Order
**Symptom:** Epilogue appeared first (line 21 of final_manuscript.md), before Foreword and Introduction. Alphabetical sorting puts 'E' before 'F' and 'I'.

**Root cause:** Phase 5 task body said "assemble all logues" without specifying order. The worker likely used alphabetical file sorting.

**Fix applied:**
- Phase 5 task body now specifies EXPLICIT reading order: Title → Copyright → Foreword → Introduction → Prologue → Chapters (numerical) → Epilogue
- Added explicit warning: "Do NOT assemble logues alphabetically"

**Pitfall for future:** Never rely on alphabetical sorting for document assembly. Always specify the exact sequence.

### 3. Report Numbering Confusion Risk
**Symptom:** Book Bible labeled reports as "Report 1" through "Report 5" with topic descriptions, but no explicit filename mapping. If the model confuses which report covers which topic (e.g., attributing victimology data from Report 5 to Report 1), it will hallucinate.

**Root cause:** No structured crosswalk between report numbers and their actual content/filenames.

**Fix applied:**
- Book Bible template now has a mandatory "Report Mapping" table: Report # → Filename → Source Authorities → Core Topic
- Phase 1 task body explicitly requires this section at the top of the Book Bible

**Pitfall for future:** Always include an explicit report-to-topic mapping in the Book Bible. Don't rely on descriptive text alone — filenames are unambiguous anchors.

### 4. No Git Commits Between Phases
**Symptom:** Intermediate outputs (chapters, logues, planning) sat uncommitted until Phase 5 or manual intervention. Only `.gitkeep` files and final_manuscript.md were committed by the pipeline itself.

**Root cause:** Task bodies didn't include `git add -A && git commit` steps for each phase — only Phase 5 did, and it was too late (only committed what *it* created).

**Fix applied:**
- Phase 1 commits planning output.
- Phase 2 commits chapters and self-review notes.
- Phase 3 commits manuscript review notes.
- Phase 4 commits logues.
- Phase 5 commits and pushes final manuscript.

### 5. No Telegram Notification on Pipeline Completion
**Symptom:** When Phase 5 completed, there was no mechanism to notify the user. The Kanban dispatcher runs tasks in isolated sessions with no callback to the orchestrator.

**Root cause:** SKILL.md didn't include a post-completion notification step.

**Fix applied:** Phase 5 now instructs the worker to send a Telegram completion notification after a successful push, including book name, final manuscript path, approximate word count, latest commit hash, and warnings/skipped logues.

## What Worked Well
- Kanban parent-child linking works perfectly for sequential execution
- Dispatcher auto-promotion is reliable
- Sonnet 4.6 produces acceptable quality for test runs (cost savings confirmed)
- Book Bible generation is comprehensive and well-structured
- Chapter drafting follows prompts faithfully
- Self-review catches formatting issues before they compound

## Pre-Production Checklist
Before running with frontier models:
1. Verify SKILL.md task bodies include "NO `---`" rules for all output phases
2. Verify Phase 5 assembly order is explicit reading order, not alphabetical, and includes Glossary after Epilogue
3. Verify Book Bible template has Report Mapping table
4. Verify Phase 0 performs production preflight validation of the 5 reports
5. Verify Phase 0 refuses to overwrite an existing non-empty book directory without explicit user approval
6. Verify each phase commits its own output
7. Verify Phase 5 sends a Telegram completion notification after successful push
