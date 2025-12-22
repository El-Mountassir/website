---
description: Initialize session by checking active missions and loading context
allowed-tools: Read, Glob, Bash(ls:*)
argument-hint: [mission-name]
---

# Purpose

Start a new work session by orienting toward existing work. Checks active missions, queued work, and draft ideas to provide context continuity between sessions.

## Variables

SPECIFIC_MISSION: $1

If empty: Run full onboarding sequence checking all mission directories.

---

## Instructions

### Step 1: Check Active Missions

```bash
ls missions/active/
```

**If missions found**:
- Read each mission file
- Extract: current status, last action, remaining objectives
- Present: "Mission X is in progress. Resume?"

**If empty**: Continue to step 2.

### Step 2: Check Queued Missions

```bash
ls missions/queue/
```

**If missions found**:
- List by priority (from YAML frontmatter)
- Present: "These missions are ready. Which to start?"

**If empty**: Continue to step 3.

### Step 3: Check Draft Missions

```bash
ls missions/drafts/
```

**If drafts found**:
- Present as options for new work

### Step 4: Display Summary

Present state to user.

### Step 5: Ask User

- "Which mission to work on?"
- "Or describe a new task?"

---

## Output

```
## Session Start

**Active**: [count] mission(s)
**Queue**: [count] mission(s)
**Drafts**: [count] idea(s)

**Recommendation**: [Resume X / Start Y / New initiative]

Which mission to work on?
```

---

## Example

```
/start
```

→ Displays session summary with all missions categorized

```
/start thaifa-migration
```

→ Directly loads the specified mission context
