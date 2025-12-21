# Pattern Extraction

**Date**: 2025-12-21

---

## Extracted Patterns

### Pattern 1: Tiered Permission Model

- **Observed In**: Official docs, Backslash Security, all sources
- **Underlying Principle**: Defense in depth via three distinct permission tiers
- **Structure**:
  | Tier | Purpose | Examples |
  |------|---------|----------|
  | **Allow** | 100% harmless, high-frequency | Read, Edit, git status |
  | **Ask** | Useful but risky, needs review | git push, docker run |
  | **Deny** | Never allowed, nuclear shield | .env, curl, secrets |
- **Generalization Test**: Would apply to any AI agent permission system → **Yes**
- **Confidence**: High

### Pattern 2: Category-Based Organization

- **Observed In**: GitHub repos, practical configurations
- **Underlying Principle**: Related permissions grouped together improve maintainability and auditability
- **Structure**:
  ```
  # Core Tools (always allowed)
  # File Operations (allowed)
  # Git Operations (allowed with patterns)
  # Build/Test Tools (allowed with patterns)
  # MCP Servers (allowed)
  # Network (caution)
  # System/Sudo (high risk)
  # Deny List (never)
  ```
- **Generalization Test**: Would apply to any configuration file → **Yes**
- **Confidence**: High

### Pattern 3: Prefix Matching Awareness

- **Observed In**: Official docs, developer blogs
- **Underlying Principle**: Bash permissions use prefix matching, not regex or glob
- **Implications**:
  - `Bash(npm:*)` matches `npm install`, `npm run test`, `npm audit fix`
  - `Bash(git commit:*)` matches any git commit variant
  - Cannot use regex patterns like `Bash(npm (run|install):*)`
- **Generalization Test**: Specific to Claude Code Bash tool → **No**
- **Confidence**: High

### Pattern 4: Explicit Dual Denial

- **Observed In**: Pete Freitag blog, confirmed in testing
- **Underlying Principle**: Read and Write are independent - denying one doesn't deny the other
- **Rule**: For sensitive files, deny BOTH:
  ```json
  "deny": [
    "Read(./.env)",
    "Write(./.env)"
  ]
  ```
- **Generalization Test**: Specific to file permission systems → **Partially**
- **Confidence**: Medium (bug may be fixed)

### Pattern 5: Principle of Least Privilege

- **Observed In**: All security sources
- **Underlying Principle**: Grant minimum permissions necessary, expand only when needed
- **Application**:
  1. Start with minimal set
  2. Add permissions as workflows require
  3. Review and remove unused permissions
  4. Prefer specific patterns over wildcards
- **Generalization Test**: Universal security principle → **Yes**
- **Confidence**: High

### Pattern 6: Hierarchical Specificity

- **Observed In**: Official docs
- **Underlying Principle**: More specific scopes override broader ones
- **Hierarchy** (highest precedence first):
  1. Enterprise managed-settings.json
  2. CLI arguments
  3. Local (.claude/settings.local.json)
  4. Project (.claude/settings.json)
  5. User (~/.claude/settings.json)
- **Generalization Test**: Common in config systems → **Yes**
- **Confidence**: High

### Pattern 7: Deduplication First

- **Observed In**: General best practice
- **Underlying Principle**: Duplicate entries add maintenance burden, zero benefit
- **Rule**: Each permission appears exactly once
- **Generalization Test**: Universal for any list/array → **Yes**
- **Confidence**: High

### Pattern 8: Network as High-Risk Zone

- **Observed In**: Security sources
- **Underlying Principle**: Network tools (curl, wget, WebFetch) are data exfiltration vectors
- **Options**:
  - Deny all: `"deny": ["WebFetch", "Bash(curl:*)", "Bash(wget:*)"]`
  - Allow specific domains only
  - Ask mode for case-by-case
- **Generalization Test**: Universal for AI agents with internet access → **Yes**
- **Confidence**: High

---

## Anti-Patterns Identified

### Anti-Pattern 1: Wildcard Everything
- **Bad**: `Bash(*)` - allows any command
- **Good**: Explicit patterns for allowed commands
- **Why**: Defeats purpose of permission system

### Anti-Pattern 2: Organic Growth Without Review
- **Bad**: Add permissions as needed, never remove
- **Good**: Periodic audit (monthly), remove unused
- **Why**: Accumulates risk, duplicates, dead entries

### Anti-Pattern 3: Trusting Deny Alone
- **Bad**: Rely solely on deny patterns for security
- **Good**: Layer with OS permissions, containers, secrets management
- **Why**: Patterns have bugs, can be bypassed

### Anti-Pattern 4: Mixing Concerns
- **Bad**: Random order, no grouping
- **Good**: Logical categories with clear separation
- **Why**: Hard to audit, easy to miss issues

### Anti-Pattern 5: Copy-Paste Accumulation
- **Bad**: Copy permissions from examples without understanding
- **Good**: Understand each permission, customize for actual use
- **Why**: Unnecessary exposure, doesn't match actual workflow

---

## Omar-Specific Considerations

From analyzing current `.claude/settings.local.json`:

| Issue | Current State | Pattern to Apply |
|-------|---------------|------------------|
| Duplicates | ls:*, tree:*, mv:*, WebSearch | Pattern 7: Deduplication |
| Redundancy | WebFetch + domain-specific | Pattern 7: Remove redundant |
| No grouping | Flat list | Pattern 2: Category-based |
| Sudo commands | 12 various | Pattern 5: Audit each need |
| MCP tools | Mixed with bash | Pattern 2: Separate category |
