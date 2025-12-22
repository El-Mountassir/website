# Mission: Sub-agent Architecture

**ID**: M4-2025-12-22
**Status**: QUEUED
**Priority**: HIGH
**Estimated effort**: 3 hours

---

## Objective

Create 5 specialized sub-agents to enable the orchestrator pattern, each with focused capabilities and skills.

## Context

Approved agents:
1. **Scout** - Read-only analysis, codebase exploration
2. **Researcher** - Web search, documentation lookup
3. **Implementer** - Code writing, file creation (background capable)
4. **Reviewer** - Code review, validation, quality checks
5. **Documenter** - Documentation updates, changelog, README

## Success Criteria

- [ ] 5 agent files created in .claude/agents/
- [ ] Each agent has appropriate tool restrictions
- [ ] Skills assigned where relevant
- [ ] Clear descriptions for auto-invocation
- [ ] Tested with sample delegations

## Agent Specifications

### Scout
- Tools: Read, Glob, Grep
- Skills: None (pure exploration)
- Output: Structured findings report

### Researcher
- Tools: WebSearch, WebFetch, Read
- Skills: None
- Output: Research summary with sources

### Implementer
- Tools: Write, Edit, Bash, Read
- Skills: As needed
- Background: Enabled

### Reviewer
- Tools: Read, Grep, Glob
- Skills: None
- Output: Review report with recommendations

### Documenter
- Tools: Write, Edit, Read
- Skills: None
- Output: Updated documentation

## Tasks

1. [ ] Create scout.md
2. [ ] Create researcher.md
3. [ ] Create implementer.md
4. [ ] Create reviewer.md
5. [ ] Create documenter.md
6. [ ] Test each agent with sample task
7. [ ] Document agent usage in orchestration guide

## Execution Log

(To be filled during execution)

---

_Created: 2025-12-22_
