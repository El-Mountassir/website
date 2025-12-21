# /sync - Synchroniser les apprentissages de session vers CLAUDE.md

Permet à chaque instance Claude de documenter ses apprentissages dans CLAUDE.md pour les futures instances.

## Input

$ARGUMENTS

Si vide: Analyser la session actuelle et proposer des ajouts.

---

## Objectif

Enrichir `CLAUDE.md` avec:

1. Nouvelles règles découvertes
2. Workflows établis
3. Erreurs à éviter
4. Patterns réutilisables

---

## Process

### 1. Analyser la session

Identifier dans la conversation:

- [ ] Nouvelles règles/conventions établies?
- [ ] Erreurs commises et corrigées?
- [ ] Workflows créés?
- [ ] Décisions importantes?

### 2. Vérifier l'existant

Lire `CLAUDE.md` et vérifier:

- [ ] L'info existe déjà? → Ne pas dupliquer
- [ ] Contradiction avec l'existant? → Signaler à Omar
- [ ] Section appropriée existe? → Y ajouter

### 3. Catégoriser

| Type                         | Destination                             |
| ---------------------------- | --------------------------------------- |
| Règle globale (tous projets) | `~/Documents/claude/memory/patterns.md` |
| Règle projet (Villa Thaifa)  | `CLAUDE.md` section "Règles Clés"       |
| Workflow                     | `CLAUDE.md` ou `docs/workflows/`        |
| Erreur ponctuelle            | `docs/lessons-learned.md`               |

### 4. Mettre à jour

Ajouter au fichier approprié avec:

- Date (YYYY-MM-DD)
- Description concise
- Impact/raison

---

## Template d'ajout (CLAUDE.md)

```markdown
## Règles Clés (Session YYYY-MM-DD)

| Règle     | Description          |
| --------- | -------------------- |
| **[Nom]** | [Description courte] |
```

---

## Checklist avant commit

- [ ] Pas de duplication avec l'existant
- [ ] Scoping correct (global vs projet)
- [ ] Concis et actionable
- [ ] Date incluse

---

## Exemple d'usage

```
/sync "Ajout règle: toujours utiliser Chrome comme fallback quand WebFetch échoue"
```

Ou simplement:

```
/sync
```

→ L'agent analyse la session et propose des ajouts.
