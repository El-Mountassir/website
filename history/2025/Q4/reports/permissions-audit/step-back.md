# Step-Back Analysis

**Date**: 2025-12-22
**Request**: Audit current permissions and recommend additions (permissive but safe)

## Problem Statement

Ensure Claude Code has maximum productivity access while protecting sensitive data.

## Success Criteria

1. All useful Bash commands allowed without prompts
2. All MCP integrations accessible
3. Sensitive files protected (env, credentials, keys)
4. No friction for common development workflows

## Key Concepts

- **Allow**: No permission prompt, auto-approved
- **Ask**: Prompt each time (default for unknown)
- **Deny**: Blocked, even if user tries to allow
- **Prefix matching**: `command:*` matches command + anything after
- **Gitignore-style paths**: `./`, `~/`, `//` for relative/home/absolute
