# Source Triangulation

## Sources

### Source 1: Official Claude Code Documentation (claude-code-guide agent)

- **URL**: [Claude Code Settings](https://docs.claude.com/en/docs/claude-code/settings)
- **Type**: Official
- **Key Claims**:
  - Precedence: `managed > local project > shared project > user`
  - Settings are **merged**, not replaced
  - Deny > Ask > Allow (most restrictive wins)
  - Bash patterns use **prefix matching only** (not glob/regex)
  - Wildcard `:*` only works at the **end** of pattern
  - File paths are relative to settings file location, not cwd
- **Evidence Quality**: Strong (official documentation)
- **Potential Bias**: None

### Source 2: GitHub Issues (Community Reports)

- **URLs**:
  - [Issue #6631 - Permission Deny Not Enforced](https://github.com/anthropics/claude-code/issues/6631)
  - [Issue #6699 - Critical Security Bug: deny not enforced](https://github.com/anthropics/claude-code/issues/6699)
  - [Issue #2720 - Permissions Bypass](https://github.com/anthropics/claude-code/issues/2720)
- **Type**: Practitioner (bug reports)
- **Key Claims**:
  - **As of version 1.0.93, deny permissions are NOT FUNCTIONAL**
  - All tested deny rules were ignored
  - Workaround: Use PreToolUse hooks instead
  - Even when denying `Read(**/.env)`, Bash `cat` can still read the file
- **Evidence Quality**: Strong (multiple independent reports)
- **Potential Bias**: Frustrated users may exaggerate, but multiple reports confirm

### Source 3: Practical Guides (ClaudeLog, Gizin, PeteFreitag)

- **URLs**:
  - [ClaudeLog Configuration Guide](https://claudelog.com/configuration/)
  - [Gizin: Running Commands Without Confirmation](https://gizin.co.jp/en/tips/claude-code-permissions-settings)
  - [Understanding Claude Code Permissions](https://www.petefreitag.com/blog/claude-code-permissions/)
- **Type**: Practitioner
- **Key Claims**:
  - `allow` rules work for most tools
  - Permission persistence differs: Bash = permanent, Edit/Write = session only
  - "Yes, don't ask again" choices accumulate over time
  - MCP tools need specific syntax: `mcp__servername__toolname`
- **Evidence Quality**: Moderate (practical experience)
- **Potential Bias**: May be outdated with recent versions

---

## Current Configuration Analysis

### File: `.claude/settings.json`
```json
{
  "hooks": { ... }  // ONLY hooks, NO permissions!
}
```

### File: `.claude/settings.local.json`
```json
{
  "permissions": {
    "allow": [ ...82 entries... ],
    "deny": [ ...8 entries... ]
  }
}
```

**CRITICAL FINDING**: Permissions are ONLY in `settings.local.json`, NOT in `settings.json`!

---

## Convergence Analysis

| Pattern | Official Docs | GitHub Issues | Practitioners | Confidence |
|---------|---------------|---------------|---------------|------------|
| Deny rules may not work | GAP | AGREE | AGREE | **HIGH** (bug confirmed) |
| Allow rules work | AGREE | AGREE | AGREE | **HIGH** |
| Prefix matching limitations | AGREE | AGREE | AGREE | **HIGH** |
| Settings merge, not replace | AGREE | GAP | AGREE | **HIGH** |
| Local > Project precedence | AGREE | GAP | AGREE | **HIGH** |
| PreToolUse hooks as workaround | AGREE | AGREE | AGREE | **HIGH** |

---

## Decision Points (Conflicts to Resolve)

1. **Settings file placement**: Should permissions be in `settings.json` (shared) or `settings.local.json` (local)?
   - Current: Local only
   - Recommendation: Both (shared baseline + local additions)

2. **Deny rules reliability**: Given the bug, should we rely on deny or use hooks?
   - Current: Using deny
   - Recommendation: Use PreToolUse hooks for critical denies

3. **Permission accumulation**: The `settings.local.json` has grown to 82 allow entries, many ad-hoc
   - Current: Organic growth
   - Recommendation: Clean up and standardize
