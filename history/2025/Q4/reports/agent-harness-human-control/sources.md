# Source Triangulation

**Date**: 2025-12-24
**Topic**: Agent Harness & Human Control Plane

---

## Sources

### Source 1: Tsamados, Floridi & Taddeo (2025) — Academic

- **Title**: Human control of AI systems: from supervision to teaming
- **URL**: https://link.springer.com/article/10.1007/s43681-024-00489-4
- **Type**: Research (Peer-reviewed, AI and Ethics journal)
- **Key Claims**:
  - Two main approaches exist: **Supervisory Human Control (SHC)** and **Human-Machine Teaming (HMT)**
  - SHC treats humans as supervisors overseeing automated agents (5 steps: Plan, Teach, Monitor, Intervene, Learn)
  - SHC is **inadequate** for foundation models due to: scale, non-determinism, unpredictability, cognitive overload
  - HMT treats AI as **collaborative agents** with dynamic task allocation based on self-governance
  - Control should be "the product of **collaborative agency** in a multi-agent system rather than exclusive human supervision"
  - **Negative control** (correcting failures) vs **Positive control** (leveraging capabilities while maintaining oversight)
  - HMT requires: shared mental models, effective communication, commitment mechanisms, convention building
- **Evidence Quality**: Strong (peer-reviewed, extensive literature review, defense domain focus)
- **Potential Bias**: Academic — may underweight practical implementation concerns

### Source 2: Millward (2025) — Practitioner

- **Title**: The Unsupervised Loop: Designing Governance for the Age of Autonomous AI Agents
- **URL**: https://medium.com/@angmillward/the-unsupervised-loop
- **Type**: Practitioner (Medium, governance perspective)
- **Key Claims**:
  - Human role shifts from "hands-on executor" to **"Team Leader"** who sets direction and validates plans
  - This is "the highest level of human-machine teaming: **Human-led, agent-operated**"
  - **Supervisory Checkpoint Model**: Human intervenes at Goal Validation and Boundary Validation
  - **Coherence Checkpoint**: Human reviews agent's "reasoning trace" (thought process), not data
  - Three governance layers: **Policy** (ethical/legal), **Platform** (zero-trust security), **Audit** (traceability)
  - Confidence-Based Routing (CBR): output below threshold triggers automatic human escalation
  - "Ethics as a Strategic Asset" — trust drives adoption and competitive advantage
- **Evidence Quality**: Moderate (practitioner experience, no empirical data)
- **Potential Bias**: Governance-focused — may overcomplicate operational reality

### Source 3: Anthropic Engineering (2025) — Official

- **Title**: Building Agents with the Claude Agent SDK / Effective Harnesses for Long-Running Agents
- **URL**: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- **Type**: Official Documentation (Anthropic)
- **Key Claims**:
  - **"The agent harness that powers Claude Code can power many other types of agents"**
  - Agent harness = context management, tool ecosystem, permissions, error handling, session management, monitoring
  - Subagents use **isolated context windows** — only send relevant info back to orchestrator
  - "CLAUDE.md to encode project conventions" — shared standards for agents
  - "Permission sprawl is the fastest path to unsafe autonomy. Treat tool access like production IAM."
  - Multi-agent coordination: orchestrator maintains **global plan + compact state**, not every detail
- **Evidence Quality**: Strong (official, production-tested with Claude Code)
- **Potential Bias**: Product-focused — promotes Anthropic ecosystem

### Source 4: CAMEL-AI (2025) — Practitioner/Research

- **Title**: Bridging Minds and Machines: Agents with Human-in-the-Loop
- **URL**: https://www.camel-ai.org/blogs/human-in-the-loop-ai-camel-integration
- **Type**: Practitioner (AI research community)
- **Key Claims**:
  - **KnowNo framework**: Agents assess confidence levels; escalate to humans when uncertain
  - **"Humans as tools"**: HumanLayer and GotoHuman embed humans as callable resources via Slack/email
  - Agents pause execution to route approval requests — keeps humans in **reactive supervisory positions**
  - Systems learn which decisions require input by tracking approval patterns → semi-autonomous over time
  - **Model Context Protocol (MCP)** abstracts human-integration infrastructure
  - "Human-in-the-loop succeeds when it treats humans as intelligent supervisors who **guide rather than replace** agent autonomy"
- **Evidence Quality**: Moderate (practical implementations, some research backing)
- **Potential Bias**: Pro-automation — emphasizes agent autonomy

### Source 5: Microsoft Agent Framework (2025) — Official

- **Title**: Implementing Human-in-the-Loop AI Agents
- **URL**: https://jamiemaguire.net/index.php/2025/12/06/microsoft-agent-framework-implementing-human-in-the-loop-ai-agents/
- **Type**: Official/Practitioner (Microsoft ecosystem)
- **Key Claims**:
  - `ApprovalRequiredAIFunction` wrapper creates mandatory checkpoints for sensitive operations
  - **Nested loop architecture**: Outer (user conversation), Inner (approval requests)
  - **Risk stratification**: High (payments, deletions) = require approval; Medium = log but auto-approve; Low = no approval
  - **Selective wrapping**: Only critical functions get approval wrapper; routine operations proceed
  - `AgentThread` objects preserve complete interaction histories (audit trails)
  - **Phased rollout**: Start restrictive, gradually loosen as confidence builds
- **Evidence Quality**: Moderate (Microsoft ecosystem, practical)
- **Potential Bias**: Enterprise-focused — may overcomplicate for small teams

### Source 6: Parallel.ai (2025) — Practitioner/Technical

- **Title**: What is an agent harness?
- **URL**: https://parallel.ai/articles/what-is-an-agent-harness
- **Type**: Practitioner (comprehensive technical deep-dive)
- **Key Claims**:
  - Agent harness = **"complete architectural system surrounding an LLM that manages the lifecycle of context"**
  - The harness is **"everything except the model itself"**
  - Six core components:
    1. **Context Engineering**: Window management, RAG, summarization, relevance scoring
    2. **Planning/Decomposition**: Task breakdown, goal representation, plan adaptation
    3. **Tool Integration**: Function calling, API abstraction, result parsing
    4. **Memory/State Management**: Short-term (scratchpad), long-term (persistence), episodic
    5. **Verification/Reflection**: Output validation, self-critique, consistency checking
    6. **Monitoring/Observability**: Logging, tracing, performance metrics
  - **Harness vs Orchestrator vs Framework**:
    - Orchestrator = coordinates MULTIPLE agents (macro-level)
    - Harness = manages SINGLE agent's lifecycle (micro-level)
    - Framework = provides building blocks for both
  - Real examples: Claude Agent SDK, LangChain DeepAgents, modular gaming harnesses
  - **Key insight**: "The harness is the difference between a chatbot and an agent"
- **Evidence Quality**: Strong (comprehensive, technically precise, production examples)
- **Potential Bias**: Technical focus — may underweight human/governance aspects

---

## Convergence Analysis

| Pattern | Tsamados | Millward | Anthropic | CAMEL-AI | Microsoft | Parallel.ai | Confidence |
|---------|----------|----------|-----------|----------|-----------|-------------|------------|
| **Human = Team Leader, not Micro-manager** | HMT over SHC | "Team Leader" | Orchestrator | "Guide not replace" | Selective wrapping | (Implicit) | ✅ HIGH |
| **Harness = Infrastructure, Human = User** | GAP | Socio-technical | SDK + human | MCP infra | AgentThread | **"Everything except model"** | ✅ HIGH |
| **Goal/Boundary Validation (Strategic)** | Positive control | Supervisory Checkpoint | Global plan | Goal-level | Risk stratification | Planning layer | ✅ HIGH |
| **Confidence-Based Escalation** | GAP | CBR thresholds | Permissions | KnowNo | ApprovalRequired | Verification layer | ✅ HIGH |
| **6 Harness Components** | GAP | GAP | Partial | Partial | Partial | **Full taxonomy** | ✅ HIGH |
| **Dynamic Task Allocation** | HMT requirement | ✅ | Subagents | Pattern learning | Phased rollout | Plan adaptation | 🟢 MEDIUM |
| **Convention/Norm Building** | HMT requirement | Coherence Checkpoint | CLAUDE.md | GAP | Audit trails | GAP | 🟢 MEDIUM |
| **Trust as Strategic Asset** | Trust dynamics | Ethics = advantage | GAP | GAP | GAP | GAP | 🟡 LOW |

---

## Key Disagreements / Decision Points

### 1. Omar = Harness, or Omar = Part of Harness?

| Source | Position |
|--------|----------|
| **ChatGPT (original)** | Omar IS the harness (supervisory layer) |
| **Tsamados** | Control = product of collaborative agency (human + AI = multi-agent system) |
| **Millward** | Harness is socio-technical (outils + règles + CI + human decisions) |
| **Anthropic** | Harness = SDK infrastructure; human = orchestrator using the harness |
| **Parallel.ai** | Harness = "everything except the model" — purely technical infrastructure |

**Resolution**: The **layered view** is most accurate:
1. **Agent Harness** = Technical infrastructure (context, tools, memory, verification, monitoring)
2. **Human Control Plane** = Omar's role WITHIN the harness (goal-setting, boundary validation, escalation handling)
3. **Socio-Technical System** = Harness + Human + Conventions (CLAUDE.md, rules, workflows)

Omar is NOT the harness. Omar OPERATES the harness and is part of the larger socio-technical system.

### 2. Terminology: Which Term to Adopt?

| Term | Source | Pros | Cons |
|------|--------|------|------|
| **Human Control Plane** | ChatGPT, Anthropic | Technical precision, systems thinking | May sound impersonal |
| **Agent Supervisor** | Millward, CAMEL-AI | Clear, simple | SHC connotation (outdated) |
| **Operator/Orchestrator** | Anthropic, Microsoft | DevOps-familiar, action-oriented | Might imply micro-management |
| **Team Leader** | Millward, Tsamados | HMT-aligned, collaborative framing | Less technical |

**Recommendation**: Use **"Human Control Plane"** for technical contexts, **"Team Leader"** for narrative contexts. Both are valid.

### 3. How Much Control vs Autonomy?

| Approach | When to Use |
|----------|-------------|
| **High Control (HITL)** | High-stakes, irreversible, client-facing, financial |
| **Medium Control (HOTL)** | Routine with monitoring, override capability |
| **Low Control (HOOTL)** | Low-risk, well-tested patterns, internal tooling |

---

## Sources Summary

| # | Source | Type | Key Contribution | Confidence |
|---|--------|------|------------------|------------|
| 1 | Tsamados et al. (2025) | Academic | SHC vs HMT framework, collaborative agency | ✅ High |
| 2 | Millward (2025) | Practitioner | Supervisory Checkpoint model, governance layers | 🟢 Medium |
| 3 | Anthropic (2025) | Official | Agent harness definition, CLAUDE.md conventions | ✅ High |
| 4 | CAMEL-AI (2025) | Research/Practitioner | HITL patterns, confidence-based escalation | 🟢 Medium |
| 5 | Microsoft (2025) | Official/Practitioner | Risk stratification, approval workflows | 🟢 Medium |
| 6 | Parallel.ai (2025) | Practitioner/Technical | Complete harness taxonomy (6 components) | ✅ High |

---

## Key Terminology Definitions (Synthesized)

| Term | Definition | Source Consensus |
|------|------------|------------------|
| **Agent Harness** | Technical infrastructure wrapping an LLM: context management, tools, memory, verification, monitoring | Anthropic, Parallel.ai (✅ High) |
| **Human Control Plane** | The human's role in setting goals, validating boundaries, and handling escalations | Millward, ChatGPT (🟢 Medium) |
| **Socio-Technical System** | Complete system: harness + human + conventions + workflows | Tsamados, Millward (✅ High) |
| **HMT (Human-Machine Teaming)** | Collaborative approach where AI is a partner, not a tool | Tsamados (✅ High) |
| **SHC (Supervisory Human Control)** | Traditional approach: human supervises, agent executes | Tsamados — **outdated for LLMs** |

---

_Next: Phase 2 - Pattern Extraction_
