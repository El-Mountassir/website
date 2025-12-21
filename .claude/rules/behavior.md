# Comportement des Instances Claude

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
