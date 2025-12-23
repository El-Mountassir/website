# The Collective's 2026 Tech Stack

> **Aligned with**: [2026 Playbook](../philosophy/2026-playbook.md) > **Principle**: Minimal, practical, commitment-driven
> **Category**: Trust-Centered Human-AI Agentic Ecosystem
> **Anti-pattern**: Enterprise buzzword bingo

---

## Why This Stack

The generic "Agentic-Native" stack talks about NVIDIA, Snowflake, TensorFlow, Zero-Trust...

**We don't need any of that.**

We're not training models. We're not running enterprise infrastructure. We're building El Mountassir — one human + AI agents.

Our stack is chosen for ONE reason: **Does it increase trust in our agents?**

---

## Stack Overview

| Layer | Name             | Components                                            |
| ----- | ---------------- | ----------------------------------------------------- |
| 4     | Out-Loop Systems | GitHub Actions, Linear, Webhooks, Slack/Discord       |
| 3     | Orchestration    | Lead Agent, Sub-Agents, Task Tool, Parallel Execution |
| 2     | Custom Agents    | Claude Code SDK, Skills, MCP Servers, CLI Tools       |
| 1     | Foundation       | Claude API (Opus 4.5 / Sonnet), Claude Code           |
| 0     | Infrastructure   | Docker AI Platform, Git, Local Dev                    |

---

## Layer 0: Infrastructure

| Component     | Purpose                         | Commitment         |
| ------------- | ------------------------------- | ------------------ |
| **Docker**    | AI Platform, sandboxes, MCP     | #5 Agent Sandboxes |
| **Git**       | Version control, collaboration  | Foundation         |
| **Local Dev** | In-loop development             | #6 In-Loop         |
| **Pop!\_OS**  | Omar's OS                       | —                  |
| **Cloudflare** | Domain, CDN, Workers, Agents SDK | #5 Sandboxes, #6 Out-Loop |

**What we DON'T need:**

- ❌ NVIDIA accelerated computing (we use APIs)
- ❌ Kubernetes (overkill)
- ❌ Snowflake (no big data)
- ❌ Edge cloud (not our scale)

---

## Layer 1: Foundation (Commitment #1)

> **Principle**: Claude is our foundation. Others are options when they excel.

### The 2026 Model Landscape

| Provider      | Model            | Input $/1M | Output $/1M | Context | Speed      | Best For                        |
| ------------- | ---------------- | ---------- | ----------- | ------- | ---------- | ------------------------------- |
| **Anthropic** | Opus 4.5         | $5.00      | $25.00      | 200K    | Medium     | Complex reasoning, architecture |
| **Anthropic** | Sonnet 4.5       | $3.00      | $15.00      | 200K–1M | Fast       | Tool calling, sub-agents        |
| **Anthropic** | Haiku 4.5        | $1.00      | $5.00       | 200K    | Very Fast  | Quick validation, cheap tasks   |
| **Google**    | Gemini 3 Pro     | $2.00      | $12.00      | 1M      | Medium     | Deep Think, agentic, multimodal |
| **Google**    | Gemini 3 Flash   | $0.50      | $3.00       | 1M+     | 218 tok/s  | Multimodal, speed               |
| **Google**    | Gemini 2.5 Flash | $0.30      | $2.50       | 1M      | ~280 tok/s | Budget, high volume             |
| **OpenAI**    | GPT-5.2          | $1.75      | TBD         | 400K    | Medium     | General intelligence            |

### Our Primary Stack (Claude)

| Component             | Purpose                                  | When to Use                             |
| --------------------- | ---------------------------------------- | --------------------------------------- |
| **Claude Opus 4.5**   | Complex reasoning, long tool chains      | Architecture, planning, complex code    |
| **Claude Sonnet 4.5** | Fast, reliable, "annihilated the market" | Routine tasks, sub-agents, tool calling |
| **Claude Haiku 4.5**  | Quick, cheap                             | Simple queries, validation              |
| **Claude Code CLI**   | Primary interface                        | Daily development                       |

### CLI Tools Landscape

| Tool            | Provider  | Pricing         | Context | Open Source   | Our Use     |
| --------------- | --------- | --------------- | ------- | ------------- | ----------- |
| **Claude Code** | Anthropic | $200/mo Max 20x | 200K    | No            | 🟢 Primary  |
| **Gemini CLI**  | Google    | Free/API        | 1M      | ✅ Apache 2.0 | 🟡 Evaluate |
| **Codex CLI**   | OpenAI    | API-based       | 400K    | ✅ Yes        | 🟡 Evaluate |

> **Commitment #1**: Claude Code is our primary interface.
> **Alternatives**: When 1M context or open-source matters.

### Claude Subscription Plans

| Plan        | Price   | vs Pro | Best For                   |
| ----------- | ------- | ------ | -------------------------- |
| **Pro**     | $20/mo  | 1x     | Light coding, productivity |
| **Max 5x**  | $100/mo | 5x     | Professional developers    |
| **Max 20x** | $200/mo | 20x    | Heavy power users          |

**Our Plan**: Max 20x ($200/mo)

| Resource    | Weekly Limit              |
| ----------- | ------------------------- |
| Opus 4.5    | 24-40 hours               |
| Sonnet 4.5  | 240-480 hours             |
| Extra usage | API rates when limits hit |

> **Why Max 20x**: Priority Opus access for complex architecture.
> When limits hit, seamlessly continues at API rates.
> Model switching: `/model opus`, `/model sonnet`, `/model haiku`

### Strategic Alternatives (When They Excel)

| Model                | Use When                                     | Why                                             |
| -------------------- | -------------------------------------------- | ----------------------------------------------- |
| **Gemini 3 Pro**     | Deep reasoning, 1M context, agentic tasks    | Deep Think mode, agentic-first design           |
| **Gemini 3 Flash**   | Multimodal input (images, video, audio, PDF) | 200 tokens/sec, top-3 intelligence, top-5 price |
| **Gemini 2.5 Flash** | High volume, budget-conscious                | 30 cents, good enough for many tasks            |

### Model Selection Matrix

| Task Type            | Primary        | Alternative      |
| -------------------- | -------------- | ---------------- |
| Complex architecture | Opus 4.5       | Gemini 3 Pro     |
| Long tool chains     | Opus 4.5       | Gemini 3 Pro     |
| Sub-agents (routine) | Sonnet 4.5     | Gemini 3 Flash   |
| Quick validation     | Haiku 4.5      | —                |
| Image/video analysis | Gemini 3 Flash | Claude (limited) |
| PDF processing       | Gemini 3 Flash | Claude           |
| High-volume tasks    | Sonnet 4.5     | Gemini 2.5 Flash |
| Code generation only | Sonnet 4.5     | —                |

> **DEFAULT**: Claude (Commitment #1)
> **SWITCH**: Only when alternative demonstrably excels

### The Trust Hierarchy

| Model             | Trust Level | Score | Notes               |
| ----------------- | ----------- | ----- | ------------------- |
| Claude Opus 4.5   | Highest     | 100%  | Our foundation      |
| Claude Sonnet 4.5 | High        | 90%   | Tool calling leader |
| Claude Haiku 4.5  | Good        | 80%   | Quick tasks         |
| Gemini 3 Pro      | Building    | 70%   | Deep Think, agentic |
| Gemini 3 Flash    | Good        | 80%   | Multimodal, speed   |
| Others            | Evaluate    | —     | Case-by-case        |

### Price vs Intelligence (2026 Reality)

From the playbook:

> "Some see a price increase. We see a price decrease. Intelligence per token is going up. Cost per intelligence is going down. **We get more for less.**"

| Model             | Cost (Input) | Intelligence     | Value |
| ----------------- | ------------ | ---------------- | ----- |
| Gemini 2.5 Flash  | $0.30/1M     | Good             | ★★★★☆ |
| Gemini 3 Flash    | $0.50/1M     | Top-3            | ★★★★★ |
| Claude Haiku 4.5  | $1.00/1M     | Good             | ★★★★☆ |
| Gemini 3 Pro      | $2.00/1M     | Top-3            | ★★★★☆ |
| Claude Sonnet 4.5 | $3.00/1M     | Excellent        | ★★★★★ |
| Claude Opus 4.5   | $5.00/1M     | State-of-the-art | ★★★★★ |

**Insight**: Don't just compare raw price. Compare **cost per correct tool call**.

### What We DON'T Need

- ❌ TensorFlow / PyTorch (we don't train models)
- ❌ Hugging Face (we don't fine-tune)
- ❌ MLOps (we don't deploy models)
- ❌ Model hosting (we use APIs)
  - *Exception: Docker Model Runner for local dev when API unavailable*

---

## Layer 2: Custom Agents (Commitment #3)

| Component           | Purpose                            | Formula                              |
| ------------------- | ---------------------------------- | ------------------------------------ |
| **Claude Code SDK** | Build custom agents                | 50 lines + 3 tools + 150-line prompt |
| **Skills**          | Reusable agent behaviors           | `/skill-name` invocation             |
| **MCP Servers**     | Tool calling for external services | Linear, GitHub, Calendar, etc.       |
| **CLI Tools**       | Custom tooling                     | Bash, Python scripts                 |

### The Custom Agent Formula

```
Custom Agent = 50 lines code + 3 tools + 150-line system prompt
             = Automation of custom problem
             = Money
```

### MCP Servers We Use

| Server                 | Purpose                   | Status       |
| ---------------------- | ------------------------- | ------------ |
| **Docker MCP Toolkit** | MCP Gateway, 200+ servers | 🟢 Connected |
| **Linear**             | Work management           | 🟢 Connected |
| **GitHub**             | Code, PRs, Issues         | 🟢 Connected |
| **Firecrawl**          | Web scraping              | 🟢 Connected |
| **Playwright**         | Browser automation        | 🟢 Connected |
| **Google Calendar**    | Time management           | 🟡 Basic     |
| **Cloudflare Remote MCP** | Deploy/manage MCP servers | 🟡 Evaluate |

### Docker AI Platform

Our infrastructure for agentic AI:

| Component | Purpose | Status |
|-----------|---------|--------|
| **MCP Toolkit** | Gateway, 270+ servers, Dynamic MCP | 🟢 Connected |
| **Model Runner** | Local LLMs via OpenAI API | 🟡 Evaluate |
| **Gordon** | Embedded AI assistant | Available |
| **Compose for Agents** | `docker compose up` agentic stacks | 🟡 Evaluate |
| **MCP Gateway** | Production orchestration (OSS) | 🟡 Evaluate |

#### Key Capabilities

| Feature | Description |
|---------|-------------|
| **Dynamic MCP** | Agents discover/add/compose tools autonomously |
| **Code Mode** | JavaScript sandbox for custom tools |
| **Security** | Signed images, SBOM, 1CPU/2GB limits, no host access |
| **OAuth** | Automatic credential management (GitHub, Notion, Linear) |
| **Hardened Images** | CVE-remediated MCP servers (Dec 2025) |

> **Alignment**: Commitment #5 (Agent Sandboxes) — Complete agentic platform with deferred trust.
> **Docker joined Agentic AI Foundation** as Gold member alongside Anthropic, OpenAI, Google.

### Cloudflare Platform

Our edge infrastructure and agentic capabilities:

| Component | Purpose | Status |
|-----------|---------|--------|
| **Domain** | el-mountassir.com | 🟢 Active |
| **Workers** | Serverless compute (100K req/day free) | 🟡 Evaluate |
| **Workers AI** | AI inference (10K Neurons/day free) | 🟡 Evaluate |
| **Agents SDK** | Build stateful agents on Durable Objects | 🟡 Evaluate |
| **Remote MCP** | Industry-first remote MCP servers | 🟡 Evaluate |
| **D1 + R2** | Database + Object storage | 🟡 Evaluate |
| **Pages** | Static hosting for el-mountassir.com | 🟡 Evaluate |

#### Key Capabilities

| Feature | Description |
|---------|-------------|
| **Durable Objects** | Stateful micro-servers for agent memory |
| **Hibernation** | Sleep agents when idle, wake when needed |
| **Remote MCP** | Deploy MCP servers accessible from Claude.ai |
| **Workers AI** | Serverless AI at the edge, 10K Neurons/day free |
| **Free Tier** | Most features usable at zero cost |

> **Alignment**:
> - Commitment #5 (Agent Sandboxes) — Workers are isolated by design
> - Commitment #6 (Out-Loop) — Workers can run autonomously
> **Cost**: Domain $10.46/year, everything else on free tier

### Agent SDK Landscape

| SDK                   | Provider  | Languages  | Model Agnostic | Multi-Agent   | Our Use     |
| --------------------- | --------- | ---------- | -------------- | ------------- | ----------- |
| **Claude Agent SDK**  | Anthropic | TS, Python | Claude-focused | Via Task tool | 🟢 Primary  |
| **Google ADK**        | Google    | Py, TS, Go | ✅ LiteLLM     | ✅ Native     | 🟡 Evaluate |
| **OpenAI Agents SDK** | OpenAI    | Py, JS     | ✅ 100+ LLMs   | ✅ Handoffs   | 🟡 Evaluate |
| **Pydantic AI**       | Pydantic  | Python     | ✅ All major   | ✅ Graphs     | 🟡 Evaluate |
| **Cloudflare Agents** | Cloudflare | JS/TS     | ✅ Any LLM     | ✅ Multi-agent | 🟡 Evaluate |

#### Why Claude Agent SDK First

| Factor             | Claude Agent SDK                 | Others              |
| ------------------ | -------------------------------- | ------------------- |
| **Alignment**      | Powers Claude Code (our primary) | Require integration |
| **Trust**          | Same vendor as foundation        | Building trust      |
| **Learning curve** | Already using it                 | New patterns        |

#### When to Consider Alternatives

| Situation                 | Consider                                  |
| ------------------------- | ----------------------------------------- |
| Need 100+ model options   | Google ADK (LiteLLM) or OpenAI Agents SDK |
| Type-safe Python priority | Pydantic AI                               |
| Multi-agent orchestration | Google ADK                                |

**What we DON'T need:**

- ❌ Complex ML pipelines
- ❌ Feature stores
- ❌ Model registries

---

## Layer 3: Orchestration (Commitments #4, #7)

| Component              | Purpose                       | Pattern            |
| ---------------------- | ----------------------------- | ------------------ |
| **Lead Agent**         | Plans, Spawns, Reviews, Ships | Agentic Coding 2.0 |
| **Sub-Agents**         | Command-level execution       | Task tool          |
| **Parallel Execution** | Multiple agents at once       | Best-of-N          |
| **Agent Sandboxes**    | Isolated environments         | Docker containers  |

### Lead Agent Model

```
Omar prompts → Lead Agent (Claude) → Sub-Agents → Results
                    ↓
              Plans, Spawns, Reviews, Ships
```

### Best-of-N Pattern

```
Problem → Spin up N agents in sandboxes → Pick winner → Merge
        (Defer trust until we need it)
```

**What we DON'T need:**

- ❌ Complex workflow engines (Airflow, Prefect)
- ❌ Kubernetes orchestration
- ❌ Enterprise service mesh

---

## Protocols: How Agents Talk

### The Two Protocols

| Protocol | Purpose       | Standard         | Our Use                          |
| -------- | ------------- | ---------------- | -------------------------------- |
| **MCP**  | Agent ↔ Tool  | Anthropic        | 🟢 Active (Linear, GitHub, etc.) |
| **A2A**  | Agent ↔ Agent | Linux Foundation | 🟡 Evaluating                    |

### MCP (Model Context Protocol)

How agents access external tools:

```
Claude → MCP → Linear API
Claude → MCP → GitHub API
Claude → MCP → Calendar API
```

**Status**: 🟢 Connected (see MCP Servers We Use table)

### A2A (Agent-to-Agent Protocol)

How agents talk to each other (and to Omar):

```
Omar ↔ Claude Lead Agent (A2A)
Claude Lead ↔ Sub-Agents (A2A)
Our Agents ↔ External Agents (A2A)
```

**Key Insight**: Omar is a first-class agent in The Collective. A2A enables:

- Omar → Claude: High-level goals
- Claude → Omar: Results, questions, status
- Agent → Agent: Delegation, handoffs

**Status**: 🟡 Evaluating (v0.3 released, 150+ organizations)

### Protocol Relationship

```
┌─────────────────────────────────────────────┐
│                 A2A Layer                    │
│    (Agent ↔ Agent communication)            │
│                                             │
│  ┌─────────┐     ┌─────────┐     ┌───────┐  │
│  │  Omar   │ ←→  │ Claude  │ ←→  │ Sub-  │  │
│  │ (Agent) │     │ (Lead)  │     │ Agent │  │
│  └─────────┘     └────┬────┘     └───────┘  │
│                       │                      │
└───────────────────────┼─────────────────────┘
                        │ MCP
                ┌───────┴───────┐
                │    Tools      │
                │ Linear,GitHub │
                │ Calendar, etc │
                └───────────────┘
```

**What we DON'T need (yet):**

- ❌ gRPC complexity (HTTP/JSON-RPC sufficient for now)
- ❌ Full A2A implementation (still evaluating)

---

## Layer 4: Out-Loop Systems (Commitment #6)

| Component          | Purpose                    | Trust Level  |
| ------------------ | -------------------------- | ------------ |
| **GitHub Actions** | CI/CD, automated workflows | Building     |
| **Linear**         | Task management, triggers  | 🟢 Connected |
| **Webhooks**       | Event-driven automation    | Building     |
| **Slack/Discord**  | Agent prompting interface  | Future       |

### Out-Loop Goal

```
In-Loop (babysitting)  →  Out-Loop (autonomous)
                            ↓
                    Progressive offloading
```

**What we DON'T need:**

- ❌ Complex ITSM tools
- ❌ Enterprise chatbots
- ❌ Third-party "AI platforms"

---

## Security: Pragmatic, Not Paranoid

The generic stack talks about "Zero-Trust Architecture" and "Agentic Purple Teaming."

**Our approach: Deferred Trust via Sandboxes**

| Concern         | Our Solution                                    |
| --------------- | ----------------------------------------------- |
| Agent runs amok | Sandbox (Docker) — if it breaks, doesn't matter |
| Bad code        | PR review before merge (Best-of-N)              |
| Credentials     | Separate from codebase, not in agents           |
| Destructive ops | Guardrails in CLAUDE.md, hooks                  |

**What we DON'T need (yet):**

- ❌ Enterprise SIEM
- ❌ Zero-Trust identity providers
- ❌ SOC 2 compliance theater

---

## Private Benchmarks (Commitment #8)

| What to Measure                  | How                     |
| -------------------------------- | ----------------------- |
| **Model accuracy for our tasks** | Custom eval scripts     |
| **Tool call success rate**       | Logging, analysis       |
| **Agent task completion**        | Before/after comparison |
| **Cost per task**                | API usage tracking      |

**Principle:** Measure ourselves, not what benchmarks tell us.

---

## What We Ship (Commitment #10)

| Product/Service       | Stack Used                          |
| --------------------- | ----------------------------------- |
| **Villa Thaifa**      | Claude Code, MCP (Linear, Calendar) |
| **Gagliano**          | Claude Code, custom agents          |
| **el-mountassir.com** | Claude Code, Cloudflare/Vercel      |
| **Internal Tools**    | Custom agents, Skills               |

---

## Stack Evolution

| Phase       | Focus         | Stack Additions              |
| ----------- | ------------- | ---------------------------- |
| **Now**     | Foundation    | Claude Code, basic MCP       |
| **Q1 2026** | Custom Agents | Claude Code SDK, more Skills |
| **Q2 2026** | Orchestration | Lead Agent model, sandboxes  |
| **Q3 2026** | Out-Loop      | GitHub Actions, webhooks     |
| **Q4 2026** | Scale         | Multi-agent, Best-of-N       |

---

## Anti-Patterns to Avoid

| ❌ Don't                          | ✅ Do                         |
| --------------------------------- | ----------------------------- |
| Chase enterprise tools            | Use minimal, practical stack  |
| Add complexity for "future scale" | Scale when needed             |
| Use tools because they're trendy  | Use tools that increase trust |
| Build infrastructure              | Use Claude Code + APIs        |
| Train models                      | Use best-in-class via API     |

---

## Summary

### Models Summary

| Category                       | Models                                   |
| ------------------------------ | ---------------------------------------- |
| Primary                        | Claude (Opus 4.5, Sonnet 4.5, Haiku 4.5) |
| Alternative (multimodal/speed) | Gemini 3 Flash                           |

### Stack Summary

| Layer         | Components                               |
| ------------- | ---------------------------------------- |
| Foundation    | Claude API + Claude Code                 |
| Agents        | Claude Code SDK + Skills + MCP           |
| Orchestration | Lead Agent + Sub-Agents + Sandboxes      |
| Out-Loop      | GitHub Actions + Linear + Webhooks       |
| Security      | Deferred Trust (Sandboxes, not paranoia) |

### Development Tools Summary

| Category          | Primary          | Alternatives                               |
| ----------------- | ---------------- | ------------------------------------------ |
| CLI               | Claude Code      | Gemini CLI, Codex CLI                      |
| SDK               | Claude Agent SDK | Google ADK, OpenAI Agents SDK, Pydantic AI |
| Protocol (Tools)  | MCP              | —                                          |
| Protocol (Agents) | A2A (evaluating) | —                                          |

### Model Selection Rule

| Condition | Use                                           |
| --------- | --------------------------------------------- |
| Default   | Claude (Commitment #1)                        |
| Exception | Others only when demonstrably better for task |

> **PRINCIPLE**: Minimal. Practical. Trust-increasing.

---

## Quick Model Reference

| Need                            | Use                  |
| ------------------------------- | -------------------- |
| Complex reasoning, architecture | **Opus 4.5**         |
| Tool calling, sub-agents        | **Sonnet 4.5**       |
| Quick validation                | **Haiku 4.5**        |
| Deep Think, 1M context          | **Gemini 3 Pro**     |
| Images, video, audio, PDF       | **Gemini 3 Flash**   |
| High volume, budget             | **Gemini 2.5 Flash** |

## Quick Tools Reference

| Need                    | Use                  |
| ----------------------- | -------------------- |
| Daily development       | **Claude Code**      |
| 1M context needed       | **Gemini CLI**       |
| Custom agents           | **Claude Agent SDK** |
| Multi-model agents      | **Google ADK**       |
| Type-safe Python agents | **Pydantic AI**      |
| Agent ↔ Tool comms      | **MCP**              |
| Agent ↔ Agent comms     | **A2A** (evaluating) |

---

_Aligned with The Collective's 2026 Playbook v0.0.1-alpha.10_
