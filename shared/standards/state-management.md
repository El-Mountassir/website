# State Management Standard

> **Standard for managing project and context state across El-Mountassir organization.**

---

## Purpose

State management provides a **Single Source of Truth (SSOT)** for tracking:

- Current state of projects, systems, or contexts
- Historical changes and decisions
- Planned actions awaiting validation
- Execution logs for traceability

---

## Directory Structure

```
state/
├── README.md              # Main index with quick navigation
├── current/               # WHAT IS NOW (live snapshots)
├── baseline/              # WHAT WAS (before changes)
├── planned/               # WHAT WILL BE (pending validation)
├── execution/             # WHAT WAS DONE (action logs)
└── historical/            # CHANGES OVER TIME (changelogs, decisions)
```

---

## Directory Purposes

| Directory     | Purpose                     | Mutability                   |
| ------------- | --------------------------- | ---------------------------- |
| `current/`    | Live state snapshots        | Updated on each state change |
| `baseline/`   | Pre-change snapshots        | **Immutable** after creation |
| `planned/`    | Proposals awaiting approval | Editable until executed      |
| `execution/`  | Action logs by date         | **Append-only**              |
| `historical/` | Changelogs and decisions    | **Append-only**              |

---

## File Naming Conventions

| Type              | Pattern                      | Example                            |
| ----------------- | ---------------------------- | ---------------------------------- |
| Current state     | `{category}.md`              | `promotions.md`, `reservations.md` |
| Baseline snapshot | `{category}-{YYYY-MM-DD}.md` | `promotions-2025-12-20.md`         |
| Execution log     | `{YYYY-MM-DD}/{category}.md` | `2025-12-20/promotions.md`         |
| Changelog         | `changelog-{category}.md`    | `changelog-promotions.md`          |
| Decision log      | `decisions.md`               | Single file per state folder       |

---

## Update Rules

### current/

- Update immediately when state changes
- Include "Last updated" timestamp
- Cross-reference to execution logs when applicable

### baseline/

- Create BEFORE making major changes
- **Never modify after creation**
- Include snapshot date and context

### planned/

- Create for proposals needing validation
- Include validation checkboxes for approver
- Move to execution/ once approved and executed

### execution/

- One folder per date: `YYYY-MM-DD/`
- One file per action category
- **Append-only** — never edit past entries
- Include timestamps, operator, and verification steps

### historical/

- Changelogs in reverse chronological order (newest first)
- Link to baseline and execution files
- Document lessons learned in `decisions.md`

---

## Required Metadata

Each file should include:

```markdown
# Title

**Last updated**: YYYY-MM-DD HH:mm
**Source**: [Origin of the data]
**Status**: [Current status if applicable]

---
```

---

## Linking Conventions

### Internal links

Use relative paths:

```markdown
→ [Current state](../current/promotions.md)
→ [Baseline](../baseline/promotions-2025-12-20.md)
```

### External references

```markdown
**Source of truth**: [state/current/promotions.md](../state/current/promotions.md)
```

---

## When to Create Snapshots

Create a baseline snapshot BEFORE:

- Major configuration changes
- Bulk updates or cleanups
- System migrations
- Any action that changes multiple items

---

## Template Files

See `templates/state/` for generic templates that can be copied for new projects.

---

## Example: Project State Structure

```
projects/thaifa/state/
├── README.md
├── current/
│   ├── README.md
│   ├── promotions.md
│   ├── reservations.md
│   └── rooms.md
├── baseline/
│   ├── README.md
│   └── promotions-2025-12-20.md
├── planned/
│   ├── README.md
│   └── pricing.md
├── execution/
│   ├── README.md
│   └── 2025-12-20/
│       └── promotions.md
└── historical/
    ├── README.md
    ├── changelog-promotions.md
    └── decisions.md
```

---

_State Management Standard v0.1.0_
_El-Mountassir Organization_
