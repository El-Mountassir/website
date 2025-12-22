# Mission: Fix Claude Code Permissions Configuration

**ID**: M-2025-12-22-01
**Created**: 2025-12-22
**Priority**: HIGH (blocks productivity every session)
**Status**: READY

---

## Context

Investigation report: `history/2025/Q4/reports/claude-permissions-config/final.md`

Omar's instances keep getting permission prompts despite extensive configuration. Root causes:
1. Permissions are ONLY in `settings.local.json` (wrong file)
2. `settings.json` contains ONLY hooks, no permissions
3. 82 accumulated entries with technical debt (path-specific, fragments)
4. Pattern syntax issues (missing `:*` suffixes)

---

## Objective

Restructure Claude Code permission configuration so that:
- Common permissions work WITHOUT prompts
- Configuration is clean, documented, maintainable
- Shared baseline in `settings.json`, personal additions in `settings.local.json`

---

## Success Criteria

- [ ] `settings.json` contains shared permissions + hooks
- [ ] `settings.local.json` contains ONLY personal additions (minimal)
- [ ] Common operations (Read, Write, Edit, git, npm, docker) work without prompts
- [ ] Configuration tested with `/permissions` command
- [ ] Before/after documented

---

## Execution Steps

### Phase 1: Backup (2 min)

```bash
cp .claude/settings.json .claude/settings.json.backup
cp .claude/settings.local.json .claude/settings.local.json.backup
```

### Phase 2: Create New settings.json (10 min)

Merge permissions INTO `settings.json` with hooks:

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Grep",
      "Glob",
      "TodoWrite",
      "Bash(ls:*)",
      "Bash(tree:*)",
      "Bash(find:*)",
      "Bash(cat:*)",
      "Bash(wc:*)",
      "Bash(sort:*)",
      "Bash(mv:*)",
      "Bash(mkdir:*)",
      "Bash(chmod:*)",
      "Bash(du:*)",
      "Bash(xargs:*)",
      "Bash(git:*)",
      "Bash(gh:*)",
      "Bash(npm:*)",
      "Bash(pnpm:*)",
      "Bash(uv:*)",
      "Bash(python3:*)",
      "Bash(docker:*)",
      "Bash(pandoc:*)",
      "Bash(typst:*)",
      "Bash(wkhtmltopdf:*)",
      "Bash(claude:*)",
      "Bash(grep:*)",
      "mcp__firecrawl__*",
      "mcp__code-execution__run_python",
      "mcp__MCP_DOCKER__*",
      "mcp__linear__*",
      "Skill",
      "SlashCommand",
      "WebFetch",
      "WebSearch"
    ],
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
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/update-structure.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Phase 3: Minimal settings.local.json (5 min)

Reset to minimal personal additions:

```json
{
  "permissions": {
    "allow": [
      "Bash(sudo:*)"
    ]
  }
}
```

### Phase 4: Verify (5 min)

1. Run `/permissions` command - verify config loaded
2. Test Read on a file - should NOT prompt
3. Test `git status` - should NOT prompt
4. Test Write/Edit - should NOT prompt (or only once per session)

### Phase 5: Document (3 min)

Add to LESSONS-LEARNED:
- What was wrong
- How it was fixed
- How to maintain going forward

---

## Risks

| Risk | Mitigation |
|------|------------|
| Breaking working config | Backups in Phase 1 |
| Missing permission patterns | Add as discovered |
| Deny still not working | Consider PreToolUse hook |

---

## Notes for Executor

- Pattern `Bash(git:*)` covers ALL git commands (simpler than listing each)
- Removed path-specific patterns (e.g., `Bash(git -C /home/omar/...`)
- Removed shell fragments (`Bash(done)`, `Bash(while read f)`)
- If still prompted for something, add to `settings.local.json` first, then consider moving to shared

---

## Related

- Report: `history/2025/Q4/reports/claude-permissions-config/`
- GitHub Issues: #6631, #6699
