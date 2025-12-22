# Leçons Apprises — Villa Thaifa

> Ce fichier documente les erreurs et apprentissages pour éviter de les répéter.
> À consulter par les futurs agents IA et humains travaillant sur ce dossier.

---

## [2025-12-19] Communication Client : Pattern Scout → Rapport → Action

### L'erreur

Envoyé un message à Said demandant des infos (nom invité, tarif, nb adultes) **SANS** d'abord lui faire un rapport de ce qu'on avait découvert en tant qu'éclaireur/scout.

**Contexte** : Mission de booking chambre 11 sur HotelRunner. On a réussi à se connecter, vérifié la disponibilité, préparé le formulaire — mais on a demandé des infos au client sans lui communiquer ces bonnes nouvelles d'abord.

**Impact** : Le client reçoit des questions sans contexte → impression qu'on ne maîtrise pas la situation.

### Ce qui aurait dû être fait

```
1. SCOUT    → Explorer la plateforme, vérifier la faisabilité
2. RAPPORT  → Tenir le client informé des découvertes
3. QUESTIONS → Demander les infos manquantes (avec contexte)
4. ACTION   → Exécuter quand tout est clair
```

### Pattern correct

| Phase         | Action                 | Exemple                                |
| ------------- | ---------------------- | -------------------------------------- |
| **Scout**     | Explorer en éclaireur  | Se connecter, vérifier dispo           |
| **Rapport**   | Informer le client     | "Bonne nouvelle, la chambre est dispo" |
| **Questions** | Demander ce qui manque | "Pour finaliser, j'ai besoin de..."    |
| **Action**    | Exécuter               | Créer la réservation                   |

### Checklist communication client

Avant d'envoyer un message au client, vérifier :

- [ ] Ai-je informé le client de ce que j'ai **découvert** ?
- [ ] Le client a-t-il le **contexte** pour comprendre mes questions ?
- [ ] Mon message montre-t-il que je **maîtrise** la situation ?
- [ ] Ai-je fait preuve d'**empathie** (me mettre à sa place) ?

### Message correctif envoyé

Après avoir réalisé l'erreur, message de suivi envoyé :

```
Au fait Said, j'aurais dû commencer par ça :

Bonne nouvelle — on a réussi à se connecter à HotelRunner et la chambre 11
(suite familiale) est bien DISPONIBLE pour les 2 nuitées !

Le formulaire de réservation est prêt, il me manque juste les infos que
je t'ai demandées dans mon message précédent.

Omar
```

### Leçon retenue

> **Ne jamais présumer que le client sait ce qu'on sait.**
> Toujours faire un rapport avant de demander des actions/infos.
> L'empathie client = se mettre à sa place et imaginer ce qu'il reçoit.

---

## [2025-12-19] Ton de communication : Adapter le registre au contexte

### L'erreur

Messages proposés avec un ton trop informel/familier ("tu", style décontracté) pour un client de +60 ans dans un contexte professionnel.

**Exemple problématique** :

```
Au fait Said, j'aurais dû commencer par ça...
```

**Ce qui aurait dû être écrit** :

```
Monsieur Thaifa,

Veuillez m'excuser, j'aurais dû commencer par vous informer que...
```

### Facteurs à considérer

| Facteur  | Impact sur le registre          |
| -------- | ------------------------------- |
| Relation | Nouveau client → formel         |
| Culture  | Maroc → respect des aînés       |
| Enjeu    | High-ticket → professionnalisme |

### Registre correct pour ce client

- ✅ **Vouvoiement** obligatoire
- ✅ **Respect** sans rigidité corporate
- ❌ Pas de : "Salut", "tu", abréviations familières

### Adaptation au canal (WhatsApp)

| Situation                        | Approche                             |
| -------------------------------- | ------------------------------------ |
| **1er message du jour**          | Salutation + signature               |
| **Messages suivants (même fil)** | Direct, fluide, pas de re-salutation |
| **Message important/formel**     | Salutation + signature               |

**Exemple fluide (message de suivi)** :

```
Excusez-moi, j'aurais dû commencer par là :
Bonne nouvelle — [contenu]
```

**Pas besoin de** : "Monsieur Thaifa" + "Cordialement, Omar" à CHAQUE message.

### Checklist avant envoi message client

- [ ] Ai-je utilisé le vouvoiement ?
- [ ] Le ton est-il adapté à l'âge et au statut du client ?
- [ ] Y a-t-il une formule de politesse appropriée ?
- [ ] Le message est-il structuré professionnellement ?

### Leçon retenue

> **Toujours adapter le registre de communication au contexte du client.**
> En cas de doute, opter pour le registre le plus formel.
> Un message trop formel est rarement mal perçu ; un message trop familier peut l'être.

---

## [2025-12-20] Livrables Client : Fichiers Prêts à l'Emploi

### L'erreur

Créé un fichier `.md` avec le message WhatsApp contenant des métadonnées, des sections d'explication, du contexte — alors qu'Omar avait besoin d'un fichier `.txt` prêt à copier-coller directement.

**Ce qui a été fait** :

```
draft-message-rapport-reservations.md  ← Markdown avec métadonnées
```

**Ce qui était attendu** :

```
2025-12-20-message-rapport-reservations.txt  ← Texte brut prêt à copier
```

### Impact

- Omar doit extraire manuellement le message du fichier markdown
- Perte de temps
- Friction inutile dans le workflow

### Ce qui aurait dû être fait

Quand on prépare un livrable pour envoi client (message, email, document) :

| Type                 | Format           | Nommage                          |
| -------------------- | ---------------- | -------------------------------- |
| Message WhatsApp/SMS | `.txt`           | `YYYY-MM-DD-message-[sujet].txt` |
| Email                | `.txt` ou `.eml` | `YYYY-MM-DD-email-[sujet].txt`   |
| Rapport/Document     | `.pdf`           | `rapport-[sujet]-YYYY-MM-DD.pdf` |
| Notes internes       | `.md`            | Libre                            |

### Structure livrables

```
communication/
├── whatsapp/
│   ├── 2025-12-20-message-rapport-reservations.txt  ← Prêt à copier
│   └── draft-*.md                                    ← Brouillons/notes
│
projects/[projet]/
└── deliverables/
    └── rapport-[sujet]-YYYY-MM-DD.pdf               ← PDF final
```

### Checklist avant création livrable client

- [ ] Le fichier est-il **directement utilisable** sans extraction ?
- [ ] Le format est-il adapté à l'usage (`.txt` pour copier, `.pdf` pour envoyer) ?
- [ ] Le nommage inclut-il la **date** et le **sujet** ?
- [ ] Le fichier est-il dans le **bon dossier** (deliverables/, whatsapp/) ?

### Leçon retenue

> **Un livrable client doit être prêt à l'emploi, pas un document de travail.**
> Toujours se demander : "Omar peut-il utiliser ce fichier immédiatement sans manipulation ?"
> Si non → mauvais format ou mauvaise structure.

---

## [2025-12-22] Confusion Dates : Vérifier les Années

### L'erreur

Dates mentionnées sans année explicite, créant confusion entre 2024 et 2025. Particulièrement problématique lors du passage d'année (décembre → janvier).

### Impact

- Mauvaise compréhension des délais
- Risque de planification incorrecte
- Confusion dans l'historique des réservations

### Ce qui doit être fait

| Situation                         | Action                     |
| --------------------------------- | -------------------------- |
| Client mentionne "le 20 décembre" | Demander/confirmer l'année |
| Date proche du Nouvel An          | Double-vérifier l'année    |
| Réservation pour "janvier"        | Clarifier 2025 ou 2026     |

**Pattern de vérification** :

- Toujours spécifier l'année complète (ex: "20 décembre 2025")
- Vérifier l'année quand un client mentionne juste le mois/jour
- Attention particulière au passage d'année (déc → jan)

### Leçon retenue

> **Toujours vérifier l'année.** "Le 20 décembre" peut être 2024 ou 2025.
> Ne jamais présumer — toujours expliciter.

---

## Template pour futures leçons

```markdown
## [YYYY-MM-DD] Titre court

### L'erreur

[Description factuelle de ce qui s'est passé]

### Impact

[Conséquences de l'erreur]

### Ce qui aurait dû être fait

[La bonne approche]

### Leçon retenue

[Principe généralisable]
```
