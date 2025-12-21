---
name: starting-session
description: Initializes a new work session by checking active missions and loading context. Use at the beginning of any session or when user types /start.
---

# /start — Session Onboarding

## Purpose

Orient a new Claude instance toward existing work and prevent context loss between sessions.

## Instructions

### Step 1: Check Active Missions

```bash
ls missions/active/
```

**If missions found**:
- Read each mission file
- Extract: current status, last action, remaining objectives
- Present: "Mission X is in progress. Resume?"

**If empty**: Proceed to Step 2.

### Step 2: Check Queued Missions

```bash
ls missions/queue/
```

**If missions found**:
- List by priority (from YAML frontmatter)
- Present: "These missions are ready. Which to start?"

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

**Active**: [count] mission(s)
**Queue**: [count] mission(s)
**Drafts**: [count] idea(s)

**Recommendation**: [Resume X / Start Y / New initiative]
```

### Step 5: Ask User

- "Which mission to work on?"
- "Or describe a new task?"

## Example

User types: `/start`

Claude responds:

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

---

_Skill v1.0.0 | Prevents context loss between sessions_
