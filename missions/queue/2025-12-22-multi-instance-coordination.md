# Mission: Multi-Instance Coordination System

```yaml
mission_id: 2025-12-22-multi-instance-coordination
status: DRAFT
assigned_to: Claude Code
created: 2025-12-22
priority: 1
depends_on: []
```

---

## Context

Quand Omar travaille avec plusieurs instances Claude Code en parallèle (différentes sessions, terminaux, ou conversations), il y a des risques de:
- Conflits sur les mêmes fichiers
- Travail dupliqué
- Pertes de contexte entre instances
- Conflits git lors des pushes

**Déjà implémenté**:
- Claiming Protocol (`/start`, `/end`) pour missions
- `missions/active/` comme verrou filesystem
- Métadonnées `claimed_at`, `claimed_by`

**Manque encore**:
- Coordination des fichiers partagés (rules/, CLAUDE.md)
- Communication inter-instances
- Gestion des conflits git
- Visibilité sur l'état global

---

## Problem Statement

Comment coordonner N instances Claude Code travaillant en parallèle sans conflits ni pertes?

---

## Objectives

### Phase 1: Design

- [ ] **O1**: Analyser les patterns de conflits actuels
- [ ] **O2**: Rechercher les solutions existantes (distributed systems patterns)
- [ ] **O3**: Designer un système de coordination minimal viable

### Phase 2: Implementation

- [ ] **O4**: Implémenter le mécanisme choisi
- [ ] **O5**: Mettre à jour `/start` et `/end` si nécessaire
- [ ] **O6**: Documenter le protocole

### Phase 3: Validation

- [ ] **O7**: Tester avec 2+ instances en parallèle
- [ ] **O8**: Documenter les edge cases

---

## Potential Solutions (to evaluate)

### Option A: Git Branches per Instance

```
main
├── instance/session-123
├── instance/session-456
└── instance/session-789
```

**Pros**: Isolation naturelle, merge explicite
**Cons**: Overhead git, merges manuels

### Option B: Lock Files for Shared Resources

```
.locks/
├── CLAUDE.md.lock  # {"instance": "...", "since": "..."}
├── rules/behavior.md.lock
```

**Pros**: Simple, granulaire
**Cons**: Stale locks, overhead

### Option C: Centralized Status File

```
.claude/status.json
{
  "instances": [
    {"id": "abc", "started": "...", "mission": "...", "files_touched": [...]}
  ]
}
```

**Pros**: Vue globale
**Cons**: Conflits sur le fichier lui-même

### Option D: Convention-Based (No Technical Lock)

- Missions = scope isolated (different directories)
- Rules/CLAUDE.md = append-only during session
- Git conflicts = manual resolution

**Pros**: Zero overhead
**Cons**: Relies on discipline

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Pas de perte de travail | ⬜ | Test avec 2 instances |
| 2 | Conflits détectables | ⬜ | Warning si même fichier |
| 3 | Overhead minimal | ⬜ | < 5s par opération |
| 4 | Documenté | ⬜ | Dans CLAUDE.md |

---

## Execution Log

> Append-only.

### 2025-12-22

- **Created**: Mission drafted after Omar identified multi-instance problem
- **Context**: 4 missions in queue being worked by different instances

---

_Mission v0.0.1-alpha.0_
