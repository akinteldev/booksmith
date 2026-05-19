# Booksmith Kanban Patterns

## Task Graph Structure

All 5 phases are created upfront in Phase 0 with strict parent-child linking:

```
T1 (booksmith-creator) → T2 (booksmith-creator) → T3 (booksmith-reviewer) → T4 (booksmith-creator) → T5 (default)
```

Each task's `parents=[previous_task_id]` ensures the dispatcher auto-promotes only when the prior phase completes. No manual coordination needed between phases.

## Phase 0: Task Creation Pattern

Phase 0 captures each returned task ID and passes it as a parent to the next creation call. This is critical — creating all tasks in parallel without linking creates a race window where the dispatcher can claim children before parents exist.

```python
t1 = kanban_create(title="...", assignee="booksmith-creator", body="...")[task_id]
t2 = kanban_create(title="...", assignee="booksmith-creator", body="...", parents=[t1])[task_id]
t3 = kanban_create(title="...", assignee="booksmith-reviewer", body="...", parents=[t2])[task_id]
t4 = kanban_create(title="...", assignee="booksmith-creator", body="...", parents=[t3])[task_id]
t5 = kanban_create(title="...", assignee="default", body="...", parents=[t4])[task_id]
```

## Review Gate Pattern (Phase 2)

The drafting task handles human-in-the-loop internally:
- Worker drafts all chapters, self-reviews each one
- If any chapter is flagged `needs_review`, the worker calls `kanban_block()` with a summary of issues
- User provides feedback via `/unblock <task_id>` in Telegram
- Dispatcher respawns the same task; worker revises based on feedback and continues

This keeps the review gate inside Phase 2 rather than creating a separate Kanban task for it.

## Task Body Design

Task bodies are self-contained instructions — they include:
- The book name (interpolated from Phase 0)
- File paths for inputs/outputs
- Template references
- Quality rules (e.g., "No Hallucination" rule, self-review checklist reference)

The worker profile reads the body as its prompt. No external context injection needed — everything is in the task body itself.

## Old Task Cleanup

Before creating new tasks per book, archive all active tasks from previous runs, including blocked and todo tasks:
```bash
hermes kanban --board booksmith list --json | python3 -c "import sys,json; [print(t['id']) for t in json.load(sys.stdin)]"
hermes kanban --board booksmith archive <task_ids...>
```

The board is reused across books — tasks accumulate unless archived.

## Pitfalls

- **Don't create tasks without parent links** if they're sequential. The dispatcher won't enforce order.
- **Always use `kanban_block()` for human-in-the-loop**, not manual waiting. It persists the block state and integrates with `/unblock`.
- **Task bodies must be self-contained.** Workers don't inherit context from previous tasks — everything needed is in the body text.
- **Assignee profiles must exist** on this machine. The dispatcher silently drops unknown assignees.
