# Source Triangulation

**Date**: 2025-12-21
**Topic**: Claude Code Permissions Optimization

---

## Sources

### Source 1: Official Claude Code Documentation

- **URL**: https://code.claude.com/docs/en/settings
- **Type**: Official
- **Key Claims**:
  - Three arrays: `allow`, `deny`, `ask`
  - Bash uses prefix matching (NOT regex)
  - File patterns support glob wildcards
  - Processing order: deny → allow → ask
  - Hierarchy: Enterprise > CLI > Local > Project > User
  - `additionalDirectories` for external access
  - Tool-specific patterns: `ToolName(pattern)`
- **Evidence Quality**: Strong (authoritative source)
- **Potential Bias**: None (official documentation)

### Source 2: Backslash Security Blog

- **URL**: https://www.backslash.security/blog/claude-code-security-best-practices
- **Type**: Practitioner (Security)
- **Key Claims**:
  - Three-layer model: Allow (harmless) → Ask (risky) → Deny (nuclear)
  - "Treat Claude like an untrusted but powerful intern"
  - Layer external defenses (Docker, filesystem, secrets management)
  - Monthly configuration audits recommended
  - Never run as root
  - Disable hooks to prevent persistence
  - Keep transcript retention short (7-14 days)
- **Evidence Quality**: Strong (security-focused, practical)
- **Potential Bias**: May be overly cautious for dev workflows

### Source 3: Pete Freitag Developer Blog

- **URL**: https://www.petefreitag.com/blog/claude-code-permissions/
- **Type**: Practitioner (Developer)
- **Key Claims**:
  - Read deny ≠ Write deny (must deny both explicitly)
  - Some bash commands bypass prompts in sandbox
  - Bash can access files outside project directory
  - Container isolation is "only way" for highest security
  - Use dedicated OS accounts for Claude Code
  - Nine CVEs exist for Claude Code
- **Evidence Quality**: Moderate (practical experience, some speculation)
- **Potential Bias**: May overstate security risks

### Source 4: Korny's Blog - Better Permissions

- **URL**: https://blog.korny.info/2025/10/10/better-claude-code-permissions
- **Type**: Practitioner (Alternative approach)
- **Key Claims**:
  - Standard permission syntax has limitations
  - Hooks can provide finer-grained control
  - Regex-based validation possible via hooks
  - Compiled Rust binaries for zero startup overhead
  - "Even simple patterns don't work reliably"
- **Evidence Quality**: Moderate (novel approach, limited adoption)
- **Potential Bias**: Promoting own tool

### Source 5: GitHub Issue #4467 / #6631

- **URL**: https://github.com/anthropics/claude-code/issues/4467
- **Type**: Official (Bug reports)
- **Key Claims**:
  - Deny patterns sometimes not enforced for Read/Write tools
  - Bash deny patterns work correctly
  - Wildcard patterns don't always match as expected
  - Test permissions thoroughly before relying on them
- **Evidence Quality**: Strong (confirmed bugs)
- **Potential Bias**: None

---

## Convergence Analysis

| Pattern | Official | Security | Developer | Hooks | Confidence |
|---------|----------|----------|-----------|-------|------------|
| Three-layer allow/ask/deny | ✓ AGREE | ✓ AGREE | ✓ AGREE | GAP | **High** |
| Prefix matching for Bash | ✓ AGREE | GAP | ✓ AGREE | DISAGREE | **High** |
| Glob patterns for files | ✓ AGREE | GAP | ✓ AGREE | GAP | **High** |
| Deny processed first | ✓ AGREE | ✓ AGREE | ✓ AGREE | ✓ AGREE | **High** |
| Minimal privilege approach | ✓ AGREE | ✓ AGREE | ✓ AGREE | ✓ AGREE | **High** |
| Read deny ≠ Write deny | GAP | GAP | ✓ NEW | GAP | **Medium** |
| Patterns have bugs | GAP | GAP | ✓ AGREE | ✓ AGREE | **Medium** |
| Hooks as alternative | GAP | GAP | GAP | ✓ UNIQUE | **Low** |
| Container for max security | GAP | ✓ AGREE | ✓ AGREE | GAP | **High** |

---

## Decision Points (Disagreements)

### 1. Pattern Reliability
- **Official docs**: Patterns work as documented
- **Developers**: Some patterns unreliable, need testing
- **Resolution**: Use proven patterns, test edge cases

### 2. Hooks vs Permissions
- **Standard approach**: Use built-in permissions
- **Advanced approach**: Custom hooks for granular control
- **Resolution**: Start with standard, hooks if needed later

### 3. Security Level Trade-off
- **High security**: Container isolation, minimal permissions
- **Dev productivity**: Broader permissions for workflow
- **Resolution**: Use `.local.json` for dev, tighter for production

---

## Key Validated Findings

1. **Duplicates are waste** - No benefit, maintenance burden
2. **Organization matters** - Group by category for maintainability
3. **Deny sensitive paths** - .env, secrets, .aws, credentials
4. **Prefix matching for Bash** - Not regex, plan accordingly
5. **Test permissions** - Don't assume patterns work as expected
6. **Deny both Read AND Write** - For sensitive files
7. **Layer defenses** - Permissions alone aren't sufficient
