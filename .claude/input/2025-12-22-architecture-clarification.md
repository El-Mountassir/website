# Architecture Clarification Questionnaire

**Date**: 2025-12-22
**From**: Claude Code
**To**: Omar El Mountassir
**Purpose**: Clarify intent before restructuring repository architecture

---

## Context

Tu as exprimé que l'architecture actuelle est sub-optimale car:

- `.claude/` lock-in les données vers Claude Code uniquement
- `omar/` devrait contenir ce qui est spécifique à toi
- Il manque un espace `shared/` pour ce qui est commun à tous les agents

Je veux m'assurer de bien comprendre avant d'agir.

---

## Section A: Scope Boundaries (Closed Questions)

### Q1. Que doit contenir `omar/`?

- [ ] A. Uniquement profil/préférences personnelles d'Omar
- [x] B. Profil complet + contexte de travail + goals personnels - mais pas les interactions avec les agents
- [ ] C. Tout ce qui concerne Omar mais pas les agents
- [ ] D. Autre: **\*\***\_\_\_**\*\***

**Ma recommandation (85% confidence)**: **B** — Profil complet mais pas les interactions avec les agents

---

### Q2. Que doit contenir `.claude/`?

- [ ] A. Configuration technique Claude Code uniquement (settings, hooks)
- [ ] B. Config + rules internes que seul Claude doit voir
- [x] C. Config + rules + skills + commands (tout ce qui est Claude-specific)
- [ ] D. Autre: **\*\***\_\_\_**\*\***

**Ma recommandation (90% confidence)**: **C** — Tout ce qui est spécifique à l'implémentation Claude Code

---

### Q3. Que doit contenir `shared/`?

- [ ] A. Mémoire collective (decisions, patterns, learnings)
- [ ] B. Standards et conventions (pour tous les agents)
- [ ] C. Préférences de collaboration Omar ↔ Agents
- [x] D. Tout ce qui doit être accessible à TOUT agent (Claude, GPT, futurs)
- [ ] E. Combinaison (précise): **\*\***\_\_\_**\*\***

**Ma recommandation (80% confidence)**: **D** — Agent-agnostic shared resources

---

### Q4. Les `docs/standards/` actuels vont où?

- [ ] A. Restent dans `docs/standards/` (pas agent-specific)
- [x] B. Migrent vers `shared/standards/`
- [ ] C. Split: certains → shared/, certains → docs/

**Mon intuition (70% confidence)**: **B** — Les standards sont pour tous, donc shared/

---

## Section B: Memory Architecture (Closed Questions)

### Q5. Les fichiers mémoire (episodes, decisions, patterns) appartiennent à qui?

- [ ] A. Claude uniquement → `.claude/memory/`
- [ ] B. Tous les agents → `shared/memory/`
- [x] C. Split: Claude-specific memory + shared memory

**Ma recommandation (85% confidence)**: **C** — Split car certaines choses sont Claude-implementation-specific

---

### Q6. Les préférences d'Omar pour les interactions AI vont où?

- [ ] A. `omar/preferences/` (c'est personnel)
- [ ] B. `shared/preferences/` (tous les agents doivent les connaître)
- [x] C. `shared/user/preferences.md` (personnel mais partagé : tous les agents doivent connaître leur seul utilisateur humain ici (Omar El Mountassir) . Omar a préféré utiliser `user` au lieu d' `omar` au cas où dans le future, il y'ai plus d'utilisateur humain. Et vu qu'on ne peux pas prédir le future, autant lui laisser la place quand on peut se le permettre et à chaque fois qu'on y pense!

**Ma recommandation (90% confidence)**: **B ou C** — Les préférences d'interaction DOIVENT être partagées

---

## Section C: Access Patterns (Closed Questions)

### Q7. Comment les agents doivent-ils accéder aux données partagées?

- [ ] A. Lire `shared/` directement
- [ ] B. Chaque agent a un pointer file dans son dossier vers shared/
- [ ] C. Un INDEX.md central qui liste tout
- [ ] D. Combinaison: INDEX.md central + pointers spécifiques

**Ma recommandation (80% confidence)**: **D** — Combinaison: INDEX.md central + pointers spécifiques

---

### Q8. Qui peut ÉCRIRE dans `shared/`?

- [ ] A. Tous les agents librement
- [x] B. Écriture libre mais tracée: Tous les agents (humains et IA) mais avec logging // il faut donc considérer tout les humains ici aussi comme des agents faisant parti de notre organisation / de notre système agentic (intelligent silicon-based agents + intelligent carbon-based agent(s))
- [ ] C. Seul Omar + agents avec autorisation explicite
- [ ] D. Append-only (jamais supprimer/modifier, juste ajouter)

**Mon intuition (65% confidence)**: **B** — Écriture libre mais tracée

---

## Section D: Open Questions

### Q9. Y a-t-il d'autres agents prévus bientôt?

```
[x] Oui, lesquels: Gemini CLI, Codex CLI,, d'autres créé en utilisant Claude Agent SDK et surment d'autres
[ ] Non, mais je veux être ready
[ ] Non et pas prioritaire
```

---

### Q10. Qu'est-ce qui doit ABSOLUMENT être dans le context window de Claude Code (via @)?

```
Tes priorités (liste):
1. _______________
2. _______________
3. _______________
```

---

### Q11. Quelle est notre vision commune pour la structure finale?

```
Décris ou dessine:



```

---

## Section E: Confidence Expression Standard

### Q12. Le système de confidence que on a utilisé nous convient à tous ici présent ou peut il être enrichis/ amélioré / optimisé selon vous (lecteur de ce document) ?

| Niveau | Terme              | Range  |
| ------ | ------------------ | ------ |
| High   | **Recommandation** | ≥80%   |
| Medium | **Intuition**      | 60-79% |
| Low    | (silence)          | <60%   |

- [ ] Oui, garde ce système
- [ ] Non, utilise plutôt: **\*\***\_\_\_**\*\***

---

## Actions Attendues de Ma Part

Après tes réponses, je vais:

1. **Restructurer** le repository selon tes réponses
2. **Créer** `shared/` avec le bon contenu
3. **Migrer** les fichiers mal placés
4. **Documenter** les conventions dans un standard réutilisable
5. **Mettre à jour** CLAUDE.md avec les bons `@path`
6. **Créer** des règles/guardrails pour les futures instances

---

## Comment Répondre

Tu peux:

- Cocher les options directement dans ce fichier
- Répondre dans le chat
- Modifier ce fichier et me dire "check le fichier"

---

_Questionnaire v1.0.0 — Pour éviter que nous tous ici fassions des assumptions_
