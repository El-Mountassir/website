# Mission: Rule File Deduplication

**ID**: M1-2025-12-22
**Status**: QUEUED
**Priority**: HIGH
**Estimated effort**: 30 min

---

## Objective

Eliminate duplicate rule files between `~/.claude/rules/` and `.claude/rules/` to save ~3.5k tokens per session.

## Context

Research found 5 files in both locations:
- 3 IDENTICAL (partnership.md, taxonomy.md, world-model.md)
- 2 DIFFERENT (behavior.md, memory-protocol.md)

## Success Criteria

- [ ] All rules consolidated in `.claude/rules/` (project-level)
- [ ] No duplicates in `~/.claude/rules/`
- [ ] Merged versions contain best of both
- [ ] Verified working after changes

## Tasks

1. [ ] Compare behavior.md versions (diff)
2. [ ] Compare memory-protocol.md versions (diff)
3. [ ] Create merged versions with best content
4. [ ] Backup original files
5. [ ] Remove duplicates from ~/.claude/rules/
6. [ ] Test new session to verify

## Execution Log

(To be filled during execution)

---

_Created: 2025-12-22_
