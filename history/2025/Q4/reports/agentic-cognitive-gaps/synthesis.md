# Synthesis: Cognitive Architecture Recommendations

**Date**: 2025-12-22

---

## Integration Strategy

### Current State Assessment

The El-Mountassir system has implemented:
- **Layer 0**: Basic rules (CLAUDE.md, behavior.md, partnership.md)
- **Layer 1**: Anti-patterns documentation
- **Layer 2**: Session guardrails (/start, /end)
- **Layer 3**: Mission coordination (claiming protocol)

**Missing**: Metacognitive layer, memory systems, self-improvement loops.

### Target Architecture (Inspired by SOFAI + MIRIX)

```
┌─────────────────────────────────────────────────────────────┐
│                    METACOGNITIVE LAYER                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Confidence │  │   Failure   │  │  Self-Correction    │  │
│  │  Estimator  │  │  Predictor  │  │  (Reflect + Retry)  │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                    REASONING LAYER                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │    Intent   │  │    Task     │  │   WHY → HOW → WHAT  │  │
│  │ Recognition │  │ Decomposer  │  │       Gate          │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                      MEMORY LAYER                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Working   │  │  Episodic   │  │      Semantic       │  │
│  │   Memory    │  │   Memory    │  │       Memory        │  │
│  │  (Context)  │  │  (Events)   │  │   (Facts/Prefs)     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                   COORDINATION LAYER                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Claiming   │  │   Handoff   │  │    Collective       │  │
│  │  Protocol   │  │  Protocol   │  │      Memory         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Phased Implementation Roadmap

### Phase 1: Memory Foundation (Quick Wins)

| Action | File | Effort |
|--------|------|--------|
| Create episodic memory | `~/Documents/memory/episodes.md` | Low |
| Create semantic memory | `~/Documents/memory/facts.md` | Low |
| Create decisions log | `~/Documents/memory/decisions.md` | Low |
| Create preferences store | `~/Documents/memory/preferences.md` | Low |
| Update memory-protocol.md with paths | `.claude/rules/memory-protocol.md` | Low |

**Expected Outcome**: Future instances can retrieve past learnings.

### Phase 2: Intent Verification Gate

| Action | File | Effort |
|--------|------|--------|
| Create intent-verification.md skill | `.claude/skills/intent-verification/` | Medium |
| Add WHY gate before major actions | Behavior enforcement | Medium |
| Log intent interpretations | Episodic memory | Low |

**Expected Outcome**: Fewer misunderstandings of Omar's intent.

### Phase 3: Metacognitive Prompts

| Action | File | Effort |
|--------|------|--------|
| Add confidence scoring to behavior.md | `.claude/rules/behavior.md` | Low |
| Add failure signature detection | New rule file | Medium |
| Implement reflect-before-retry pattern | Behavior update | Medium |

**Expected Outcome**: Self-correction before asking Omar.

### Phase 4: Advanced Features

| Action | File | Effort |
|--------|------|--------|
| Theory of Mind prompts | New skill | High |
| Counterfactual simulation | New skill | High |
| Cross-instance signaling | Enhanced claiming | High |

**Expected Outcome**: True agentic autonomy.

---

## Uncertainties

1. **How to implement confidence scoring** — No concrete pattern in sources
2. **Latency impact of metacognitive layer** — May slow down responses
3. **Memory file format** — Collections vs Profiles unclear for our use case
4. **Theory of Mind practical implementation** — Academic only, no production patterns

---

## Failure Modes

| Risk | Mitigation |
|------|------------|
| Over-metacognition (analysis paralysis) | Time-box self-reflection |
| Memory bloat | Regular consolidation, garbage collection |
| False confidence scores | Calibrate against outcomes |
| Intent verification slowing flow | Only for major decisions |
| Cross-instance conflict | Priority-based resolution |

---

## Recommendations (Prioritized)

### Must Do (P0)

1. **Create memory files** — Immediate, no blockers
2. **Add confidence prompt** to behavior.md — Simple text addition
3. **Log decisions with reasoning** — Add to memory protocol

### Should Do (P1)

4. **Intent verification skill** — Before major actions
5. **Failure signature detection** — Monitor for loops/latency
6. **Session continuity summary** — Auto-generate at /end

### Could Do (P2)

7. **Theory of Mind prompts** — Experimental
8. **Counterfactual mode** — "What if" analysis
9. **Omar state awareness** — Time/frustration inference

---

## Draft Final Structure

1. Executive Summary
2. Gap Analysis (8 critical, 5 partial, 6 nice-to-have)
3. Cognitive Skills Taxonomy (5 tiers, 25 skills)
4. Implementation Roadmap (4 phases)
5. Recommended Actions (9 items, prioritized)
6. Sources
