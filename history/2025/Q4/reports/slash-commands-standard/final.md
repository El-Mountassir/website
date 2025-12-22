# Slash Commands Standard

**Generated**: 2025-12-22
**Pipeline**: history/2025/Q4/reports/slash-commands-standard/

## Summary

This report establishes the standard for creating custom slash commands in Claude Code. It addresses the gap identified when `/start` and `/end` commands were created without proper YAML frontmatter, making them non-conformant with Claude Code best practices.

## Key Insights

| Insight | Confidence | Sources |
|---------|------------|---------|
| YAML frontmatter is mandatory | High | Official docs, existing good commands |
| `description` enables discoverability | High | Official docs |
| `allowed-tools` improves security | High | Official docs, principle of least privilege |
| Structured body (Purpose/Variables/Instructions) | Medium | Project examples |
| Variables section clarifies defaults | High | Official docs, project examples |

## Deliverables

### 1. Template

**Location**: `templates/commands/slash-command.md`

A reusable template for creating new slash commands with:
- Complete YAML frontmatter reference
- Standard body structure
- Variable syntax reference
- Pre-commit checklist

### 2. Skill

**Location**: `.claude/skills/creating-commands/SKILL.md`

A skill that guides future Claude instances to create proper commands:
- Workflow for command creation
- Anti-patterns to avoid
- Examples of good commands

### 3. Fixed Commands

| Command | Changes Made |
|---------|--------------|
| `/start` | Added frontmatter, restructured body |
| `/end` | Added frontmatter, restructured body |
| `/sync` | Added frontmatter, restructured body |

## Standard Summary

### Mandatory Frontmatter

```yaml
---
description: [Verb] [what] [context] (max 80 chars)
allowed-tools: [Only needed tools]
argument-hint: [expected arguments]
---
```

### Standard Body Structure

```markdown
# Purpose
[What and when]

## Variables
NAME: $1
If empty: [default]

---

## Instructions
[Step-by-step]

---

## Output
[Expected format]

---

## Example
[Usage]
```

### Anti-Patterns

| Don't | Do |
|-------|-----|
| Skip frontmatter | Always include `---` block |
| Generic description | Action-oriented, specific |
| Unrestricted tools | List only needed tools |
| No examples | At least one example |

## Limitations & Gaps

- **`disable-model-invocation`**: Use case unclear, not documented in project
- **Model selection**: When to specify `model:` vs inherit conversation model

## Files Created/Modified

| File | Action |
|------|--------|
| `templates/commands/slash-command.md` | CREATED |
| `.claude/skills/creating-commands/SKILL.md` | CREATED |
| `.claude/commands/start.md` | MODIFIED |
| `.claude/commands/end.md` | MODIFIED |
| `.claude/commands/sync.md` | MODIFIED |

## Sources

- [Claude Code Slash Commands Docs](https://code.claude.com/docs/en/slash-commands.md)
- `.claude/commands/elevate.md` (project example)
- `.claude/commands/question-w-mermaid-diagrams.md` (project example)
