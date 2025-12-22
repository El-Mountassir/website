---
name: starting-session
description: Initializes a new work session by checking active missions and loading context. Use at the beginning of any session or when user types /start.
---

# /start — Session Onboarding

## Purpose

Orient a new Claude instance toward existing work and prevent context loss between sessions.

**CRITICAL**: This skill enforces the Claiming Protocol to prevent multiple instances from working on the same mission.

## Instructions

### Step 1: Check Active Missions (CRITICAL)

```bash
ls missions/active/
```

**If missions found** (NOT empty):

> **WARNING**: Another instance may be working on this mission.

1. Read each mission file in `active/`
2. Extract: `claimed_at`, `claimed_by`, status, last execution log entry
3. Calculate time since claim
4. Present with warning:

```
## Active Mission Detected

**Mission**: [mission_id]
**Claimed at**: [timestamp]
**Claimed by**: [session description]
**Time since claim**: [X hours/minutes ago]
**Last action**: [from execution log]

This mission appears to be actively worked on by another instance.

**Options**:
1. **Resume** - Take over this mission (if abandoned)
2. **Work on queue** - Pick a different mission
3. **New initiative** - Start something else

Which option?
```

**Conflict rules**:
- If claimed < 24h ago: Strongly recommend Option 2 or 3
- If claimed > 24h ago: May be abandoned, Option 1 is reasonable
- Always ask user before claiming an active mission

**If empty**: Proceed to Step 2.

### Step 2: Check Queued Missions

```bash
ls missions/queue/
```

**If missions found**:
- List by priority (from YAML frontmatter)
- Present: "These missions are ready. Which to start?"

**To claim a mission**:
1. Move file: `mv missions/queue/{mission}.md missions/active/`
2. Update YAML: Set `status: ACTIVE`, add `claimed_at`, `claimed_by`
3. Log: Add "CLAIMED" as first execution entry
4. Begin work

**If empty**: Proceed to Step 3.

### Step 3: Check Draft Missions

```bash
ls missions/drafts/
```

**If drafts found**:
- Present as options for new work
- Ask: "Promote one to queue, or new initiative?"

### Step 4: Display Context Summary

Present to user:

```
## Session Start

**Active**: [count] mission(s) [WARN if > 0]
**Queue**: [count] mission(s)
**Drafts**: [count] idea(s)

**Recommendation**: [Resume X / Start Y / New initiative]
```

### Step 5: Ask User

- "Which mission to work on?"
- "Or describe a new task?"

## Claiming Protocol Summary

```
CHECK → MOVE → UPDATE → LOG → WORK
```

| Step | Action |
|------|--------|
| CHECK | `ls missions/active/` - verify empty |
| MOVE | `mv queue/{x}.md active/` |
| UPDATE | Set `claimed_at`, `claimed_by` in YAML |
| LOG | First entry: "CLAIMED by [session description]" |
| WORK | Begin execution |

**Never work from queue/** - if it's in queue, it's unclaimed.

## Example: Empty Active

User types: `/start`

```
## Session Start

**Active**: 0 missions
**Queue**: 2 missions
  - 2025-12-22-thaifa-migration-critical.md (P1)
  - 2025-12-22-thaifa-migration-operational.md (P2)
**Drafts**: 1 idea
  - claude-web-sync.md

**Recommendation**: Start with thaifa-migration-critical (P1)

Which mission to work on?
```

## Example: Active Mission Found

User types: `/start`

```
## Active Mission Detected

**Mission**: 2025-12-22-thaifa-migration-critical
**Claimed at**: 2025-12-22T02:30:00+01:00
**Claimed by**: "Thaifa P0 migration session"
**Time since claim**: 1 hour ago
**Last action**: "Copied 15 files to new location"

This mission appears to be actively worked on by another instance.

**Options**:
1. Resume - Take over this mission
2. Work on queue - Pick a different mission (Recommended)
3. New initiative - Start something else

Which option?
```

---

_Skill v2.0.0 | Enforces Claiming Protocol | Prevents context loss and mission conflicts_
