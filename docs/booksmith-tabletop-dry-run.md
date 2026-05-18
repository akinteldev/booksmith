# Booksmith Tabletop Dry Run

This is a text-only walkthrough of a normal Booksmith run. It describes what the user does, what Hermes does, and what the model does at each stage.

## Scenario

You want to create a new book called:

```text
The Ransomware Factory
```

You already have five finished research reports from the research repo.

## Timeline

### T-0 — You start the run

**You do:**

Send Hermes a message:

```text
Run booksmith for "The Ransomware Factory"
```

**Hermes does:**

- Parses the book name.
- Creates a normalized slug:

```text
the-ransomware-factory
```

- Checks whether this folder already exists:

```text
books/the-ransomware-factory/
```

**Model does:**

Nothing major yet. Hermes is mostly doing setup and safety checks.

### T+1 min — Hermes creates the book structure

**Hermes does:**

Creates:

```text
books/the-ransomware-factory/
├── reports/
├── planning/
├── chapters/
├── review/
├── logues/
└── manuscript/
```

Commits the empty structure to Git.

**Hermes tells you:**

```text
Booksmith Setup Complete.
Directory created at books/the-ransomware-factory/reports/.
Drop your 5 production research reports there and reply "ready" when done.
```

**You do:**

Copy the five research reports into:

```text
books/the-ransomware-factory/reports/
```

Then reply:

```text
ready
```

**Model does:**

Still nothing substantial. This is mostly file orchestration.

### T+5 min — Hermes validates the reports

**Hermes does:**

Checks that:

- exactly 5 markdown reports exist
- none are empty
- none are duplicates
- each has a title or top-level heading
- each has meaningful length

If something is wrong, Hermes stops and tells you exactly what to fix.

Example failure:

```text
Validation failed: found 4 markdown reports, expected 5.
```

If all good, Hermes continues.

**You do:**

Nothing unless validation fails.

**Model does:**

No drafting yet. Hermes is protecting the pipeline from bad input.

### T+6 min — Hermes queues the pipeline

**Hermes does:**

Archives old Booksmith Kanban tasks.

Creates five linked tasks:

```text
Phase 1: Planning
  ↓
Phase 2: Drafting + Self-Review
  ↓
Phase 3: Manuscript Review
  ↓
Phase 4: Logues Writing
  ↓
Phase 5: Final Assembly
```

Each task has a parent-child dependency, so only one phase runs after the previous one completes.

**You do:**

Nothing.

**Model does:**

Still waiting. The dispatcher will call the right model profile when each task becomes ready.

## Phase 1 — Planning

### T+10 min — Planning task starts

**Hermes does:**

Assigns Phase 1 to:

```text
booksmith-planner
```

Passes it:

- the five reports
- the Book Bible template
- the chapter prompt template
- the formatting rules
- the requirement to create a report mapping
- the requirement to assign exact Required Source Files per chapter

**Planner model does:**

Reads all five reports and creates:

```text
books/the-ransomware-factory/planning/book_bible.md
```

Also creates chapter prompts, for example:

```text
books/the-ransomware-factory/planning/chapter_01_the_business.md
books/the-ransomware-factory/planning/chapter_02_the_affiliate.md
books/the-ransomware-factory/planning/chapter_03_the_broker.md
```

Each chapter prompt includes exact repo-relative source paths for that chapter, for example:

```text
Required Source Files:
- books/the-ransomware-factory/reports/report_1_ransomware_economics.md
- books/the-ransomware-factory/reports/report_3_affiliate_operations.md
```

The Book Bible includes:

- title
- subtitle
- thesis
- voice
- structure
- chapter list
- source/report mapping
- per-chapter Required Source Files
- continuity rules

**Hermes does after model finishes:**

Commits Phase 1 output:

```text
Phase 1: Plan the-ransomware-factory
```

Marks Phase 1 done.

**You do:**

Nothing unless the task fails.

## Phase 2 — Drafting

### T+1–2 hours — Drafting starts

**Hermes does:**

Assigns Phase 2 to:

```text
booksmith-author
```

Passes it:

- Book Bible
- all chapter prompts
- self-review template
- formatting rules

**Author model does:**

Works serially.

For each chapter:

1. Reads the Book Bible.
2. Reads the chapter prompt.
3. Extracts the Required Source Files list.
4. Reads only those exact report files unless the Book Bible or prompt explicitly requires another report.
5. Drafts the chapter.
6. Saves a source-use sidecar note listing files read and main facts used.
7. Self-reviews it, including the source-routing checklist.
8. Revises once automatically.
9. Saves the final chapter.

Example output:

```text
books/the-ransomware-factory/chapters/chapter_01_the_business.md
books/the-ransomware-factory/chapters/chapter_01_the_business.sources.md
books/the-ransomware-factory/chapters/chapter_01_the_business.self_review.md
books/the-ransomware-factory/chapters/chapter_02_the_affiliate.md
books/the-ransomware-factory/chapters/chapter_03_the_broker.md
```

**Hermes does:**

Tracks the task state.

If all chapters pass self-review, Hermes commits:

```text
Phase 2: Draft chapters for the-ransomware-factory
```

Then marks Phase 2 done.

### Optional branch — review gate

If the model finds serious unresolved issues:

**Author model does:**

Blocks the Kanban task and writes something like:

```text
Blocked: Chapter 5 has unresolved contradiction between Report 2 and Report 4 about affiliate revenue share.
Need user guidance before continuing.
```

**Hermes does:**

Stops Phase 2 at the review gate.

**You do:**

Reply with guidance, for example:

```text
Use Report 4 as the newer source. Mention that earlier estimates were lower.
```

Then unblock the task.

**Author model does:**

Resumes, revises the affected material, and continues.

## Phase 3 — Manuscript review

### T+3–4 hours — Full manuscript review starts

**Hermes does:**

Assigns Phase 3 to:

```text
booksmith-author
```

Passes it the drafted chapters.

**Author model does:**

Reads the full manuscript and checks:

- pacing
- repetition
- continuity
- chapter-to-chapter flow
- formatting issues
- excessive cross-references
- missing connective tissue

Creates:

```text
books/the-ransomware-factory/review/manuscript_review.md
```

**Hermes does:**

Commits:

```text
Phase 3: Review manuscript for the-ransomware-factory
```

Marks Phase 3 done.

**You do:**

Usually nothing.

## Phase 4 — Logues

### T+4–5 hours — Front/back matter starts

**Hermes does:**

Assigns Phase 4 to:

```text
booksmith-author
```

Passes it:

- Book Bible
- manuscript
- logues template
- enabled logues config

**Author model does:**

Writes enabled logues in reading order:

```text
Foreword
Introduction
Prologue
Epilogue
Glossary
```

Example files:

```text
books/the-ransomware-factory/logues/foreword.md
books/the-ransomware-factory/logues/introduction.md
books/the-ransomware-factory/logues/prologue.md
books/the-ransomware-factory/logues/epilogue.md
books/the-ransomware-factory/logues/glossary.md
```

Expected behavior:

- Foreword explains the research basis briefly.
- Introduction introduces the conceptual cast.
- Prologue opens with a scene.
- Epilogue closes the arc.
- Glossary defines key terms.

**Hermes does:**

Commits:

```text
Phase 4: Write logues for the-ransomware-factory
```

Marks Phase 4 done.

**You do:**

Nothing unless you want to inspect the logues manually.

## Phase 5 — Final assembly

### T+5–6 hours — Final manuscript assembly starts

**Hermes does:**

Assigns Phase 5 to the default/finalizing worker.

**Model or worker does:**

Assembles the book in exact reading order:

```text
1. Title Page
2. Copyright Notice
3. Foreword
4. Introduction
5. Prologue
6. Chapters 1-N
7. Epilogue
8. Glossary
```

Cleans formatting:

- removes horizontal rules
- removes unwanted subheadings
- removes italic subtitle lines
- normalizes spacing

Creates:

```text
books/the-ransomware-factory/manuscript/final_manuscript.md
```

**Hermes does:**

Commits and pushes:

```text
Phase 5: Assemble final manuscript for the-ransomware-factory
```

Then sends you a completion message.

## Final message you receive

Example:

```text
Booksmith complete.

Book: the-ransomware-factory
Final manuscript:
books/the-ransomware-factory/manuscript/final_manuscript.md

Approximate word count: 72,400
Latest commit: abc1234
Pushed to GitHub: yes

Warnings:
- No unresolved review blocks.
- Glossary assembled after Epilogue.
- Formatting cleanup completed.
```

## Division of labor

**You:**

- Start the run.
- Provide the five research reports.
- Reply `ready`.
- Intervene only if Hermes asks for guidance at a review gate.
- Read the final manuscript.

**Hermes:**

- Creates folders.
- Validates inputs.
- Queues Kanban tasks.
- Assigns work to the right profiles.
- Tracks phase dependencies.
- Commits each phase.
- Pushes final output.
- Notifies you.

**Model:**

- Reads reports.
- Creates Book Bible.
- Creates chapter prompts with Required Source Files.
- Drafts chapters.
- Saves source-use notes.
- Self-reviews and revises.
- Reviews manuscript.
- Writes logues.
- Helps assemble polished final text.
