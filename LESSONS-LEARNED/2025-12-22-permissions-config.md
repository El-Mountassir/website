# 2025-12-22: Claude Code Permissions Configuration Fix

## Problem

Claude Code instances kept asking for permissions despite extensive configuration in `.claude/settings.local.json`.

## Root Cause

**Structural misconfiguration**:
- Permissions were ONLY in `settings.local.json` (82 entries)
- `settings.json` contained ONLY hooks, no permissions
- Many patterns were path-specific or fragment-based (technical debt)

## Solution

1. **Merged** permissions + hooks into `settings.json` (shared, committed)
2. **Simplified** patterns: `Bash(git:*)` instead of 15+ git-specific patterns
3. **Minimized** `settings.local.json` to personal additions only (`sudo:*`)

## Before/After

| Metric | Before | After |
|--------|--------|-------|
| settings.json allow entries | 0 | 40 |
| settings.local.json allow entries | 82 | 1 |
| Path-specific patterns | ~15 | 0 |
| Shell fragments | ~3 | 0 |

## Key Learnings

1. **File placement matters**: Shared config in `settings.json`, personal in `settings.local.json`
2. **Use wildcards**: `Bash(git:*)` covers all git commands
3. **Avoid path-specific patterns**: They're not portable
4. **Clean up organic growth**: Regular maintenance prevents technical debt

## References

- Investigation report: `history/2025/Q4/reports/claude-permissions-config/`
- GitHub Issues: [#6631](https://github.com/anthropics/claude-code/issues/6631), [#6699](https://github.com/anthropics/claude-code/issues/6699)
