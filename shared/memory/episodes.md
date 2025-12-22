# Episodes — Significant Events

> **Collective memory of what happened.**
> All agents contribute. All agents learn.

---

## Format

```markdown
## [YYYY-MM-DD] Title

**Author**: [Agent/Human name]
**Type**: [Success | Failure | Learning | Incident]

Description of what happened.

**Impact**: What changed because of this
**Lesson**: What we learned
```

---

## Entries

### [2025-12-21] Premature Session Closure

**Author**: Claude Code
**Type**: Failure

Session ended with items not captured as missions. Multiple learnings and next steps were lost because they existed only in ephemeral chat.

**Impact**: Created `/end` guardrails to prevent recurrence
**Lesson**: NEVER close session without verifying all items are captured

---

### [2025-12-22] Cognitive Overload Pattern Identified

**Author**: Claude Code + Omar
**Type**: Learning

Claude asked "What next?" when obvious actions (archive mission, commit changes) should have been done automatically. Omar identified this as a toxic anti-pattern.

**Impact**: Created R→A (Recognition→Action) principle and anti-patterns.md
**Lesson**: If action is obvious, DO IT. Don't ask.

---

### [2025-12-22] Architecture Lock-in Identified

**Author**: Omar
**Type**: Learning

Putting memory files in `.claude/` would lock data to Claude Code only. Omar pointed out that `shared/` is needed for all agents (current and future).

**Impact**: Created `shared/` directory structure
**Lesson**: Always consider multi-agent access when designing architecture

---

### [2025-12-22] Future-Proofing with `user/` vs `omar/`

**Author**: Omar
**Type**: Decision

Used `shared/user/` instead of `shared/omar/` to allow for potential future multi-user scenarios.

**Impact**: More flexible architecture
**Lesson**: When we can afford to plan for the future, do it

---
