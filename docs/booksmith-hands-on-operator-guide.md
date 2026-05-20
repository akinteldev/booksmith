# Booksmith Hands-On Operator Guide

This guide is the operator checklist for running Booksmith without losing control of the process. The pipeline automates execution; you still control the gates, cost visibility, source routing, and intervention decisions.

Use this guide during real production runs.

## Control Model

Booksmith has these human control points:

1. **Input gate** — you place the five reports and reply `ready`.
2. **Planning approval gate** — mandatory. Phase 1 blocks after creating the Book Bible and chapter prompts. Drafting cannot start until you approve or provide corrections with `/unblock <task_id>`.
3. **Chapter issue gate** — conditional. Phase 2 drafts all chapters serially. It only blocks if self-review finds critical unresolved issues after one automatic revision pass.
4. **Manuscript structure gate** — conditional. Phase 3 blocks before logues if review finds major chapter/body issues that would make the framing stale or misleading.
5. **Final inspection** — after final assembly and push, inspect the final manuscript before publication/export.

There is intentionally **no first-chapter/sample review gate**. After planning approval, Booksmith drafts all chapters serially unless a critical issue is detected.

## Before You Start

Open these before invoking the workflow:

- Telegram chat with Hermes.
- Claude usage dashboard: `https://platform.claude.com/usage`.
- Kanban board status terminal.
- Booksmith repo terminal:

```bash
cd /home/akay/projects/booksmith
git status --short --branch
```

Start gateways if needed:

```bash
booksmith-creator gateway start
booksmith-reviewer gateway start
```

Check the Kanban board is not carrying stale active tasks:

```bash
hermes kanban --board booksmith list --json
```

## Invoking the Workflow

From Telegram, send:

```text
Run booksmith for "The Ransomware Factory"
```

Hermes normalizes the title into a slug such as:

```text
the-ransomware-factory
```

Phase 0 creates:

```text
books/the-ransomware-factory/
├── reports/
├── planning/
├── chapters/
├── review/
├── logues/
└── manuscript/
```

Hermes then asks you to place the five research reports in:

```text
books/the-ransomware-factory/reports/
```

After copying the five markdown files, reply in Telegram:

```text
ready
```

Phase 0 validates the reports, archives stale board tasks, and queues the linked phase tasks.

## Monitoring While Running

Monitor three surfaces at the same time: Claude usage, Kanban, and files/Git.

### 1. Claude Platform Usage

Open:

```text
https://platform.claude.com/usage
```

Watch for:

- which model is consuming tokens
- request count growth
- unusually large spikes during a single phase
- continued token usage while the Kanban board appears blocked or idle
- Opus activity before drafting/logues should begin
- planning activity after Phase 1 should already be blocked for approval

Expected pattern:

- Phase 1 planning: `booksmith-creator`, normally Opus/frontier model.
- Phase 2 drafting: `booksmith-creator`, normally Opus/frontier model.
- Phase 3 review: `booksmith-reviewer`, normally Sonnet/strong reviewer model.
- Phase 4 logues: `booksmith-creator`.
- Phase 5 finalizing: default worker, mostly assembly/cleanup.

Warning signs:

- drafting tokens start before you approved planning
- token usage continues after you stopped both gateways
- a phase repeats many times without new commits/files
- model usage does not match the configured profile
- one chapter creates a much larger spike than the others

If token usage looks wrong, pause first and inspect second:

```bash
booksmith-creator gateway stop
booksmith-reviewer gateway stop
```

### 2. Kanban Board

View board status:

```bash
hermes kanban --board booksmith list --json
```

Inspect a specific task:

```bash
hermes kanban show <task_id>
```

Expected flow:

```text
Phase 1 Planning → blocked for planning approval
/unblock after approval
Phase 2 Drafting → runs serially
Phase 3 Manuscript Review
Phase 4 Logues
Phase 5 Finalizing
```

Watch for:

- Phase 2 should not become active before Phase 1 is approved and completed.
- Only the expected phase should be active.
- A blocked task should explain exactly what it needs.
- A task stuck in `todo` may be waiting on a parent.
- A task stuck in `ready` may mean the gateway is not running.
- Wrong assignees can silently prevent execution.

Known valid assignees:

```text
booksmith-creator
booksmith-reviewer
default
```

### 3. Files and Git

Check recent commits:

```bash
git log --oneline -5
```

Check working tree:

```bash
git status --short --branch
```

Check generated files:

```bash
find books/<book-name> -maxdepth 3 -type f | sort
```

Expected phase outputs:

- Phase 1:
  - `books/<book-name>/planning/book_bible.md`
  - `books/<book-name>/planning/chapter_prompts/`
- Phase 2:
  - chapter drafts in `books/<book-name>/chapters/`
  - source-use sidecars, e.g. `chapter_01_*.sources.md`
  - self-review notes, e.g. `chapter_01_*.self_review.md`
- Phase 3:
  - `books/<book-name>/review/manuscript_review.md`
  - blocks before Phase 4 if the chapter body is not structurally sound enough for logues
- Phase 4:
  - enabled logues in `books/<book-name>/logues/`
- Phase 5:
  - `books/<book-name>/manuscript/final_manuscript.md`

## Mandatory Planning Approval Gate

After Phase 1, Booksmith blocks before drafting.

Review:

```text
books/<book-name>/planning/book_bible.md
books/<book-name>/planning/chapter_prompts/
```

Checklist:

- title and subtitle fit the book
- thesis is clear and non-generic
- chapter sequence has a strong arc
- chapter count and scope are appropriate
- Report Mapping correctly identifies all five reports
- each chapter has sensible Required Source Files
- no chapter is under-sourced
- no chapter defaults to all five reports unless justified
- voice matches the veteran investigative journalist style
- structure is publishable before expensive drafting starts

Approve with:

```text
/unblock <planning_task_id> approved
```

Request corrections with concise direction, then unblock:

```text
Chapter 4 and Chapter 5 are too similar. Merge the infrastructure material into Chapter 4 and make Chapter 5 focus on monetization. Keep source routing narrow.
/unblock <planning_task_id>
```

The creator should apply corrections, commit them, then complete Phase 1. Only then should Phase 2 begin.

## Monitoring Drift

Drift means the process is still running, but not following the intended operating envelope.

### Planning Drift

Signs:

- generic book thesis
- too many chapters with identical source files
- all chapters use all reports by default
- weak Report Mapping
- title/subtitle do not match source material
- chapter sequence reads like a report outline instead of a book arc

Intervention:

- Do not approve planning.
- Provide concise corrections at the planning gate.
- Unblock only after giving the correction instruction.

### Drafting Drift

Signs:

- chapters ignore Required Source Files
- missing `.sources.md` sidecars
- self-review files missing
- repeated explicit chapter-number cross-references
- formatting violations: `##`, `###`, horizontal rules, italic subtitle lines
- tone becomes hype-driven, melodramatic, or detached analyst prose
- chapter files appear in the wrong book directory

Intervention:

- Stop the creator gateway.
- Inspect the active task and latest files.
- Decide whether to resume, correct via task feedback, or revert.

```bash
booksmith-creator gateway stop
hermes kanban --board booksmith list --json
hermes kanban show <task_id>
git status --short --branch
git log --oneline -5
```

### Cost Drift

Signs:

- unexpected Opus usage during planning
- high token use before Phase 2
- tokens continue while task is blocked
- repeated attempts without new output files

Intervention:

```bash
booksmith-creator gateway stop
booksmith-reviewer gateway stop
```

Then inspect:

```bash
hermes kanban show <task_id>
git status --short --branch
find books/<book-name> -maxdepth 3 -type f | sort
```

## Intervention Playbook

### Approve a Blocked Review Gate

Use when output is acceptable.

```text
/unblock <task_id> approved
```

### Provide Corrections at a Blocked Gate

Use when the task blocked correctly, but needs direction.

```text
Keep the current title, but revise the chapter sequence so infrastructure comes before monetization. Preserve the Required Source Files mapping and avoid assigning all reports to every chapter.
/unblock <task_id>
```

### Pause the Pipeline

Use when cost, model choice, source routing, or output direction looks wrong.

```bash
booksmith-creator gateway stop
booksmith-reviewer gateway stop
```

Resume:

```bash
booksmith-creator gateway start
booksmith-reviewer gateway start
```

### Inspect a Task

```bash
hermes kanban show <task_id>
```

Look for:

- status
- assignee
- parent dependencies
- block reason
- current task body
- whether the task instructions match the intended phase

### Reclaim a Stuck Task

Use only if a worker crashed or left a task claimed but inactive.

```bash
hermes kanban reclaim <task_id>
```

### Archive a Bad Task

Use when the task itself is wrong and should not continue.

```bash
hermes kanban --board booksmith archive <task_id>
```

Then recreate or rerun the phase with corrected instructions.

### Revert a Bad Commit

Prefer revert over destructive reset after pushing.

```bash
git log --oneline
git revert <commit_hash>
git push origin main
```

Use when:

- a phase committed bad output
- wrong book directory was modified
- planning/drafting output should be explicitly undone

## Review Stops

### Existing Stops

- **Phase 0 input stop:** waits for reports and `ready`.
- **Phase 1 planning approval gate:** mandatory; blocks before drafting.
- **Phase 2 chapter issue gate:** conditional; only if critical issues remain after self-review and one automatic revision.
- **Final completion notice:** review final manuscript after assembly and push.

### Non-Stops by Design

These are intentionally not human gates:

- no first-chapter sample approval gate
- no per-chapter routine approval gate
- no manual intervention between chapters unless the model finds unresolved critical issues

Reason: after you approve the plan, the pipeline should draft all chapters serially without routine interruption.

## Emergency Stop

If the process appears out of control:

1. Stop gateways:

```bash
booksmith-creator gateway stop
booksmith-reviewer gateway stop
```

2. Check active tasks:

```bash
hermes kanban --board booksmith list --json
```

3. Inspect the active task:

```bash
hermes kanban show <task_id>
```

4. Check files and commits:

```bash
cd /home/akay/projects/booksmith
git status --short --branch
git log --oneline -5
find books/<book-name> -maxdepth 3 -type f | sort
```

5. Decide:

- resume gateways if behavior is correct
- provide corrections if blocked
- reclaim if stuck
- archive/recreate if task instructions are wrong
- revert if bad committed output must be undone

## Operator Principle

Do not let automation substitute for editorial control.

The correct control point is early: approve the plan, source routing, and book arc before drafting begins. After that, let the system draft serially, monitor for drift, and intervene only when the process violates the approved plan or self-review finds critical unresolved issues.
