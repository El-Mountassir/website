# Pending Items

> **Items needing Omar's attention.**
> AI Agents add items here. Human Agent Omar processes them.

**Last checked**: —

---

## [2025-12-23] Linear MCP Server Not Enabled

**Priority**: 🟢 Low
**Type**: FYI
**From**: Claude Code

Linear OAuth is configured but the MCP server is not currently running (not in active server list).

**Current state**:

- OAuth: ✅ Authorized
- MCP Server: 🟡 Available but not enabled
- Active servers: memory, notion, sequentialthinking

**To enable**: Run `docker mcp server enable linear` when needed.

**Impact**: No impact if using Linear via web UI. Only matters if wanting to use Linear tools via MCP.

---

## ✅ [2025-12-23] Gagliano Brothers Email Response — DONE

**Status**: ✅ Completed
**From**: Claude Code

Email sent 2025-12-23 at 2:50 AM with booking links.

**Booking links shared**:

- 30-min: https://calendar.app.google/i1Q4t8G8Zg328caE8
- 60-min: https://calendar.app.google/B9jKSicLyqcD8zkw5

**Thread saved**: `projects/gagliano/communication/2025-12-cash-depot-demo-thread.md`

---

## 🔴 [2025-12-23] Transfer Gagliano Project Folder — URGENT

**Priority**: 🔴 High
**Type**: Action Required (Omar) — BLOCKER
**From**: Claude Code

The main Gagliano project folder exists elsewhere on Omar's computer. Need to transfer/merge it with `projects/gagliano/` in El-Mountassir repo.

**Why URGENT**: Blocks full context for payment/invoicing discussion. This client = 50 sites potential (~$15k).

**Current state**:

- `projects/gagliano/` exists in repo with CLAUDE.md + communication/
- Full project folder is elsewhere on Omar's system

**Action needed**: Omar to transfer/merge the external Gagliano folder BEFORE 25 Dec discussion

---

## 🔴 [2025-12-25] Gagliano — Débloquer Premier Paiement (CLIENT STRATÉGIQUE)

**Priority**: 🔴 High — CRITICAL
**Type**: Discussion + Action Required
**From**: Claude Code (via Omar 2025-12-23 3:23 AM)
**When**: 25 décembre matin

### 💰 Enjeu Stratégique

| Facteur             | Valeur                                        |
| ------------------- | --------------------------------------------- |
| **Potentiel total** | 50 sites web                                  |
| **Revenue estimé**  | ~$15,000                                      |
| **Impact**          | Portfolio massif + cash flow + preuve sociale |
| **Risque**          | Friction paiement = peut bloquer le deal      |

> **Ce n'est pas de la paperasse — c'est débloquer un client stratégique.**

### À préparer AVANT la réunion

| Sujet                | Détails                                             | Status |
| -------------------- | --------------------------------------------------- | ------ |
| **Facturation**      | Préparer la facture pour Cash Depot                 | ⬜     |
| **Compte bancaire**  | Choisir : compte marocain (Omar) ou espagnol (père) | ⬜     |
| **Montant**          | Recevoir 50% upfront                                | ⬜     |
| **Mode de paiement** | Ils préfèrent carte — Omar a des contraintes        | ⬜     |
| **Square Payments**  | Rechercher si compatible auto-entrepreneur Maroc    | ⬜     |

### Questions à résoudre

1. **Square Payments** : Fonctionne pour auto-entrepreneur au Maroc ?
2. **Alternatives** : Stripe, PayPal, Wise, virement direct ?
3. **Contraintes carte** : Quelles sont-elles exactement ?

### Contexte manquant

Omar expliquera détails après transfert du dossier Gagliano.

**Dépendance CRITIQUE**: Transfert du dossier Gagliano (voir item précédent)

---

## 🟡 [2025-12-24] Système d'Apprentissage IndyDevDan — COMPLET

**Priority**: 🟡 Medium
**Type**: Discussion + Préparation
**From**: Claude Code (via Omar 2025-12-23 3:30 AM)
**When**: Demain (24 décembre)

### 🎯 Objectif

Capturer et intégrer TOUT le contenu d'IndyDevDan (TAC, Agentic Coding 2.0, etc.)

### 📦 Contenu à Capturer

| Format             | Source             | Défi                                          |
| ------------------ | ------------------ | --------------------------------------------- |
| **Vidéos YouTube** | Chaîne IndyDevDan  | Multimodal — besoin de transcription + visuel |
| **Lootbox**        | Ressources premium | Formats variés                                |

### 🔧 Stack Recommandée

> Ref: `shared/drafts/2026-tech-stack.md` — Model Selection Matrix

| Besoin            | Modèle               | Pourquoi                                  |
| ----------------- | -------------------- | ----------------------------------------- |
| **Vidéos**        | Gemini 3 Flash       | Multimodal (video, audio, PDF), 200 tok/s |
| **Deep analysis** | Gemini 3 Pro         | Deep Think, 1M context                    |
| **Intégration**   | Claude (Sonnet/Opus) | Notre fondation, cohérence                |

---

### 🧠 FRAMEWORK COMPLET (Recherche 2024-2025)

> Sources: [Forte Labs PKM](https://fortelabs.com/blog/the-4-levels-of-personal-knowledge-management/), [Enterprise Knowledge](https://enterprise-knowledge.com/extending-taxonomies-to-ontologies/), [Retrieval Practice](https://pdf.retrievalpractice.org/SpacingGuide.pdf)

#### 1️⃣ CAPTURE — Comment collecter

| Composant                 | Description                                     | Status |
| ------------------------- | ----------------------------------------------- | ------ |
| **Mécanismes de capture** | Comment on collecte (clips, notes, screenshots) | ⬜     |
| **Sources multiples**     | Vidéos, PDFs, transcripts, code snippets        | ⬜     |
| **Capture in-flow**       | Intégré au travail quotidien, pas séparé        | ⬜     |

#### 2️⃣ ORGANIZE — Comment structurer

| Composant           | Description                                      | Status |
| ------------------- | ------------------------------------------------ | ------ |
| **Taxonomie**       | Hiérarchie de concepts (TAC > Skills > Specific) | ⬜     |
| **Ontologie**       | Relations entre concepts (X "enables" Y)         | ⬜     |
| **Tagging system**  | Vocabulaire contrôlé pour indexation             | ⬜     |
| **Metadata schema** | Champs standards (source, date, confidence)      | ⬜     |
| **Linking**         | Connexions entre notes (bidirectional)           | ⬜     |

#### 3️⃣ DISTILL — Comment raffiner

| Composant                     | Description                             | Status |
| ----------------------------- | --------------------------------------- | ------ |
| **Progressive summarization** | Résumé → Key points → Essence           | ⬜     |
| **Extraction patterns**       | Quoi extraire de chaque type de contenu | ⬜     |
| **Quality criteria**          | Quand une note est "complète"           | ⬜     |
| **Templates**                 | Format standardisé par type de contenu  | ⬜     |

#### 4️⃣ EXPRESS — Comment appliquer

| Composant              | Description                                           | Status |
| ---------------------- | ----------------------------------------------------- | ------ |
| **Integration points** | Où les learnings s'intègrent (CLAUDE.md, rules, etc.) | ⬜     |
| **Action triggers**    | Quand un learning devient une règle/pattern           | ⬜     |
| **Retrieval practice** | Mécanisme pour revoir et renforcer                    | ⬜     |
| **Spaced repetition**  | Révision à intervalles croissants                     | ⬜     |

---

### 📋 QUALITY GATES

| Gate                          | Description                              | Status |
| ----------------------------- | ---------------------------------------- | ------ |
| **DoR (Definition of Ready)** | Quand une ressource est prête à capturer | ⬜     |
| **DoD (Definition of Done)**  | Quand une ressource est "capturée"       | ⬜     |
| **Integration criteria**      | Quand un learning est intégré au système | ⬜     |

---

### 🔄 RETENTION & RETRIEVAL

> Source: [Spaced Repetition Research](https://maestrolearning.com/blogs/how-to-use-spaced-repetition/)

| Mécanisme              | Description                             | Status     |
| ---------------------- | --------------------------------------- | ---------- |
| **Active recall**      | Tester la mémoire, pas juste relire     | ⬜         |
| **Spaced intervals**   | Revoir à J+1, J+3, J+7, J+14...         | ⬜         |
| **Confidence ratings** | Marquer ce qu'on maîtrise vs pas encore | ⬜         |
| **Anki/Flashcards**    | Outils de spaced repetition             | ⬜ Évaluer |

---

### 🗂️ KNOWLEDGE ORGANIZATION

> Sources: [Taxonomy & Ontology 2025](https://enterprise-knowledge.com/services/taxonomy-ontology/), [KM Trends 2025](https://enterprise-knowledge.com/top-knowledge-management-trends-2025/), [TOMs for GenAI](https://squirro.com/squirro-blog/genai-taxonomy-ontology)

| Niveau                    | Description              | Example                              |
| ------------------------- | ------------------------ | ------------------------------------ |
| **Controlled vocabulary** | Termes standardisés      | "Sub-agent" pas "sous-agent"         |
| **Taxonomy**              | Hiérarchie parent-enfant | Agentic > Orchestration > Lead Agent |
| **Ontology**              | Relations sémantiques    | "Lead Agent" SPAWNS "Sub-agents"     |
| **Knowledge graph**       | Réseau interconnecté     | MCP memory graph                     |

#### 🆕 Insights 2025

| Trend                                             | Impact pour nous                                             |
| ------------------------------------------------- | ------------------------------------------------------------ |
| **AI + Taxonomy**                                 | Tagging cohérent = meilleure performance AI                  |
| **TOMs (Taxonomy & Ontology Management Systems)** | Système pour classifier/gouverner les données                |
| **Learning recommendation**                       | Ontologie peut suggérer quoi apprendre ensuite               |
| **Grounded LLM responses**                        | Données tagguées = réponses ancrées dans des règles logiques |

---

### 📍 OUTPUT LOCATIONS

| Type de learning               | Destination                      |
| ------------------------------ | -------------------------------- |
| **Patterns réutilisables**     | `shared/memory/patterns.md`      |
| **Faits persistants**          | `shared/memory/facts.md`         |
| **Décisions avec reasoning**   | `shared/memory/decisions.md`     |
| **Règles comportementales**    | `.claude/rules/*.md`             |
| **Contenu brut (archive)**     | `learning/tac/`, `learning/pac/` |
| **Philosophie opérationnelle** | `shared/philosophy/`             |

---

### 💡 Questions à Discuter

1. **Priorité des vidéos** : Par quoi commencer ?
2. **Niveau de détail** : Progressive summarization levels ?
3. **Taxonomie** : Quelles catégories principales ?
4. **Retention** : Anki ? Autre système ?
5. **Gemini CLI** : À installer/configurer pour le multimodal ?
6. **Knowledge graph** : Utiliser MCP memory pour les relations ?

---

### 🎓 Contenu Attendu

| Topic                  | Source                  | Impact                 |
| ---------------------- | ----------------------- | ---------------------- |
| **TAC**                | Tactical Agentic Coding | Pratiques quotidiennes |
| **PAC**                | Principled AI Coding    | Philosophie            |
| **Agentic Coding 2.0** | Lead Agent model        | Orchestration          |
| **ZTE**                | Zero Touch Engineering  | Out-loop automation    |

> **Omar's note**: "Je pense que tu vas aimer !" 🎉

---

<!-- Add new items above this line -->
