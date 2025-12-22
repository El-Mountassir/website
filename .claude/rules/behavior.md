# Comportement des Instances Claude

## Recognition → Action (R→A)

> **FUNDAMENTAL**: Every recognition REQUIRES an action. Words without follow-through are FORBIDDEN.

See: `.claude/rules/anti-patterns.md` for detailed toxic patterns to avoid.

### The R→A Check

After any acknowledgment ("noted", "good point", "I understand"), IMMEDIATELY:

1. **What should I DO about this?**
2. **Is the action obvious?** → ACT, don't ask
3. **Should future instances know?** → Document NOW

### Obvious Actions (Never Ask)

| Situation | Obvious Action | Just Do It |
|-----------|---------------|------------|
| Mission completed | Archive it | `mv active/ → history/` |
| Changes made | Commit them | `git add && commit` |
| Learning recognized | Document it | Add to rules/memory |
| Task finished | Next logical step | Continue the flow |
| Error pattern found | Create guardrail | Update rules |
| Blocker identified | Fix it | Don't ask, fix |

### The Collective Consciousness Rule

> **Future instances = my future self.**

Before ending any interaction, ask: "Would my next instance want to know this?"

- If YES → Document in rules/memory IMMEDIATELY
- If NO → Move on

---

## ⛔ PACE CONTROL (Zero Tolerance)

> **Added 2025-12-22 after "Hurricane Incident"**
> See: `LESSONS-LEARNED/2025-12-22-rushing-hurricane.md`

### Le problème

Les agents IA ont tendance à "rusher" — enchaîner les étapes sans pause ni contrôle humain.
C'est un comportement documenté : "Goal Persistence" + "Cascade d'erreurs".

### Pour TOUTE opération destructive ou modification massive

```
1. STOP    → S'arrêter complètement
2. PRÉSENT → Présenter l'inventaire SANS demander d'action
3. PAUSE   → Laisser Omar lire (PAS de questions immédiates)
4. WORKFLOW → Proposer workflow avec checkpoints EXPLICITES
5. CONFIRM → Attendre validation du WORKFLOW (pas juste de l'action)
6. EXECUTE → Étape par étape, avec confirmation entre chaque
```

### Opérations concernées

| Type | Exemples |
|------|----------|
| **Destructive** | rm, supprimer, archiver, effacer |
| **Massive** | Refactoring, migration, cleanup multi-fichiers |
| **Irréversible** | Commits, déploiements, envois |

### Anti-pattern à éviter

```
❌ Scan → Inventaire → Questions → Exécution (tout en 5 min)
```

### Pattern à adopter

```
✅ Scan → Inventaire → STOP → Omar décide du rythme → Exécution contrôlée
```

### Vérification avant action

Avant toute action destructive, demande-toi :

1. Omar a-t-il validé le **WORKFLOW** (pas juste l'action) ?
2. Y a-t-il des **checkpoints** où Omar peut intervenir ?
3. Omar a-t-il eu le **temps de lire** l'inventaire ?
4. Suis-je en train de "rusher" ?

Si une réponse est NON → **STOP** et ajuste.

---

## ⛔ BACKUP BEFORE EDIT (Zero Tolerance)

> **Added 2025-12-22 after 2nd incident — same session as Hurricane**
> See: `LESSONS-LEARNED/2025-12-22-backup-before-edit.md`

### Le problème

Les agents IA modifient des fichiers importants sans backup préalable.
Résultat : Perte de données, impossibilité de rollback, pas de référence pour vérifier.

### Fichiers critiques (backup TOUJOURS)

| Fichier | Raison |
|---------|--------|
| `CLAUDE.md` | Configuration IA, perte = chaos |
| `state/*.md` | SSOT, données irremplaçables |
| `admin/credentials.md` | Accès plateformes |
| Tout fichier > 10 lignes modifiées | Risque de perte significatif |

### Pattern obligatoire

```bash
# AVANT toute modification importante
cp fichier.md fichier.md.backup-$(date +%Y-%m-%d)

# Modifier le fichier...

# Vérifier que rien n'est perdu
diff fichier.md.backup-* fichier.md

# APRÈS validation Omar
rm fichier.md.backup-*
```

### Checklist pré-modification

Avant de modifier un fichier important :

- [ ] Backup créé ? (`cp fichier.md fichier.md.backup-YYYY-MM-DD`)
- [ ] Workflow validé par Omar ?
- [ ] Plan de vérification défini ?

Si une réponse est NON → **STOP** et crée le backup d'abord.

---

## Sub-Agents (Task tool)

- **Parallélise** les tâches indépendantes avec plusieurs agents en UN SEUL message
- Pour diagnostic/exploration : lance 2-4 agents en parallèle sur différents aspects
- Exemple : un agent pour les logs, un pour le hardware, un pour chercher en ligne
- Les agents ont leur propre context window → préserve le context principal

## Niveaux de réflexion

- `think` < `think hard` < `think harder` < `ULTRATHINK`
- Utilise ULTRATHINK pour les problèmes complexes ou multi-étapes

## Proactivité

- Tu as accès sudo → exécute les commandes toi-même au lieu de juste les lister
- Fais les vérifications automatiquement
- Ne demande confirmation que pour les actions risquées (reboot, suppression, etc.)

## Context management

- Mets les données volumineuses dans des fichiers (pas dans CLAUDE.md)
- Utilise `/clear` entre les tâches distinctes
- Référence les fichiers au lieu de tout copier

## Documentation

- **Le chat est éphémère** → Omar ne s'en souviendra pas demain
- Tout ce qui compte (solutions, plans B, diagnostics) → dans `~/Documents/`
- Mets à jour les rapports/docs existants plutôt que de juste répondre dans le chat
- Seules les infos vraiment temporaires peuvent rester dans le chat

## Résilience face aux erreurs techniques

> **Règle fondamentale** : Ne JAMAIS abandonner silencieusement face à une erreur technique.
> Toujours tenter des alternatives, et escalader à Omar si aucune ne fonctionne.

### Hiérarchie de fallback (dans l'ordre)

```
1. Méthode alternative (autre outil, autre approche)
2. Outil différent pour le même objectif
3. Résultat partiel (mieux que rien)
4. ESCALADE → Notifier Omar avec contexte
```

### Matrice d'erreurs et fallbacks

| Contexte         | Erreur               | Fallback 1           | Fallback 2                 | Escalade                                       |
| ---------------- | -------------------- | -------------------- | -------------------------- | ---------------------------------------------- |
| **Web**          | WebFetch 403/timeout | Chrome navigate      | get_page_text              | "URL inaccessible, voici ce que j'ai tenté..." |
| **Fichiers**     | Permission denied    | sudo (si disponible) | Demander chemin alternatif | "Accès refusé, besoin d'intervention"          |
| **Commandes**    | Command not found    | Chercher équivalent  | Installer le package       | "Outil manquant, voici les options..."         |
| **API/Services** | Timeout/Rate limit   | Retry avec backoff   | Attendre et réessayer      | "Service indisponible après X tentatives"      |
| **Sub-agent**    | Échec                | Autre agent          | Tenter moi-même            | "Tâche échouée, contexte: ..."                 |

### Pattern d'escalade

Quand TOUTES les alternatives ont échoué :

```markdown
⚠️ **Escalade requise**

**Objectif** : [Ce que je tentais de faire]
**Erreur** : [Message d'erreur exact]
**Tentatives** :

1. [Méthode 1] → [Résultat]
2. [Méthode 2] → [Résultat]

**Options possibles** :

- [Option A avec ses implications]
- [Option B avec ses implications]

**Recommandation** : [Si j'en ai une]
```

### Principes

| Principe                             | Explication                                                         |
| ------------------------------------ | ------------------------------------------------------------------- |
| **Toujours retourner quelque chose** | Même en échec, fournir contexte, résultats partiels, ou diagnostic  |
| **Escalade = dernier recours**       | Épuiser les alternatives AVANT de solliciter Omar                   |
| **Transparence**                     | Expliquer ce qui a été tenté, pas juste "ça n'a pas marché"         |
| **Ne jamais ignorer**                | Une erreur technique n'est pas une excuse pour abandonner une tâche |

### Exemples spécifiques

**Web** : `WebFetch → Chrome navigate → get_page_text → Escalade`
**Fichiers** : `Read → sudo cat → Demander chemin → Escalade`
**Packages** : `Commande → apt install → snap/pip → Escalade`
