# Questions: Unification docs/standards/

**Date**: 2025-12-21
**Contexte**: Restructuration de `docs/standards/` pour éliminer le bordel
**Plan**: `~/.claude/plans/composed-weaving-parrot.md`

---

## Résumé du Problème

```
docs/standards/
├── project-standards.md          (292 lignes) — Contient 4 sujets différents
├── state-management.md           (173 lignes) — OK
├── management/
│   ├── missions/README.md        (303 lignes) — OK
│   └── time/README.md            (331 lignes) — OK
└── specs/
    └── versioning.md             (0 lignes) — VIDE ⚠️ Fichier fantôme!
```

**Problèmes**:

1. `specs/versioning.md` est **VIDE** mais référencé dans CLAUDE.md
2. `project-standards.md` contient Work Management, mais missions/ et time/ ont leurs propres dossiers → incohérence
3. INDEX.md référence des fichiers qui n'existent pas

---

## Questions

### Q1: Option de restructuration

| Option | Description                                                                                                | Effort |
| ------ | ---------------------------------------------------------------------------------------------------------- | ------ |
| **A**  | Tout éclater: chaque standard = 1 fichier (semver.md, dublin-core.md, changelog.md, work/)                 | Élevé  |
| **B**  | Minimal: juste supprimer les fichiers fantômes, garder project-standards.md intact                         | Faible |
| **C**  | Hybride: extraire Work Management vers management/work/, garder project-standards.md pour specs techniques | Moyen  |

**Ma recommandation**: Option C (hybride)

**Ta réponse**: [ ] A / [ ] B / [x] C / [ ] Autre: **\*\***\_**\*\***

---

### Q2: Que faire avec state-management.md?

| Option                              | Description                            |
| ----------------------------------- | -------------------------------------- |
| **Garder à la racine**              | state-management.md reste où il est    |
| **Déplacer vers management/state/** | Pour cohérence avec missions/ et time/ |

**Ma recommandation**: Garder à la racine (il couvre aussi les templates, pas juste le management)

**Ta réponse**: [x] Racine / [ ] management/state/ / [ ] Autre: **\*\***\_**\*\***

---

### Q3: Renommer project-standards.md?

Si on garde Option C, le fichier ne contiendra plus que SemVer, Dublin Core, et Changelog.

| Option            | Description                                   |
| ----------------- | --------------------------------------------- |
| **Garder le nom** | project-standards.md (même si contenu réduit) |
| **Renommer**      | technical-specs.md (plus précis)              |

**Ma recommandation**: Garder le nom (moins de références à casser)

**Ta réponse**: [x] Garder / [ ] Renommer → **\*\***\_**\*\*** / [ ] Autre: **\*\***\_**\*\***

---

### Q4: Mission omar-cleanup en queue

La session 3 a créé une mission `missions/queue/2025-12-21-omar-cleanup.md`.

**Question**: On l'exécute maintenant ou après l'unification des standards?

**Ta réponse**: [ ] Maintenant / [x] Après unification / [ ] Annuler la mission

---

## Pour Répondre

Édite ce fichier en cochant [x] tes choix, puis dis-moi "c'est bon" et je réactiverai le plan mode.

---

_Fichier créé pour faciliter la prise de décision — 2025-12-21_
