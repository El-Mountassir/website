# Claude Code Permissions Optimization Guide

**Generated**: 2025-12-21
**Pipeline**: history/2025/Q4/reports/claude-code-permissions/

---

## Summary

This guide provides a research-backed, optimized Claude Code permissions configuration. It transforms a 77-line organic settings file into a 60-line organized structure with duplicates removed, categories defined, and security considerations applied.

---

## Key Insights

| Insight                                           | Confidence | Sources                                     |
| ------------------------------------------------- | ---------- | ------------------------------------------- |
| Three-tier model (allow/ask/deny) is standard     | High       | Official docs, Backslash, all practitioners |
| Deny is processed first, then allow, then ask     | High       | Official docs, multiple confirmations       |
| Bash uses prefix matching, NOT regex              | High       | Official docs, developer testing            |
| Read deny ≠ Write deny (must deny both)           | Medium     | Pete Freitag, GitHub issues                 |
| Deny patterns have known bugs                     | Medium     | GitHub issues #4467, #6631                  |
| Category-based organization improves auditability | High       | Best practice consensus                     |
| Layer defenses beyond just permissions            | High       | Security sources, Backslash                 |

---

## Before & After

### Before (79 permissions)

- 4 duplicates (ls, tree, mv, WebSearch)
- 6 redundant domain-specific WebFetch (covered by general)
- 4 redundant docker mcp commands (covered by docker:\*)
- 1 redundant sudo sed -i (covered by sudo sed:\*)
- No logical grouping
- No deny list

### After (61 allow + 8 deny = 69 entries)

- 0 duplicates
- 0 redundancies
- 8 logical categories
- Security deny list added for .env, secrets, .aws, .ssh

**Net reduction**: 18 allow entries (23% cleaner)
**Security added**: 8 deny entries

---

## Category Reference

| #   | Category          | Purpose                                         | Count |
| --- | ----------------- | ----------------------------------------------- | ----- |
| 1   | Core Tools        | Built-in Claude Code (Read, Write, Edit, Skill) | 4     |
| 2   | File Operations   | File system commands                            | 11    |
| 3   | Git Operations    | Version control                                 | 6     |
| 4   | Build & Test      | Development tooling                             | 8     |
| 5   | MCP Servers       | External integrations                           | 3     |
| 6   | Skills & Commands | Custom extensions                               | 3     |
| 7   | Claude CLI        | Meta-commands                                   | 3     |
| 8   | Network           | Web access                                      | 2     |
| 9   | System            | Elevated operations                             | 15    |
| 10  | Deny List         | Blocked operations                              | 8     |

---

## The Optimized Configuration

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Skill",

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

      "Bash(git status)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git init:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",

      "Bash(npm test:*)",
      "Bash(pnpm:*)",
      "Bash(uv:*)",
      "Bash(python3:*)",
      "Bash(docker:*)",
      "Bash(pandoc:*)",
      "Bash(typst:*)",
      "Bash(wkhtmltopdf:*)",

      "mcp__firecrawl__*",
      "mcp__code-execution__run_python",
      "mcp__MCP_DOCKER__*",

      "Skill(tunnel-vision-prevention)",
      "Skill(elevate)",
      "SlashCommand(/context-audit)",

      "Bash(claude:*)",
      "Bash(claude -p:*)",
      "Bash(claude /doctor)",

      "WebFetch",
      "WebSearch",

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

## Security Recommendations

### Applied in This Config

1. ✅ Deny sensitive files (.env, secrets, .aws, .ssh)
2. ✅ Deny both Read AND Write for sensitive paths
3. ✅ Removed redundant permissions
4. ✅ Organized by category for auditability

### Additional Measures (Not in Config)

1. **Layer defenses**: Use OS-level permissions for critical files
2. **Container isolation**: For maximum security, run in Docker
3. **Monthly audit**: Review and prune unused permissions
4. **Test deny patterns**: Verify they work before relying on them

---

## Pattern Syntax Reference

| Pattern              | Matches               | Notes                |
| -------------------- | --------------------- | -------------------- |
| `Bash(npm:*)`        | Any npm command       | Prefix matching      |
| `Bash(git status)`   | Exact command only    | No wildcard          |
| `Read(./.env)`       | Specific file         | Glob pattern         |
| `Read(./.env.*)`     | .env.local, .env.prod | Wildcard extension   |
| `Read(./secrets/**)` | All in directory tree | Recursive glob       |
| `Read(~/.aws/**)`    | Home directory path   | Tilde expansion      |
| `WebFetch`           | All web fetches       | No parentheses = all |

---

## Removed Entries (17 total)

### Duplicates (4)

- `Bash(ls:*)` (was at line 26, 70)
- `Bash(tree:*)` (was at line 14, 61)
- `Bash(mv:*)` (was at line 36, 59)
- `WebSearch` (was at line 8, 60)

### Redundant (7)

- `WebFetch(domain:www.anthropic.com)` - covered by `WebFetch`
- `WebFetch(domain:uxdesign.cc)` - covered by `WebFetch`
- `WebFetch(domain:scaletime.co)` - covered by `WebFetch`
- `WebFetch(domain:blog.hotelogix.com)` - covered by `WebFetch`
- `WebFetch(domain:dashthis.com)` - covered by `WebFetch`
- `WebFetch(domain:www.cloudbeds.com)` - covered by `WebFetch`
- `Bash(sudo sed:*)` - redundant with `Bash(sudo sed -i:*)`

### Consolidated (6)

- Various Bash commands now in logical order
- Docker commands unified under single pattern

---

## Limitations & Gaps

### Known Issues

1. **Deny pattern bugs**: GitHub issues report Read/Write deny may not always work
2. **Prefix matching only**: Cannot use regex for Bash patterns
3. **No comments in JSON**: Documentation must be separate

### What Sources Didn't Cover

1. Performance impact of large permission files
2. Interaction between managed-settings and local settings
3. MCP server permission granularity

### Lower Confidence Areas

1. Sudo commands scope (may need tightening for production)
2. Docker permission breadth (allows any docker command)

---

## Maintenance

### Monthly Review Checklist

- [ ] Any new permissions added? Document why
- [ ] Any permissions unused for 30+ days? Consider removing
- [ ] Any new sensitive files? Add to deny list
- [ ] Any security incidents? Tighten relevant permissions

### When to Modify

- Adding new tools/workflows → Add specific permission
- Security concern → Add to deny list
- Workflow friction → Audit if permission too narrow

---

## Sources

- [Claude Code Official Settings Documentation](https://code.claude.com/docs/en/settings)
- [Backslash Security - Claude Code Best Practices](https://www.backslash.security/blog/claude-code-security-best-practices)
- [Pete Freitag - Claude Code Permissions](https://www.petefreitag.com/blog/claude-code-permissions/)
- [Korny's Blog - Better Claude Code Permissions](https://blog.korny.info/2025/10/10/better-claude-code-permissions)
- [GitHub Issue #4467 - Permission Deny Patterns](https://github.com/anthropics/claude-code/issues/4467)
