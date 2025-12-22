# Claude Memory System

> **SCOPE DEFINITION**: All Claude memory files live in `/home/omar/Work/El-Mountassir/.claude/memory/`
>
> **OBSOLETE**: Any reference to `~/Documents/` is outdated. Everything is in this repository.

---

## Purpose

This directory stores persistent memory for Claude instances to learn across sessions.

---

## Files

| File | Purpose | When to Update |
|------|---------|----------------|
| `episodes.md` | Specific past events, successes, failures | After significant sessions |
| `facts.md` | Persistent facts about the system | When learning new facts |
| `decisions.md` | Decisions made with reasoning | After important decisions |
| `preferences.md` | Omar's preferences | When preferences are expressed |
| `patterns.md` | Reusable patterns discovered | When patterns are generalized |

---

## Format

Each entry follows this structure:

```markdown
## [YYYY-MM-DD] Title

Description.

**Context**: Why this matters
**Action**: What to do about it
**Source**: Where this was learned
```

---

## Usage

### Read Before Acting
- Check `episodes.md` for similar past situations
- Check `decisions.md` for related decisions
- Check `patterns.md` for applicable patterns

### Write After Learning
- Document new learnings immediately (R→A principle)
- Don't wait for /end - document as you go

---

## Migration Note

**2025-12-22**: All references to `~/Documents/` in rules files are being migrated to this location.

Old paths → New paths:
- `~/Documents/user/memory/preferences.md` → `.claude/memory/preferences.md`
- `~/Documents/tech/memory/issues.md` → `.claude/memory/episodes.md`
- `~/Documents/core/decisions.md` → `.claude/memory/decisions.md`
- `~/Documents/core/patterns.md` → `.claude/memory/patterns.md`

---

_v1.0.0 — Central memory location for all Claude instances_
