# Synthesis Notes

## Confirmed Diagnosis

### Primary Issues Found

1. **Structural Problem**: Permissions are in `settings.local.json` ONLY
   - `settings.json` contains ONLY hooks, no permissions
   - This is backwards: shared baseline should be in `settings.json`

2. **Organic Growth**: 82 allow entries accumulated ad-hoc
   - Many are path-specific (non-portable)
   - Many are duplicative (multiple git variants)
   - Some are fragments (e.g., `Bash(done)`, `Bash(while read f)`)

3. **Potential Bug**: Deny rules may not be enforced reliably
   - Reported in issues #6631, #6699 for version 1.0.93
   - Status in 2.0.75 unclear, but risk remains

### Why Permissions Keep Being Asked

Most likely causes (in order of probability):

1. **Pattern Mismatch**: Command doesn't match prefix pattern
   - Example: `Bash(git status)` is exact, won't match `git status --short`
   - Need `:*` suffix for wildcards

2. **Tool Variants**: Some tools have multiple invocation patterns
   - Example: SubAgents, Task tool, etc. may need separate entries

3. **Session Scope**: Edit/Write permissions reset each session
   - "Don't ask again" is session-only for file modifications

4. **New Commands**: Each new command pattern requires explicit allow

---

## Solution Architecture

### Layer 1: Clean Configuration Structure

```
.claude/
├── settings.json              # SHARED (committed)
│   └── permissions.allow[]    # Baseline permissions for team/project
│   └── permissions.deny[]     # Security denials
│   └── hooks{}                # Automation hooks
│
└── settings.local.json        # LOCAL (gitignored)
    └── permissions.allow[]    # Personal additions only
```

### Layer 2: Clean Permission Categories

| Category | Examples | File |
|----------|----------|------|
| Core tools | Read, Write, Edit, Glob, Grep | settings.json |
| Safe Bash | git, npm, pnpm, docker | settings.json |
| MCP tools | mcp__*, mcp__linear__* | settings.json |
| Security denials | .env, secrets, .aws, .ssh | settings.json |
| Personal additions | User-specific paths/commands | settings.local.json |

### Layer 3: Pattern Fixes

| Current Pattern | Problem | Fixed Pattern |
|-----------------|---------|---------------|
| `Bash(git status)` | Exact only | `Bash(git status:*)` |
| `Bash(done)` | Fragment | Remove (not a command) |
| `Bash(while read f)` | Fragment | Remove (not a command) |
| `Bash(git -C /path...)` | Path-specific | `Bash(git -C:*)` |

---

## Uncertainties

1. **Bug status in 2.0.75**: Are deny rules enforced now?
   - Need to test explicitly

2. **SubAgent permissions**: Do Task tool subagents inherit permissions?
   - Unclear from documentation

3. **MCP wildcard syntax**: Does `mcp__server__*` work?
   - Documentation says yes, need to verify

---

## Failure Modes

| Failure | Cause | Mitigation |
|---------|-------|------------|
| Still asked for permissions | Pattern mismatch | Use `:*` suffix consistently |
| Deny bypassed | Known bug | Use PreToolUse hooks as backup |
| Config not loaded | File location/format | Verify with `/permissions` command |
| Local overrides shared | Precedence rules | Keep shared permissive, local additive |

---

## Recommended Action Plan

### Phase 1: Diagnose (5 min)
1. Run `/permissions` to see what's actually loaded
2. Identify which specific tools/commands still prompt
3. Compare loaded config vs file contents

### Phase 2: Restructure (15 min)
1. Move core permissions to `settings.json`
2. Clean up `settings.local.json` to minimal personal additions
3. Fix pattern syntax (add `:*` where needed)

### Phase 3: Verify (5 min)
1. Test common commands without prompts
2. Verify deny rules work (test reading .env)
3. Document any remaining issues

### Phase 4: Harden (Optional)
1. Add PreToolUse hook for critical denies
2. Create template for future projects
