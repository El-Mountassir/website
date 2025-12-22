# Pattern Extraction

## Extracted Patterns

### Pattern 1: Mandatory YAML Frontmatter

- **Observed In**: Official docs, elevate.md, question-w-mermaid-diagrams.md
- **Underlying Principle**: Metadata enables discoverability, tool restriction, and proper argument handling
- **Generalization Test**: Would apply to any CLI tool with plugins? → Yes
- **Confidence**: High

**Template**:
```yaml
---
description: One-line description for /help
allowed-tools: Tool1, Tool2, Bash(cmd:*)
argument-hint: [required-arg] [optional-arg]
model: claude-3-5-sonnet-20241022  # optional
---
```

### Pattern 2: Description-First Design

- **Observed In**: Official docs, all good examples
- **Underlying Principle**: The `description` field is used for:
  1. Display in `/help` command list
  2. SlashCommand tool discovery
  3. User understanding before invocation
- **Generalization Test**: Would apply to any plugin system? → Yes
- **Confidence**: High

**Rule**: `description` MUST be:
- Under 80 characters
- Action-oriented (verb first)
- Clear about WHEN to use

### Pattern 3: Tool Restriction for Security

- **Observed In**: Official docs, elevate.md, question-w-mermaid-diagrams.md
- **Underlying Principle**: Commands should only access tools they need
- **Generalization Test**: Principle of least privilege? → Yes (universal)
- **Confidence**: High

**Format**:
```yaml
allowed-tools: Read, Write, Bash(git:*), Bash(ls:*)
```

### Pattern 4: Structured Body Layout

- **Observed In**: elevate.md, question-w-mermaid-diagrams.md
- **Underlying Principle**: Consistent structure enables:
  1. Quick comprehension
  2. Predictable execution
  3. Maintainability
- **Generalization Test**: Would any documentation benefit? → Yes
- **Confidence**: Medium (not in official docs, but strong pattern)

**Structure**:
```markdown
# Purpose
[One paragraph: what and why]

## Variables
VARIABLE_NAME: $1
ARGUMENTS: $ARGUMENTS
If empty: [default behavior]

---

## Instructions / Process
[Step-by-step workflow]

---

## Output / Report
[Expected output format]

---

## Example
[Concrete usage example]
```

### Pattern 5: Variable Binding

- **Observed In**: Official docs, elevate.md
- **Underlying Principle**: Named variables in ## Variables section clarify intent
- **Generalization Test**: Would any parameterized template benefit? → Yes
- **Confidence**: High

**Patterns**:
```markdown
## Variables

USER_QUESTION: $1
ISSUE_NUMBER: $1
PRIORITY: $2
ALL_ARGS: $ARGUMENTS

If empty: [fallback behavior]
```

### Pattern 6: Bash Execution with `!` Prefix

- **Observed In**: Official docs, question-w-mermaid-diagrams.md
- **Underlying Principle**: Dynamic context from system state
- **Generalization Test**: Would any context-aware system benefit? → Yes
- **Confidence**: High

**Requires**: `allowed-tools: Bash(command:*)` in frontmatter

```markdown
Current branch: !`git branch --show-current`
File list: !`git ls-files`
```

---

## Anti-Patterns Identified

### Anti-Pattern 1: Missing Frontmatter

**What**: Command without YAML frontmatter
**Why Bad**:
- Not visible in `/help` properly
- No tool restrictions
- No argument hints
**Example**: start.md, end.md, sync.md (current state)

### Anti-Pattern 2: Generic Description

**What**: Vague description like "Session management"
**Why Bad**: Users can't tell when to use it
**Fix**: "Initialize session by checking active missions and loading context"

### Anti-Pattern 3: Unrestricted Tool Access

**What**: No `allowed-tools` specified
**Why Bad**: Command can access ALL tools (security risk)
**Fix**: Explicitly list only needed tools

### Anti-Pattern 4: Mixing $ARGUMENTS and $1

**What**: Using both in same command inconsistently
**Why Bad**: Confusing, error-prone
**Fix**: Choose one approach based on need:
- Single arg or all combined → `$ARGUMENTS`
- Multiple distinct args → `$1`, `$2`, etc.

### Anti-Pattern 5: Unstructured Body

**What**: Prose without clear sections
**Why Bad**: Hard to parse, maintain, extend
**Fix**: Use Purpose/Variables/Instructions/Output structure
