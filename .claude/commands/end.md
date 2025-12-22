# /end - Session Closure with Guardrails

Safely close a session. **Enforces HARD STOP #6**: No premature closure.

## Input

$ARGUMENTS

If empty: Run full guardrail check.

---

## HARD RULE

> **NEVER authorize closure if ANY guardrail fails.**

See: `LESSONS-LEARNED/2025-12-21-premature-closure.md`

---

## Guardrails

### Guardrail 1: Uncaptured Items (BLOCKING)

Scan the conversation for:
- Tasks mentioned but not in missions
- "TODO", "later", "should", "need to" statements
- User requests not fully addressed
- Questions asked but not resolved

**If found → BLOCK:**

```
## BLOCKED: Uncaptured Items

The following items were mentioned but not captured:

1. [Item]
2. [Item]

Create missions for these before closing?
```

### Guardrail 2: Git Status (BLOCKING)

```bash
git status --porcelain
```

**If NOT empty → BLOCK:**

```
## BLOCKED: Uncommitted Changes

[git status output]

Commit these changes before closing?
```

### Guardrail 3: CHANGELOG (WARNING)

If significant changes were made this session, warn if CHANGELOG.md wasn't updated.

```
## WARNING: CHANGELOG Not Updated

Consider updating before next session.
```

---

## If All Guardrails Pass

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

If user insists despite blocks:

1. Require explicit: "I understand items will be lost. Close anyway."
2. Log the override
3. Still attempt to capture what's possible

**Never silently allow premature closure.**
