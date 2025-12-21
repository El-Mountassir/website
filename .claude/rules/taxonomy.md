# Taxonomie Hiérarchique

## Pattern
`{area}/{domain}/{category}/`

**Ne jamais utiliser de tirets composés** comme `agentic-ai/` ou `dev-tools/`

---

## Areas (Niveau 1)

| Area | Description | Exemples de domains |
|------|-------------|---------------------|
| `tech/` | Technique & technologie | ai/, dev/, data/, infra/ |
| `biz/` | Business & stratégie | strategy/, clients/, market/ |
| `knowledge/` | Connaissance & concepts | concepts/, methodology/, research/ |
| `personal/` | Personnel & privé | docs/, notes/, journal/ |

---

## Domains (Niveau 2)

### tech/
- `ai/` - Intelligence artificielle
- `dev/` - Développement
- `data/` - Données & graphs
- `infra/` - Infrastructure & hardware

### biz/
- `strategy/` - Stratégie d'entreprise
- `clients/` - Clients & prospects
- `market/` - Marché & concurrence

### knowledge/
- `concepts/` - Concepts théoriques
- `methodology/` - Méthodologies
- `research/` - Recherche & papers

### personal/
- `docs/` - Documents personnels
- `notes/` - Notes diverses

---

## Categories (Niveau 3)

Exemples :
- `tech/ai/agentic/` - IA agentique
- `tech/ai/prompting/` - Prompt engineering
- `tech/dev/tools/` - Outils de dev
- `tech/infra/hardware/` - Specs matériel
- `biz/clients/potential/` - Prospects

---

## Structure KB

```
~/Documents/kb/
├── sources/      # Contenu brut capturé (inbox)
├── knowledge/    # Contenu raffiné validé
├── resources/    # Templates, prompts, configs
├── refs/         # Docs, papers, bookmarks
└── archive/      # Inactif préservé
```

---

## Règles

1. **Max 4 niveaux** de profondeur
2. **Noms courts** en minuscules
3. **Pas de tirets composés** → utiliser la hiérarchie
4. **Cohérence** → même structure partout
