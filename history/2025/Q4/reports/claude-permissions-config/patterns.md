# Pattern Extraction

## Extracted Patterns

### Pattern 1: File Placement Matters

- **Observed In**: Official Docs, Configuration Analysis
- **Underlying Principle**: `settings.json` (committed) = team baseline; `settings.local.json` (gitignored) = personal additions
- **Current Problem**: Permissions ONLY in local file → not shared, not visible
- **Generalization Test**: Any team config → Yes
- **Confidence**: High

### Pattern 2: Organic Permission Growth = Technical Debt

- **Observed In**: Current `settings.local.json` (82 entries)
- **Underlying Principle**: Ad-hoc additions during sessions accumulate without cleanup
- **Current Problem**: Many entries are:
  - Duplicative (e.g., multiple git variants)
  - Path-specific (e.g., `/home/omar/Work/El-Mountassir/...`)
  - One-off (e.g., `Bash(done)`, `Bash(while read f)`)
- **Generalization Test**: Any config that grows organically → Yes
- **Confidence**: High

### Pattern 3: Prefix Matching Creates Gaps

- **Observed In**: Official Docs, Community Reports
- **Underlying Principle**: `Bash(git:*)` doesn't match `git` alone, and bypasses are easy
- **Current Problem**: Some patterns may not match intended commands
- **Generalization Test**: Any prefix-based security → Yes
- **Confidence**: High

### Pattern 4: Deny Rules Are Unreliable

- **Observed In**: GitHub Issues #6631, #6699
- **Underlying Principle**: As of certain versions, deny rules were not enforced
- **Current Problem**: Even if fixed in 2.0.75, relying solely on deny is risky
- **Generalization Test**: Any security-critical deny → Yes
- **Confidence**: Medium (may be fixed in 2.0.75)

### Pattern 5: Hooks as Enforcement Mechanism

- **Observed In**: Official Docs, Community Workarounds
- **Underlying Principle**: PreToolUse hooks can block tool calls before execution
- **Current Use**: Only PostToolUse for structure update
- **Generalization Test**: Any enforcement needing reliability → Yes
- **Confidence**: High

---

## Anti-Patterns Identified

| Anti-Pattern | Found In | Problem |
|--------------|----------|---------|
| Permissions only in local file | Current config | Not shared, not documented |
| Path-specific patterns | `settings.local.json` | Non-portable, cluttered |
| Relying on deny for security | Current config | May not be enforced |
| No version control on permissions | Current setup | No history of changes |
| Mixing shared + personal in local | Current config | Should be separated |

---

## Root Cause Analysis

```
Symptom: Claude keeps asking for permissions
       ↓
Why? Permissions in settings.local.json not being respected
       ↓
Why? Possible: Bug in deny enforcement, OR pattern syntax issues, OR file not being read
       ↓
Why? Unknown - need to verify if file is being loaded correctly
       ↓
Root: Need diagnostic to confirm which layer is failing
```

### Diagnostic Questions

1. Is `settings.local.json` being loaded at all?
2. Are the allow patterns matching the commands being executed?
3. Is there a conflict between project and local settings?
4. What specific tools/commands are still asking for permission?
