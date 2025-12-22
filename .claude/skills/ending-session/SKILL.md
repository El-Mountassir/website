---
name: ending-session
description: Safely closes a session with guardrails preventing premature closure. Blocks if uncaptured items exist or git is dirty. Use when ending a session or when user types /end.
---

# /end — Session Closure with Guardrails

## Purpose

Prevent premature session closure. Ensure ALL work items are captured before ending.

**Background**: On 2025-12-21, a session ended with items lost. See `LESSONS-LEARNED/2025-12-21-premature-closure.md`.

## HARD RULE

> **NEVER authorize session closure if ANY guardrail fails.**
> **After identifying a blocker, FIX IT AUTOMATICALLY if the action is obvious. Don't ask.**

## Guardrail Order

1. **Active Missions State** (BLOCKING) — Check first
2. **Session Learnings** (BLOCKING) — New
3. **Uncaptured Items** (BLOCKING)
4. **Git Status** (BLOCKING)
5. **CHANGELOG** (WARNING)

---

## Instructions

### Guardrail 1: Active Missions State (BLOCKING)

```bash
ls missions/active/
```

**If NOT empty**:

1. Read each mission file
2. Check `status` field in YAML
3. Take action based on status:

| Status | Action | Ask? |
|--------|--------|------|
| `COMPLETED` | Archive to `history/YYYY/QQ/missions/` | NO — just do it |
| `ACTIVE` | Document stopping point in execution log | YES — ask if should complete or pause |

```
## BLOCKED: Active Missions Exist

missions/active/ is not empty:

| Mission | Status | Action |
|---------|--------|--------|
| mission-claim-protocol | COMPLETED | Archiving now... |
| thaifa-migration | ACTIVE | Need to document stopping point |

Proceeding with automatic fixes...
```

**DO NOT authorize closure with missions in active/.**

### Guardrail 2: Session Learnings (BLOCKING)

Scan the conversation for:
- Mistakes made and recognized
- New patterns discovered
- Preferences expressed by Omar
- Behaviors to change
- Insights gained

**If found and NOT documented**:

```
## BLOCKED: Undocumented Learnings

The following learnings were recognized but not documented:

1. [Learning description]
2. [Learning description]

**Action**: Documenting now in appropriate rules/memory files...
```

**Automatically document learnings before proceeding.**

### Guardrail 3: Uncaptured Items (BLOCKING)

Scan the conversation for:
- Mentioned tasks not in missions
- Questions asked but not resolved
- "TODO", "later", "should", "need to" statements
- User requests not fully addressed

**If found**:

```
## BLOCKED: Uncaptured Items Detected

The following items were mentioned but not captured as missions:

1. [Item description]
2. [Item description]

**Action**: Creating missions for these items...
```

**Automatically create missions for uncaptured items.**

### Guardrail 4: Git Status (BLOCKING)

```bash
git status --porcelain
```

**If output is NOT empty**:

```
## BLOCKED: Uncommitted Changes

You have uncommitted changes:

[git status output]

**Action**: Committing changes now...
```

**Automatically commit changes with appropriate message.**

### Guardrail 5: CHANGELOG.md (WARNING)

**If significant changes were made this session**:
- Check if CHANGELOG.md was updated
- If not, warn (but don't block):

```
## WARNING: CHANGELOG Not Updated

Significant changes were made this session but CHANGELOG.md was not updated.

Consider updating before next session.
```

---

## If All Guardrails Pass

```
## Session Closure Authorized

### Summary
- **Missions completed**: [list]
- **Missions archived**: [list]
- **Learnings documented**: [list]
- **Commits made**: [count]

### Git Status
Clean. All changes committed.

### Next Session
- Pending in queue: [count]
- Recommended next: [mission name]

---

Session may be safely closed.
```

---

## Override Protocol

If user insists on closing despite blocks:

1. Require explicit confirmation: "I understand items will be lost. Close anyway."
2. Log the override in execution log
3. Still attempt to capture what's possible

**Never silently allow premature closure.**

---

## Key Principle

> **Fix blockers automatically. Don't ask Omar to decide obvious things.**

| Blocker | Automatic Fix |
|---------|---------------|
| Completed mission not archived | Archive it |
| Learning not documented | Document it |
| Changes not committed | Commit them |
| Uncaptured items | Create missions |

Only ask when the action is genuinely ambiguous.

---

_Skill v2.0.0 | Enforces HARD STOP rule #6 | Auto-fixes obvious blockers_
