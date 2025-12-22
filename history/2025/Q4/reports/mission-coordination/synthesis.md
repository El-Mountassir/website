# Synthesis — Mission Coordination Solution

## Integration Strategy

The solution combines three reinforcing mechanisms:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MISSION COORDINATION                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  1. FILESYSTEM STATE (Primary)                                   │
│     └── queue/ → active/ move = claim                            │
│                                                                   │
│  2. YAML METADATA (Secondary)                                    │
│     └── claimed_at + claimed_by fields                           │
│                                                                   │
│  3. EXECUTION LOG (Tertiary)                                     │
│     └── First entry = claim record with timestamp                │
│                                                                   │
│  4. /start CHECK (Enforcement)                                   │
│     └── Warn if active/ has missions, ask before claiming new    │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Proposed Changes

### A. Update Mission Template YAML

```yaml
# ADD these fields to mission template
claimed_at:       # ISO timestamp when work started
claimed_by:       # Description of claiming session
```

### B. Update /start Command

Add to the check sequence:

```markdown
## Step 2: Check Active Missions

1. List `missions/active/` contents
2. For each mission:
   - Show title, claimed_at, claimed_by
   - Warn: "⚠️ Mission already in progress"
3. If active missions exist:
   - Ask: "Resume existing mission or start new from queue?"
```

### C. Update Claim Protocol in Standard

Add to `docs/standards/management/missions/README.md`:

```markdown
### Claiming a Mission

Before starting work on a queued mission:

1. **Check**: Verify `missions/active/` is empty or you're resuming
2. **Move**: `mv missions/queue/{mission}.md missions/active/`
3. **Update YAML**:
   - `status: ACTIVE`
   - `claimed_at: [current ISO timestamp]`
   - `claimed_by: "[session description]"`
4. **Log**: Add first execution entry: "Mission claimed"
5. **Work**: Begin execution

⚠️ NEVER work on a queue/ mission without moving it first.
```

### D. Update CLAUDE.md Session Handling

Add section:

```markdown
## MISSION CLAIMING

When starting work on a mission:

| Step | Action | Why |
|------|--------|-----|
| 1 | Check active/ | See if another instance is working |
| 2 | Move queue/ → active/ | Claim the mission |
| 3 | Update YAML | Record claimed_at, claimed_by |
| 4 | Log "Claimed" | Create audit trail |

If `active/` already has missions, you're likely resuming another session's work.
Read the execution log before continuing.
```

---

## Uncertainties

1. **Race condition window**: Between check and move, another instance could claim
   - Mitigation: Short window, Omar usually only runs one instance
   - Future: Could add actual file lock if needed

2. **Stale claims**: What if instance crashes and leaves mission in active/?
   - Mitigation: Check `claimed_at` timestamp; if >24h old, may be stale
   - Protocol: Omar can manually move back to queue/

3. **No true instance ID**: Sessions don't have persistent unique IDs
   - Mitigation: `claimed_by` description is human-readable
   - Future: Could generate UUID per session

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Instance claims and crashes | Mission in active/ with old timestamp | Next instance resumes or Omar moves to queue/ |
| Two instances claim simultaneously | Conflict on move (rare) | Check execution log, newest entry wins |
| Instance forgets to claim | Mission still in queue/ after work | Audit: execution log empty = work lost |
| Stale active/ missions | claimed_at > 24h | Omar cleanup or instance asks before touching |

---

## Implementation Cost

| Change | Effort | Impact |
|--------|--------|--------|
| Update mission template | 5 min | Low |
| Update /start skill | 15 min | Medium |
| Update missions standard | 10 min | Low |
| Update CLAUDE.md | 5 min | Low |
| **Total** | ~35 min | **High value** |

---

## Alternative: Simpler Approach

If full protocol is too heavy:

**Minimum Viable Coordination**:
1. Just move to active/ (already in standard, just enforce)
2. /start always checks active/ first

This gives 80% of the benefit with 20% of the changes.
