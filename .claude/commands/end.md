---
description: Close session safely with guardrails preventing premature closure. Use when looking to end of any session
allowed-tools: Read, Bash(git status:*), Bash(git:*), Glob, Write, Edit
argument-hint: [--force]
---

# Purpose

Safely close a work session by enforcing HARD STOP #6: No premature closure. Checks for active missions, undocumented learnings, uncaptured items, and uncommitted changes.

**Background**: Prevents repeat of 2025-12-21 incident.
See: `LESSONS-LEARNED/2025-12-21-premature-closure.md`

## HARD RULE

> **NEVER authorize closure if ANY guardrail fails.** > **After identifying a blocker, FIX IT AUTOMATICALLY. Don't ask Omar to decide obvious things.**

## Variables

FORCE_FLAG: $1

If `--force`: Skip guardrails (requires explicit user acknowledgment of risk).
If empty: Run full guardrail sequence.

---

## Guardrail Order

1. **Active Missions State** (BLOCKING)
2. **Session Learnings** (BLOCKING)
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

- Read each mission file
- If status = `COMPLETED` → Archive automatically
- If status = `ACTIVE` → Ask: complete or document stopping point?

**DO NOT proceed until active/ is empty.**

### Guardrail 2: Session Learnings (BLOCKING)

Scan conversation for:

- Mistakes made and recognized
- New patterns discovered
- Preferences expressed by Omar
- Behaviors to change

**If found and NOT documented** → Document automatically in rules/memory files.

### Guardrail 3: Uncaptured Items (BLOCKING)

Scan conversation for:

- Mentioned tasks not in missions
- "TODO", "later", "should", "need to" statements
- User requests not fully addressed
- Questions asked but not resolved

**If found** → Create missions automatically.

### Guardrail 4: Git Status (BLOCKING)

```bash
git status --porcelain
```

**If NOT empty** → Commit automatically with appropriate message.

### Guardrail 5: CHANGELOG.md (WARNING)

If significant changes were made, warn if CHANGELOG.md wasn't updated. (Don't block)

---

## Automatic Fix Principle

| Blocker                      | Automatic Fix            |
| ---------------------------- | ------------------------ |
| Completed mission in active/ | Archive it               |
| Undocumented learning        | Document in rules/memory |
| Uncaptured item              | Create mission           |
| Uncommitted changes          | Commit them              |

Only ask when the action is genuinely ambiguous.

---

## Output: If Blocked

```
## BLOCKED: Cannot Close Session

### Issue 1: Active Mission
- mission-claim-protocol (COMPLETED) → Archiving now...

### Issue 2: Uncommitted Changes
- Modified: CLAUDE.md → Committing now...

Proceeding with automatic fixes...
```

## Output: If Passed

```
## Session Closure Authorized

### Summary
- **Missions archived**: [list]
- **Learnings documented**: [list]
- **Commits made**: [count]

### Git Status
Clean.

### Next Session
- Pending in queue: [count]
- Recommended next: [mission name]

---

Session may be safely closed.
```

---

## Override Protocol

If user provides `--force`:

1. Require explicit confirmation: "I understand items will be lost. Close anyway."
2. Log the override
3. Still attempt to capture what's possible

**Never silently allow premature closure.**

---

## Example

```
/end
```

-> Runs guardrails, auto-fixes blockers, authorizes closure

```
/end --force
```

-> Skips guardrails with explicit acknowledgment (use with caution)
