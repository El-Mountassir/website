---
description: Close session safely with guardrails preventing premature closure
allowed-tools: Read, Bash(git status:*), Glob
argument-hint: [--force]
---

# Purpose

Safely close a work session by enforcing HARD STOP #6: No premature closure. Checks for uncaptured items, uncommitted changes, and CHANGELOG updates before authorizing session end.

**Background**: Prevents repeat of 2025-12-21 incident.
See: `LESSONS-LEARNED/2025-12-21-premature-closure.md`

## Variables

FORCE_FLAG: $1

If `--force`: Skip guardrails (requires explicit user acknowledgment of risk).
If empty: Run full guardrail sequence.

---

## Instructions

### HARD RULE

> **NEVER authorize closure if ANY guardrail fails.**

### Guardrail 1: Uncaptured Items (BLOCKING)

Scan the conversation for:
- Tasks mentioned but not in missions
- "TODO", "later", "should", "need to" statements
- User requests not fully addressed
- Questions asked but not resolved

**If found → BLOCK and list items.**

### Guardrail 2: Git Status (BLOCKING)

```bash
git status --porcelain
```

**If NOT empty → BLOCK and show changes.**

### Guardrail 3: CHANGELOG (WARNING)

If significant changes were made this session, warn if CHANGELOG.md wasn't updated.

---

## Output

### If Blocked

```
## BLOCKED: Cannot Close Session

### Issue 1: Uncaptured Items
- [Item 1]
- [Item 2]

### Issue 2: Uncommitted Changes
- [File 1]
- [File 2]

**Required Actions**:
1. Create missions for uncaptured items
2. Commit pending changes

Proceed with these actions?
```

### If Passed

```
## Session Closure Authorized

### Summary
- **Missions advanced**: [list]
- **Missions archived**: [list]
- **Missions created**: [list]

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

1. Require explicit confirmation: "I understand items may be lost."
2. Log the override
3. Still attempt to capture what's possible

**Never silently allow premature closure.**

---

## Example

```
/end
```

→ Runs full guardrail check, blocks or authorizes closure

```
/end --force
```

→ Skips guardrails with explicit acknowledgment (use with caution)
