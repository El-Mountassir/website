# Source Triangulation

## Sources

### Source 1: Claude Code Official Documentation

- **URL**: https://code.claude.com/docs/en/slash-commands.md
- **Type**: Official
- **Key Claims**:
  - Fichier `.md` dans `.claude/commands/` ou `~/.claude/commands/`
  - YAML frontmatter avec: `description`, `allowed-tools`, `argument-hint`, `model`, `disable-model-invocation`
  - Variables: `$ARGUMENTS` (tous), `$1`, `$2`, `$3` (positionnels)
  - `!` prefix pour exécuter bash, `@` prefix pour inclure fichiers
  - `description` requis pour visibilité dans `/help`
- **Evidence Quality**: Strong (official docs)
- **Potential Bias**: None

### Source 2: Existing Project Commands (elevate.md, question-w-mermaid-diagrams.md)

- **URL**: Local `.claude/commands/`
- **Type**: Practitioner (in-project)
- **Key Claims**:
  - Frontmatter YAML avec `allowed-tools`, `description`, `argument-hint`, `model`
  - Structure: Purpose → Variables → Pipeline/Process → Output
  - Commandes complexes utilisent sections claires et templates
- **Evidence Quality**: Strong (working examples)
- **Potential Bias**: Specific to this project

### Source 3: Non-Conforming Commands (start.md, end.md, sync.md)

- **URL**: Local `.claude/commands/`
- **Type**: Practitioner (counter-example)
- **Key Claims**:
  - Fonctionnent SANS frontmatter (Claude les exécute quand même)
  - Mais pas visibles correctement dans `/help`
  - Manquent les restrictions `allowed-tools`
  - Variables mal documentées
- **Evidence Quality**: Moderate (functional but incomplete)
- **Potential Bias**: Created hastily without standard reference

## Convergence Analysis

| Pattern | Official Docs | Good Examples | Bad Examples | Confidence |
|---------|---------------|---------------|--------------|------------|
| YAML frontmatter requis | AGREE | AGREE | DISAGREE | High |
| `description` obligatoire | AGREE | AGREE | GAP | High |
| `allowed-tools` pour bash | AGREE | AGREE | GAP | High |
| `argument-hint` pour UX | AGREE | AGREE | GAP | High |
| Structure Purpose/Variables/Process | GAP | AGREE | PARTIAL | Medium |
| `$ARGUMENTS` vs `$1, $2` | AGREE | AGREE | GAP | High |

## Decision Points (Disagreements)

1. **Commandes sans frontmatter fonctionnent** mais ne sont pas best-practice
   - Décision: Toujours ajouter frontmatter (standard)

2. **Structure du body (Purpose/Variables/etc.)** n'est pas dans les docs officielles
   - Décision: Adopter le pattern des bons exemples existants

3. **Langue du contenu** (FR vs EN)
   - Décision: English (meilleure performance AI, per CLAUDE.md)
