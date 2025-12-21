# Mission: Restructuration docs/standards/ (Option C+)

```yaml
mission_id: 2025-12-22-restructuration-standards
status: DRAFT
assigned_to: Claude Code
created: 2025-12-22
assigned:
completed:
archived:
priority: 3
blocks: [omar-cleanup]
```

---

## Context

Analyse de `docs/standards/` a révélé un "bordel":
- `specs/versioning.md` est VIDE (fichier fantôme)
- `project-standards.md` contient Work Management, mais missions/ et time/ ont leurs propres dossiers
- Incohérence structurelle

**Décision**: Option C+ (Hybride + Index) recommandée par Claude Web et Claude Code.

---

## Objectives

- [ ] **O1**: Supprimer `specs/versioning.md` (fichier fantôme)
- [ ] **O2**: Créer `management/work/README.md` avec contenu extrait
- [ ] **O3**: Retirer section Work Management de `project-standards.md`
- [ ] **O4**: Créer `docs/standards/INDEX.md` (hub)
- [ ] **O5**: Mettre à jour références dans CLAUDE.md
- [ ] **O6**: Commit et vérifier cohérence

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Fichier fantôme supprimé | ⬜ | `specs/versioning.md` n'existe plus |
| 2 | Work Management extrait | ⬜ | `management/work/README.md` existe |
| 3 | project-standards.md allégé | ⬜ | Section 4 retirée |
| 4 | Index créé | ⬜ | `docs/standards/INDEX.md` existe |
| 5 | Références à jour | ⬜ | CLAUDE.md cohérent |

---

## Constraints

- **Doit bloquer M7** (omar-cleanup) — structure stable avant nettoyage
- **Préserver** contenu, juste réorganiser

---

## Execution Steps

### Step 1: Supprimer fichier fantôme

```bash
rm docs/standards/specs/versioning.md
rmdir docs/standards/specs/  # Si vide
```

### Step 2: Créer management/work/

```bash
mkdir -p docs/standards/management/work/
```

Créer `README.md` avec la section 4 de `project-standards.md`.

### Step 3: Modifier project-standards.md

Retirer la section "4. Work Management Protocols" (tout après "## 4. Work Management Protocols").

Ajouter à la fin:

```markdown
---

> **Work Management Protocols** moved to `management/work/README.md` for consistency with missions/ and time/.
```

### Step 4: Créer INDEX.md

`docs/standards/INDEX.md`:

```markdown
# Standards Index

> Hub central pour tous nos standards.

---

## Standards Techniques

| Standard | Fichier | Description |
|----------|---------|-------------|
| SemVer 2.0.0 | `project-standards.md` | Versioning sémantique |
| Dublin Core | `project-standards.md` | Métadonnées |
| Keep a Changelog | `project-standards.md` | Format changelog |
| State Management | `state-management.md` | Gestion d'état projets |

## Standards Management

| Standard | Fichier | Description |
|----------|---------|-------------|
| Missions | `management/missions/README.md` | Work packages multi-step |
| Time | `management/time/README.md` | Gestion du temps |
| Work | `management/work/README.md` | DoR, DoD, Task Lifecycle |

---

_Auto-référencé par CLAUDE.md_
```

### Step 5: Mettre à jour CLAUDE.md

Vérifier que les références sont correctes. Ajouter `@docs/standards/INDEX.md` si approprié.

### Step 6: Commit

```bash
git add -A docs/standards/
git add CLAUDE.md
git commit -m "refactor(standards): restructure with Option C+ (hybrid + index)

- Remove ghost file specs/versioning.md (was empty)
- Extract Work Management to management/work/README.md
- Create INDEX.md as central hub
- Maintain consistency with missions/ and time/ structure

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Execution Log

> Append-only.

### 2025-12-22

- **Created**: Mission drafted based on Claude Web recommendation

---

_Mission v0.0.1-alpha.0_
