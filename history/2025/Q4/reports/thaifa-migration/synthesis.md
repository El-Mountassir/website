# Synthesis — Thaifa Migration Strategy

## Integration Strategy

The migration follows a **Progressive Consolidation** approach:

```
Phase 1: Secure Critical Data (P0)
    → admin/, CLAUDE.md enrichment, lessons-learned

Phase 2: Migrate Operational Content (P1)
    → assets/, communication/, reports archive, task conversion

Phase 3: Adapt Structure (P2)
    → templates, sub-projects → missions, docs structure

Phase 4: Cleanup (P3)
    → Delete verified duplicates, archive OLD path
```

---

## Target Structure

After migration, `projects/thaifa/` should look like:

```
projects/thaifa/
├── CLAUDE.md                    # Enriched with OLD operational context
├── state/                       # KEEP AS-IS (already migrated, English)
│   ├── baseline/
│   ├── current/
│   ├── execution/
│   ├── historical/
│   └── planned/
├── admin/                       # FROM OLD
│   ├── client/
│   │   └── PROFILE.md
│   ├── credentials.md           # Protected
│   └── contacts.md
├── assets/                      # FROM OLD
│   └── images/
├── communication/               # FROM OLD
│   └── whatsapp/
├── docs/                        # FROM OLD (adapted)
│   ├── lessons-learned.md
│   ├── services-transport.md
│   └── templates/
│       └── report-style.css
└── .claude/                     # NEW structure for active work
    ├── input/
    └── output/
```

**Note**: `tasks/` NOT migrated as folder - converted to Linear + missions

---

## Uncertainties

1. **TODOs.md conversion scope** - Need to read file to determine which items are:
   - Still relevant (→ Linear or missions)
   - Already completed (→ discard)
   - Blocked (→ note in blockers.md)

2. **Sub-projects status**:
   - `booking-hotelrunner/` - Is this active or completed?
   - `jisr-mokawala/` - What's the status?

3. **Reports archive value** - Some `.claude/output/` reports may be redundant with state/ snapshots

---

## Failure Modes

| Risk | Impact | Mitigation |
|------|--------|------------|
| Credentials exposed in git | High | Verify .gitignore before commit |
| Data loss during cleanup | Medium | Full backup before deleting OLD |
| Path references broken | Low | Search/replace old paths |
| Client work disrupted | High | Complete before RDV 22 Dec 10:00 |

---

## Mission Breakdown

Based on analysis, I recommend **3 missions**:

### Mission 1: Thaifa Migration - Critical Data (P0)

**Scope**:
- Migrate `admin/` folder (credentials, profile, contacts)
- Enrich `CLAUDE.md` with OLD operational context
- Migrate `docs/lessons-learned.md`
- Delete duplicate `state/` from OLD path

**Success Criteria**:
- All protected data in NEW path
- CLAUDE.md has full operational context
- OLD state/ deleted

**Estimate**: 30 min

---

### Mission 2: Thaifa Migration - Operational Content (P1)

**Scope**:
- Migrate `assets/` folder
- Migrate `communication/` folder
- Migrate `docs/templates/` folder
- Create `.claude/input/` and `.claude/output/` structure
- Archive OLD reports to `history/2025/Q4/reports/thaifa-*/`

**Success Criteria**:
- All assets accessible in NEW path
- Communication history preserved
- Reports archived in org structure

**Estimate**: 45 min

---

### Mission 3: Thaifa Migration - Task Conversion & Cleanup (P2)

**Scope**:
- Read `tasks/TODOs.md` and triage:
  - P0/P1 items → Create in Linear
  - Multi-step items → Create as missions/
  - Completed → Discard
- Review sub-projects status
- Final backup of OLD path
- Delete OLD path (after Omar approval)

**Success Criteria**:
- All actionable items tracked in Linear or missions/
- OLD path safely archived or deleted
- Single source of truth established

**Estimate**: 1 hour

---

## Immediate Next Step

Create the 3 missions in `missions/queue/` and await Omar's prioritization.

---

## Alternative: Single Comprehensive Mission

If Omar prefers, all 3 phases could be a single mission with clear sub-tasks. This simplifies tracking but may be harder to interrupt/resume.
