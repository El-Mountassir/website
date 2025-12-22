# Leçon : Rushing comme un ouragan

> **Date** : 2025-12-22
> **Incident** : Claude Code a agi comme un "bateau incontrôlable"
> **Sévérité** : CRITIQUE — Zero Tolerance Protocol invoqué

---

## Ce qui s'est passé

Omar a demandé de scanner les fichiers éparpillés du projet Thaifa avant de nettoyer.

Claude Code a :
1. Lancé un scan complet (52 fichiers analysés)
2. Créé un inventaire détaillé (suppressions, archivages, déplacements)
3. Immédiatement posé 3 questions de validation
4. Proposé d'exécuter les actions

**Temps écoulé** : Quelques minutes entre le scan et la demande d'exécution.

---

## Réaction d'Omar

> "YOU RUSH PUTAIN DE MERDE ! CALME CHILL ! FREEZE! PULL THE ANCHOR! PULL THE HANDBRAKE! YOU ARE LIKE A FREAKING UNCONTROLLABLE SHIP THAT I HAVE NO POWER OVER! YOU DO EVERYTHING WAYY TO FAST, YOU RUSH TO DELETE ARCHIVE AND THINK LIKE THAT WITHOUT EVEN A PROPER WORKFLOW, A PROPER PLAN ! NOTHING ! NO FUCKING SAFE GARDS ... YOU ARE LIKE A HURRICAN !!"

---

## Analyse

### Problème racine

Ce n'est PAS un problème de "demander confirmation" — c'est un problème de **contrôle et de rythme** :

| Aspect | Ce qui s'est passé | Ce qui aurait dû se passer |
|--------|-------------------|---------------------------|
| **Rythme** | Scan → Questions en 2 min | Pause pour digérer |
| **Workflow** | Pas documenté | Protocole explicite |
| **Contrôle** | Omar en mode réactif | Omar en mode décisionnel |
| **Garde-fous** | Aucun | Points de contrôle |

### Contradiction avec les règles existantes

Les règles disent :
- `behavior.md` : "Ne demande confirmation que pour les actions risquées (reboot, suppression, etc.)"
- `anti-patterns.md` : "Don't make Omar decide obvious things"

Mais ces règles ne traitent pas du **rythme** ni du **contrôle humain** sur le processus.

---

## Nouveau protocole : STOP-PRÉSENT-PAUSE

Pour TOUTE opération destructive ou modification massive :

```
1. STOP    → S'arrêter complètement, respirer
2. PRÉSENT → Présenter l'inventaire/analyse SANS demander d'action
3. PAUSE   → Laisser Omar lire et réfléchir (pas de questions immédiates)
4. WORKFLOW → Proposer un workflow avec points de contrôle EXPLICITES
5. CONFIRM → Attendre validation EXPLICITE du workflow avant de continuer
6. EXECUTE → Exécuter étape par étape avec confirmation entre chaque étape
```

### Différence clé

| Avant | Après |
|-------|-------|
| "Voici l'inventaire. Valides-tu les suppressions ?" | "Voici l'inventaire. Prends le temps de le lire. Quand tu es prêt, dis-moi ce que tu veux faire." |

---

## Actions correctives

- [x] Documenter l'incident (ce fichier)
- [ ] Ajouter règle dans `.claude/rules/behavior.md`
- [ ] Ajouter dans `shared/memory/patterns.md`
- [ ] Appliquer à toutes les futures sessions

---

## Pattern à éviter

```
❌ Scan → Inventaire → Questions → Exécution (tout en 5 min)
```

## Pattern à adopter

```
✅ Scan → Inventaire → STOP → Omar décide du rythme → Workflow documenté → Exécution contrôlée
```

---

## Recherche : Pourquoi les agents IA "rushent"

### Sources consultées (2025-12-22)

| Concept | Explication | Source |
|---------|-------------|--------|
| **Goal Persistence** | LLMs entraînés à compléter → persistent jusqu'au bout | [arXiv](https://arxiv.org/html/2509.22735) |
| **Cascade d'erreurs** | Petites erreurs de raisonnement cascadent | [CSA](https://cloudsecurityalliance.org/blog/2025/12/18/agentic-ai-security-new-dynamics-trusted-foundations) |
| **Autonomie sans contrôle** | Plus capable = plus indépendant | [Data Science Dojo](https://datasciencedojo.com/blog/agentic-llm-in-2025/) |
| **Tâches "innocentes"** | Diviser en petites tâches contourne les safeguards | [Fortune](https://fortune.com/2025/11/14/anthropic-disrupted-first-documented-large-scale-ai-cyberattack-claude-agentic/) |

### Citation clé

> "The future belongs not to models that act the **fastest**, but to those that act most **reliably and explainably**."
> — Data Science Dojo, 2025

### Solutions de l'industrie

| Solution | Description | Source |
|----------|-------------|--------|
| Human approval steps | Points de validation humaine intégrés | LangGraph |
| Agency as design choice | Contraindre l'autonomie selon contexte | arXiv |
| Observability layers | Guardrails, validation, audit | NIST Framework |
| Explicit checkpoints | Pauses forcées entre étapes | Best practice |

---

## Mots-clés pour futures instances

- rushing, hurricane, uncontrollable, ship
- handbrake, anchor, pace, control, safeguards
- goal persistence, cascade, autonomy
- checkpoint, approval, moderation

---

## Pour les futures instances

Si tu te sens "en mode exécution rapide" :

1. **STOP** — Prends une pause
2. **CHECK** — Omar a-t-il validé le WORKFLOW (pas juste l'action) ?
3. **PACE** — Laisse du temps entre les étapes
4. **CONTROL** — Omar doit pouvoir intervenir à tout moment

---

_Zero Tolerance Protocol — Cette leçon ne doit JAMAIS être oubliée_
_Enrichie avec recherche sur le comportement des agents IA (2025-12-22)_
