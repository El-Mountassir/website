# /start - Session Onboarding

Initialize a new work session by loading context and orienting toward existing work.

## Input

$ARGUMENTS

If empty: Run full onboarding sequence.

---

## Process

### 1. Check Active Missions

```bash
ls missions/active/
```

**If missions found**:
- Read each mission file
- Extract: current status, last action, remaining objectives
- Present: "Mission X is in progress. Resume?"

**If empty**: Continue to step 2.

### 2. Check Queued Missions

```bash
ls missions/queue/
```

**If missions found**:
- List by priority (from YAML frontmatter)
- Present: "These missions are ready. Which to start?"

**If empty**: Continue to step 3.

### 3. Check Draft Missions

```bash
ls missions/drafts/
```

**If drafts found**:
- Present as options for new work

### 4. Display Summary

Present to user:

```
## Session Start

**Active**: [count] mission(s)
**Queue**: [count] mission(s)
**Drafts**: [count] idea(s)

**Recommendation**: [Resume X / Start Y / New initiative]
```

### 5. Ask User

- "Which mission to work on?"
- "Or describe a new task?"

---

## Example Output

```
## Session Start

**Active**: 0 missions
**Queue**: 3 missions
  - thaifa-migration-critical (P1)
  - thaifa-migration-operational (P2)
  - thaifa-migration-cleanup (P3)
**Drafts**: 1 idea
  - claude-web-sync

**Recommendation**: Start with thaifa-migration-critical (P1)

Which mission to work on?
```
