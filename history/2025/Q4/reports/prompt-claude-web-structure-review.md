# Prompt pour Claude Web — Structure Review

**Date**: 2025-12-21 (mis à jour)
**De**: Omar (via Claude Code)
**Pour**: Claude Web

---

## Contexte

Claude Code a effectué un diagnostic complet de notre repo El-Mountassir. Voici ce qui a été fait dans cette session:

### Actions Complétées

| Action | Résultat |
|--------|----------|
| Diagnostic GitHub | 8 questions répondues factuellement |
| `.gitignore` créé | `admin/finance/` et `admin/legal/` protégés |
| Repo renommé | `El-Mountassir/El-Mountassir` → `El-Mountassir/website` |
| Commit | `6636a8f` — .gitignore + rapport diagnostic |
| Structure capturée | STRUCTURE.md créé au root |
| **NOUVEAU: Hook auto-update** | STRUCTURE.md se met à jour automatiquement |
| **NOUVEAU: CLAUDE.md mis à jour** | Inclut `@STRUCTURE.md` + répertoires manquants |

### État GitHub

| Repo | Contenu |
|------|---------|
| `El-Mountassir/website` | Contenu marketing/public (ancien El-Mountassir) |
| `El-Mountassir/El-Mountassir` | **DISPONIBLE** — prêt pour push du repo opérationnel |
| Remote local | Non configuré (à faire) |

---

## NOUVEAU: Mécanisme Auto-Update STRUCTURE.md

Claude Code a mis en place un hook PostToolUse qui:
1. Se déclenche sur chaque Write/Edit/Bash
2. Filtre pour ne régénérer que sur changements structurels (mkdir, mv, rm, etc.)
3. Met à jour automatiquement `STRUCTURE.md` avec `tree`

**Fichiers créés:**
- `.claude/hooks/update-structure.sh` — Script de régénération
- `.claude/settings.json` — Configuration du hook

**Implication pour toi:**
- `STRUCTURE.md` est maintenant **auto-généré** — ne pas éditer manuellement
- Le diagnostic original a été archivé: `history/2025/Q4/reports/structure-diagnostic-2025-12-21.md`
- CLAUDE.md référence maintenant `@STRUCTURE.md` pour que toutes les instances y aient accès

---

## Fichiers Joints

| Fichier | Description |
|---------|-------------|
| `STRUCTURE.md` | Arbre actuel (auto-généré) |
| `history/.../structure-diagnostic-2025-12-21.md` | Diagnostic avec questions Q1-Q5 |

---

## Questions Clés pour Toi

### 1. Alignement CLAUDE.md ↔ Réalité

Le REPOSITORY STRUCTURE dans CLAUDE.md ne reflète pas la réalité:

- `missions/` existe mais n'est pas documenté
- `history/` existe mais n'est pas documenté
- `.claude/` (skills, commands) existe mais n'est pas documenté
- `docs/standards/management/work/` est déclaré mais **N'EXISTE PAS**

**Question**: On met à jour CLAUDE.md pour refléter la réalité? Ou on réorganise?

### 2. Répertoires Vides Sans But Clair

- `omar/model/` — C'était prévu pour quoi?
- `omar/tools/` — C'était prévu pour quoi?
- `configs/system/prompts/` — Quand sera-t-il utilisé?

**Question**: On les garde, on les documente, ou on les supprime?

### 3. Incohérence de Nommage

- `LESSONS-LEARNED/` est en CAPS
- Tout le reste est en lowercase

**Question**: On standardise?

### 4. Standard work/ Manquant

CLAUDE.md déclare `docs/standards/management/work/README.md` mais il n'existe pas.

**Question**: On le crée? On le fusionne avec missions/? On supprime la référence?

---

## Prochaines Étapes Suggérées

1. **Omar + Claude Web**: Décider sur les 5 questions dans STRUCTURE.md
2. **Claude Code**: Implémenter les décisions (créer mission si nécessaire)
3. **Claude Code**: Push vers `El-Mountassir/El-Mountassir` une fois structure validée

---

## Pour Continuer

Une fois vos décisions prises, créez une mission ou transmettez directement à Claude Code avec:

- Décisions sur Q1-Q5
- Priorités si tout ne peut pas être fait maintenant
- Toute autre observation sur la structure

---

_Prompt généré par Claude Code — 2025-12-21_
