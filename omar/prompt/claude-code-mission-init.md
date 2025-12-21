# Mission: Initialize El-Mountassir Repository & Configure Calendar

## Context

You are Claude Code, executing for Omar El Mountassir. This is the initial setup of the El Mountassir organization repository.

**Location:** `/home/omar/Work/El-Mountassir` (already created, currently empty)

**Chrome:** Open with Google Calendar tab logged in as omar@el-mountassir.com

---

## Mission Objectives

### Phase 1: Create Repository Structure

Create the following folder structure:

```
El-Mountassir/
├── CLAUDE.md                # Copy from provided content below
├── ROADMAP.md               # Create minimal placeholder
├── INDEX.md                 # Create minimal placeholder
├── LESSONS-LEARNED/
│   └── .gitkeep
│
├── docs/
│   ├── standards/
│   │   └── calendar-standards.md   # Copy from provided content below
│   └── reference/
│       └── .gitkeep
│
├── system/
│   ├── prompts/
│   │   └── claude-web-system-prompt.md  # Placeholder for now
│   └── agents/
│       └── .gitkeep
│
├── projects/
│   ├── thaifa/
│   │   └── CLAUDE.md        # Create project-specific context
│   └── gagliano/
│       └── CLAUDE.md        # Create project-specific context
│
├── admin/
│   ├── time/
│   │   └── .gitkeep
│   ├── finance/
│   │   └── .gitkeep
│   └── legal/
│       └── .gitkeep
│
└── learning/
    ├── tac/
    │   └── .gitkeep
    ├── pac/
    │   └── .gitkeep
    └── zte/
        └── .gitkeep
```

### Phase 2: Initialize Git

```bash
cd /home/omar/Work/El-Mountassir
git init
git add .
git commit -m "chore: initial repository structure"
```

### Phase 3: Configure Google Calendar (via Chrome)

Use Chrome integration to configure Omar's Google Calendar:

#### 3.1 Enable "Speedy Meetings"

1. Navigate to Google Calendar Settings
2. Go to "Event settings"
3. Enable "Speedy meetings" (30 min → 25 min, 60 min → 50 min)

#### 3.2 Create Protected Time Blocks (Recurring)

Create these recurring events on the PRIMARY calendar:

| Event                     | Days    | Time        | Color           | Type                                   |
| ------------------------- | ------- | ----------- | --------------- | -------------------------------------- |
| `FOCUS - Deep Work Block` | Mon-Fri | 10:30-13:00 | Grape (Purple)  | Focus Time                             |
| `BREAK - Lunch`           | Mon-Fri | 13:00-14:30 | Graphite (Gray) | Out of Office                          |
| `FOCUS - Night Deep Work` | Mon-Thu | 21:00-00:00 | Grape (Purple)  | Focus Time (optional, no auto-decline) |

**Settings for Focus Time blocks:**

- Auto-decline meetings: Yes (for morning block)
- Visibility: Public

**Settings for Lunch block:**

- Auto-decline meetings: Yes
- Visibility: Public

#### 3.3 Verify Existing Events

- Confirm "RDV - Villa Thaifa" on Dec 22 (10:00-15:00) exists and is properly colored (Red/Tomato)

---

## Files to Create

### CLAUDE.md (root)

[Omar will paste the content - it's the org-level CLAUDE.md]

### ROADMAP.md (placeholder)

```markdown
# ROADMAP — El Mountassir

> **Source of truth for priorities and phases.**

---

## Current Phase

> LEARN FIRST, THEN BUILD.

---

## Immediate (This Week)

- [x] Initialize repository structure
- [x] Configure Google Calendar basics
- [ ] Complete TAC Module 1
- [ ] Setup Linear integration
- [ ] Deploy docs site to Vercel

---

## Short Term (This Month)

- [ ] Complete TAC course
- [ ] Establish daily/weekly rhythms
- [ ] Client project organization (Thaifa, Gagliano)

---

## Medium Term (Q1 2026)

- [ ] PAC course
- [ ] First agent deployment
- [ ] ZTE exploration

---

_ROADMAP.md v0.0.1-alpha.0_
```

### INDEX.md (placeholder)

```markdown
# INDEX — El Mountassir

> **Master index for quick reference.**

---

## Areas

| ID  | Area          | Path        | Description                   |
| --- | ------------- | ----------- | ----------------------------- |
| A1  | Documentation | `docs/`     | Standards, reference material |
| A2  | System        | `system/`   | Prompts, agent configs        |
| A3  | Projects      | `projects/` | Client work                   |
| A4  | Admin         | `admin/`    | Life administration           |
| A5  | Learning      | `learning/` | Courses, practice             |

---

## Active Projects

| ID  | Project      | Client          | Path                 | Status           |
| --- | ------------ | --------------- | -------------------- | ---------------- |
| P1  | Villa Thaifa | Said Thaifa     | `projects/thaifa/`   | Active           |
| P2  | Cash Depot   | Robert Gagliano | `projects/gagliano/` | Pending response |

---

## Standards

| ID  | Standard        | Path                                       | Version       |
| --- | --------------- | ------------------------------------------ | ------------- |
| S1  | Calendar        | `docs/standards/management/time/README.md` | 0.0.2-alpha.0 |
| S2  | Work Management | `docs/standards/work-management.md`        | TBD           |

---

_INDEX.md v0.0.1-alpha.0_
```

### projects/thaifa/CLAUDE.md

```markdown
# CLAUDE.md — Villa Thaifa Project

> **Project-specific context for Villa Thaifa.**

---

## Project Overview

| Field   | Value                  |
| ------- | ---------------------- |
| Client  | Said Thaifa            |
| Project | Villa Thaifa           |
| Type    | Hospitality / IT Audit |
| Status  | Active                 |

---

## Key Contacts

| Role  | Name        | Contact |
| ----- | ----------- | ------- |
| Owner | Said Thaifa | [TBD]   |

---

## Current Focus

- IT Audit
- Meeting scheduled: Dec 22, 2025 (10:00-15:00)

---

## Important Context

[To be filled after Dec 22 meeting]

---

_CLAUDE.md v0.0.1-alpha.0_
```

### projects/gagliano/CLAUDE.md

```markdown
# CLAUDE.md — Gagliano Project

> **Project-specific context for Gagliano / Cash Depot.**

---

## Project Overview

| Field   | Value                   |
| ------- | ----------------------- |
| Client  | Robert Gagliano         |
| Project | Cash Depot              |
| Type    | Web Application Demo    |
| Status  | Pending client response |

---

## Key Links

| Resource | URL                           |
| -------- | ----------------------------- |
| Demo     | https://cashdepot.vercel.app/ |

---

## Timeline

| Date         | Event                                        |
| ------------ | -------------------------------------------- |
| Dec 12, 2025 | Demo delivered                               |
| Dec 12, 2025 | Robert: will review with brother             |
| Dec 15, 2025 | Omar: acknowledged                           |
| Dec 19, 2025 | Robert: busy week, meeting Wed or week after |
| Dec 21, 2025 | Awaiting Omar's response to schedule         |

---

## Next Action

**Omar needs to respond to Robert to schedule meeting.**

---

_CLAUDE.md v0.0.1-alpha.0_
```

---

## Success Criteria

1. ✅ Folder structure created
2. ✅ Git initialized with first commit
3. ✅ Google Calendar "Speedy meetings" enabled
4. ✅ Recurring focus blocks created
5. ✅ Recurring lunch block created
6. ✅ All CLAUDE.md files in place

---

## Notes

- Use Chrome integration (`--chrome` flag) for calendar configuration
- Create minimal, functional files — we iterate from there
- Don't over-engineer — this is alpha, we'll improve

---

_Mission prepared by Claude Web for Claude Code CLI_
_Date: 2025-12-21_
