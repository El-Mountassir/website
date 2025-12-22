# Synthesis Notes

## Integration Strategy

Combiner les 6 patterns en:
1. **Template** → `.claude/templates/commands/slash-command.md`
2. **Skill** → `.claude/skills/creating-commands/SKILL.md`
3. **Corrections** → Aligner start.md, end.md, sync.md

## Deliverables

### 1. Template (slash-command.md)

Location: `templates/commands/slash-command.md`

Contenu:
- YAML frontmatter complet
- Structure standardisée
- Placeholders annotés
- Instructions d'utilisation

### 2. Skill (creating-commands)

Location: `.claude/skills/creating-commands/SKILL.md`

Rôle: Guider les futures instances à créer des commandes conformes
- Référence le template
- Inclut les anti-patterns à éviter
- Workflow step-by-step

### 3. Corrections à appliquer

| Commande | Action |
|----------|--------|
| start.md | Ajouter frontmatter, restructurer body |
| end.md | Ajouter frontmatter, restructurer body |
| sync.md | Ajouter frontmatter |

## Uncertainties

- **`disable-model-invocation`**: Quand l'utiliser? → Documenter mais ne pas inclure par défaut
- **`model`**: Quand spécifier? → Seulement si performance/coût critique

## Failure Modes

1. **Over-engineering**: Template trop complexe → garder simple
2. **Inconsistency**: Certaines commandes non alignées → audit régulier
3. **Obsolescence**: Standard évolue → lier aux docs officielles

## Draft Structure

### Template Structure

```markdown
---
description: [Action verb] [what] [when/why]
allowed-tools: [Tool1, Tool2, Bash(cmd:*)]
argument-hint: [required] [optional]
---

# Purpose

[One paragraph explaining what this command does and when to use it]

## Variables

VARIABLE: $1
If empty: [default behavior]

---

## Instructions

### Step 1: [Title]
[Instructions]

### Step 2: [Title]
[Instructions]

---

## Output

[Expected output format]

---

## Example

/command-name arg1 arg2
→ [Expected result]
```

### Skill Structure

```markdown
---
name: creating-commands
description: Creates custom slash commands following project standards...
---

# Purpose
Help Claude instances create proper slash commands.

## Instructions
1. Read the template
2. Follow the pattern
3. Validate against anti-patterns

## Template
Reference: templates/commands/slash-command.md

## Anti-Patterns
[List from patterns.md]

## Examples
[2-3 examples]
```
