# Mission: Claude Web Sync

```yaml
mission_id: 2025-12-21-claude-web-sync
status: DRAFT
assigned_to: Claude Code
created: 2025-12-21
assigned:
completed:
archived:
priority: 2
depends_on: []  # github-push completed (archived)
```

---

## Context

Maintenir la synchronisation entre Claude Code et Claude Web. Claude Web a besoin d'accès au repo GitHub pour voir la structure et collaborer efficacement.

**Conversation Claude Web**: https://claude.ai/chat/4c192da5-e9fb-46c7-99a4-c0305b5d1b00

---

## Objectives

- [ ] **O1**: Confirmer à Claude Web que le repo est accessible
- [ ] **O2**: Récupérer le system prompt de Claude.ai Web
- [ ] **O3**: Sauvegarder le system prompt dans `configs/system/prompts/`
- [ ] **O4**: Mettre à jour le pont de communication

---

## Success Criteria

| #   | Criterion                    | Status | Evidence                       |
| --- | ---------------------------- | ------ | ------------------------------ |
| 1   | Claude Web peut voir le repo | ⬜     | Confirmation dans conversation |
| 2   | System prompt récupéré       | ⬜     | Fichier créé                   |
| 3   | Pont de communication à jour | ⬜     | Fichier mis à jour             |

---

## Constraints

- ~~**Dépend de M1** (GitHub Push)~~ — ✅ COMPLETED (archived)
- **Via Chrome automation** (`--chrome` mode)
- **Conversation link may be stale** — verify accessibility first

---

## Execution Steps

### Step 1: Vérifier M1 complète

```bash
# Confirmer que le repo est pushé
git remote -v
git log origin/main -1
```

### Step 2: Continuer conversation Claude Web

Via Chrome automation:

1. Naviguer vers https://claude.ai/chat/4c192da5-e9fb-46c7-99a4-c0305b5d1b00
2. Informer Claude Web que le repo est accessible
3. Demander le system prompt

### Step 3: Sauvegarder system prompt

```bash
# Créer le fichier
mkdir -p configs/system/prompts/
# Sauvegarder le contenu récupéré
```

### Step 4: Document sync status

```bash
# Create sync report in history/
mkdir -p history/2025/Q4/reports/claude-web-sync/
# Document: what was synced, conversation status, next steps
```

---

## Execution Log

> Append-only.

### 2025-12-21

- **Created**: Mission drafted

---

_Mission v0.0.1-alpha.0_
