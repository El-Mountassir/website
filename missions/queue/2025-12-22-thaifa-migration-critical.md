# Mission: Thaifa Migration - Critical Data (P0)

```yaml
mission_id: 2025-12-22-thaifa-migration-critical
status: QUEUED
assigned_to: Claude Code
created: 2025-12-22
assigned: 2025-12-22
completed:
archived:
priority: P0
```

---

## Context

Two Thaifa project locations exist:
- **OLD**: `/home/omar/Documents/projects/clients/external/dossiers/villa-thaifa/` (88 files, 7.1 MB)
- **NEW**: `/home/omar/Work/El-Mountassir/projects/thaifa/` (20 files, 116 KB)

The NEW path has `state/` already migrated (translated to English). This mission migrates critical data that's missing from NEW.

**Urgency**: Client RDV scheduled for 22 Dec 2025 10:00 — work should be complete before then.

---

## Objectives

- [ ] Migrate `admin/` folder (client profile, credentials, contacts)
- [ ] Enrich `CLAUDE.md` with operational context from OLD
- [ ] Migrate `docs/lessons-learned.md`
- [ ] Delete duplicate `state/` from OLD path (NEW is authoritative)
- [ ] Verify .gitignore protects credentials

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | `admin/client/PROFILE.md` exists in NEW | ⬜ | `ls` output |
| 2 | `admin/credentials.md` exists in NEW | ⬜ | `ls` output |
| 3 | CLAUDE.md has operational context | ⬜ | Content includes comms patterns, workflow |
| 4 | `docs/lessons-learned.md` exists in NEW | ⬜ | File present |
| 5 | OLD state/ deleted | ⬜ | `ls` shows no state/ |
| 6 | Credentials protected in .gitignore | ⬜ | Grep shows pattern |

---

## Constraints

- Must complete before 22 Dec 10:00 (client RDV)
- No credential exposure in git history
- Preserve file permissions

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
