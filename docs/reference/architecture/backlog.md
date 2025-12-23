# Architecture Reference — Backlog

> **Tracks remaining improvements identified in [evaluation.md](evaluation.md)**
> **Source**: Comprehensive evaluation (2025-12-24), Score: 4.65/5

---

## Status Legend

| Status | Meaning           |
| ------ | ----------------- |
| `[ ]`  | Not started       |
| `[~]`  | In progress       |
| `[x]`  | Complete          |
| `[-]`  | Deferred/Won't do |

---

## Completed This Session

- [x] **P1: `omar/` → `.omar/` migration** — Structural inconsistency resolved
- [x] **Mermaid migration** — 8 diagrams converted from ASCII
- [x] **Core Four enrichment** — INPUT → PROCESS → OUTPUT → FEEDBACK
- [x] **Substrate Layer** — Section 0 added (Carbon-Silicon Partnership)
- [x] **File Access Pattern** — Unified AGENT-SPECIFIC category

---

## Priority 2: Three-Layer Model Gaps

### [ ] Escalation Rules

**Section**: 1 (Three-Layer Model)
**Gap**: When exactly does an agent escalate to Human Control Plane?

**Proposed content**:

```markdown
### Escalation Triggers

| Condition                 | Action                   |
| ------------------------- | ------------------------ |
| Confidence < 60% (🟡🟠⚠️) | Escalate to Omar         |
| Business/client decision  | Always escalate          |
| Irreversible action       | Confirm before executing |
| Safety concern            | Immediate escalation     |
| Ambiguous intent          | Ask, don't assume        |
```

### [ ] Trust Calibration Details

**Section**: 1 (Three-Layer Model)
**Gap**: "Trust Calibration" mentioned but not detailed

**Proposed content**:

- Define autonomy levels (1-5)
- Map confidence to autonomy
- Show how trust changes over time

---

## Priority 3: Hybrid Multi-Repo Gaps

### [ ] Migration Trigger

**Section**: 3 (Hybrid Multi-Repo)
**Gap**: When do we migrate from mono-repo to multi-repo?

**Proposed trigger**:

```markdown
### Migration Trigger

| Metric                 | Threshold | Action             |
| ---------------------- | --------- | ------------------ |
| Client count           | ≥ 10      | Begin planning     |
| Client count           | ≥ 15      | Execute migration  |
| Repo size              | > 500MB   | Consider migration |
| Cross-client conflicts | > 3/month | Urgent migration   |
```

### [ ] Migration Checklist

**Section**: 3 (Hybrid Multi-Repo)
**Gap**: No step-by-step procedure

**Proposed checklist**:

- [ ] 1. Create `core/` repository
- [ ] 2. Extract shared resources
- [ ] 3. Set up git submodules OR @imports
- [ ] 4. Migrate projects one by one
- [ ] 5. Update CI/CD pipelines
- [ ] 6. Verify all imports work

---

## Priority 4: Agent Harness Gaps

### [ ] Verification Action Plan

**Section**: 5 (Agent Harness)
**Current**: 🟡 Partial

**Proposed improvements**:

- Add automated tests for rules
- Implement triple-check for destructive operations
- Create verification checklist template

### [ ] Monitoring Action Plan

**Section**: 5 (Agent Harness)
**Current**: 🟡 Partial

**Proposed improvements**:

- Define key metrics to track
- Set up structured logging
- Create dashboard (Linear? Custom?)

---

## Priority 5: Minor Gaps

### [ ] Non-File Artifacts (EaC)

**Section**: 2 (Everything-as-Code)
**Gap**: Env vars, secrets not addressed

**Proposed**: Add note about:

- `.env.example` patterns
- Secret management (1Password? Vault?)
- Environment-specific configs

### [ ] Positioning Context Usage

**Section**: 7 (Positioning Formula)
**Gap**: HOW to use each context

**Proposed**: Add examples for Marketing, Technical, Internal contexts

### [ ] Day-to-Day Rules (Substrate)

**Section**: 0 (Substrate Layer)
**Gap**: When does Carbon decide vs Silicon?

**Note**: This is partially covered by Escalation Rules (P2)

---

## Metrics

| Metric          | Value   |
| --------------- | ------- |
| **Total items** | 9       |
| **Completed**   | 5       |
| **Remaining**   | 9       |
| **Priority 2**  | 2 items |
| **Priority 3**  | 2 items |
| **Priority 4**  | 2 items |
| **Priority 5**  | 3 items |

---

## Next Actions

1. **Immediate**: Commit this tracking file + evaluation report
2. **Next session**: Tackle P2 (Escalation Rules, Trust Calibration)
3. **Future**: P3-P5 as time permits

---

_Created: 2025-12-24_
_Last updated: 2025-12-24_
