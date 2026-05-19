# Production Preflight Checklist

Use this checklist before queueing a new production Booksmith run.

## 1. Repository state

```bash
cd /home/emkay/projects/booksmith
git status --short --branch
git fetch origin
git status --short --branch
```

Required state:

- Working tree clean before staging a new book.
- Branch is the intended production branch, normally `main`.
- No unpushed pipeline/tooling changes unless intentionally included before the run.

## 2. Profile state

```bash
hermes profile list
booksmith-creator gateway status
booksmith-reviewer gateway status
```

Required profiles:

- `booksmith-creator`: Phase 1 planning, Phase 2 drafting/self-review, Phase 4 logues.
- `booksmith-reviewer`: Phase 3 manuscript review.
- `default`: Phase 5 final assembly.

Start only the gateways needed for the run:

```bash
booksmith-creator gateway start
booksmith-reviewer gateway start
```

## 3. Skill symlinks

Profile-local Booksmith skills must be symlinks to the canonical skill:

```bash
ls -ld ~/.hermes/profiles/booksmith-creator/skills/booksmith
ls -ld ~/.hermes/profiles/booksmith-reviewer/skills/booksmith
```

Expected target:

```text
~/.hermes/skills/booksmith
```

Do not maintain independent profile-local copies unless intentionally debugging.

## 4. Book directory safety

Before creating a new book slug, verify it does not already contain work:

```bash
find books/<book-name> -maxdepth 3 -type f ! -name .gitkeep 2>/dev/null
```

If any file exists, stop and choose a new slug or explicitly approve reuse. Never overwrite reports, planning files, chapters, reviews, logues, or manuscripts silently.

## 5. Source report validation

Before queueing Kanban tasks, verify `books/<book-name>/reports/` contains exactly five usable markdown files:

```bash
find books/<book-name>/reports -maxdepth 1 -type f -name '*.md' ! -name '.gitkeep' -print
```

Checks:

- Exactly 5 markdown files.
- No empty files.
- No duplicate files by checksum.
- Each report has a title or top-level heading.
- Each report has meaningful length.
- Filenames are stable enough to be used in Book Bible report mapping and per-chapter Required Source Files.

## 6. Commit and push source inputs before queueing

After validation, make the exact corpus durable before any worker starts:

```bash
git add books/<book-name>/reports
git commit -m "Add source reports for <book-name>"
git push origin main
```

If commit or push fails, stop and fix Git/auth/remotes before queueing the pipeline.

## 7. Kanban board cleanup

Archive previous Booksmith tasks before creating a new run:

```bash
hermes kanban --board booksmith list --json | python3 -c "import sys,json; [print(t['id']) for t in json.load(sys.stdin)]"
hermes kanban --board booksmith archive <task_ids...>
```

Archive blocked and todo tasks too, not only completed tasks.

## 8. Workspace rule

Production Kanban tasks should run in the actual repo workspace, not scratch directories:

```text
--workspace dir:/home/emkay/projects/booksmith --skill booksmith
```

This keeps file writes and phase commits in the intended monorepo.

## 9. Expected assignees

- Phase 1 Planning: `booksmith-creator`
- Phase 2 Drafting: `booksmith-creator`
- Phase 3 Manuscript Review: `booksmith-reviewer`
- Phase 4 Logues: `booksmith-creator`
- Phase 5 Finalizing: `default`

Unknown profile assignees can be silently dropped by the dispatcher, so verify assignees before unblocking production work.
