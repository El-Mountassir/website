# Claude Code Permissions Configuration - Investigation Report

**Generated**: 2025-12-22
**Pipeline**: `history/2025/Q4/reports/claude-permissions-config/`

## Summary

Investigation into why Claude Code instances continue asking for permissions despite configuration in `.claude/settings.local.json`. Root causes identified: **structural misconfiguration** (permissions in wrong file), **pattern syntax issues**, and **potential deny rule bugs**. Solution requires restructuring configuration files and fixing permission patterns.

## Key Insights

| Insight | Confidence | Sources |
|---------|------------|---------|
| Permissions only in `settings.local.json`, not `settings.json` | High | File analysis |
| 82 accumulated entries with organic growth/technical debt | High | File analysis |
| Deny rules may not be enforced (version-dependent bug) | Medium | GitHub Issues #6631, #6699 |
| Prefix matching requires `:*` suffix for wildcards | High | Official docs, community |
| Edit/Write permissions reset each session | High | Official docs |

## Root Cause

```
Primary: Permissions in settings.local.json ONLY (settings.json has only hooks)
Secondary: Pattern syntax issues (missing :* suffixes, path-specific entries)
Tertiary: Possible deny rule enforcement bug
```

## Recommended Fix

### 1. Restructure Configuration Files

**settings.json** (committed, shared baseline):
```json
{
  "permissions": {
    "allow": [
      "Read", "Write", "Edit", "Grep", "Glob", "TodoWrite",
      "Bash(ls:*)", "Bash(tree:*)", "Bash(find:*)", "Bash(cat:*)",
      "Bash(git:*)", "Bash(npm:*)", "Bash(pnpm:*)", "Bash(docker:*)",
      "Bash(uv:*)", "Bash(python3:*)", "Bash(claude:*)",
      "Bash(mkdir:*)", "Bash(mv:*)", "Bash(chmod:*)",
      "Bash(pandoc:*)", "Bash(typst:*)",
      "mcp__MCP_DOCKER__*", "mcp__linear__*", "mcp__firecrawl__*",
      "Skill", "SlashCommand", "WebFetch", "WebSearch"
    ],
    "deny": [
      "Read(./.env)", "Read(./.env.local)", "Read(./.env.*)",
      "Write(./.env)", "Write(./.env.local)", "Write(./.env.*)",
      "Read(./secrets/**)", "Write(./secrets/**)",
      "Read(~/.aws/**)", "Read(~/.ssh/**)"
    ]
  },
  "hooks": {
    "PostToolUse": [...]
  }
}
```

**settings.local.json** (gitignored, personal only):
```json
{
  "permissions": {
    "allow": [
      "Bash(sudo:*)",
      "Bash(gh:*)"
    ]
  }
}
```

### 2. Fix Pattern Syntax

| Problem Pattern | Fixed Pattern |
|-----------------|---------------|
| `Bash(git status)` | `Bash(git:*)` (covers all git) |
| `Bash(git -C /path...)` | Remove (covered by `Bash(git:*)`) |
| `Bash(done)`, `Bash(while read f)` | Remove (shell fragments, not commands) |

### 3. Test with `/permissions` Command

After restructuring, run `/permissions` to verify:
- Both files are loaded
- Patterns are recognized
- Deny rules appear

## Limitations & Gaps

- Deny rule enforcement in version 2.0.75 not verified
- SubAgent permission inheritance unclear
- MCP wildcard syntax (`mcp__server__*`) not tested

## Sources

- [Claude Code Settings - Official Docs](https://docs.claude.com/en/docs/claude-code/settings)
- [GitHub Issue #6631 - Deny Not Enforced](https://github.com/anthropics/claude-code/issues/6631)
- [GitHub Issue #6699 - Critical Security Bug](https://github.com/anthropics/claude-code/issues/6699)
- [ClaudeLog Configuration Guide](https://claudelog.com/configuration/)

---

## Next Step

Execute mission: `missions/queue/2025-12-22-claude-permissions-fix.md`
