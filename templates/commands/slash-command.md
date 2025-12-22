# Slash Command Template

> **Usage**: Copy this template to `.claude/commands/your-command.md` > **Reference**: https://code.claude.com/docs/en/slash-commands.md

---

## Template

````markdown
---
description: [Verb] [what] [when/context] (max 80 chars)
allowed-tools: Read, Write, Bash(git:*), Glob, Grep
argument-hint: [required-arg] [optional-arg]
---

# Purpose

[One paragraph: What this command does and when to use it]

## Variables

VARIABLE_NAME: $1
OPTIONAL_VAR: $2
ALL_ARGS: $ARGUMENTS

If empty: [Describe default behavior when no arguments provided]

---

## Instructions

### Step 1: [Action Title]

[What Claude should do]

```bash
# Example command if needed
command --flag
```
````

### Step 2: [Action Title]

[Next step...]

---

## Output

[Describe expected output format, template if applicable]

```
## Result

- **Status**: [success/failure]
- **Details**: [...]
```

---

## Example

```
/command-name arg1 arg2
```

→ [Describe what happens]

```

---

## Frontmatter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `description` | ✅ YES | Shown in `/help`, max 80 chars, action-oriented |
| `allowed-tools` | Recommended | Restrict tools for security (principle of least privilege) |
| `argument-hint` | Recommended | Shown in autocomplete, clarifies expected input |
| `model` | Optional | Force specific model (e.g., `claude-3-5-haiku-20241022`) |
| `disable-model-invocation` | Optional | Prevent SlashCommand tool from calling this |

---

## Variable Reference

| Variable | Use Case |
|----------|----------|
| `$ARGUMENTS` | All arguments as single string |
| `$1`, `$2`, `$3` | Individual positional arguments |
| `!`command`` | Execute bash, include output (requires allowed-tools) |
| `@path/to/file` | Include file contents |

---

## Checklist Before Commit

- [ ] `description` is action-oriented and under 80 chars
- [ ] `allowed-tools` only includes necessary tools
- [ ] `argument-hint` clarifies expected input
- [ ] Variables section explains defaults
- [ ] At least one example provided
- [ ] Language is English (per project standards)
```
