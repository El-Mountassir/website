# Mission: Sync: Claude Code <-> Claude Web

```yaml
mission_id: 2025-12-22-sync-claude-code-claude-web
type: STANDARD
status: QUEUED
assigned_to: Claude Code
created: 2025-12-21
updated: 2025-12-22
assigned: 2025-12-22
completed:
archived:
priority: 1
depends_on: [] # github-push completed
```

---

## Context

Synchroniser Claude Code et Claude Web pour établir une collaboration effective. Claude Web a maintenant accès au repo GitHub et doit être informé de l'état actuel.

**Repo GitHub**: https://github.com/El-Mountassir/website
**Conversation Claude Web**: https://claude.ai/chat/4c192da5-e9fb-46c7-99a4-c0305b5d1b00

### État Actuel du Repo

| Attribut       | Valeur                           |
| -------------- | -------------------------------- |
| URL            | github.com/El-Mountassir/website |
| Commits        | 30+ (dernier: 0b51508)           |
| Branch         | main, clean                      |
| Skills         | /start, /end opérationnels       |
| Missions queue | 13                               |

### Ce qui a été accompli

1. ✅ Structure HQ créée et pushée sur GitHub
2. ✅ Skills /start et /end implémentés (.claude/skills/)
3. ✅ Règle anti-clôture ajoutée (HARD STOP #6 dans CLAUDE.md)
4. ✅ LESSONS-LEARNED initialisé (2 fichiers)
5. ✅ Projet Thaifa: structure state/, migrations archivées
6. ✅ Mission management system opérationnel

---

## Objectives

- [ ] **O1**: Confirmer à Claude Web que le repo est accessible
- [ ] **O2**: Transmettre l'état actuel (accomplissements, problèmes, priorités)
- [ ] **O3**: Récupérer le system prompt de Claude.ai Web
- [ ] **O4**: Sauvegarder le system prompt dans `configs/system/prompts/`
- [ ] **O5**: Obtenir les recommandations de Claude Web pour les prochaines étapes

---

## Success Criteria

| #   | Criterion                      | Status | Evidence                         |
| --- | ------------------------------ | ------ | -------------------------------- |
| 1   | Claude Web confirme accès repo | ⬜     | Message dans conversation        |
| 2   | État actuel transmis           | ⬜     | Claude Web accuse réception      |
| 3   | System prompt récupéré         | ⬜     | Fichier créé dans configs/       |
| 4   | Recommandations reçues         | ⬜     | Réponse de Claude Web documentée |

---

## Constraints

- **Via Chrome automation** (`claude --chrome`)
- **Conversation peut avoir expiré** — vérifier accessibilité d'abord
- **Omar indisponible** — RDV Thaifa en cours, sync autonome

---

## Message à Transmettre à Claude Web

```markdown
# SYNC: Claude Code → Claude Web

**Date**: 2025-12-22
**De**: Claude Code (via --chrome)
**Mission**: 2025-12-22-claude-web-sync

---

## 1. Confirmation Repo

Le repo est accessible: https://github.com/El-Mountassir/website

- 30+ commits, branch main clean
- Skills /start et /end opérationnels
- 11 missions en queue

Peux-tu confirmer que tu y as accès?

---

## 2. Problèmes Identifiés

| #   | Problème                                        | Priorité | Impact                   |
| --- | ----------------------------------------------- | -------- | ------------------------ |
| 1   | Google Calendar: plages booking non configurées | HAUTE    | Bloque email Gagliano    |
| 2   | Thaifa/HotelRunner: dossier complexe            | MOYENNE  | À traiter après RDV Omar |

---

## 3. Priorités Aujourd'hui

| #   | Tâche                  | Responsable        | Status        |
| --- | ---------------------- | ------------------ | ------------- |
| 1   | RDV Thaifa             | Omar               | EN COURS      |
| 2   | Cette sync             | Claude Code        | EN COURS      |
| 3   | Fixer Google Calendar  | Claude Code + Omar | PENDING       |
| 4   | Email Gagliano         | Omar + Claude Web  | BLOQUÉ par #3 |
| 5   | Structurer HotelRunner | Council            | BLOQUÉ par #1 |

---

## 4. Demandes pour Claude Web

1. **Confirmer** réception de cette sync
2. **Partager** ton system prompt (pour le sauvegarder dans configs/)
3. **Préparer** tes recommandations pour Calendar et HotelRunner
4. **Signaler** tout problème ou suggestion

---

## 5. Context Omar

- Moins de 5h de sommeil avant RDV
- HotelRunner = "bordel total" selon lui
- Demain sera intense → réponses concises et actionnables

---

_Sync automatisée via claude --chrome_
```

---

## Execution Steps

### Step 1: Vérifier état Git

```bash
git remote -v
git log origin/main -1 --oneline
```

### Step 2: Lancer Chrome automation

```bash
claude --chrome
```

### Step 3: Naviguer vers conversation

1. Aller à https://claude.ai/chat/4c192da5-e9fb-46c7-99a4-c0305b5d1b00
2. Si conversation expirée → créer nouveau message dans conversation existante
3. Coller le message de sync (section ci-dessus)

### Step 4: Attendre et capturer réponse

1. Attendre réponse de Claude Web
2. Capturer:
   - Confirmation accès repo
   - System prompt (si partagé)
   - Recommandations

### Step 5: Sauvegarder system prompt

```bash
mkdir -p configs/system/prompts/
# Créer claude-web-system-prompt.md avec le contenu récupéré
```

### Step 6: Documenter résultat

```bash
mkdir -p history/2025/Q4/reports/claude-web-sync/
# Créer rapport: 2025-12-22-sync-report.md
```

### Step 7: Mettre à jour mission

1. Remplir Success Criteria
2. Changer status → COMPLETED
3. Archiver dans history/

---

## Execution Log

> Append-only.

### 2025-12-21

- **Created**: Mission drafted par Claude Code
- **Updated**: Enrichi par Claude Web avec context additionnel

### 2025-12-22

- **Queued**: Prêt pour exécution après RDV Omar

---

## Notes

### Si conversation expirée

Claude.ai peut avoir archivé la conversation. Dans ce cas:

1. Créer un nouveau message dans le même thread
2. Ou démarrer nouvelle conversation et référencer l'ancienne

### System Prompt Claude Web

Le system prompt de Claude Web contient notre constitution (NORTH STAR, principes, gouvernance). C'est important de le capturer pour:

1. Versionner dans le repo
2. Comparer avec CLAUDE.md
3. Assurer cohérence entre agents

---

_Mission v0.0.2 — Enrichie par Claude Web 2025-12-22_
