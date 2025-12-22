# Architecture Clarification Questionnaire

**Date**: 2025-12-22
**From**: Claude Code
**To**: Omar El Mountassir
**Status**: ✅ COMPLETED — All answers validated, architecture implemented

---

## Context

Tu as exprimé que l'architecture actuelle est sub-optimale car:

- `.claude/` lock-in les données vers Claude Code uniquement
- `omar/` devrait contenir ce qui est spécifique à toi
- Il manque un espace `shared/` pour ce qui est commun à tous les agents

---

## Section A: Scope Boundaries (Closed Questions)

### Q1. Que doit contenir `omar/`?

- [ ] A. Uniquement profil/préférences personnelles d'Omar
- [x] B. Profil complet + contexte de travail + goals personnels - mais pas les interactions avec les agents
- [ ] C. Tout ce qui concerne Omar mais pas les agents
- [ ] D. Autre: \_\_\_

**Réponse validée**: **B**

---

### Q2. Que doit contenir `.claude/`?

- [ ] A. Configuration technique Claude Code uniquement (settings, hooks)
- [ ] B. Config + rules internes que seul Claude doit voir
- [x] C. Config + rules + skills + commands (tout ce qui est Claude-specific)
- [ ] D. Autre: \_\_\_

**Réponse validée**: **C**

---

### Q3. Que doit contenir `shared/`?

- [ ] A. Mémoire collective (decisions, patterns, learnings)
- [ ] B. Standards et conventions (pour tous les agents)
- [ ] C. Préférences de collaboration Omar ↔ Agents
- [x] D. Tout ce qui doit être accessible à TOUT agent (Claude, GPT, futurs)
- [ ] E. Combinaison (précise): \_\_\_

**Réponse validée**: **D** — Agent-agnostic shared resources

---

### Q4. Les `docs/standards/` actuels vont où?

- [ ] A. Restent dans `docs/standards/` (pas agent-specific)
- [x] B. Migrent vers `shared/standards/`
- [ ] C. Split: certains → shared/, certains → docs/

**Réponse validée**: **B** — ✅ Migration effectuée

---

## Section B: Memory Architecture (Closed Questions)

### Q5. Les fichiers mémoire (episodes, decisions, patterns) appartiennent à qui?

- [ ] A. Claude uniquement → `.claude/memory/`
- [ ] B. Tous les agents → `shared/memory/`
- [x] C. Split: Claude-specific memory + shared memory

**Réponse validée**: **C** — Split car certaines choses sont Claude-implementation-specific

---

### Q6. Les préférences d'Omar pour les interactions AI vont où?

- [ ] A. `omar/preferences/` (c'est personnel)
- [ ] B. `shared/preferences/` (tous les agents doivent les connaître)
- [x] C. `shared/user/preferences.md` (personnel mais partagé)

**Réponse validée**: **C** — Omar a préféré `user` au lieu d'`omar` pour future-proofing multi-utilisateur

---

## Section C: Access Patterns (Closed Questions)

### Q7. Comment les agents doivent-ils accéder aux données partagées?

- [ ] A. Lire `shared/` directement
- [ ] B. Chaque agent a un pointer file dans son dossier vers shared/
- [ ] C. Un INDEX.md central qui liste tout
- [x] D. Combinaison: INDEX.md central + pointers spécifiques

**Réponse validée**: **D** — Implémenté via `shared/INDEX.md`

---

### Q8. Qui peut ÉCRIRE dans `shared/`?

- [ ] A. Tous les agents librement
- [x] B. Écriture libre mais tracée: Tous les agents (humains et IA) mais avec logging
- [ ] C. Seul Omar + agents avec autorisation explicite
- [ ] D. Append-only (jamais supprimer/modifier, juste ajouter)

**Réponse validée**: **B** — Humains = carbon-based agents, tous font partie du système

---

## Section D: Open Questions

### Q9. Y a-t-il d'autres agents prévus bientôt?

```
[x] Oui, lesquels: Gemini CLI, Codex CLI, Claude Agent SDK, et d'autres
[ ] Non, mais je veux être ready
[ ] Non et pas prioritaire
```

**Réponse validée**: Oui — Architecture prête pour multi-agent

---

### Q10. Qu'est-ce qui doit ABSOLUMENT être dans le context window de Claude Code (via @)?

```
1. @CLAUDE.md — Contexte org + NORTH STAR
2. @shared/INDEX.md — Ressources disponibles
3. @shared/standards/confidence-system.md — Système de confiance
4. @shared/user/preferences.md — Préférences utilisateur
```

**Réponse validée**: ✅ Implémenté dans CLAUDE.md

---

### Q11. Quelle est notre vision commune pour la structure finale?

```
El-Mountassir/
├── shared/                    # ALL agents access
│   ├── INDEX.md              # Central discovery
│   ├── user/                 # Human context (future-proof)
│   │   └── preferences.md
│   ├── memory/               # Collective memory
│   │   ├── episodes.md
│   │   ├── decisions.md
│   │   ├── patterns.md
│   │   └── facts.md
│   └── standards/            # Migrated from docs/standards/
│       ├── INDEX.md
│       ├── confidence-system.md
│       ├── project-standards.md
│       └── management/
├── omar/                      # Human-specific (NOT for agents)
│   ├── context/
│   ├── model/
│   └── tools/
├── .claude/                   # Claude Code ONLY
│   ├── settings.json
│   ├── rules/
│   ├── skills/
│   ├── commands/
│   └── memory/               # Claude-implementation-specific
├── .gemini/                   # Future: Gemini CLI
├── .codex/                    # Future: Codex CLI
└── docs/                      # Project documentation (not standards)
    └── reference/
```

**Réponse validée**: ✅ Structure implémentée

---

## Section E: Confidence Expression Standard

### Q12. Le système de confidence nous convient?

| Niveau    | Terme              | Range  | Emoji |
| --------- | ------------------ | ------ | ----- |
| Very High | **Certitude**      | ≥95%   | ✅    |
| High      | **Recommandation** | 80-94% | 🟢    |
| Medium    | **Intuition**      | 60-79% | 🟡    |
| Low       | **Hypothèse**      | 40-59% | 🟠    |
| Very Low  | **Spéculation**    | <40%   | ⚠️    |

**Réponse validée**: ✅ 5 niveaux avec emojis — Implémenté dans `shared/standards/confidence-system.md`

---

## Implementation Status

| Action                                         | Status  |
| ---------------------------------------------- | ------- |
| Créer `shared/` structure                      | ✅ Done |
| Créer `shared/INDEX.md`                        | ✅ Done |
| Créer `shared/standards/confidence-system.md`  | ✅ Done |
| Créer `shared/user/preferences.md`             | ✅ Done |
| Créer `shared/memory/` files                   | ✅ Done |
| Migrer `docs/standards/` → `shared/standards/` | ✅ Done |
| Mettre à jour CLAUDE.md                        | ✅ Done |
| Mettre à jour références critiques             | ✅ Done |

---

## Patterns Captured During Session

1. **Migrate with Move, Not Copy** — `mv` plutôt que `cp` pour éviter duplication
2. **Triple-Check Before Deletion** — 3 vérifications avant tout `rm`/`rmdir`

Ces patterns sont documentés dans `shared/memory/patterns.md`.

---

_Questionnaire v1.0.0 — COMPLETED 2025-12-22_
