# Mission Coordination Protocol — Design Report

**Generated**: 2025-12-22
**Pipeline**: `history/2025/Q4/reports/mission-coordination/`

---

## Summary

When multiple Claude Code instances work in the same repository, they can unknowingly claim the same mission because no signaling mechanism exists. This report proposes a lightweight **Claim Protocol** using filesystem state (move to `active/`), YAML metadata (`claimed_at`, `claimed_by`), and `/start` command enforcement.

---

## Key Insights

| Insight | Confidence | Sources |
|---------|------------|---------|
| Claude Code has no built-in coordination (by design) | High | [Official docs](https://docs.anthropic.com/claude-code) |
| Filesystem location can serve as state | High | Current mission standard |
| Clear task boundaries prevent conflicts | High | [Anthropic multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system) |
| File-based signaling works for markdown workflows | Medium | [Industry patterns](https://www.confluent.io/blog/event-driven-multi-agent-systems/) |

---

## The Problem

**Current state**:
```
missions/queue/2025-12-22-thaifa-migration-critical.md
  status: QUEUED
  assigned_to: Claude Code  ← Generic, all instances see this
```

**What happened**: Instance A started working on Thaifa migration. Instance B (me) didn't know. Omar had to manually clarify.

**Root cause**: No mechanism to indicate "I'm working on this."

---

## The Solution: Claim Protocol

### Overview

```
┌─────────────────────────────────────────────────────────┐
│                   CLAIM WORKFLOW                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   /start                                                 │
│      │                                                   │
│      ├── Check missions/active/                          │
│      │      └── If not empty → Show & ask to resume      │
│      │                                                   │
│      ├── Check missions/queue/                           │
│      │      └── If has missions → Offer to claim         │
│      │                                                   │
│      └── Claim chosen mission:                           │
│             1. Move queue/ → active/                     │
│             2. Update YAML (status, claimed_at, by)      │
│             3. Log "Claimed" in execution log            │
│             4. Begin work                                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### YAML Changes

```yaml
# BEFORE (current)
mission_id: 2025-12-22-thaifa-migration-critical
status: QUEUED
assigned_to: Claude Code
created: 2025-12-22

# AFTER (proposed)
mission_id: 2025-12-22-thaifa-migration-critical
status: ACTIVE
assigned_to: Claude Code
created: 2025-12-22
claimed_at: 2025-12-22T02:30:00+01:00    # ← NEW: ISO timestamp
claimed_by: "Thaifa P0 migration session"  # ← NEW: Session description
```

### Execution Log Entry

```markdown
## Execution Log

### 2025-12-22

- 02:30 - **CLAIMED** by session "Thaifa P0 migration"
- 02:31 - Starting objective 1: Migrate admin/ folder
- ...
```

---

## Implementation

### 1. Update Mission Template

Add to YAML frontmatter:

```yaml
claimed_at:     # Filled when claimed
claimed_by:     # Description of claiming session
```

### 2. Update /start Skill

Modify `.claude/skills/starting-session/SKILL.md`:

```markdown
## Phase 2: Check Active Missions

1. `ls missions/active/`
2. If NOT empty:
   - Display: "⚠️ Active missions found:"
   - List each with title, claimed_at, claimed_by
   - Ask: "Resume this work or start new from queue?"
3. If empty:
   - Proceed to check queue
```

### 3. Update Missions Standard

Add to `docs/standards/management/missions/README.md` Section 2:

```markdown
### 2.3 Claiming Protocol

Before starting work on a queued mission, an instance MUST:

1. **CHECK**: Verify no mission already in `active/`
2. **MOVE**: `mv missions/queue/{mission}.md missions/active/`
3. **UPDATE YAML**:
   - `status: ACTIVE`
   - `claimed_at: [ISO timestamp]`
   - `claimed_by: "[session description]"`
4. **LOG**: Add "CLAIMED" entry to execution log
5. **WORK**: Begin execution

⚠️ **HARD RULE**: Never work on a queue/ mission without claiming first.
```

### 4. Update CLAUDE.md

Add to SESSION COMMANDS section:

```markdown
### Mission Claiming

When an instance claims a mission:

| Action | Purpose |
|--------|---------|
| Move queue/ → active/ | Filesystem = state |
| Add claimed_at | Timestamp for staleness check |
| Add claimed_by | Human-readable session ID |
| Log "CLAIMED" | Audit trail |

**Check before claiming**: If `active/` has missions, another instance may be working.
```

---

## Rollout Plan

| Phase | Action | When |
|-------|--------|------|
| 1 | Update mission template | Now |
| 2 | Update /start skill | Now |
| 3 | Update missions standard | Now |
| 4 | Update CLAUDE.md | Now |
| 5 | Apply to existing queue missions | Next session |

---

## Edge Cases

| Case | Handling |
|------|----------|
| Instance crashes mid-work | Next instance sees active/ mission, resumes from execution log |
| `claimed_at` > 24h old | Likely stale; ask Omar or move back to queue |
| Two instances claim simultaneously | Rare; check execution log, coordinate via Omar |
| Instance forgets to claim | Work may be lost; audit via empty execution log |

---

## Minimum Viable Version

If full protocol is too heavy, enforce just:

1. **Move to active/** before working (already in standard)
2. **/start checks active/** first

This gives 80% benefit with minimal changes.

---

## Limitations & Gaps

- No true instance ID (using description instead)
- Race condition window between check and move (mitigated by single-user context)
- Relies on instance discipline (no automatic enforcement)

---

## Sources

- [Anthropic Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Confluent: Event-Driven Multi-Agent Systems](https://www.confluent.io/blog/event-driven-multi-agent-systems/)
- [Microsoft: AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [Galileo: Multi-Agent Coordination Strategies](https://galileo.ai/blog/multi-agent-coordination-strategies)
- Current: `docs/standards/management/missions/README.md`

---

## Artifacts

| File | Purpose |
|------|---------|
| `step-back.md` | Problem analysis |
| `sources.md` | Research sources |
| `patterns.md` | Extracted patterns |
| `synthesis.md` | Solution design |
| `final.md` | This summary |

---

_Report complete. Ready for implementation._
