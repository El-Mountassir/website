# Source Triangulation — Mission Coordination

## Sources

### Source 1: Claude Code Official Documentation

- **Type**: Official
- **Key Claims**:
  - No built-in coordination mechanism (intentional)
  - Isolation by design via Git worktrees
  - Subagents have `agentId` but main instances don't
  - Sessions are per-directory, resumable by name
- **Evidence Quality**: Strong (official docs)
- **Implication**: We need a custom solution

### Source 2: Anthropic Multi-Agent Research System

- **URL**: [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Type**: Practitioner (Anthropic internal)
- **Key Claims**:
  - Uses orchestrator-worker pattern
  - Avoids conflict through clear task decomposition
  - Subagents get explicit objectives, output format, boundaries
  - Currently synchronous (no async coordination)
- **Evidence Quality**: Strong (direct from Anthropic)
- **Implication**: Clear task boundaries > complex locking

### Source 3: Multi-Agent Coordination Patterns (Industry)

- **URLs**:
  - [Confluent: Event-Driven Multi-Agent Systems](https://www.confluent.io/blog/event-driven-multi-agent-systems/)
  - [Microsoft: AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
  - [Galileo: Multi-Agent Coordination Strategies](https://galileo.ai/blog/multi-agent-coordination-strategies)
- **Type**: Industry best practices
- **Key Claims**:
  - Lock-based shared state: `threading.Lock()` for shared knowledge bases
  - File-based spatial decomposition: agents work on separate parts
  - Resource contention causes most errors
  - Exponential backoff for lock conflicts
- **Evidence Quality**: Moderate (general patterns, not Claude-specific)
- **Implication**: File-based approach fits our markdown workflow

---

## Convergence Analysis

| Pattern | Claude Code Docs | Anthropic Research | Industry | Confidence |
|---------|------------------|-------------------|----------|------------|
| Isolation by default | AGREE | AGREE | AGREE | High |
| Clear task boundaries | GAP | AGREE | AGREE | High |
| File-based coordination | GAP | GAP | AGREE | Medium |
| Lock mechanism | DISAGREE (not built-in) | GAP | AGREE | Medium |
| Instance/Session ID | EXISTS (session names) | GAP | AGREE | Medium |

---

## Key Insight from Sources

**Anthropic's approach**: Don't try to coordinate concurrent access. Instead:
1. Decompose tasks clearly so agents work on different things
2. Use synchronous execution when possible
3. Let the orchestrator manage handoffs

**Industry approach**: When concurrent access is unavoidable:
1. Use explicit locks/claims
2. File-based signaling
3. Exponential backoff on conflicts

---

## Decision Points

### 1. Lock vs Claim vs Move

| Approach | Pros | Cons |
|----------|------|------|
| **Lock file** (`.lock`) | Explicit, can include metadata | Extra file to manage |
| **Claim in YAML** | Self-contained, visible in mission | Requires parsing |
| **Move to active/** | Already in standard, visible in filesystem | File move may not be atomic |

**Recommendation**: Combine **Move to active/** + **Claim entry in execution log**

### 2. Instance Identification

| Approach | Pros | Cons |
|----------|------|------|
| Session name (`/rename`) | User-controllable | Not automatic |
| Timestamp | Automatic | Not unique |
| Random ID | Unique | Not meaningful |
| Context hash | Deterministic | Complex |

**Recommendation**: Use **timestamp + context description** (e.g., "2025-12-22 02:15 - Working on Thaifa migration")

### 3. Conflict Detection

| Approach | Pros | Cons |
|----------|------|------|
| Check before claim | Prevents conflicts | Race condition window |
| Move-and-check | Atomic-ish | Requires recovery |
| Ask Omar | Always correct | Adds friction |

**Recommendation**: **Check → Claim → Verify** with Omar escalation if conflict detected
