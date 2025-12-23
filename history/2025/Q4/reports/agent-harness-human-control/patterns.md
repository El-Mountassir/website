# Pattern Extraction

**Date**: 2025-12-24
**Topic**: Agent Harness & Human Control Plane
**Phase**: 2 of 4

---

## Extracted Patterns

### Pattern 1: Three-Layer Architecture

**Confidence**: ✅ HIGH (6/6 sources)

```
┌─────────────────────────────────────────────────────────┐
│             SOCIO-TECHNICAL SYSTEM                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │           HUMAN CONTROL PLANE                     │  │
│  │  • Goal setting                                   │  │
│  │  • Boundary validation                            │  │
│  │  • Escalation handling                            │  │
│  │  • Strategic decisions                            │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │              AGENT HARNESS                        │  │
│  │  • Context management                             │  │
│  │  • Tool integration                               │  │
│  │  • Memory/State                                   │  │
│  │  • Verification                                   │  │
│  │  • Monitoring                                     │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │              CONVENTIONS                          │  │
│  │  • CLAUDE.md (rules, standards)                   │  │
│  │  • Workflows                                      │  │
│  │  • Permissions                                    │  │
│  │  • Memory files                                   │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

| Layer | What It Is | Omar's Implementation |
|-------|-----------|----------------------|
| **Socio-Technical System** | The complete ecosystem | The Collective |
| **Human Control Plane** | Omar's strategic role | Goal-setting, escalation, validation |
| **Agent Harness** | Technical infrastructure | Claude Code SDK, MCP, tools |
| **Conventions** | Shared norms | CLAUDE.md, rules/, memory/ |

---

### Pattern 2: Human as Strategic Layer (HMT over SHC)

**Confidence**: ✅ HIGH (6/6 sources)

| Old Model (SHC) | New Model (HMT) |
|-----------------|-----------------|
| Human supervises every step | Human sets goals, validates boundaries |
| Human approves every action | Human handles escalations |
| Human is bottleneck | Human is strategic input |
| AI is tool | AI is partner |

**Omar's Role in HMT**:

| Responsibility | Description | Frequency |
|---------------|-------------|-----------|
| **Goal Setting** | Define WHAT to achieve | Per mission |
| **Boundary Validation** | Verify scope stays within limits | At checkpoints |
| **Escalation Handling** | Decide when agents are uncertain | As needed |
| **Strategic Decisions** | Business, clients, money | Always |
| **Trust Calibration** | Adjust autonomy based on performance | Continuously |

---

### Pattern 3: Confidence-Based Escalation

**Confidence**: ✅ HIGH (5/6 sources)

```
Agent Confidence Level → Action

✅ ≥95%  → Act autonomously
🟢 80-94% → Act, inform human
🟡 60-79% → Propose, wait confirmation (important decisions)
🟠 40-59% → Ask before acting
⚠️ <40%   → Don't act, gather information
```

**Implementation Points**:

| Component | Mechanism | Omar's Current Implementation |
|-----------|-----------|------------------------------|
| **Threshold Definition** | Configure what confidence triggers escalation | `shared/standards/confidence-system.md` |
| **Escalation Channel** | How agents reach human | `admin/inbox/pending.md` |
| **Response SLA** | Expected response time | Not defined (TO DO) |
| **Learning Loop** | System learns from decisions | Not implemented (TO DO) |

---

### Pattern 4: Six Harness Components

**Confidence**: ✅ HIGH (Parallel.ai canonical, validated by others)

| Component | Description | Omar's Implementation |
|-----------|-------------|----------------------|
| **1. Context Engineering** | Window management, RAG, summarization | CLAUDE.md hierarchy, @imports |
| **2. Planning/Decomposition** | Task breakdown, goal representation | Missions, TODO lists |
| **3. Tool Integration** | Function calling, API abstraction | MCP servers, bash tools |
| **4. Memory/State** | Short-term, long-term, episodic | shared/memory/, state/ folders |
| **5. Verification/Reflection** | Output validation, self-critique | Triple-check pattern, rules |
| **6. Monitoring/Observability** | Logging, tracing, metrics | CHANGELOG, history/, git |

**Gap Analysis**:

| Component | Current State | Gap |
|-----------|--------------|-----|
| Context Engineering | ✅ Strong | — |
| Planning | 🟢 Good | Could formalize plan templates |
| Tool Integration | ✅ Strong | — |
| Memory/State | 🟢 Good | Long-term learning not automated |
| Verification | 🟡 Partial | Self-critique not systematic |
| Monitoring | 🟡 Partial | No metrics dashboard |

---

### Pattern 5: Supervisory Checkpoints

**Confidence**: ✅ HIGH (Millward, Microsoft, CAMEL-AI)

```
Mission Flow with Checkpoints:

START → [Agent: Plan] → CHECKPOINT 1: Goal Validation
                              ↓
                        Omar validates scope
                              ↓
        [Agent: Execute] → CHECKPOINT 2: Boundary Check
                              ↓
                        Omar verifies constraints
                              ↓
        [Agent: Complete] → CHECKPOINT 3: Coherence Review
                              ↓
                        Omar reviews reasoning trace
                              ↓
                           END
```

**Checkpoint Types**:

| Checkpoint | When | What Human Reviews | Action |
|------------|------|-------------------|--------|
| **Goal Validation** | Before execution | Is the scope correct? | Approve/Redirect |
| **Boundary Check** | During execution | Are we staying within limits? | Continue/Constrain |
| **Coherence Review** | After execution | Does the reasoning make sense? | Accept/Revise |

---

### Pattern 6: Risk Stratification

**Confidence**: 🟢 MEDIUM (Microsoft, Millward)

| Risk Level | Characteristics | Human Involvement |
|------------|-----------------|-------------------|
| **High** | Payments, deletions, external comms, irreversible | HITL: Require approval |
| **Medium** | Internal changes, config updates, routine + impact | HOTL: Log, auto-approve, monitor |
| **Low** | Internal tooling, well-tested patterns, reversible | HOOTL: Autonomous |

**Omar's Risk Matrix** (proposed):

| Domain | High Risk | Medium Risk | Low Risk |
|--------|-----------|-------------|----------|
| **Clients** | Contracts, payments, promises | Status updates | Internal notes |
| **Code** | Production deploy, security | Feature branches | Local dev |
| **Data** | Deletion, external share | Internal edits | Reads |
| **Comms** | Client emails | Internal docs | Chat |

---

### Pattern 7: Trust as Capital

**Confidence**: 🟡 LOW (Tsamados, Millward only)

| Concept | Description |
|---------|-------------|
| **Trust Builds** | Successful autonomous actions → more autonomy |
| **Trust Depletes** | Errors, escalations → more oversight |
| **Trust is Asymmetric** | Harder to build than to lose |
| **Trust is Contextual** | High trust in Domain A ≠ high trust in Domain B |

**Implementation Idea**:

```markdown
## Agent Trust Ledger

| Agent | Domain | Trust Level | Last Updated | Reason |
|-------|--------|-------------|--------------|--------|
| Claude Code | Technical | 🟢 High | 2025-12-24 | Consistent quality |
| Claude Code | Client Comms | 🟡 Medium | 2025-12-23 | Needs supervision |
| Claude Code | Financial | 🟠 Low | — | Not authorized |
```

---

### Pattern 8: Convention Building

**Confidence**: 🟢 MEDIUM (Tsamados, Anthropic, Millward)

| Mechanism | Description | Omar's Implementation |
|-----------|-------------|----------------------|
| **Shared Mental Models** | Agents understand the same concepts | CLAUDE.md, taxonomies |
| **Explicit Norms** | Written rules for behavior | .claude/rules/*.md |
| **Commitment Mechanisms** | Agreements agents honor | Patterns in memory/ |
| **Feedback Loops** | Learning from outcomes | LESSONS-LEARNED/, decisions.md |

---

### Pattern 9: Dynamic Task Allocation

**Confidence**: 🟢 MEDIUM (Tsamados, CAMEL-AI, Microsoft)

| Principle | Description |
|-----------|-------------|
| **Capability-Based** | Assign based on who can do it best |
| **Adaptive** | Reallocate as conditions change |
| **Self-Organized** | Agents can spawn sub-agents |
| **Phased Rollout** | Start restrictive, loosen with trust |

**Current State**: Partially implemented via subagent spawning (Task tool).

**Gap**: No formal capability registry for agents.

---

## Pattern Summary

| # | Pattern | Confidence | Implementation Status |
|---|---------|------------|----------------------|
| 1 | Three-Layer Architecture | ✅ HIGH | 🟢 Implicit, needs formalization |
| 2 | Human as Strategic Layer | ✅ HIGH | ✅ Implemented |
| 3 | Confidence-Based Escalation | ✅ HIGH | ✅ Implemented |
| 4 | Six Harness Components | ✅ HIGH | 🟡 Partial gaps |
| 5 | Supervisory Checkpoints | ✅ HIGH | 🟡 Informal |
| 6 | Risk Stratification | 🟢 MEDIUM | 🟠 Not formalized |
| 7 | Trust as Capital | 🟡 LOW | ⚠️ Concept only |
| 8 | Convention Building | 🟢 MEDIUM | ✅ Strong |
| 9 | Dynamic Task Allocation | 🟢 MEDIUM | 🟡 Partial |

---

_Next: Phase 3 - Synthesis_
