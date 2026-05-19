# Profile Setup Guide

## SOUL.md Design Principle

**SOUL.md must contain identity only.** No planning instructions, review checklists, style-rule dumps, pacing instructions, or metaphor lists. These belong in the Book Bible, templates, and Kanban task prompts.

### Why This Matters

* **User prompts > System prompts:** Style and phase instructions injected via templates/tasks are fresher and more controllable.
* **SOUL = who you are.** The Book Bible/task prompt = what this book/phase needs.
* **One creator identity:** A strong author can plan the book and write it without a separate planner persona.

## Profile: `booksmith-creator`

**Model:** Opus/frontier creative model by default; can be switched via Hermes profile model settings.
**Role:** Investigative non-fiction creator.
**Phases:** Phase 1 planning, Phase 2 drafting/self-review, Phase 4 logues.
**SOUL.md Content:** Use the existing author SOUL unchanged in spirit: elite investigative journalist and narrative non-fiction author, cybersecurity translator, "information, not ammunition."

## Profile: `booksmith-reviewer`

**Model:** Sonnet/strong analytical reviewer by default; can be switched via Hermes profile model settings.
**Role:** Manuscript reviewer for structural soundness, pacing, continuity, redundancy, source fidelity, and readiness for logues.
**Phases:** Phase 3 manuscript review.
**SOUL.md Content:** Same identity base as creator. Do not add a separate reviewer persona; the review task prompt supplies the phase role.

## Skill Symlink Rule

The Booksmith skill has one canonical copy:

```text
~/.hermes/skills/booksmith
```

Profile skill entries should be symlinks, not independent copies:

```text
~/.hermes/profiles/booksmith-creator/skills/booksmith  -> ~/.hermes/skills/booksmith
~/.hermes/profiles/booksmith-reviewer/skills/booksmith -> ~/.hermes/skills/booksmith
```

This prevents skill drift across profiles. Patch the canonical skill once.

## Where to Store SOUL Files

```text
~/.hermes/profiles/booksmith-creator/SOUL.md
~/.hermes/profiles/booksmith-reviewer/SOUL.md
```

Hermes loads these automatically when the profile is invoked. Do not pass SOUL content through templates or pipeline data.
