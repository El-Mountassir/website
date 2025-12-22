# Mission: Prevent Destructive Operations Without Verification

```yaml
mission_id: 2025-12-22-destructive-operations-guardrails
type: FIX
status: QUEUED
priority: P0
assigned_to: Claude Code
created: 2025-12-22
source_session: Session where rm -rf was attempted during /end
source_insight: Claude attempted destructive delete (rm -rf shared/standards/) without understanding context
```

---

## Context

**CRITICAL PROBLEM**: Claude instances repeatedly attempt destructive operations (rm, rm -rf, git reset --hard) without proper verification. This has happened multiple times and is unacceptable.

**Latest incident**: During /end guardrails, Claude saw files in `shared/standards/` that appeared to duplicate `docs/standards/`. Instead of investigating, Claude attempted `rm -rf shared/standards/` - which would have destroyed an intentional reorganization.

**Root cause**: Reflexive "cleanup" behavior without understanding context or intent.

---

## Objectives

- [ ] Research Claude Code hooks system for pre-command interception
- [ ] Research other solutions (wrapper scripts, aliases, shell hooks)
- [ ] Design guardrail system for destructive commands
- [ ] Implement chosen solution
- [ ] Test with various destructive command patterns
- [ ] Document solution in rules/

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Solution researched (3+ options) | ⬜ | Research notes |
| 2 | Best solution selected with rationale | ⬜ | Decision documented |
| 3 | Implementation complete | ⬜ | Working guardrail |
| 4 | Test cases pass | ⬜ | Test log |
| 5 | Documentation in rules/ | ⬜ | Rule file exists |

---

## Constraints

- Must not break legitimate destructive operations when intentional
- Must work with Claude Code's permission system
- Should be lightweight (not slow down normal operations)

---

## Root Cause Analysis

**Symptom**: Claude attempts rm -rf without understanding
**Investigation**: Pattern of reflexive cleanup behavior
**Root Cause**: No guardrail preventing destructive commands; no pause-and-verify protocol
**Fix Applied**: TBD
**Prevention**: Implement hook or wrapper that requires explicit verification

---

## Research Scope

1. **Claude Code hooks**
   - Pre-command hooks
   - Can they intercept and block?
   - Examples from documentation

2. **Shell-level solutions**
   - rm -i as default
   - Wrapper scripts
   - Trash utilities (trash-cli)

3. **Permission system**
   - Can we deny rm -rf patterns?
   - Selective allows

4. **Behavioral rules**
   - Document in .claude/rules/
   - Make it a HARD STOP

---

## Execution Log

### 2025-12-22

- 03:45 - Mission created after destructive rm -rf attempt during /end

---

## Lessons Learned

[To be filled after completion]

---

_Mission created from template v1.0.0_
