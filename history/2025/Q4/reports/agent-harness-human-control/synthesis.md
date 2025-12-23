# Synthesis: The Collective's Operating Model

**Date**: 2025-12-24
**Topic**: Agent Harness & Human Control Plane
**Phase**: 3 of 4

---

## The Core Question

> **Should we adopt/adapt the "agent harness" concept for The Collective?**

**Answer**: ✅ **YES, with refinements.**

ChatGPT's initial framing was partially correct but needed adjustment. Here's the refined model based on 6 cross-referenced sources.

---

## What ChatGPT Got Right

| Claim | Validation |
|-------|------------|
| Agent harness = infrastructure around the model | ✅ Confirmed by all sources |
| Omar provides supervision and governance | ✅ Confirmed — but "supervision" is outdated term |
| Harness includes: context, tools, memory, verification | ✅ Confirmed (Parallel.ai: 6 components) |
| Omar is the "human layer" in the system | ✅ Confirmed — better term: "Human Control Plane" |

## What ChatGPT Got Wrong

| Claim | Correction |
|-------|------------|
| "Omar = the harness" | ❌ Omar is NOT the harness. Omar OPERATES the harness. |
| Supervisory framing | ❌ SHC (Supervisory Human Control) is outdated for LLMs. Use HMT (Human-Machine Teaming). |
| Harness is just technical | ❌ The complete system is socio-technical: harness + human + conventions. |

---

## The Refined Model: Three Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    THE COLLECTIVE                           │
│              (Socio-Technical System)                       │
│  ┌───────────────────────────────────────────────────────┐  │
│  │           OMAR: HUMAN CONTROL PLANE                   │  │
│  │                                                       │  │
│  │  • Goal Setting (WHY)                                 │  │
│  │  • Boundary Validation (LIMITS)                       │  │
│  │  • Escalation Handling (UNCERTAINTY)                  │  │
│  │  • Strategic Decisions (BUSINESS/CLIENTS/MONEY)       │  │
│  │  • Trust Calibration (AUTONOMY DIAL)                  │  │
│  │                                                       │  │
│  │  Decision Weight: 51% (only human, legally liable)    │  │
│  └───────────────────────────────────────────────────────┘  │
│                           ↕                                 │
│  ┌───────────────────────────────────────────────────────┐  │
│  │           AGENT HARNESS (Technical)                   │  │
│  │                                                       │  │
│  │  • Context Engineering (CLAUDE.md, @imports)          │  │
│  │  • Planning/Decomposition (missions, todos)           │  │
│  │  • Tool Integration (MCP, bash, APIs)                 │  │
│  │  • Memory/State (shared/memory/, state/)              │  │
│  │  • Verification (rules, triple-check)                 │  │
│  │  • Monitoring (CHANGELOG, git, history/)              │  │
│  │                                                       │  │
│  │  Implementation: Claude Code SDK + Extensions         │  │
│  └───────────────────────────────────────────────────────┘  │
│                           ↕                                 │
│  ┌───────────────────────────────────────────────────────┐  │
│  │           CONVENTIONS (Shared Norms)                  │  │
│  │                                                       │  │
│  │  • CLAUDE.md hierarchy (org → project)                │  │
│  │  • Rules (.claude/rules/*.md)                         │  │
│  │  • Standards (shared/standards/)                      │  │
│  │  • Memory (patterns, decisions, facts)                │  │
│  │  • Workflows (missions, inbox, escalation)            │  │
│  │                                                       │  │
│  │  Purpose: Shared mental model across all instances    │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Terminology Recommendation

| Context | Term to Use | Why |
|---------|-------------|-----|
| **Technical documentation** | Human Control Plane | Precise, systems-thinking |
| **Narrative/Philosophy** | Team Leader | HMT-aligned, collaborative |
| **Internal reference** | Omar | Simple, clear |
| **External explanation** | Human Operator | Industry-standard |

**Avoid**: "Supervisor" (SHC connotation, outdated), "Manager" (implies micro-management).

---

## What This Changes in Practice

### 1. Formalize Omar's Role

| Responsibility | Frequency | Mechanism |
|---------------|-----------|-----------|
| **Goal Setting** | Per mission | Mission brief, success criteria |
| **Boundary Validation** | At checkpoints | Review scope, constraints |
| **Escalation Handling** | On demand | `admin/inbox/pending.md` |
| **Strategic Decisions** | Always | Veto power (51%) |
| **Trust Calibration** | Continuously | Adjust permissions, autonomy |

### 2. Formalize the Agent Harness

The harness already exists but isn't named. Name it. Document it.

| Component | Current Implementation | Formalization |
|-----------|----------------------|---------------|
| Context | CLAUDE.md, @imports | Document the hierarchy |
| Planning | Missions, todos | Create plan templates |
| Tools | MCP, bash | Document tool access |
| Memory | shared/memory/ | Define retention policy |
| Verification | rules/*.md | Systematize self-critique |
| Monitoring | git, CHANGELOG | Add metrics if needed |

### 3. Adopt HMT Mindset

| From (SHC) | To (HMT) |
|------------|----------|
| "I supervise the agents" | "I lead a team that includes agents" |
| "Agents need approval for everything" | "Agents have autonomy within boundaries" |
| "I check every output" | "I validate goals and handle escalations" |
| "AI is a tool I use" | "AI is a partner I collaborate with" |

---

## Integration with Existing Governance

| Existing Document | How It Relates | Update Needed? |
|------------------|----------------|----------------|
| `GOVERNANCE.md` | Defines overall system | Add "Three-Layer Model" section |
| `CLAUDE.md` | Part of Conventions layer | Add reference to this model |
| `.claude/rules/partnership.md` | Already HMT-aligned | Add terminology |
| `shared/standards/confidence-system.md` | Implements escalation pattern | Already correct |
| `shared/user/preferences.md` | Defines Omar's role | Already correct |

---

## Actionable Recommendations

### Immediate (This Session)

| Action | Why | Status |
|--------|-----|--------|
| Create summary document in patterns.md | Capture the model | ✅ Done |
| Add terminology definitions | Shared vocabulary | ✅ Done (sources.md) |

### Short-Term (Next Sessions)

| Action | Why | Priority |
|--------|-----|----------|
| Add "Three-Layer Model" to GOVERNANCE.md | Formalize the architecture | 🟢 Medium |
| Create `admin/harness/README.md` | Document harness components | 🟢 Medium |
| Define Risk Stratification matrix | Clarify escalation triggers | 🟡 Low |
| Create Agent Trust Ledger | Track trust by domain | 🟡 Low |

### Long-Term (Future)

| Action | Why | Priority |
|--------|-----|----------|
| Implement learning loop | System improves from decisions | 🟡 Future |
| Add verification layer | Systematic self-critique | 🟡 Future |
| Build observability dashboard | Real-time harness monitoring | 🟡 Future |

---

## Answer to Omar's Question

> "Comment formaliser le rôle d'Omar dans 'The Collective' en utilisant la terminologie et les patterns établis du domaine multi-agent?"

**Answer**:

1. **Omar's Role** = **Human Control Plane** (technical) / **Team Leader** (narrative)
   - NOT the harness itself
   - The strategic decision layer WITHIN the socio-technical system

2. **The System** = **The Collective** (socio-technical)
   - Human Control Plane (Omar)
   - Agent Harness (Claude Code SDK + extensions)
   - Conventions (CLAUDE.md, rules, memory, standards)

3. **The Model** = **HMT (Human-Machine Teaming)**, not SHC
   - Collaborative agency, not supervision
   - Dynamic task allocation, not micro-management
   - Trust-based autonomy, not approval-for-everything

4. **Integration** = Already mostly aligned
   - `partnership.md` already uses HMT thinking
   - `confidence-system.md` implements escalation
   - CLAUDE.md encodes conventions
   - Minor updates needed for terminology consistency

---

_Next: Phase 4 - Quality Gates + Final Output_
