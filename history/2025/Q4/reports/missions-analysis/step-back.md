# Step-Back Analysis

**Date**: 2025-12-22
**Request**: Analyser les missions restantes car "c'est pas top"

## Problem Statement

Les 4 missions restantes (M2, M3, M4, M7) ont été créées dans la précipitation lors de la consolidation du chaos. Elles présentent des problèmes structurels qui les rendent difficiles à exécuter proprement.

## Initial Observations

| Mission | Fichier | Problèmes Identifiés |
|---------|---------|----------------------|
| **M2** claude-web-sync | `drafts/claude-web-sync.md` | O5 est ÉNORME et hors scope ("harmoniser le repo") |
| **M3** deferred-items | `drafts/deferred-items.md` | Extrêmement vague, O1 duplique M2, aucune liste d'items |
| **M4** session-commands | `drafts/session-commands.md` | Dépendance stale (M5 déjà archivée), sinon bien définie |
| **M7** omar-cleanup | `queue/2025-12-21-omar-cleanup.md` | Bien définie, prête à exécuter |

## Success Criteria

Pour que les missions soient "top":

1. **Scope clair**: Chaque mission = UN problème distinct, pas un fourre-tout
2. **Objectifs SMART**: Specific, Measurable, Achievable, Relevant, Time-bound
3. **Dépendances correctes**: Pas de références à des missions archivées
4. **Aucune duplication**: Chaque objectif apparaît une seule fois
5. **Priorité définie**: Ordre d'exécution clair
6. **Exécutable**: Un agent peut prendre la mission et savoir exactement quoi faire

## Domain Concepts

- **Mission**: Work package multi-step avec objectifs et critères de succès
- **Scope creep**: Ajout d'objectifs hors-scope qui diluent la mission
- **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable
- **DoR (Definition of Ready)**: Critères pour qu'une mission soit prête à exécuter

## Verdict Préliminaire

| Mission | Verdict | Action |
|---------|---------|--------|
| M2 | **REFACTOR** | Retirer O5, créer mission séparée |
| M3 | **DELETE** | Trop vague, duplique M2, apporte rien |
| M4 | **UPDATE** | Corriger dépendance stale |
| M7 | **READY** | Peut être exécutée telle quelle |

---

_Step-back completed | 2025-12-22_
