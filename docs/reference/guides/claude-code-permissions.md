# Claude Code Permissions Configuration Guide

```yaml
Title: Claude Code Permissions Configuration Guide
Creator: Omar El Mountassir + Claude Code
Subject: Permissions, Settings, Security, Claude Code
Description: Reference for configuring Claude Code permissions - file placement, pattern syntax, security
Date: 2025-12-22
Type: Text
Format: Markdown
Identifier: guides/claude-code-permissions.md
Language: en
Version: 0.0.1-alpha.0
Status: REFERENCE
Dimension: Configuration
```

---

## Purpose

A reusable reference for configuring Claude Code permissions. Covers file placement, pattern syntax, security considerations, and troubleshooting.

---

## 1. Settings File Hierarchy

Claude Code loads settings in this order (higher = higher precedence):

| Level | File | Purpose | Git Status |
|-------|------|---------|------------|
| 1 | Managed settings | Enterprise policies | N/A |
| 2 | Command line args | Temporary overrides | N/A |
| 3 | `.claude/settings.local.json` | Personal project overrides | Gitignored |
| 4 | `.claude/settings.json` | Shared project settings | Committed |
| 5 | `~/.claude/settings.json` | Global user defaults | N/A |

### File Placement Philosophy

| File | What Goes Here | Example |
|------|----------------|---------|
| `settings.json` | Team standards, security policies, common tools | `Bash(git:*)`, deny rules for .env |
| `settings.local.json` | Personal additions, experiments | `Bash(sudo:*)` |

**Rule**: If it benefits all team members, put it in `settings.json`. If it's personal, use `settings.local.json`.

---

## 2. Pattern Syntax Reference

### Permission Categories

```json
{
  "permissions": {
    "allow": [...],   // Always allowed (no prompt)
    "ask": [...],     // Prompt each time (default)
    "deny": [...]     // Never allowed (blocked)
  }
}
```

### Tool Patterns

| Pattern | Matches | Example |
|---------|---------|---------|
| `Read` | All file reads | Any `Read` call |
| `Bash(git:*)` | All git commands | `git status`, `git commit`, `git push` |
| `Bash(npm run test:*)` | npm test with any args | `npm run test`, `npm run test:unit` |
| `mcp__linear__*` | All Linear MCP calls | Any Linear integration |

**Key**: The `:*` suffix enables prefix matching (wildcards only work at the end).

### Path Patterns (Gitignore-style)

| Pattern | Meaning | Example |
|---------|---------|---------|
| `Read(./.env)` | Relative to project root | `.env` in project |
| `Read(./.env.*)` | Wildcard in filename | `.env.local`, `.env.prod` |
| `Read(./secrets/**)` | Recursive directory | All files under `secrets/` |
| `Read(~/.aws/**)` | Home directory | AWS credentials |
| `Read(//etc/passwd)` | Absolute filesystem path | System files |

**Gotcha**: `/path` is relative to settings file. Use `//path` for absolute filesystem paths.

---

## 3. Deny List Best Practices

### Essential Denies

```json
"deny": [
  "Read(./.env)",
  "Read(./.env.local)",
  "Read(./.env.*)",
  "Write(./.env)",
  "Write(./.env.local)",
  "Write(./.env.*)",
  "Read(./secrets/**)",
  "Write(./secrets/**)",
  "Read(~/.aws/**)",
  "Read(~/.ssh/**)"
]
```

### Why These Matter

| Pattern | Protects |
|---------|----------|
| `.env*` | API keys, database credentials |
| `secrets/**` | Sensitive project files |
| `~/.aws/**` | AWS access keys |
| `~/.ssh/**` | SSH private keys |

---

## 4. Security Matrix

### Solo Developer (Permissive)

```json
{
  "permissions": {
    "allow": [
      "Read", "Write", "Edit",
      "Bash(git:*)", "Bash(npm:*)", "Bash(docker:*)",
      "WebFetch", "WebSearch"
    ],
    "deny": [
      "Read(./.env*)", "Read(~/.aws/**)", "Read(~/.ssh/**)"
    ]
  }
}
```

**Trade-off**: Maximum productivity, relies on deny rules for security.

### Team Environment (Restrictive)

```json
{
  "permissions": {
    "allow": [
      "Read", "Grep", "Glob",
      "Bash(git status:*)", "Bash(git diff:*)",
      "Bash(npm run test:*)"
    ],
    "ask": [
      "Write", "Edit",
      "Bash(git commit:*)", "Bash(git push:*)"
    ],
    "deny": [
      "Bash(rm:*)", "Bash(sudo:*)",
      "Edit(/etc/**)", "Edit(*.prod.json)"
    ]
  }
}
```

**Trade-off**: Friction for safety, each destructive action requires approval.

---

## 5. Common Patterns

### Version Control

```json
"Bash(git:*)"       // All git commands
"Bash(gh:*)"        // GitHub CLI
```

### Package Managers

```json
"Bash(npm:*)"       // npm
"Bash(pnpm:*)"      // pnpm
"Bash(uv:*)"        // uv (Python)
```

### Build Tools

```json
"Bash(docker:*)"    // Docker
"Bash(python3:*)"   // Python
```

### MCP Integrations

```json
"mcp__linear__*"    // Linear
"mcp__firecrawl__*" // Firecrawl
"mcp__MCP_DOCKER__*" // Docker MCP
```

---

## 6. Troubleshooting

### "Claude keeps asking for permission"

**Check**:
1. Is the pattern in `settings.json` (not just `settings.local.json`)?
2. Does the pattern have `:*` suffix for prefix matching?
3. Run `/permissions` to verify loaded patterns

**Fix**: Move shared permissions to `settings.json` with wildcards.

### "Deny rules don't seem to work"

**Known Issue**: Some Claude Code versions have deny rule bugs.

**Workarounds**:
1. Use PreToolUse hooks as alternative enforcement
2. Update to latest Claude Code version
3. Check GitHub issues #6631, #6699

### "Patterns are too specific"

**Problem**: Path-specific patterns like `Bash(git -C /home/user/project...)` aren't portable.

**Fix**: Use simple wildcards: `Bash(git:*)` covers all git commands regardless of path.

---

## 7. Migration from Cluttered Config

If you have 80+ entries in `settings.local.json`:

1. **Backup**: `cp settings.local.json settings.local.json.backup`
2. **Identify patterns**: Group similar entries (15 git commands -> 1 `Bash(git:*)`)
3. **Move to settings.json**: Shared patterns belong in committed file
4. **Minimize local**: Only personal additions remain

**Before**: 82 entries in local, 0 in shared
**After**: 40 entries in shared, 1 in local

---

## 8. References

- [Claude Code Settings Docs](https://docs.claude.com/en/docs/claude-code/settings)
- [GitHub Issue #6631](https://github.com/anthropics/claude-code/issues/6631) - Deny not enforced
- [GitHub Issue #6699](https://github.com/anthropics/claude-code/issues/6699) - Security bug

---

## Changelog

### 0.0.1-alpha.0 (2025-12-22)

- Initial version promoted from `/elevate` pipeline
- Validated via claude-code-guide research
