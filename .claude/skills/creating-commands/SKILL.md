---
name: creating-commands
description: Creates custom slash commands following project standards. Use when user asks to create a new command, add a slash command, or when you need to create /something.
---

# Purpose

Create custom slash commands that conform to Claude Code standards and project conventions.

## Instructions

### Prerequisites

Read the template before creating any command:
- [Slash Command Template](../../../templates/commands/slash-command.md)

### When to Use This Skill

| Trigger | Example |
|---------|---------|
| "create a command" | "Create a /review command" |
| "add slash command" | "Add a command to check tests" |
| "make /something" | "Make /deploy for production" |

### Workflow

#### Step 1: Gather Requirements

Ask or determine:
1. **Name**: What should the command be called? (lowercase, hyphens)
2. **Purpose**: What does it do?
3. **Arguments**: What input does it need?
4. **Tools needed**: What tools will it use?

#### Step 2: Create File

Location: `.claude/commands/{name}.md`

```bash
touch .claude/commands/{name}.md
```

#### Step 3: Write Frontmatter

**MANDATORY** - Always include:

```yaml
---
description: [Verb] [what] [context] (max 80 chars)
allowed-tools: [Only tools needed]
argument-hint: [expected arguments]
---
```

**Rules**:
- `description`: Action verb first, under 80 chars
- `allowed-tools`: Principle of least privilege
- `argument-hint`: Use `[required]` and `[optional]` format

#### Step 4: Write Body

Follow this structure:

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
[Usage example]
```

#### Step 5: Validate

Check against anti-patterns:
- [ ] Has YAML frontmatter?
- [ ] Has description?
- [ ] Has allowed-tools (if using bash)?
- [ ] Variables documented?
- [ ] At least one example?

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| No frontmatter | Not visible in /help | Always add `---` block |
| Generic description | Users don't know when to use | Be specific: "Initialize session by..." |
| No allowed-tools | Unrestricted access | List only needed tools |
| Mixing $ARGUMENTS and $1 | Confusing | Pick one approach |
| No examples | Unclear usage | Add at least one example |

---

## Examples

### Example 1: Simple Command

```markdown
---
description: Run all project tests and report results
allowed-tools: Bash(npm test:*), Bash(pnpm test:*)
argument-hint: [--coverage] [--watch]
---

# Purpose

Run the project test suite with optional flags.

## Variables

FLAGS: $ARGUMENTS
If empty: Run all tests without flags.

---

## Instructions

1. Run tests with provided flags
2. Report results with pass/fail counts
3. Highlight any failures

---

## Example

/test --coverage
→ Runs tests with coverage report
```

### Example 2: Command with Multiple Args

```markdown
---
description: Create a new mission from template
allowed-tools: Read, Write, Bash(mkdir:*)
argument-hint: [mission-name] [priority]
---

# Purpose

Create a new mission file in missions/drafts/ with standard template.

## Variables

MISSION_NAME: $1
PRIORITY: $2
If empty: Prompt for mission name.

---

## Instructions

1. Validate mission name (lowercase, hyphens)
2. Create file: `missions/drafts/{name}.md`
3. Apply mission template with priority $2 or default P3

---

## Example

/new-mission api-refactor P1
→ Creates missions/drafts/api-refactor.md with priority 1
```

---

## Quick Reference

```
.claude/commands/
├── command-name.md     → /command-name
└── subfolder/
    └── other.md        → /other (subfolder context)
```

**Files**:
- Template: `templates/commands/slash-command.md`
- Official docs: https://code.claude.com/docs/en/slash-commands.md
