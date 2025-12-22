# Villa Thaifa — Instructions pour Agents IA

## Client

- **Nom** : Said Thaifa
- **Âge** : +60 ans
- **Établissement** : Villa Thaifa (maison d'hôtes, Marrakech)
- **Relation** : Nouveau client potentiel (high-ticket)

---

## Communication

### Ton

- **Vouvoiement** obligatoire
- **Respect** sans rigidité corporate
- Pas de : "Salut", "tu", abréviations familières

### WhatsApp

| Situation                    | Approche                             |
| ---------------------------- | ------------------------------------ |
| 1er message du jour          | Salutation + signature               |
| Messages suivants (même fil) | Direct, fluide, pas de re-salutation |
| Message important/formel     | Salutation + signature               |

### Pattern de communication

```
1. SCOUT    → Explorer, vérifier la faisabilité
2. RAPPORT  → Tenir le client informé des découvertes
3. QUESTIONS → Demander les infos manquantes (avec contexte)
4. ACTION   → Exécuter quand tout est clair
```

> Ne jamais demander des infos sans d'abord faire un rapport de ce qu'on a découvert.

---

## Admin

**Omar El Mountassir** est l'administrateur par défaut de ce dossier client.

---

## Utilisateurs

| Utilisateur            | Rôle                              | Notes                   |
| ---------------------- | --------------------------------- | ----------------------- |
| **Omar El Mountassir** | Admin, gestionnaire projet        | Décisions finales       |
| **Said Thaifa**        | Client, propriétaire Villa Thaifa | Vouvoiement obligatoire |

> Les deux peuvent être présents simultanément dans la conversation.

---

## Structure dossiers

| Dossier                    | Contenu                                                       |
| -------------------------- | ------------------------------------------------------------- |
| `admin/`                   | Credentials, contacts client                                  |
| `.claude/input/`           | **Zone de dépôt Omar → IA** (fichiers à traiter)              |
| `.claude/output/`          | **Outputs IA** organisés par `YYYY/QQ/type/topic/`            |
| `state/`                   | **États centralisés (SSOT)** — Voir section dédiée ci-dessous |
| `assets/`                  | Images, documents (global)                                    |
| `communication/`           | Échanges client (WhatsApp, email)                             |
| `communication/whatsapp/`  | Messages .txt prêts à copier                                  |
| `projects/`                | Missions actives (1 dossier par mission)                      |
| `projects/*/deliverables/` | Livrables finaux (PDF, etc.)                                  |
| `docs/`                    | Documentation générale, workflows                             |
| `tasks/TODOs.md`           | Tâches avec priorités (P0-P5)                                 |
| `archives/`                | Projets terminés                                              |

### Workflow Input/Output

```
1. Omar dépose un fichier dans `.claude/input/`
2. IA traite le fichier
3. IA déplace vers destination finale (deliverables/, archives/, etc.)
4. Le dossier input/ reste vide entre les traitements
```

### Output Structure

`.claude/output/YYYY/QQ/type/topic/`

| Niveau    | Exemple       | Description                                            |
| --------- | ------------- | ------------------------------------------------------ |
| Année     | `2025/`       | Année courante                                         |
| Trimestre | `Q4/`         | Q1 (Jan-Mar), Q2 (Apr-Jun), Q3 (Jul-Sep), Q4 (Oct-Dec) |
| Type      | `reports/`    | `reports/`, `drafts/`, `exports/`                      |
| Topic     | `resilience/` | Sujet en slug (lowercase, hyphens)                     |

**Exemple:** `.claude/output/2025/Q4/reports/error-resilience/final.md`

### Structure state/ (Single Source of Truth)

> **RÈGLE SSOT** : Toute information d'état existe UNIQUEMENT dans `state/`.
> Les rapports contiennent des liens vers `state/`, pas des copies des données.

```
state/
├── README.md                    # Index central de tous les états
│
├── current/                     # CE QUI EST maintenant
│   ├── README.md               # Vue d'ensemble états actuels
│   ├── promotions.md           # Promotions actives (5)
│   ├── reservations.md         # Réservations confirmées (11)
│   ├── rooms.md                # Chambres, pricing, mapping
│   └── blockers.md             # Dépendances actives
│
├── baseline/                    # CE QUI ÉTAIT (avant changements)
│   ├── README.md               # Index baseline
│   └── promotions-YYYY-MM-DD.md # Snapshots avant modifications
│
├── planned/                     # CE QUI SERA (objectifs)
│   ├── README.md               # Index planned
│   ├── assignments.md          # Propositions assignations
│   └── pricing.md              # Prix à configurer
│
├── execution/                   # CE QUI A ÉTÉ FAIT
│   ├── README.md               # Index exécutions
│   └── YYYY-MM-DD/             # Logs par date
│       ├── promotions.md       # Actions promotions
│       └── assignments.md      # Actions assignations
│
└── historical/                  # ÉVOLUTIONS/CORRECTIONS
    ├── README.md               # Index + timeline globale
    ├── decisions.md            # Leçons apprises, corrections
    ├── changelog-promotions.md # Historique changements promotions
    ├── changelog-reservations.md # Historique assignations
    └── snapshots/              # Snapshots avant changements majeurs
```

| Catégorie     | Question                         | Exemple                  |
| ------------- | -------------------------------- | ------------------------ |
| `current/`    | Quel est l'état **maintenant** ? | 5 promotions actives     |
| `baseline/`   | Quel était l'état **avant** ?    | 8 promotions avant audit |
| `planned/`    | Quel sera l'état **prévu** ?     | Assignations proposées   |
| `execution/`  | Qu'a-t-on **fait** ?             | 6 désactivations         |
| `historical/` | Comment a-t-on **évolué** ?      | Changelog, leçons        |

---

## Credentials

→ **LIRE `admin/credentials.md` AVANT d'accéder aux plateformes**

⚠️ **Ne jamais copier en clair ailleurs**

| Règle                 | Description                                         |
| --------------------- | --------------------------------------------------- |
| **Compte par défaut** | Utiliser **Admin Omar** (`omar@el-mountassir.com`)  |
| **Compte M. Thaifa**  | Ne PAS utiliser sauf demande explicite              |
| **Raison**            | Éviter de déranger le client avec des notifications |

---

## Leçons importantes

→ **Lire `docs/lessons-learned.md` AVANT toute action**

Résumé des erreurs passées :

- Communication sans rapport préalable
- Ton trop informel avec client senior
- Confusion années 2024/2025

---

## Workflow Tâches

> **Règle** : `tasks/TODOs.md` est la passerelle obligatoire pour TOUTE tâche.

### Pattern

1. **AVANT** d'agir → Lire `tasks/TODOs.md`
2. **NOUVELLE TÂCHE** → Ajouter dans TODOs.md d'abord
3. **EN COURS** → Marquer in_progress
4. **TERMINÉ** → Marquer completed + mettre à jour

### Pourquoi

- Traçabilité de tout le travail
- Continuité entre sessions
- Visibilité pour Omar

---

## Prochaines échéances

- **Lundi 22 décembre 2025, 10h** — RDV avec M. Thaifa

---

## Règles Clés (Session 2025-12-20)

| Règle          | Description                                                |
| -------------- | ---------------------------------------------------------- |
| **Resilience** | Ne jamais abandonner silencieusement. Fallback → Escalade. |
| **Anti-Dodge** | Installer/résoudre, pas contourner.                        |
| **Output**     | `.claude/output/YYYY/QQ/type/topic/`                       |
| **Patterns**   | Voir `~/Documents/claude/memory/patterns.md`               |

---

## Génération PDF Professionnels

### Template CSS

`docs/templates/report-style.css` — Style professionnel pour rapports client

### Commande de génération

```bash
# 1. Markdown → HTML (avec CSS embedded)
pandoc rapport.md -o /tmp/temp.html --standalone --self-contained --css=docs/templates/report-style.css

# 2. HTML → PDF
wkhtmltopdf --enable-local-file-access \
  --page-size A4 \
  --margin-top 12mm --margin-bottom 12mm \
  --margin-left 18mm --margin-right 18mm \
  --encoding UTF-8 \
  /tmp/temp.html output.pdf
```

### Structure rapport (Gold Standard)

```
1. EN-TÊTE (titre, date, "confidentiel")
2. ALERTE URGENTE (encadré rouge si applicable)
3. RÉSUMÉ EXÉCUTIF (KPIs clés, 30 sec de lecture)
4. SITUATION ACTUELLE (faits, tableaux)
5. PROPOSITIONS (encadré bleu "en attente de validation")
6. NOTES + FOOTER
```

### Distinction Faits vs Propositions

| Type                   | Visuel                                                |
| ---------------------- | ----------------------------------------------------- |
| Fait confirmé          | Tableau standard                                      |
| Proposition en attente | Encadré bleu + label "En attente de votre validation" |
| Alerte urgente         | Encadré rouge                                         |

---

## Références

- Mission en cours : `projects/2025-12_booking-hotelrunner/report.md`
- Types de chambres : voir rapport de mission
- Contacts : `admin/contacts.md`
- **Patterns globaux** : `~/Documents/claude/memory/patterns.md`
