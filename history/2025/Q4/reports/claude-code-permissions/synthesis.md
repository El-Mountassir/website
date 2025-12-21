# Synthesis Notes

**Date**: 2025-12-21

---

## Integration Strategy

Combine patterns into a **Category-Based, Tiered Permission System**:

### Category Structure

```
1. CORE TOOLS        - Built-in Claude Code tools (Read, Write, Edit, etc.)
2. FILE OPERATIONS   - File system commands (ls, tree, find, etc.)
3. GIT OPERATIONS    - Version control (git status, diff, log, commit, etc.)
4. BUILD & TEST      - Project tooling (npm, pnpm, docker, python, etc.)
5. MCP SERVERS       - Model Context Protocol integrations
6. SKILLS            - Custom Claude Code skills
7. SYSTEM            - System operations (sudo commands)
8. NETWORK           - Web access (WebFetch, WebSearch)
9. DENY LIST         - Explicitly blocked operations
```

### Tiered Approach per Category

For each category:
- **Allow**: High-frequency, low-risk operations
- **Ask** (future): Moderate-risk, needs case-by-case review
- **Deny**: Never allowed regardless of context

---

## Current File Analysis

### Duplicates to Remove (4)
- `Bash(ls:*)` - appears twice (lines 26, 70)
- `Bash(tree:*)` - appears twice (lines 14, 61)
- `Bash(mv:*)` - appears twice (lines 36, 59)
- `WebSearch` - appears twice (lines 8, 60)

### Redundancies to Consolidate
- `WebFetch` (general, line 73) makes domain-specific ones unnecessary:
  - `WebFetch(domain:www.anthropic.com)` (line 57)
  - `WebFetch(domain:uxdesign.cc)` (line 62)
  - `WebFetch(domain:scaletime.co)` (line 63)
  - `WebFetch(domain:blog.hotelogix.com)` (line 64)
  - `WebFetch(domain:dashthis.com)` (line 65)
  - `WebFetch(domain:www.cloudbeds.com)` (line 66)

### Sudo Commands Audit

| Command | Purpose | Verdict |
|---------|---------|---------|
| `sudo useradd:*` | User management | Keep (admin workflow) |
| `sudo usermod:*` | User modification | Keep (admin workflow) |
| `sudo chmod:*` | Permission change | Keep (common need) |
| `sudo setfacl:*` | ACL management | Keep (specific workflow) |
| `sudo chown:*` | Ownership change | Keep (common need) |
| `sudo ls:*` | Root listing | Keep (diagnostic) |
| `sudo cat:*` | Root file read | Keep (diagnostic) |
| `sudo find:*` | Root file search | Keep (diagnostic) |
| `sudo sed -i:*` | Root file edit | **Review** (risky) |
| `sudo grep:*` | Root search | Keep (diagnostic) |
| `sudo sed:*` | Root stream edit | Redundant with sed -i |
| `sudo apt-get update:*` | Package update | Keep |
| `sudo apt-get install:*` | Package install | Keep |

---

## Proposed Optimized Structure

```json
{
  "permissions": {
    "allow": [
      "// ═══════════════════════════════════════════════════════════",
      "// CORE TOOLS - Built-in Claude Code capabilities",
      "// ═══════════════════════════════════════════════════════════",
      "Read",
      "Write",
      "Edit",
      "Skill",

      "// ═══════════════════════════════════════════════════════════",
      "// FILE OPERATIONS - File system navigation and management",
      "// ═══════════════════════════════════════════════════════════",
      "Bash(ls:*)",
      "Bash(tree:*)",
      "Bash(find:*)",
      "Bash(cat:*)",
      "Bash(wc:*)",
      "Bash(sort:*)",
      "Bash(mv:*)",
      "Bash(mkdir:*)",
      "Bash(chmod:*)",
      "Bash(du -sh:*)",
      "Bash(xargs:*)",

      "// ═══════════════════════════════════════════════════════════",
      "// GIT OPERATIONS - Version control",
      "// ═══════════════════════════════════════════════════════════",
      "Bash(git status)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git init:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",

      "// ═══════════════════════════════════════════════════════════",
      "// BUILD & TEST - Development tooling",
      "// ═══════════════════════════════════════════════════════════",
      "Bash(npm test:*)",
      "Bash(pnpm:*)",
      "Bash(uv:*)",
      "Bash(python3:*)",
      "Bash(docker:*)",
      "Bash(pandoc:*)",
      "Bash(typst:*)",
      "Bash(wkhtmltopdf:*)",

      "// ═══════════════════════════════════════════════════════════",
      "// MCP SERVERS - External integrations",
      "// ═══════════════════════════════════════════════════════════",
      "mcp__firecrawl__*",
      "mcp__code-execution__run_python",
      "mcp__MCP_DOCKER__*",

      "// ═══════════════════════════════════════════════════════════",
      "// SKILLS & COMMANDS - Custom Claude Code extensions",
      "// ═══════════════════════════════════════════════════════════",
      "Skill(tunnel-vision-prevention)",
      "Skill(elevate)",
      "SlashCommand(/context-audit)",

      "// ═══════════════════════════════════════════════════════════",
      "// CLAUDE CLI - Claude Code meta-commands",
      "// ═══════════════════════════════════════════════════════════",
      "Bash(claude:*)",
      "Bash(claude -p:*)",
      "Bash(claude /doctor)",

      "// ═══════════════════════════════════════════════════════════",
      "// NETWORK - Web access (WebFetch general covers all domains)",
      "// ═══════════════════════════════════════════════════════════",
      "WebFetch",
      "WebSearch",

      "// ═══════════════════════════════════════════════════════════",
      "// SYSTEM - Elevated operations (use with care)",
      "// ═══════════════════════════════════════════════════════════",
      "Bash(sudo apt-get update:*)",
      "Bash(sudo apt-get install:*)",
      "Bash(sudo useradd:*)",
      "Bash(sudo usermod:*)",
      "Bash(sudo chmod:*)",
      "Bash(sudo chown:*)",
      "Bash(sudo setfacl:*)",
      "Bash(sudo ls:*)",
      "Bash(sudo cat:*)",
      "Bash(sudo find:*)",
      "Bash(sudo grep:*)",
      "Bash(sudo sed -i:*)",
      "Bash(getfacl:*)",
      "Bash(getent passwd:*)",
      "Bash(sudo -u node ls:*)"
    ],

    "deny": [
      "// ═══════════════════════════════════════════════════════════",
      "// SENSITIVE FILES - Never read or write",
      "// ═══════════════════════════════════════════════════════════",
      "Read(./.env)",
      "Read(./.env.*)",
      "Write(./.env)",
      "Write(./.env.*)",
      "Read(./secrets/**)",
      "Write(./secrets/**)",
      "Read(~/.aws/**)",
      "Read(~/.ssh/**)"
    ]
  }
}
```

---

## Uncertainties

### 1. JSON Comments
- JSON doesn't support comments natively
- Options: (a) Remove comments, (b) Use JSONC, (c) Put in separate doc
- **Recommendation**: Remove for valid JSON, document in companion file

### 2. Deny Pattern Reliability
- Sources report bugs in Read/Write deny patterns
- Mitigation: Test critical denies, don't rely solely on them
- Layer with OS-level protections where critical

### 3. Sudo Scope
- Current config has broad sudo access
- May need tightening for production/sensitive projects
- **For Omar's dev workflow**: Acceptable, but be aware

---

## Failure Modes

### 1. Permission Creep
Over time, new permissions added without removing unused ones.
**Mitigation**: Monthly review, document why each is needed.

### 2. False Sense of Security
Relying on deny patterns that have bugs.
**Mitigation**: Layer defenses, test patterns.

### 3. Workflow Friction
Too restrictive → Claude asks too often → productivity loss.
**Mitigation**: Allow proven safe patterns generously.

---

## Final Structure (JSON-valid)

Since JSON doesn't support comments, the final file will:
1. Group permissions by category (logically ordered)
2. Use clear separators (empty lines between groups - but JSON doesn't allow that either)
3. Document structure in this synthesis file

**Practical solution**: Flat array, but ordered by category. Document mapping in companion file.
