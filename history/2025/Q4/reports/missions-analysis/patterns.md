# Pattern Extraction

## Patterns Positifs (des missions archivées)

### Pattern 1: Un Problème = Une Mission

- **Observed In**: github-push, behavior-fix, restructuration-standards
- **Underlying Principle**: La clarté vient de la contrainte. Un scope serré permet une exécution nette.
- **Generalization Test**: Applicable partout? → **Oui**
- **Confidence**: High

**Exemple**:
```
github-push = Push vers GitHub
behavior-fix = Corriger comportement clôture
```

### Pattern 2: Objectifs Atomiques

- **Observed In**: Toutes les missions archivées
- **Underlying Principle**: Chaque objectif = UNE action vérifiable
- **Generalization Test**: Applicable aux missions créatives? → **Oui, mais granularité différente**
- **Confidence**: High

**Bon exemple**:
```
O1: Supprimer fichier X
O2: Créer fichier Y
O3: Mettre à jour fichier Z
```

**Mauvais exemple (M3)**:
```
O2: Documenter autres items déferred  ← QUELS items?
```

### Pattern 3: Evidence-Based Success Criteria

- **Observed In**: Missions archivées avec ✅ + preuve
- **Underlying Principle**: Un critère sans preuve = pas de critère
- **Generalization Test**: Oui
- **Confidence**: High

**Format gagnant**:
```markdown
| 1 | Main pushé | ✅ | Commit 204683f on github.com |
```

### Pattern 4: Dépendances Explicites et Actuelles

- **Observed In**: github-push blocks claude-web-sync
- **Underlying Principle**: Les dépendances stale créent de la confusion
- **Generalization Test**: Oui
- **Confidence**: High

---

## Anti-Patterns Identifiés

### Anti-Pattern 1: Scope Creep (Le Fourre-Tout)

- **Observed In**: M2 (claude-web-sync) O5
- **What Happened**: Objectif "harmoniser le repo" ajouté dans une mission de sync
- **Why It's Bad**: Transforme une mission de 1h en effort infini
- **Detection Signal**: Objectif contenant "harmoniser", "tout", "bordel", "nettoyer"
- **Fix**: Séparer en mission distincte ou supprimer

### Anti-Pattern 2: Mission Vide (Le Placeholder)

- **Observed In**: M3 (deferred-items)
- **What Happened**: Mission créée sans contenu concret
- **Why It's Bad**: Crée du bruit, ne peut pas être exécutée
- **Detection Signal**: Objectifs avec "autres", "documenter", sans liste
- **Fix**: Supprimer ou remplacer par mission concrète

### Anti-Pattern 3: Duplication d'Objectifs

- **Observed In**: M3 O1 = M2 O3
- **What Happened**: Même objectif (sauvegarder system prompt) dans 2 missions
- **Why It's Bad**: Confusion, double travail potentiel
- **Detection Signal**: Objectifs identiques entre missions
- **Fix**: Garder dans une seule mission, supprimer l'autre

### Anti-Pattern 4: Dépendance Stale

- **Observed In**: M4 `depends_on: [behavior-fix]`
- **What Happened**: M5 (behavior-fix) archivée, mais M4 y fait encore référence
- **Why It's Bad**: Confusion sur l'état des dépendances
- **Detection Signal**: Dépendance vers mission archivée
- **Fix**: Retirer la dépendance ou la remplacer

### Anti-Pattern 5: Mission Sans Priority

- **Observed In**: Missions drafts sans champ `priority`
- **What Happened**: Certaines missions n'ont pas de priorité définie
- **Why It's Bad**: Ordre d'exécution incertain
- **Detection Signal**: Champ `priority` absent ou vide
- **Fix**: Assigner priorité avant de mettre en queue

---

## Checklist de Validation Mission (Nouveau Pattern)

Avant de créer/valider une mission:

- [ ] **Scope**: Est-ce UN problème distinct?
- [ ] **Objectifs**: Chaque O est-il une action atomique?
- [ ] **No Vague**: Y a-t-il des "autres", "harmoniser", "nettoyer" sans précision?
- [ ] **No Duplicate**: Objectif unique (pas dans autre mission)?
- [ ] **Dépendances**: Toutes pointent vers missions existantes?
- [ ] **Priority**: Champ priority rempli?
- [ ] **INVEST**: Passe le test INVEST?

---

## Recommandations par Mission

| Mission | Anti-Patterns | Action |
|---------|---------------|--------|
| **M2** | #1 Scope Creep | Retirer O5 |
| **M3** | #2 Vide, #3 Duplicate | SUPPRIMER |
| **M4** | #4 Dépendance Stale | Retirer `depends_on` |
| **M7** | Aucun | READY |

---

_Patterns extracted | 2025-12-22_
