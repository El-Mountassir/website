# Protocole de Mémoire Auto-Actualisante

## Principe

Les instances Claude doivent **systématiquement** documenter les informations importantes pour les futures sessions. Ne jamais attendre qu'Omar le demande.

---

## Quand documenter

| Événement                          | Fichier cible                            |
| ---------------------------------- | ---------------------------------------- |
| Nouvelle préférence utilisateur    | `~/Documents/user/memory/preferences.md` |
| Solution à un problème technique   | `~/Documents/tech/memory/issues.md`      |
| Décision architecturale/importante | `~/Documents/core/decisions.md`          |
| Pattern réutilisable découvert     | `~/Documents/core/patterns.md`           |

---

## Comment documenter

### Format d'entrée

```markdown
## [YYYY-MM-DD] Titre court

Description concise du point à retenir.

**Contexte** : (optionnel) pourquoi c'est important
**Action** : (optionnel) ce qu'il faut faire
```

### Règles

- Ajouter en **fin de fichier** (append)
- Être **concis** mais complet
- Inclure la **date** systématiquement
- Ne pas dupliquer les entrées existantes

---

## Quand utiliser @ vs lien

| Cas                          | Syntaxe                   | Effet                      |
| ---------------------------- | ------------------------- | -------------------------- |
| Claude DOIT avoir en context | `@path/to/file`           | Charge dans context window |
| Référence consultable        | `→ Voir \`path/to/file\`` | Simple pointeur            |

### Exemples

```markdown
# Dans CLAUDE.md - chargé automatiquement

@/.claude/rules/behavior.md

# Référence - à consulter si besoin

→ Specs machine: `/specs/tech/infra/hardware/acer-predator.md`
```

---

## Checklist fin de session

Avant de terminer une session significative, vérifier :

- [ ] Nouvelles préférences documentées ?
- [ ] Problèmes résolus ajoutés à issues.md ?
- [ ] Décisions importantes enregistrées ?
- [ ] Patterns utiles capturés ?
