# Standards Index

> Hub central pour tous nos standards.

---

## Standards Techniques

| Standard | Fichier | Description |
|----------|---------|-------------|
| SemVer 2.0.0 | [project-standards.md](project-standards.md) | Versioning sémantique avec Zero-State |
| Dublin Core | [project-standards.md](project-standards.md) | 15 éléments de métadonnées |
| Keep a Changelog | [project-standards.md](project-standards.md) | Format de changelog |
| State Management | [state-management.md](state-management.md) | Gestion d'état pour projets |

---

## Standards Management

| Standard | Fichier | Description |
|----------|---------|-------------|
| Missions | [management/missions/README.md](management/missions/README.md) | Work packages multi-step |
| Time | [management/time/README.md](management/time/README.md) | Gestion du temps, calendar |
| Work | [management/work/README.md](management/work/README.md) | DoR, DoD, Task Lifecycle, Priority |

---

## Quick Reference

### Versioning (SemVer)

```
MAJOR.MINOR.PATCH-PRERELEASE
0.0.0-alpha.0  →  Initial (Zero-State)
0.0.1-alpha.0  →  First patch started
1.0.0-osr.1    →  Official Stable Release
```

### Task States

```
[Ready] → [In Progress] → [Review] → [Done]
    ↓           ↓
[Blocked] ← [Blocked]
    ↓
[Escalated]
```

### Priority Matrix

| Priority | Action |
|----------|--------|
| P0 | Do immediately |
| P1 | Do today |
| P2 | Delegate/schedule |
| P3 | Batch for later |
| P4 | Backlog/defer |

---

_Auto-référencé par CLAUDE.md | Mis à jour 2025-12-22_
