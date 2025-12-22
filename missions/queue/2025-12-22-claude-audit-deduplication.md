---
title: "Audit CLAUDE.md & .claude/ — Déduplication et Cohérence"
type: STANDARD
priority: P0
created: 2025-12-22
assigned_to: Claude Code
status: READY
version: 0.0.1-alpha.0
verification_required: true
verification_instances: 2
---

# Mission: Audit CLAUDE.md & .claude/ — Déduplication et Cohérence

## Context

L'audit du repository a révélé **11 catégories de problèmes** représentant une dette structurelle massive :

| Catégorie | Sévérité |
|-----------|----------|
| Références @ manquantes | CRITIQUE |
| Duplication User Preferences | HAUTE |
| Hard Stops triplés | HAUTE |
| Agents non documentés (7) | HAUTE |
| Skills non documentés (5) | HAUTE |
| Memory protocol x5 | HAUTE |
| Scope confusion .claude/ vs shared/ | HAUTE |
| Identifier: obsolètes (3) | MOYENNE |
| Lien cassé templates/ (1) | MOYENNE |
| CLAUDE.md > 300 lignes | MOYENNE |

## Objectives

1. Réduire CLAUDE.md de ~300 lignes à < 150 lignes
2. Charger tous les fichiers critiques via @
3. Éliminer toute duplication (SSOT)
4. Documenter agents et skills
5. Séparer clairement .claude/ (Claude) vs shared/ (org)
6. Fixer metadata et liens cassés
7. Vérifier par 2 instances

## Success Criteria

| # | Criterion | Verification |
|---|-----------|--------------|
| 1 | CLAUDE.md < 150 lignes | `wc -l CLAUDE.md` |
| 2 | Tous fichiers critiques chargés via @ | Grep @shared/, @.claude/ |
| 3 | Zéro duplication | Diff entre fichiers |
| 4 | Agents documentés | Section dans CLAUDE.md |
| 5 | Skills documentés | Section dans CLAUDE.md |
| 6 | Metadata corrects | Grep Identifier: |
| 7 | Zéro lien cassé | Test liens markdown |
| 8 | Vérifié par 2 instances | Sign-off dans log |

## Plan Reference

**Full plan**: `/home/omar/.claude/plans/agile-tickling-lobster.md`

## Phases Summary

| Phase | Description | Fichiers |
|-------|-------------|----------|
| 1 | Références @ critiques | CLAUDE.md |
| 2 | Migration rules → shared | 5 fichiers |
| 3 | Déduplication CLAUDE.md | CLAUDE.md + 2 créations |
| 4 | Consolidation User Context | omar/context/ → archive |
| 5 | Fix Metadata & Liens | 4 fichiers |
| 6 | Documentation Agents/Skills | CLAUDE.md, shared/INDEX.md |
| 7 | Clarification Memory | .claude/memory/ |

## Verification Protocol

> **RÈGLE**: Cette mission doit être vérifiée par 2 sessions séparées.

### Session 1 (Exécution)
- Claim depuis queue/ → active/
- Exécute phases 1-7
- Commit
- Archive vers history/

### Session 2 (Vérification 1)
- Nouvelle session
- Vérifie @ chargement
- Vérifie absence duplication
- Documente problèmes

### Session 3 (Vérification 2)
- Nouvelle session
- Contre-vérifie session 2
- Teste /start, /end, /sync, /elevate
- Sign-off final

---

## Execution Log

_À remplir par l'instance qui exécute_

---

_Mission v0.0.1-alpha.0_
