# Mission: Align Documentation with ~/Documents/base/

```yaml
mission_id: 2025-12-22-docs-base-alignment
status: QUEUED
assigned_to: Claude Code
created: 2025-12-22
priority: 1
depends_on: []
```

---

## Context

Omar a récemment restructuré `~/Documents/` vers une nouvelle architecture `~/Documents/base/`. Plusieurs fichiers de configuration référencent des chemins obsolètes.

**Nouvelle structure**:
```
~/Documents/base/sources/
├── core/          # identity, partnership, principles, world-model, current
├── framework/     # thinking, verification, capture, internet
├── memory/        # decisions, issues, patterns, preferences
├── knowledge/     # concepts, refined, sources
├── resources/     # prompts, templates
├── tech/, biz/, personal/
└── vault/         # secrets, credentials
```

---

## Objectives

### Phase 1: Audit & Map (Discovery)

- [ ] **O1**: Lister TOUS les fichiers qui référencent des chemins ~/Documents/
- [ ] **O2**: Créer une table de mapping: ancien chemin → nouveau chemin
- [ ] **O3**: Identifier les fichiers dupliqués (rules/, core/, etc.)

### Phase 2: Décisions (Requires Omar)

- [ ] **O4**: Décider: règles globales (~/.claude/rules/) vs projet (.claude/rules/)
- [ ] **O5**: Décider: merger kb/ → base/sources/knowledge/ ou garder séparés?
- [ ] **O6**: Valider le mapping des chemins

### Phase 3: Exécution

- [ ] **O7**: Mettre à jour memory-protocol.md avec nouveaux chemins
- [ ] **O8**: Consolider les règles (supprimer duplications)
- [ ] **O9**: Migrer kb/ si décidé
- [ ] **O10**: Mettre à jour toutes les références dans le projet

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Aucun chemin cassé | ⬜ | `grep -r "~/Documents/" .` retourne 0 références obsolètes |
| 2 | Pas de duplication | ⬜ | Un seul fichier par concept (pas rules/ + core/) |
| 3 | memory-protocol.md fonctionnel | ⬜ | Chemins pointent vers fichiers existants |

---

## Scope Creep Warning

**Ne PAS faire dans cette mission**:
- Restructurer ~/Documents/base/ lui-même
- Créer de nouveaux fichiers (seulement aligner l'existant)
- Changer la logique des fichiers (seulement les chemins)

---

## Files to Audit

| File | Contains ~/Documents/ refs? |
|------|----------------------------|
| `.claude/rules/memory-protocol.md` | ✅ YES - chemins obsolètes |
| `~/.claude/rules/memory-protocol.md` | ✅ YES - chemins obsolètes |
| `CLAUDE.md` | ⬜ To check |
| `.claude/skills/*/SKILL.md` | ⬜ To check |

---

## Execution Log

> Append-only.

### 2025-12-22

- **Created**: Mission created after discovering structure mismatch
- **Discovery**: memory-protocol.md references `~/Documents/user/memory/` but actual path is `~/Documents/base/sources/memory/`

---

_Mission v0.0.1-alpha.0_
