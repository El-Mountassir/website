# Directory Reorganization Checklist

Use this checklist before executing any directory reorganization.

---

## Pre-Flight Checks

### 1. Understanding

- [ ] **Purpose clear**: I understand WHY this reorganization is needed
- [ ] **Scope defined**: I know exactly which directories/files are affected
- [ ] **User confirmed**: I've confirmed ambiguous decisions with the user

### 2. Current State

- [ ] **Git status clean**: No unrelated pending changes in affected area
- [ ] **Structure documented**: I've run `tree` or `ls` to understand current state
- [ ] **Empty dirs identified**: I know which directories are empty and why

### 3. Separation of Concerns

| Question | Answer | Implication |
|----------|--------|-------------|
| Is this about WHO someone is? | | → `{user}/context/` |
| Is this a system or process? | | → `admin/` |
| Is this client/project work? | | → `projects/` |
| Is this learning material? | | → `learning/` |

- [ ] **Concerns separated**: Each directory has a single clear purpose

### 4. References

- [ ] **CLAUDE.md checked**: No broken `@` references will result
- [ ] **INDEX.md checked**: IDs and references still valid
- [ ] **Other .md files**: No broken relative links

### 5. Decision Log

For each change, document:

| From | To | Rationale |
|------|-----|-----------|
| | | |
| | | |
| | | |

---

## Execution Checks

### 6. Git Operations

- [ ] **Use `git mv`**: For moves (preserves history)
- [ ] **Use `git rm`**: For deletions (clean tracking)
- [ ] **Placeholder READMEs**: Empty dirs have documented intent

### 7. Verification

- [ ] **`git status`**: Shows expected changes only
- [ ] **`tree` or `ls`**: Structure matches target
- [ ] **Test references**: `@` paths in CLAUDE.md work

### 8. Commit

- [ ] **Conventional format**: `chore(scope): description`
- [ ] **Atomic change**: One logical reorganization per commit
- [ ] **Clear message**: Future instances understand what/why

---

## Post-Flight Checks

### 9. Documentation

- [ ] **Decisions captured**: If significant, add to LESSONS-LEARNED/
- [ ] **Mission archived**: If part of a mission, update execution log

### 10. Cleanup

- [ ] **No orphaned files**: Everything is where it should be
- [ ] **No broken references**: All links work
- [ ] **Git clean**: `git status` shows clean working tree

---

## Quick Reference

### Commit Message Template

```
chore(scope): brief description

- Change 1: what → what (why)
- Change 2: what → what (why)
- Change 3: what → what (why)
```

### Common Mistakes

| Mistake | Prevention |
|---------|------------|
| Delete without checking references | Always `grep -r` first |
| Leave empty dirs without explanation | Add README with intent |
| Mix multiple reorganizations | One logical change per commit |
| Forget to update CLAUDE.md | Check `@` references |
| Lose git history | Use `git mv`, not delete+create |

---

_Checklist v0.1.0 — Use with reorganizing-directories skill_
