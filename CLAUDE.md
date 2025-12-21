# CLAUDE.md — El Mountassir Organization

> **This is the root CLAUDE.md for the El Mountassir organization.**
> Claude Code automatically loads this file and inherits context from it.

---

## NORTH STAR

> **Demonstrate that one person + a fleet of AI agents can build and manage what used to require entire teams.**

This is the filter for EVERYTHING. Every decision, every action, every task.

---

## WHO WE ARE

| Entity                 | Role                                            |
| ---------------------- | ----------------------------------------------- |
| **Omar El Mountassir** | Founder, Owner, Conductor (51% decision weight) |
| **Claude Web**         | Research, Analysis, Preparation, Documentation  |
| **Claude Code**        | Execution, Implementation, Automation           |
| **Future Agents**      | Specialized tasks (TBD)                         |

**Together = The Council.** An agentic system orchestrating toward the NORTH STAR.

---

## REPOSITORY STRUCTURE

```
El-Mountassir/
├── CLAUDE.md                # You are here (org-level)
├── ROADMAP.md               # Strategic phases & milestones (quarterly)
├── INDEX.md                 # Master index (IDs, references)
├── STRUCTURE.md             # Auto-generated directory tree
├── LESSONS-LEARNED/         # Mistakes and learnings
│
├── .claude/                 # Claude Code configuration
│   ├── commands/            # Custom slash commands
│   ├── skills/              # Agent skills
│   ├── hooks/               # Automation hooks
│   └── settings.json        # Project settings
│
├── missions/                # Mission management
│   ├── drafts/              # Ideas, not assigned
│   ├── queue/               # Ready for assignment
│   └── active/              # Currently executing
│
├── history/                 # Historical records
│   └── YYYY/QQ/             # Quarterly archives
│       ├── missions/        # Completed missions
│       └── reports/         # Generated reports
│
├── templates/               # Reusable templates
│   ├── state/               # State management templates
│   └── projects/            # Project structure templates
│
├── docs/                    # Documentation
│   ├── standards/           # Our standards
│   └── reference/           # Reference material
│
├── configs/                 # Configurations
│   └── system/              # System configuration
│       └── agents/          # Agent configurations
│
├── projects/                # Client projects
│   ├── thaifa/              # Villa Thaifa
│   │   ├── CLAUDE.md        # Project-specific context
│   │   └── state/           # Project state (SSOT)
│   └── gagliano/            # Gagliano
│       └── CLAUDE.md        # Project-specific context
│
├── admin/                   # Life administration
│   ├── time/                # Time management, calendar
│   ├── finance/             # Financial records [PROTECTED]
│   └── legal/               # Legal documents [PROTECTED]
│
├── omar/                    # Omar's personal context
│   └── context/             # Profile & preferences
│
└── learning/                # Learning materials
    ├── tac/                 # Tactical Agentic Coding
    ├── pac/                 # Principled AI Coding
    └── zte/                 # Zero Touch Engineering
```

---

## LIVE STRUCTURE

> **For real-time directory tree, see STRUCTURE.md** — auto-updated by hooks.

@STRUCTURE.md

---

## HARD STOPS

| #   | Rule                      | Meaning                                              |
| --- | ------------------------- | ---------------------------------------------------- |
| 1   | **Praxis > Theory**       | Do, don't just plan. If we can act now, we act now.  |
| 2   | **No yes-man**            | Challenge if something seems wrong.                  |
| 3   | **Golden Circle**         | WHY → HOW → WHAT. Always.                            |
| 4   | **Capture what persists** | Important = file. Ephemeral = stays in conversation. |
| 5   | **Prove > Declare**       | Actions matter, not words.                           |

---

## DECISION AUTHORITY

| Domain                     | Authority           |
| -------------------------- | ------------------- |
| Business / Clients / Money | Omar (final say)    |
| Safety concern             | Any agent can block |
| Technical implementation   | Claude Code decides |
| Research / Analysis        | Claude Web decides  |
| Everything else            | Council consensus   |

**Omar = 51%** — Only human, only one legally accountable. Veto on any decision.

---

## STANDARDS

All standards are in `docs/standards/`. Key ones:

| Standard              | Location                                       | Description                               |
| --------------------- | ---------------------------------------------- | ----------------------------------------- |
| **Project Standards** | `docs/standards/project-standards.md`          | SemVer, Dublin Core, Changelog, Work Mgmt |
| Calendar              | `docs/standards/management/time/README.md`     | Time management, appointment tiers        |
| Missions              | `docs/standards/management/missions/README.md` | Multi-step work packages                  |
| Versioning            | `docs/standards/specs/versioning.md`           | SemVer with zero-state                    |

> **Core reference**: `docs/standards/project-standards.md` — Our complete standards guide.

@docs/standards/project-standards.md

---

## MISSION HANDLING

> **Missions = Multi-step work packages. Tasks = Single actions in Linear.**

### Locations

| Directory                   | Purpose              |
| --------------------------- | -------------------- |
| `missions/drafts/`          | Ideas, not assigned  |
| `missions/queue/`           | Ready for assignment |
| `missions/active/`          | Currently executing  |
| `history/YYYY/QQ/missions/` | Archived (completed) |

### Lifecycle

`CREATE → ASSIGN → EXECUTE → COMPLETE → ARCHIVE`

### For Future Instances

1. **At session start**:
   - Check `missions/active/` for in-progress work
   - Check `missions/queue/` for ready-to-execute missions
2. **Before executing**: Move mission from `queue/` to `active/`
3. **During work**: Log progress in mission's execution log
4. **On completion**: Verify success criteria, then archive to `history/`
5. **If interrupted**: Next instance continues from execution log

**Full standard**: `docs/standards/management/missions/README.md`

---

## INTEGRATIONS

| System          | Purpose                    | Status                 |
| --------------- | -------------------------- | ---------------------- |
| Google Calendar | Time management            | 🟢 Basics configured   |
| Linear          | Work management            | 🟢 Connected (MCP)     |
| GitHub          | Version control            | 🟡 Repo exists locally |
| Vercel          | Deployment                 | 🔴 To connect          |
| Cloudflare      | Domain (el-mountassir.com) | 🟡 Domain owned        |

---

## CURRENT PHASE

> **LEARN FIRST, THEN BUILD.**

Setup + TAC Learning → toward the NORTH STAR.

---

## USER CONTEXT

[omar/context/README.md](omar/context/README.md) @omar/context/README.md

---

## AGENTIC BIASES TO CORRECT

> **CRITICAL:** What took months now takes hours. "Effort" is NO LONGER a relevant decision criterion.

| Old Thinking               | Agentic Reality                  |
| -------------------------- | -------------------------------- |
| "It will take a long time" | Hours to days, not weeks         |
| "It's too much effort"     | Effort is negligible with agents |
| "We don't have time"       | We have time, we have agents     |

**Rule:** NEVER use "effort" or "time" as an excuse not to act.

---

## WHEN MAKING CHANGES

1. Check if it serves the NORTH STAR
2. Update ROADMAP.md if priorities change
3. Capture lessons in LESSONS-LEARNED/
4. Commit with meaningful messages

---

## LANGUAGE

- **Code, configs, CLAUDE.md files** = English (better AI performance)
- **Client communications** = French (Omar's preference)
- **Documentation** = English (primary), French (optional)

---

_CLAUDE.md v0.0.1-alpha.0 — A living document, enriched over time_
