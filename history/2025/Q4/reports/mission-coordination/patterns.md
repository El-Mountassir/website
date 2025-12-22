# Pattern Extraction — Mission Coordination

## Extracted Patterns

### Pattern 1: Explicit Claim Before Work

- **Observed In**: Industry lock patterns, Anthropic task decomposition
- **Underlying Principle**: Before working on something, declare intent explicitly
- **Application**: Add `CLAIMED` status + timestamp + description to mission YAML
- **Generalization Test**: Applies to any shared resource → YES
- **Confidence**: High

### Pattern 2: Move = Claim (Filesystem as State)

- **Observed In**: Current mission standard (queue/ → active/)
- **Underlying Principle**: Filesystem location IS the state
- **Application**: Moving file to `active/` is the claim action
- **Advantage**: Visible in directory listing, no parsing needed
- **Generalization Test**: Works for file-based workflows → YES
- **Confidence**: High

### Pattern 3: Execution Log as Audit Trail

- **Observed In**: Current mission standard (append-only log)
- **Underlying Principle**: First entry in log = claim; subsequent = progress
- **Application**: `CLAIMED at TIMESTAMP by DESCRIPTION` as first entry
- **Generalization Test**: Works for any mission → YES
- **Confidence**: High

### Pattern 4: Session Start Check (/start)

- **Observed In**: Current CLAUDE.md `/start` command
- **Underlying Principle**: Before starting work, survey the landscape
- **Application**: `/start` must check `active/` and warn if missions in progress
- **Generalization Test**: Works for any session → YES
- **Confidence**: High

### Pattern 5: Graceful Handoff on Interruption

- **Observed In**: Industry patterns (exponential backoff, recovery)
- **Underlying Principle**: Crashed instances should leave recoverable state
- **Application**: Execution log should always be up-to-date; next instance resumes from last entry
- **Generalization Test**: Works for any interruptible work → YES
- **Confidence**: High

---

## Anti-Patterns Identified

### Anti-Pattern 1: Silent Start

- **Observed**: Instance starts working without updating mission status
- **Problem**: Other instances don't know work has begun
- **Fix**: Mandate claim action before any work

### Anti-Pattern 2: Generic Assignment

- **Observed**: `assigned_to: Claude Code` (not specific)
- **Problem**: All instances see themselves as "assigned"
- **Fix**: Add `claimed_by` with instance-specific info

### Anti-Pattern 3: No Timestamp

- **Observed**: YAML has `assigned:` date but no time
- **Problem**: Can't tell if work started recently or is stale
- **Fix**: Use full ISO timestamp with time

### Anti-Pattern 4: Skip the Move

- **Observed**: Instances work on queue/ missions without moving to active/
- **Problem**: Filesystem doesn't reflect actual state
- **Fix**: Make move mandatory in /start workflow

---

## Proposed Claim Protocol

```
1. CHECK: Is mission in active/? → Already claimed
2. MOVE: queue/{mission}.md → active/{mission}.md
3. UPDATE: status: QUEUED → status: ACTIVE
4. ADD: claimed_at: YYYY-MM-DDTHH:MM:SS
5. ADD: claimed_by: "[Description of this session]"
6. LOG: First execution log entry = claim record
7. WORK: Begin execution
8. HANDOFF: If interrupted, log saves state
```

---

## Claim YAML Addition

```yaml
# Current
mission_id: 2025-12-22-thaifa-migration-critical
status: QUEUED
assigned_to: Claude Code

# Proposed
mission_id: 2025-12-22-thaifa-migration-critical
status: ACTIVE
assigned_to: Claude Code
claimed_at: 2025-12-22T02:30:00+01:00
claimed_by: "Session working on Thaifa P0 migration"
```
