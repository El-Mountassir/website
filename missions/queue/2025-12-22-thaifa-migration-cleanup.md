# Mission: Thaifa Migration - Task Conversion & Cleanup (P2)

```yaml
mission_id: 2025-12-22-thaifa-migration-cleanup
status: QUEUED
assigned_to: Claude Code
created: 2025-12-22
assigned: 2025-12-22
completed:
archived:
priority: P2
depends_on: 2025-12-22-thaifa-migration-operational
```

---

## Context

Final phase of Thaifa migration:
1. Convert OLD tasks to Linear or missions
2. Handle sub-projects (booking-hotelrunner, jisr-mokawala)
3. Clean up or archive OLD path

---

## Objectives

- [ ] Read `tasks/TODOs.md` and triage items
- [ ] Create Linear issues for P0/P1 tactical items
- [ ] Convert multi-step items to missions if needed
- [ ] Evaluate `projects/2025-12_booking-hotelrunner/` status
- [ ] Evaluate `projects/jisr-mokawala/` status
- [ ] Create full backup of OLD path
- [ ] Delete or archive OLD path (after Omar approval)
- [ ] Update `missions/README.md` to reflect Thaifa migration

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | TODOs.md triaged | ⬜ | Documented decisions |
| 2 | Active items in Linear or missions | ⬜ | Linear issues / mission files |
| 3 | Sub-projects handled | ⬜ | Archived or converted |
| 4 | OLD path backed up | ⬜ | Backup location documented |
| 5 | OLD path removed/archived | ⬜ | Path no longer exists |
| 6 | Single source of truth established | ⬜ | Only NEW path exists |

---

## Constraints

- Requires Omar approval before deleting OLD path
- Need to verify nothing valuable is lost
- Linear integration for task items

---

## Task Triage Matrix

| Item Type | Action |
|-----------|--------|
| P0 tactical (< 1 day) | → Linear |
| P1 tactical (< 1 day) | → Linear |
| Multi-step work | → missions/ |
| Completed items | → Discard |
| Blocked items | → Document in blockers.md |
| Obsolete items | → Discard |

---

## Execution Log

> Append-only. Add entries as work progresses.

### 2025-12-22

- Mission created from scout analysis

---

## Deviations

_None yet_

---

## Lessons Learned

_To be filled after completion_

---

_Mission v0.0.1-alpha.0_
