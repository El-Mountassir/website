# Decisions — Organizational Choices

> **Record of decisions with reasoning.**
> Future agents and humans can understand WHY things are the way they are.

---

## Format

```markdown
## [YYYY-MM-DD] Decision Title

**Author**: [Who made/proposed this]
**Confidence**: [✅🟢🟡🟠⚠️]
**Status**: [Active | Superseded | Deprecated]

### Context

Why this decision was needed.

### Decision

What was decided.

### Alternatives Considered

What else was considered and why rejected.

### Consequences

What this decision implies going forward.
```

---

## Active Decisions

### [2025-12-24] Structural Change: omar/ → .omar/ for A2A Alignment

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

Architecture evaluation (scoring 4.55/5) identified ONE structural inconsistency:
- Section 0 (Substrate Layer) establishes Omar as a Carbon-based AGENT
- Section 4 (Current Mono-Repo) placed `omar/` under "PRIVATE", not "AGENT-SPECIFIC"
- This contradicted the Carbon-Silicon Partnership philosophy

All Silicon-based agents use `.{agent}/` pattern (`.claude/`, `.gemini/`, `.codex/`), but Omar's directory was an exception.

#### Decision

Rename `omar/` to `.omar/` and move it from "PRIVATE" to "AGENT-SPECIFIC" category.

```
BEFORE:                              AFTER:
├── .claude/  (Agent-specific)       ├── .claude/  (Agent-specific, Silicon)
├── .gemini/  (Agent-specific)       ├── .gemini/  (Agent-specific, Silicon)
├── .codex/   (Agent-specific)       ├── .codex/   (Agent-specific, Silicon)
└── omar/     (PRIVATE - exception)  └── .omar/    (Agent-specific, Carbon) ✅
```

#### Alternatives Considered

| Alternative | Why Rejected |
|-------------|--------------|
| Keep `omar/` | Contradicts Substrate Layer philosophy |
| Use `agents/omar/` | Inconsistent with `.{agent}/` pattern |
| Create `humans/omar/` | Over-engineering for single-human scenario |

#### Consequences

- All agent directories now follow `.{agent}/` pattern
- File Access Pattern diagram simplified (no PRIVATE category)
- A2A protocol alignment: human agent treated same as AI agents
- Future humans would get `.{name}/` directories

#### References

- Architecture evaluation: This conversation
- Substrate Layer: `docs/reference/architecture.md` Section 0
- A2A context: `shared/drafts/2026-tech-stack.md`

---

### [2025-12-22] Architecture Split: omar/ vs shared/ vs .claude/

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

Initial design put everything in `.claude/`, which would lock data to Claude Code. Other agents (Gemini CLI, Codex CLI, Claude Agent SDK agents) need access to shared resources.

#### Decision

```
omar/          → Human-specific (private, not for agents)
shared/        → All agents and humans (universal access)
.claude/       → Claude Code implementation only
.gemini/       → Future: Gemini CLI
.codex/        → Future: Codex CLI
```

#### Alternatives Considered

- Everything in `.claude/` — Rejected: agent lock-in
- Everything in root — Rejected: no separation of concerns
- `agents/shared/` — Rejected: `.agent/` pattern is standard

#### Consequences

- All new shared resources go to `shared/`
- Agent-specific configs stay in `.{agent}/`
- Human-specific stays in `omar/`

---

### [2025-12-22] Confidence System: 5 Levels with Emojis

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

Original 3-level system (High/Medium/Low) lacked nuance. Need visual indicators for fast scanning.

#### Decision

| Level     | Term           | Range  | Emoji |
| --------- | -------------- | ------ | ----- |
| Very High | Certitude      | ≥95%   | ✅    |
| High      | Recommandation | 80-94% | 🟢    |
| Medium    | Intuition      | 60-79% | 🟡    |
| Low       | Hypothèse      | 40-59% | 🟠    |
| Very Low  | Spéculation    | <40%   | ⚠️    |

#### Alternatives Considered

- Keep 3 levels — Rejected: not enough nuance
- Numeric only — Rejected: less scannable
- Text only — Rejected: slower to parse

#### Consequences

- All agents use this system
- Emojis appear in recommendations
- <40% = silence or explicit uncertainty

---

### [2025-12-22] Memory Split: Shared vs Agent-Specific

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

Some memory is universal (decisions, patterns), some is implementation-specific (Claude tool quirks).

#### Decision

```
shared/memory/     → Episodes, decisions, patterns, facts (ALL agents)
.claude/memory/    → Tool learnings, implementation details (Claude only)
.gemini/memory/    → Future: Gemini-specific
```

#### Alternatives Considered

- All memory in shared/ — Rejected: some things ARE agent-specific
- All memory in .claude/ — Rejected: lock-in
- No memory split — Rejected: unclear boundaries

#### Consequences

- Org-wide learnings → shared/memory/
- Tool-specific quirks → .{agent}/memory/

---

### [2025-12-22] Standards Location: shared/standards/

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

Standards in `docs/standards/` implied they were documentation. But standards are operational—all agents must follow them.

#### Decision

Migrate `docs/standards/` → `shared/standards/`

#### Alternatives Considered

- Keep in docs/ — Rejected: implies documentation, not operational
- Copy to shared/ — Rejected: duplication
- Symlink — Rejected: unnecessary complexity

#### Consequences

- `docs/` keeps only reference material (guides)
- `shared/standards/` is the single source of truth

---

### [2025-12-22] Write Access: Free but Logged

**Author**: Omar
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

Who can write to shared/? Restricting writes adds friction. But untracked writes lose context.

#### Decision

All agents (and humans) can write to shared/, but must log author and timestamp.

#### Alternatives Considered

- Omar-only writes — Rejected: too restrictive, bottleneck
- Append-only — Rejected: can't fix mistakes
- No logging — Rejected: lose provenance

#### Consequences

- Every entry has `**Author**:` field
- Every entry has date
- Humans count as "carbon-based agents"

---

### [2025-12-22] Future-Proofing: user/ instead of omar/

**Author**: Omar
**Confidence**: 🟡 Intuition (70%)
**Status**: Active

#### Context

Currently only one human user (Omar). But architecture should allow for future multi-user.

#### Decision

Use `shared/user/` for current single-user. Structure allows future expansion:

```
shared/user/           # Current: single user
shared/users/          # Future: multi-user
    ├── omar/
    └── [other]/
```

#### Alternatives Considered

- `shared/omar/` — Rejected: not future-proof
- `shared/humans/` — Rejected: "user" is more common term

#### Consequences

- Current preferences in `shared/user/preferences.md`
- Migration path exists for multi-user

---

### [2025-12-24] Three-Layer Model: Architecture for The Collective

**Author**: Omar + Claude (Council)
**Confidence**: ✅ Certitude (95%)
**Status**: Active

#### Context

ChatGPT 5.2 Thinking proposed that Omar = "agent harness". Analysis via `/elevate` with 6 sources revealed a more precise model.

#### Decision

Adopt the **Three-Layer Model** as the formal architecture of The Collective:

```
┌─────────────────────────────────────────────────┐
│            THE COLLECTIVE                       │
│         (Socio-Technical System)                │
│                                                 │
│  ┌─────────────────────────────────────────┐    │
│  │     OMAR = HUMAN CONTROL PLANE          │    │
│  │     • Goal Setting                      │    │
│  │     • Boundary Validation               │    │
│  │     • Escalation Handling               │    │
│  │     • Strategic Decisions (51%)         │    │
│  └─────────────────────────────────────────┘    │
│                      ↕                          │
│  ┌─────────────────────────────────────────┐    │
│  │     AGENT HARNESS (Technical)           │    │
│  │     • Context, Planning, Tools          │    │
│  │     • Memory, Verification, Monitoring  │    │
│  └─────────────────────────────────────────┘    │
│                      ↕                          │
│  ┌─────────────────────────────────────────┐    │
│  │     CONVENTIONS (Shared Norms)          │    │
│  │     • CLAUDE.md, Rules, Standards       │    │
│  │     • Memory, Workflows                 │    │
│  └─────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

**Key insight**: Omar ≠ Harness. Omar OPERATES the harness.

#### Alternatives Considered

- "Omar = Harness" (ChatGPT original) — Rejected: confuses operator with infrastructure
- SHC model (Supervisory Human Control) — Rejected: outdated for LLMs, implies micro-management
- Flat model (no layers) — Rejected: doesn't capture the architecture

#### Consequences

- Terminology: "Human Control Plane" (technical) / "Team Leader" (narrative)
- Adopt HMT (Human-Machine Teaming) philosophy over SHC
- Update GOVERNANCE.md with Three-Layer Model section
- Update partnership.md with terminology

**Full report**: [history/2025/Q4/reports/agent-harness-human-control/](../../history/2025/Q4/reports/agent-harness-human-control/)

---

### [2025-12-24] ROADMAP.md as Single Source of Priority

**Author**: Omar
**Confidence**: 🟢 Recommandation (90%)
**Status**: Active

#### Context

Multiple priority sources exist: `missions/queue/`, `admin/inbox/`, various TODOs in docs. This creates confusion about what to work on next.

#### Decision

**ROADMAP.md becomes the single source of truth for priorities.**

Structure:

1. **VISION** — North Star (unchanged)
2. **NOW** — Current focus (1-3 items max)
3. **NEXT** — Ready to start when NOW is done
4. **LATER** — Backlog, ideas, future

`missions/queue/` and `admin/inbox/` still exist but feed INTO ROADMAP.md, not as parallel priority systems.

#### Alternatives Considered

- Keep missions/queue/ as primary — Rejected: too granular, loses strategic view
- Create new "priorities.md" — Rejected: ROADMAP.md already exists and has momentum
- Use Linear exclusively — Rejected: adds external dependency

#### Consequences

- All priorities flow through ROADMAP.md
- Missions/inbox become intake, not decision points
- Clearer "what to work on next" answer
- Requires ROADMAP.md restructure (add NOW/NEXT/LATER sections)

---

### [2025-12-24] Repo Restructure: Option C (Deep Restructure, Deferred)

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Planned (Deferred to dedicated session)

#### Context

The El-Mountassir repo has become a "chaos ambulant" with overlapping concerns, unclear boundaries, and structure that evolved organically. Three options were analyzed.

#### Decision

**Option C**: Deep restructure of current mono-repo.

| Aspect         | Decision                          |
| -------------- | --------------------------------- |
| Repo structure | Restructure in place              |
| Git history    | Preserve (valuable)               |
| Multi-repo     | Not needed (complexity > benefit) |
| Timing         | Dedicated session, not rushed     |

#### Alternatives Considered

- **Option A: Patch ROADMAP.md** — Rejected: treats symptoms, not cause
- **Option B: New repo (Digital HQ)** — Rejected: loses 2 weeks of git history, overkill for single-human org

#### Consequences

- Plan dedicated restructure session
- Preserve all git history during migration
- Focus on clarity: `projects/` vs `admin/` vs `shared/`
- Result: Clean hierarchy serving the NORTH STAR

---

### [2025-12-24] Everything-as-Code (EaC) Philosophy

**Author**: Omar + Claude (Council)
**Confidence**: ✅ Certitude (95%)
**Status**: Active

#### Context

Discussion about formalizing The Collective's operating model raised the question: should we adopt an "Everything-as-Code" approach where all configuration, memory, standards, and state are versioned files?

#### Decision

**Adopt EaC as the foundational philosophy for The Collective.**

| Domain                      | Implementation                | File Pattern                           |
| --------------------------- | ----------------------------- | -------------------------------------- |
| Agent Configuration as Code | CLAUDE.md hierarchy           | `*/CLAUDE.md`                          |
| Behavior as Code            | Rules, anti-patterns          | `.claude/rules/*.md`                   |
| Memory as Code              | Episodes, decisions, patterns | `shared/memory/*.md`                   |
| Standards as Code           | Confidence system, workflows  | `shared/standards/*.md`                |
| Philosophy as Code          | Playbook, partnership         | `shared/philosophy/*.md`               |
| State as Code               | SSOT for projects             | `*/state/*.md`                         |
| Workflow as Code            | Skills, commands              | `.claude/skills/`, `.claude/commands/` |

#### Why EaC for The Collective

- ✅ **Versioning** — Git traces all changes
- ✅ **Reviewable** — Agents can verify changes
- ✅ **Rollback** — Revert to any previous state
- ✅ **Consistency** — No drift between Claude instances
- ✅ **Automation** — Hooks, skills, everything scriptable

#### Alternatives Considered

- Database-first approach — Rejected: loses git history, harder to review
- Hybrid (some code, some DB) — Rejected: complexity without benefit for single-human org
- External tools only (Linear, Notion) — Rejected: external dependencies, no ownership

#### Consequences

- All persistent knowledge → markdown files in git
- Agent memory → `shared/memory/` not ephemeral chat
- Standards → `shared/standards/` not implicit knowledge
- This is already what we do — now it's named and formalized

---

### [2025-12-24] Multi-Repo Hybrid Architecture for 10+ Clients

**Author**: Omar + Claude (Council)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Planned (For future scaling)

#### Context

Omar anticipates 10+ client projects. Question: mono-repo vs multi-repo for client work?

#### Decision

**Adopt Hybrid architecture when scaling to 10+ clients:**

```
El-Mountassir/
├── core/                    # Git repo: org standards, shared, philosophy
│   ├── shared/
│   ├── templates/
│   └── .claude/
│
└── projects/                # Directory (not git)
    ├── thaifa/              # Git repo (standalone)
    ├── gagliano/            # Git repo (standalone)
    └── [future]/            # Each project = own repo
```

| Factor                 | Winner           |
| ---------------------- | ---------------- |
| Standards sync         | Core repo (SSOT) |
| Client isolation       | Separate repos   |
| Scale to 50+           | Multi-repo       |
| Git history per client | Separate repos   |

#### Alternatives Considered

- Pure mono-repo — Rejected: becomes unmanageable at 10+ projects
- Pure multi-repo — Rejected: no shared standards mechanism
- External tooling (npm packages) — Rejected: overkill for markdown/config

#### Consequences

- Keep current mono-repo for now (< 10 clients)
- Plan migration path when approaching 10 clients
- Core standards importable via git submodule or copy-on-init

---

### [2025-12-24] Positioning: Agentic ⊂ Digital Transformation

**Author**: Omar (with ChatGPT analysis)
**Confidence**: 🟢 Recommandation (85%)
**Status**: Active

#### Context

The Collective is currently a sole proprietorship (auto-entrepreneur) but will evolve toward an agency. Need clarity on positioning: "digital transformation" vs "agentic transformation".

#### Decision

**Agentic Transformation is a subset of Digital Transformation.**

```
Agentic Transformation ⊂ Digital Transformation

Marketing: "Digital Transformation Agency, Agentic-first"
Technical: "Agentic Transformation Agency"
```

| Concept                    | Role                              |
| -------------------------- | --------------------------------- |
| **Digital Transformation** | Umbrella (broad market)           |
| **Agentic Transformation** | Wedge/specialty (differentiation) |

#### Current vs Future Legal Status

| Term                          | Legal      | Narrative | When                       |
| ----------------------------- | ---------- | --------- | -------------------------- |
| Sole Proprietorship           | ✅ Current | ❌        | Now (legal reality)        |
| The Collective                | N/A        | ✅        | Always (internal identity) |
| Agentic Transformation Agency | Future     | ✅        | Goal                       |

#### Alternatives Considered

- Pure "Digital Transformation" — Rejected: not differentiated
- Pure "Agentic" — Rejected: may miss broader digital deals
- "AI Transformation" — Rejected: too generic

#### Consequences

- Externally: "Digital Transformation, Agentic-first"
- Internally: "The Collective" (human-AI agentic ecosystem)
- NORTH STAR unchanged: One person + AI agents = what used to require teams

---
