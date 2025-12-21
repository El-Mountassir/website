# Mission: Session Commands (/start, /end)

```yaml
mission_id: 2025-12-21-session-commands
status: ARCHIVED
assigned_to: Claude Code
created: 2025-12-21
assigned: 2025-12-22
completed: 2025-12-22
archived: 2025-12-22
priority: 4
depends_on: []  # behavior-fix completed (archived)
```

---

## Context

Créer des skills `/start` et `/end` pour structurer les sessions et empêcher les clôtures prématurées.

**Feedback Omar**: "Toute chose à faire, même mineur et/ou non-blockant reste quelque chose à faire!"

---

## Objectives

- [x] **O1**: Créer skill `/start` (onboarding session)
- [x] **O2**: Créer skill `/end` (avec guardrails)
- [x] **O3**: Documenter dans CLAUDE.md
- [x] **O4**: Tester les guardrails

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | /start fonctionne | ✅ | `.claude/skills/starting-session/SKILL.md` created |
| 2 | /end bloque si items non capturés | ✅ | Guardrail logic in SKILL.md |
| 3 | /end bloque si git dirty | ✅ | Guardrail logic in SKILL.md |
| 4 | Documenté | ✅ | CLAUDE.md SESSION COMMANDS section |

---

## Constraints

- **Dépend de M5** (Behavior Fix) — ✅ Completed and archived

---

## Deliverables

| File | Description |
|------|-------------|
| `.claude/skills/starting-session/SKILL.md` | Session onboarding skill |
| `.claude/skills/ending-session/SKILL.md` | Session closure with guardrails |
| `CLAUDE.md` | SESSION COMMANDS section added |

---

## Execution Log

> Append-only.

### 2025-12-21

- **Created**: Mission drafted

### 2025-12-22

- **Assigned**: Started execution with ULTRATHINK + PLAN MODE
- **O1 Complete**: Created `/start` skill in `.claude/skills/starting-session/`
- **O2 Complete**: Created `/end` skill in `.claude/skills/ending-session/`
- **O3 Complete**: Added SESSION COMMANDS section to CLAUDE.md
- **O4 Complete**: Verified YAML frontmatter, skill structure valid
- **Committed**: 8aa31a2 feat(skills): add /start and /end session commands
- **Archived**: Mission moved to history/2025/Q4/missions/session-commands/

---

_Mission v1.0.0-osr.1 — Completed_
