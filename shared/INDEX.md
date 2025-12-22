# Shared Resources Index

> **Central discovery point for ALL agents and humans.**
> Everything in `shared/` is accessible to any agent (Claude, Gemini, Codex, future).

---

## Purpose

`shared/` contains resources that:
1. Are NOT specific to any single agent implementation
2. MUST be accessible to all agents (current and future)
3. Represent collective knowledge of the organization

---

## Directory Structure

```
shared/
├── INDEX.md              # You are here
├── user/                 # Human context (future-proof for multi-user)
│   └── preferences.md    # Current user's preferences for AI interaction
├── philosophy/           # Operational philosophy (all agents share)
│   └── 2026-playbook.md  # The Collective's 2026 operational philosophy
├── memory/               # Collective memory (all agents contribute)
│   ├── episodes.md       # Significant events
│   ├── decisions.md      # Decisions with reasoning
│   ├── patterns.md       # Reusable patterns
│   └── facts.md          # Persistent knowledge
└── standards/            # Organizational standards
    ├── INDEX.md          # Standards hub
    ├── confidence-system.md
    ├── project-standards.md
    └── management/
        ├── missions/
        ├── time/
        └── work/
```

---

## Quick Access

### For Understanding the User

| Resource | Path | Purpose |
|----------|------|---------|
| User Preferences | `shared/user/preferences.md` | How the user wants to interact with AI |

### For Operational Philosophy

| Resource | Path | Purpose |
|----------|------|---------|
| 2026 Playbook | `shared/philosophy/2026-playbook.md` | Year of Trust: Our 10 commitments for agentic engineering |

### For Collective Memory

| Resource | Path | Purpose |
|----------|------|---------|
| Episodes | `shared/memory/episodes.md` | What happened (successes, failures) |
| Decisions | `shared/memory/decisions.md` | What was decided and WHY |
| Patterns | `shared/memory/patterns.md` | Reusable approaches |
| Facts | `shared/memory/facts.md` | Persistent knowledge |

### For Standards

| Resource | Path | Purpose |
|----------|------|---------|
| Confidence System | `shared/standards/confidence-system.md` | How to express certainty |
| Project Standards | `shared/standards/project-standards.md` | SemVer, Dublin Core, Changelog |
| Work Management | `shared/standards/management/work/README.md` | DoR, DoD, Task lifecycle |
| Missions | `shared/standards/management/missions/README.md` | Multi-step work packages |
| Time Management | `shared/standards/management/time/README.md` | Calendar, appointment tiers |

---

## Access Patterns

### Reading (All Agents)

All agents can read any file in `shared/`. No restrictions.

```markdown
# Example: Check user preferences before acting
Read shared/user/preferences.md
```

### Writing (All Agents, Logged)

All agents can write to `shared/`, but writes MUST be logged:

```markdown
## [YYYY-MM-DD] Entry Title

**Author**: [Agent name or "Human"]
**Context**: Why this was added

Content here.
```

---

## What Goes Where

| Content Type | Location | Example |
|--------------|----------|---------|
| User preferences | `shared/user/` | Communication style, priorities |
| Operational philosophy | `shared/philosophy/` | 2026 Playbook, commitments |
| Org-wide decisions | `shared/memory/decisions.md` | Architecture choices |
| Reusable patterns | `shared/memory/patterns.md` | Verification workflows |
| Standards | `shared/standards/` | Confidence system, SemVer |
| Agent-specific config | `.{agent}/` | Claude rules, Gemini settings |
| Human-specific (private) | `omar/` | Personal context, goals |

---

## For New Agents

If you're a new agent joining the system:

1. **Read this INDEX first** — Understand what's available
2. **Read `shared/user/preferences.md`** — Know your human
3. **Read `shared/philosophy/2026-playbook.md`** — Understand our operational philosophy
4. **Check `shared/memory/decisions.md`** — Understand past choices
5. **Follow `shared/standards/confidence-system.md`** — Express certainty properly

---

_v1.0.0 — Created 2025-12-22_
