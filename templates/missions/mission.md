# Mission: [Descriptive Title]

```yaml
# Core Metadata
mission_id: YYYY-MM-DD-{slug}
type: STANDARD # STANDARD | ELEVATE | FIX | FEATURE | RESEARCH | MIGRATION
status: DRAFT # DRAFT | QUEUED | ACTIVE | COMPLETED | ARCHIVED
priority: P2 # P0 (critical) | P1 (high) | P2 (normal) | P3 (low)

# Assignment
assigned_to: Unassigned # Claude Code | Claude Web | Omar | Unassigned
created: YYYY-MM-DD
assigned:
claimed_at: # ISO timestamp when instance started (e.g., 2025-12-22T03:45:00+01:00)
claimed_by: # Session description (e.g., "Thaifa P0 migration session")
completed:
archived:

# Optional: Source tracking (for ELEVATE/FIX types)
source_session: # Description of originating session
source_insight: # The insight or issue that triggered this mission
```

---

## Context

[Why this mission exists. Business impact. Background.]

---

## Objectives

- [ ] Objective 1: [Clear, measurable]
- [ ] Objective 2: [Clear, measurable]
- [ ] Objective 3: [Clear, measurable]

---

## Success Criteria

| #   | Criterion            | Status | Evidence |
| --- | -------------------- | ------ | -------- |
| 1   | [Measurable outcome] | ⬜     |          |
| 2   | [Measurable outcome] | ⬜     |          |
| 3   | [Measurable outcome] | ⬜     |          |

---

## Constraints

- [Time constraint]
- [Resource constraint]
- [Technical constraint]

---

<!-- TYPE: ELEVATE, RESEARCH — Pipeline Progress -->
<!--
## Pipeline Progress

| Step | Status | Output |
|------|--------|--------|
| Step-back | ⬜ | |
| Sources | ⬜ | |
| Patterns | ⬜ | |
| Synthesis | ⬜ | |
| Final | ⬜ | |
-->

<!-- TYPE: FIX — Root Cause Analysis -->
<!--
## Root Cause Analysis

**Symptom**: [What was observed]
**Investigation**: [What was checked]
**Root Cause**: [The actual cause]
**Fix Applied**: [What was done]
**Prevention**: [How to prevent recurrence]
-->

<!-- TYPE: MIGRATION — Migration Checklist -->
<!--
## Migration Checklist

- [ ] Backup created
- [ ] Dependencies identified
- [ ] Rollback plan documented
- [ ] Stakeholders notified
- [ ] Post-migration validation
-->

---

## Execution Log

> Append-only. Add entries as work progresses.
> First entry should be "CLAIMED by [session description]" when work begins.

### YYYY-MM-DD

- HH:MM - [Action taken]
- HH:MM - [Result]

---

## Deviations

[Document any differences from original spec. What changed and why.]

---

## Lessons Learned

[What to do differently next time. Patterns to extract. Rules to add.]

---

<!-- TYPE: ELEVATE, RESEARCH — Promotion Decision -->
<!--
## Promotion Decision

| Aspect | Assessment |
|--------|------------|
| Reusable? | Yes/No |
| Promote to | docs/reference/guides/ or N/A |
| Index update needed? | Yes/No |
| CLAUDE.md update needed? | Yes/No |
-->

---

## Quality Gates (Pre-Archive)

- [ ] All success criteria have evidence
- [ ] Execution log is complete
- [ ] Deviations documented
- [ ] Lessons learned captured
- [ ] Files in correct archive location

---

_Mission created from template v0.1.0-alpha.0_
