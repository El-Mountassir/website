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
| Level | Term | Range | Emoji |
|-------|------|-------|-------|
| Very High | Certitude | ≥95% | ✅ |
| High | Recommandation | 80-94% | 🟢 |
| Medium | Intuition | 60-79% | 🟡 |
| Low | Hypothèse | 40-59% | 🟠 |
| Very Low | Spéculation | <40% | ⚠️ |

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
