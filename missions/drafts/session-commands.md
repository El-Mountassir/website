# Mission: Session Commands (/start, /end)

```yaml
mission_id: 2025-12-21-session-commands
status: DRAFT
assigned_to: Claude Code
created: 2025-12-21
assigned:
completed:
archived:
priority: 4
depends_on: [behavior-fix]
```

---

## Context

Créer des skills `/start` et `/end` pour structurer les sessions et empêcher les clôtures prématurées.

**Feedback Omar**: "Toute chose à faire, même mineur et/ou non-blockant reste quelque chose à faire!"

---

## Objectives

- [ ] **O1**: Créer skill `/start` (onboarding session)
- [ ] **O2**: Créer skill `/end` (avec guardrails)
- [ ] **O3**: Documenter dans CLAUDE.md
- [ ] **O4**: Tester les guardrails

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | /start fonctionne | ⬜ | Skill crée, testé |
| 2 | /end bloque si items non capturés | ⬜ | Test avec items pendants |
| 3 | /end bloque si git dirty | ⬜ | Test avec changes non commit |
| 4 | Documenté | ⬜ | Dans CLAUDE.md |

---

## Constraints

- **Dépend de M5** (Behavior Fix) — la règle doit exister d'abord

---

## Execution Steps

### Step 1: Créer /start skill

`.claude/skills/session-start/SKILL.md`:

```markdown
# /start - Session Start

## Behavior

1. Check missions/active/
   - Si mission(s) active(s) → "Laquelle reprendre?"
   - Si aucune → "Quelle nouvelle initiative?"
2. Charger contexte (CLAUDE.md, état mission)
3. Afficher: objectifs restants, dernière action, prochaine étape
```

### Step 2: Créer /end skill

`.claude/skills/session-end/SKILL.md`:

```markdown
# /end - Session End

## Guardrails (BLOQUANTS)

1. Items non capturés en missions? → BLOQUER + créer missions
2. Git dirty? → BLOQUER + demander commit
3. CHANGELOG.md à jour? → Avertir si non

## Si OK

- Résumer session
- Lister missions créées/avancées
- Autoriser clôture
```

### Step 3: Documenter

Ajouter dans CLAUDE.md section sur `/start` et `/end`.

### Step 4: Tester

Exécuter `/end` avec des items pendants pour vérifier le blocage.

---

## Execution Log

> Append-only.

### 2025-12-21

- **Created**: Mission drafted

---

_Mission v0.0.1-alpha.0_
