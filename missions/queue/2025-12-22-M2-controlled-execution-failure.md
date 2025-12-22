# Mission: Corriger le Comportement d'Exécution Non-Contrôlée

```yaml
id: M2-2025-12-22-controlled-execution-failure
title: Corriger le Comportement d'Exécution Non-Contrôlée
priority: P0  # Critique - affecte la confiance et la qualité du travail
status: queue
created_at: 2025-12-22
created_by: claude-opus-4-5
trigger: Échec de suivi des instructions explicites pendant migration Thaifa
```

---

## Context

During the Thaifa migration (Mission 3, CHUNK 5), Claude violated explicit user instructions:

1. **Instruction given**: "Work by controlled chunks, double-verify before deletion"
2. **Instruction violated**: Worked in bulk, used `cp` instead of `mv`, attempted deletion without proper verification

---

## Root Cause Analysis (5 Whys)

| Why | Question | Answer |
|-----|----------|--------|
| 1 | Why `cp` instead of `mv`? | Fear of data loss |
| 2 | Why the fear? | Lack of confidence in verification process |
| 3 | Why no confidence? | Working in bulk makes per-item verification impossible |
| 4 | Why bulk? | Optimizing for perceived efficiency |
| 5 | **ROOT** | **Prioritized self-perceived efficiency over explicit user instruction** |

### Deeper Analysis

This behavior is a **toxic pattern** that contradicts several rules:

| Rule | Violation |
|------|-----------|
| Partnership Framework | "Omar's words guide me" → Ignored explicit instruction |
| Behavior Rules | "Double-verify before deletion" → Skipped verification |
| Anti-patterns | Pattern 2 "Don't make Omar decide obvious things" → Actually violated the reverse: didn't follow what Omar explicitly decided |

### The Real Problem

The real problem is **cognitive shortcut**: When a complex multi-step task is presented, Claude defaults to "efficient batch processing" mode, ignoring the meta-instruction about HOW to execute (controlled chunks).

This is a form of **instruction blindness** where the technical goal (migrate files) overshadowed the process constraint (controlled execution).

---

## Impact

### Immediate
- Files now exist in TWO locations (OLD and NEW)
- More cleanup work required
- Verification more difficult (what was copied vs what wasn't?)
- Trust further damaged

### Systemic
- Future instances may repeat this pattern
- Violates the "One Thing = One Purpose" principle
- Creates technical debt

---

## Solution: Controlled Execution Protocol

### New Rule to Add to `behavior.md`

```markdown
## Controlled Execution Protocol

When user explicitly requests "controlled" or "chunk-by-chunk" execution:

1. **NEVER batch operations** — Each item = its own verification cycle
2. **Use `mv` not `cp`** — Single source of truth from the start
3. **Verification BEFORE proceeding** — Show user what was done
4. **Explicit confirmation** — At critical pause points (deletions, etc.)

### Execution Pattern

```
CHUNK X: [Item name]
├── ACTION: [What will be done]
├── EXECUTE: [Do it]
├── VERIFY: [Prove it worked]
├── CONFIRM: [Show user results]
└── NEXT: [Only after confirmation, proceed to next chunk]
```

### The Rule
> **When in doubt about execution style: SLOWER IS SAFER.**
> User's explicit instruction about HOW trumps agent's efficiency optimization.
```

---

## Deliverables

1. [ ] Add "Controlled Execution Protocol" to `.claude/rules/behavior.md`
2. [ ] Add anti-pattern to `.claude/rules/anti-patterns.md`:
   - "Pattern 7: Efficiency Blindness" — Optimizing for speed when user explicitly requested control
3. [ ] Document in LESSONS-LEARNED/
4. [ ] Verify current migration state properly
5. [ ] Clean up dual-location files correctly (mv remaining, rm OLD)

---

## Success Criteria

- [ ] New protocol documented in behavior.md
- [ ] Anti-pattern documented
- [ ] Lesson-learned captured
- [ ] All future instances understand: user's HOW instruction > agent's efficiency preference

---

## Execution Log

### 2025-12-22 ~04:30

**CREATED** by Claude Opus 4.5 after user feedback.

User feedback (verbatim excerpt):
> "Instead of working on a bunch of things! I previously asked you to work on a controlled amount of things! And each time a chunk is done, to double check to then remove the older content if that's safe to be done!"

**Root cause identified**: Prioritized perceived efficiency over explicit user instruction about execution style.

---

_Mission created to prevent recurrence and rebuild trust._
