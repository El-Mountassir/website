# Mission: Behavior Fix

```yaml
mission_id: 2025-12-21-behavior-fix
status: DRAFT
assigned_to: Claude Code
created: 2025-12-21
assigned:
completed:
archived:
priority: 2
blocks: [session-commands]
```

---

## Context

Omar a identifié un problème de comportement: dire "session complete" sans avoir capturé les items restants en missions. Cette mission documente la correction.

**Feedback Omar**: "Toute chose à faire, même mineur et/ou non-blockant reste quelque chose à faire!"

---

## Objectives

- [ ] **O1**: Ajouter règle anti-clôture dans CLAUDE.md
- [ ] **O2**: Créer LESSONS-LEARNED/2025-12-21-premature-closure.md
- [ ] **O3**: Commit la correction

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Règle dans CLAUDE.md | ⬜ | Section HARD STOPS mise à jour |
| 2 | Lesson learned créée | ⬜ | Fichier existe avec contenu |
| 3 | Commit fait | ⬜ | Commit hash |

---

## Constraints

- **Haute priorité** — affecte toutes les sessions futures
- **Doit bloquer M4** (Session Commands)

---

## Execution Steps

### Step 1: Ajouter règle dans CLAUDE.md

Dans la section HARD STOPS, ajouter:

```markdown
| 6   | **No premature closure** | NEVER say "session complete" without capturing ALL remaining items as missions. Even minor/non-blocking items must be captured. |
```

### Step 2: Créer lesson learned

`LESSONS-LEARNED/2025-12-21-premature-closure.md`:

```markdown
# Lesson: Premature Session Closure

**Date**: 2025-12-21
**Category**: Behavioral
**Severity**: High

---

## What Happened

Instance said "session complete" without capturing remaining items:
- Questions structure (Q1-Q5) not captured as missions
- GitHub push not captured as mission
- Items mentioned but not formalized

## Impact

- Items lost between sessions
- User frustration
- Broken continuity

## Root Cause

- Focus on immediate tasks over completeness
- No systematic check before closure
- "Session complete" used too liberally

## Correction

1. Added HARD STOP rule #6 in CLAUDE.md
2. Will implement /end skill with guardrails (Mission: session-commands)

## Prevention

Before ANY session closure:
- [ ] Check for uncaptured items
- [ ] Create missions for ALL remaining work
- [ ] Verify git status is clean
- [ ] Update CHANGELOG.md if changes made

---

_Lesson documented by Claude Code | 2025-12-21_
```

### Step 3: Commit

```bash
git add CLAUDE.md LESSONS-LEARNED/2025-12-21-premature-closure.md
git commit -m "fix(behavior): add anti-premature-closure rule

- Add HARD STOP #6: never say 'session complete' without capturing items
- Document lesson learned from 2025-12-21 incident
- This enables future /end skill with guardrails

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Execution Log

> Append-only.

### 2025-12-21

- **Created**: Mission drafted

---

_Mission v0.0.1-alpha.0_
