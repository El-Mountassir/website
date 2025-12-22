# Mission Management Standard

```yaml
# Dublin Core Metadata
Title: Mission Management Standard
Creator: Omar El Mountassir + Claude Code
Subject: Mission Lifecycle, Work Packages, Agent Coordination
Description: Standard for creating, executing, and archiving multi-step work packages
Date: 2025-12-21
Type: Text
Format: Markdown
Identifier: docs/standards/management/missions/README.md
Language: en
Rights: Internal Team Standard

# Extended Metadata
Version: 0.0.3-alpha.0
Status: ACTIVE
Dimension: Work
Maturity: Tested (1 mission archived)
Automation_Target: true
Integration_Required: Linear (future)
```

---

## 1. Philosophy

> **Missions are multi-step work packages. Tasks are single actions.**

| Concept         | Definition                                                         | Example                                        |
| --------------- | ------------------------------------------------------------------ | ---------------------------------------------- |
| **Mission**     | Multi-step work package with clear objectives and success criteria | "Initialize repository and configure calendar" |
| **Task**        | Single, atomic action                                              | "Create CLAUDE.md file"                        |
| **Linear Task** | Task tracked in Linear                                             | Bug fix, single feature                        |

### When to Use Missions

| Use Mission                         | Use Linear Task       |
| ----------------------------------- | --------------------- |
| Multi-day effort                    | Single session        |
| Multiple objectives                 | Single objective      |
| Cross-system work                   | Single system         |
| Requires handoff between sessions   | Completable in one go |
| Needs archival for future reference | Routine, forgettable  |

---

## 2. Mission Lifecycle

```
CREATE → ASSIGN → EXECUTE → COMPLETE → ARCHIVE
   ↓        ↓         ↓          ↓          ↓
 Draft   Claude   In-Progress  Verify    History
```

### 2.1 Phase Details

| Phase        | Location                    | Actor              | Actions                                 |
| ------------ | --------------------------- | ------------------ | --------------------------------------- |
| **CREATE**   | `missions/drafts/`          | Omar or Claude Web | Write mission spec with objectives      |
| **ASSIGN**   | `missions/queue/`           | Omar               | Move to queue, assign to agent          |
| **EXECUTE**  | `missions/active/`          | Assigned agent     | Work through objectives, log progress   |
| **COMPLETE** | `missions/active/`          | Agent              | Verify success criteria, update status  |
| **ARCHIVE**  | `history/YYYY/QQ/missions/` | Agent              | Move to history with full documentation |

### 2.2 Status Values

| Status      | Meaning                  | File Location                      |
| ----------- | ------------------------ | ---------------------------------- |
| `DRAFT`     | Idea, not ready          | `missions/drafts/`                 |
| `QUEUED`    | Ready for assignment     | `missions/queue/`                  |
| `ACTIVE`    | Currently being executed | `missions/active/`                 |
| `COMPLETED` | Done, awaiting archival  | `missions/active/`                 |
| `ARCHIVED`  | Closed, in history       | `history/YYYY/QQ/missions/{slug}/` |

### 2.3 Claiming Protocol

> **Problem**: Multiple Claude instances can unknowingly work on the same mission.
> **Solution**: Filesystem location IS the claim. Move = Claim.

#### The Claim Process

```
CHECK → MOVE → UPDATE → LOG → WORK
```

| Step       | Action                                 | Purpose                           |
| ---------- | -------------------------------------- | --------------------------------- |
| **CHECK**  | `ls missions/active/`                  | See if someone is already working |
| **MOVE**   | `mv queue/{mission}.md active/`        | Filesystem state = claim          |
| **UPDATE** | Set `claimed_at`, `claimed_by` in YAML | Metadata for audit                |
| **LOG**    | First execution entry = "CLAIMED"      | Audit trail                       |
| **WORK**   | Begin execution                        | Actual work                       |

#### Claiming Rules

| Rule                       | Rationale                                  |
| -------------------------- | ------------------------------------------ |
| **Never work from queue/** | If it's in queue/, it's unclaimed          |
| **Check active/ first**    | Another instance may be working            |
| **Move before work**       | Filesystem location is the source of truth |
| **Log the claim**          | Audit trail for handoff                    |

#### Conflict Detection

If `missions/active/` is NOT empty when you start:

1. **Read the active mission file**
2. **Check `claimed_at` timestamp** - How recent?
3. **If < 24h**: Assume another instance is working. Ask user before proceeding.
4. **If > 24h**: May be abandoned. Ask user if they want to resume or reassign.

#### Example Claim

```yaml
mission_id: 2025-12-22-thaifa-migration
status: ACTIVE
claimed_at: 2025-12-22T03:45:00+01:00
claimed_by: "Thaifa P0 migration session"
```

```markdown
## Execution Log

### 2025-12-22

- 03:45 - **CLAIMED** by session "Thaifa P0 migration"
- 03:46 - Starting objective 1...
```

---

## 3. Storage Convention

```
El-Mountassir/
├── missions/
│   ├── README.md              # Index of missions
│   ├── drafts/                # Ideas, not assigned
│   │   └── {slug}.md
│   ├── queue/                 # Ready for assignment
│   │   └── {YYYY-MM-DD}-{slug}.md
│   └── active/                # Currently executing
│       └── {YYYY-MM-DD}-{slug}.md
│
└── history/
    └── YYYY/QQ/missions/      # Archived missions
        └── {slug}/
            ├── mission.md       # Final mission doc
            ├── execution-log.md # Timestamped actions
            └── deviations.md    # Differences from spec
```

### Naming Convention

| Stage    | Pattern                  | Example                        |
| -------- | ------------------------ | ------------------------------ |
| Draft    | `{slug}.md`              | `calendar-setup.md`            |
| Queued   | `{YYYY-MM-DD}-{slug}.md` | `2025-12-22-calendar-setup.md` |
| Active   | `{YYYY-MM-DD}-{slug}.md` | `2025-12-22-calendar-setup.md` |
| Archived | `{slug}/` directory      | `calendar-setup/`              |

---

## 4. Mission Template

> **Template location**: [`templates/missions/mission.md`](../../../../templates/missions/mission.md)

The unified mission template supports multiple mission types:

| Type | Use Case |
|------|----------|
| `STANDARD` | General multi-step work packages |
| `ELEVATE` | /elevate outputs requiring mission-level tracking |
| `FIX` | Bug fixes with root cause analysis |
| `FEATURE` | New feature implementation |
| `RESEARCH` | Investigation and analysis |
| `MIGRATION` | Data or system migrations |

Type-specific sections are included as HTML comments in the template. Uncomment the sections relevant to your mission type.

---

## 5. Archival Process

When a mission is COMPLETED:

### Step 1: Verify Success Criteria

All criteria must be checked with evidence:

```markdown
| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Files created | ✅ | `ls` output shows files |
| 2 | Tests pass | ✅ | CI green |
````

### Step 2: Create Archive Directory

```bash
mkdir -p history/YYYY/QQ/missions/{slug}
```

### Step 3: Create Archive Files

| File               | Content                              |
| ------------------ | ------------------------------------ |
| `mission.md`       | Updated mission with ARCHIVED status |
| `execution-log.md` | Full execution history               |
| `deviations.md`    | Documented differences from spec     |

### Step 4: Remove from Active

```bash
rm missions/active/{YYYY-MM-DD}-{slug}.md
```

### Step 5: Update missions/README.md

Remove from active list, add to completed count.

---

## 6. Instance Handoff Protocol

### At Session Start

1. Check `missions/active/` for in-progress work
2. Read execution log to understand last state
3. Continue from where previous instance left off
4. Log session start in execution log

### At Session End (Normal)

1. Update execution log with progress
2. If mission complete: archive
3. If incomplete: document stopping point

### At Session End (Interrupted)

1. Execution log should be append-only during work
2. Next instance can pick up from log entries

### Context Preservation

Key information to preserve:

- Current objective being worked on
- Files modified
- Decisions made
- Blockers encountered

---

## 7. Linear Integration (Future)

> To be implemented when automation matures.

| Mission Event     | Linear Action       |
| ----------------- | ------------------- |
| Mission created   | Create parent issue |
| Objective added   | Create sub-issue    |
| Mission completed | Close parent issue  |
| Deviation logged  | Add comment         |

---

## 8. Examples

### Example 1: Repository Init Mission

**Archived at**: `history/2025/Q4/missions/claude-code-mission-init/`

This was the first mission executed, establishing this standard.

---

## 9. Quality Gates

Before archiving, verify:

- [ ] All success criteria have evidence
- [ ] Execution log is complete
- [ ] Deviations documented
- [ ] Lessons learned captured
- [ ] Files in correct archive location

---

## Changelog

| Version       | Date       | Changes                                                                 |
| ------------- | ---------- | ----------------------------------------------------------------------- |
| 0.0.3-alpha.0 | 2025-12-22 | Extracted template to `templates/missions/`, added type system          |
| 0.0.2-alpha.0 | 2025-12-22 | Added Claiming Protocol (Section 2.3), `claimed_at`/`claimed_by` fields |
| 0.0.1-alpha.0 | 2025-12-21 | Initial version based on first mission                                  |

---

_Status: ACTIVE — Standard in use, will evolve with practice._
