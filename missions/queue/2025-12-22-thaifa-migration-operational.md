# Mission: Thaifa Migration - Operational Content (P1)

```yaml
mission_id: 2025-12-22-thaifa-migration-operational
status: QUEUED
assigned_to: Claude Code
created: 2025-12-22
assigned: 2025-12-22
completed:
archived:
priority: P1
depends_on: 2025-12-22-thaifa-migration-critical
```

---

## Context

After critical data is migrated (Mission 1), this mission handles operational content:
- Assets (images, documents)
- Communication logs (WhatsApp)
- Templates and docs
- Report archival

---

## Objectives

- [ ] Migrate `assets/` folder (4 images)
- [ ] Migrate `communication/` folder (WhatsApp logs)
- [ ] Migrate `docs/templates/` (CSS + report templates)
- [ ] Migrate `docs/services-transport.md`
- [ ] Create `.claude/input/` and `.claude/output/` structure
- [ ] Archive OLD reports to `history/2025/Q4/reports/thaifa-*/`

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | `assets/images/` contains 4 images | ⬜ | `ls` output |
| 2 | `communication/whatsapp/` exists | ⬜ | `ls` output |
| 3 | `docs/templates/report-style.css` exists | ⬜ | File present |
| 4 | `.claude/input/` and `.claude/output/` exist | ⬜ | `ls` output |
| 5 | OLD reports archived | ⬜ | Files in history/ |

---

## Constraints

- Depends on Mission 1 completion
- Preserve file timestamps where possible
- Report organization follows org structure (history/YYYY/QQ/)

---

## Files to Migrate

| Source (OLD) | Destination (NEW) |
|--------------|-------------------|
| `assets/` | `projects/thaifa/assets/` |
| `communication/` | `projects/thaifa/communication/` |
| `docs/templates/` | `projects/thaifa/docs/templates/` |
| `docs/services-transport.md` | `projects/thaifa/docs/services-transport.md` |
| `.claude/output/2025/Q4/reports/*` | `history/2025/Q4/reports/thaifa-*` |

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
