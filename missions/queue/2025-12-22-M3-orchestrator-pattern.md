# Mission: Orchestrator Pattern Implementation

**ID**: M3-2025-12-22
**Status**: QUEUED
**Priority**: CRITICAL
**Estimated effort**: 2 hours

---

## Objective

Transform main Claude instance from worker to conductor/orchestrator, preserving context window by delegating work to sub-agents.

## Context

Current problem:
- Main instance does all work itself
- Context window destroyed by file reads, code analysis, etc.
- Sub-agents underutilized

Target behavior:
- Main instance = Conductor (orchestration, decisions, user communication)
- Sub-agents = Specialists (research, implementation, review)
- Context preserved for high-level thinking

## Success Criteria

- [ ] Orchestration standard documented in docs/standards/orchestration/
- [ ] behavior.md updated with delegation patterns
- [ ] Clear guidelines for when to delegate vs do directly
- [ ] Examples of good orchestration patterns

## Tasks

1. [ ] Create docs/standards/orchestration/README.md
2. [ ] Define delegation decision tree
3. [ ] Document sub-agent communication patterns
4. [ ] Update .claude/rules/behavior.md
5. [ ] Create examples in docs/standards/orchestration/examples/

## Deliverables

- docs/standards/orchestration/README.md
- docs/standards/orchestration/examples/*.md
- Updated .claude/rules/behavior.md

## Execution Log

(To be filled during execution)

---

_Created: 2025-12-22_
