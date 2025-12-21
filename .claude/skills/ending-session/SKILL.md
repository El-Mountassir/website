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

## Instructions

### Guardrail 1: Uncaptured Items (BLOCKING)

**Scan the conversation for**:
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

**Action Required**: Create missions for these items before closing.

Would you like me to create missions for these items now?
```

**DO NOT proceed until items are captured or explicitly dismissed by user.**

### Guardrail 2: Git Status (BLOCKING)

```bash
git status --porcelain
```

**If output is NOT empty**:
```
## BLOCKED: Uncommitted Changes

You have uncommitted changes:

[git status output]

**Action Required**: Commit or stash changes before closing.

Would you like me to commit these changes now?
```

**DO NOT proceed until git is clean.**

### Guardrail 3: CHANGELOG.md (WARNING)

**If significant changes were made this session**:
- Check if CHANGELOG.md was updated
- If not, warn (but don't block):

```
## WARNING: CHANGELOG Not Updated

Significant changes were made this session but CHANGELOG.md was not updated.

Consider updating before next session.
```

### If All Guardrails Pass

```
## Session Closure Authorized

### Summary
- **Missions advanced**: [list]
- **Missions archived**: [list]
- **Missions created**: [list]

### Git Status
Clean. All changes committed.

### Next Session
- Pending in queue: [count]
- Recommended next: [mission name]

---

Session may be safely closed.
```

## Override Protocol

If user insists on closing despite blocks:

1. Require explicit confirmation: "I understand items will be lost. Close anyway."
2. Log the override in execution log
3. Still attempt to capture what's possible

**Never silently allow premature closure.**

## Example: Blocked Closure

User types: `/end`

Claude checks and finds:
- Uncommitted file: `CLAUDE.md`
- Mentioned but uncaptured: "fix the API bug"

Claude responds:

```
## BLOCKED: Cannot Close Session

### Issue 1: Uncaptured Items
- "fix the API bug" — mentioned but no mission created

### Issue 2: Uncommitted Changes
- Modified: CLAUDE.md

**Required Actions**:
1. Create mission for "fix the API bug"
2. Commit CLAUDE.md changes

Shall I proceed with these actions?
```

## Example: Clean Closure

User types: `/end`

Claude checks:
- No uncaptured items
- Git is clean
- CHANGELOG updated

Claude responds:

```
## Session Closure Authorized

### Summary
- **Missions advanced**: session-commands (M4)
- **Missions archived**: omar-cleanup (M7)
- **Missions created**: 0

### Git Status
Clean.

### Next Session
- Pending in queue: 3 missions
- Recommended next: thaifa-migration-critical

---

Session may be safely closed.
```

---

_Skill v1.0.0 | Enforces HARD STOP rule #6_
