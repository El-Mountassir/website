# Lesson: Premature Session Closure

**Date**: 2025-12-21
**Category**: Behavioral
**Severity**: High

---

## What Happened

Instance said "session complete" without capturing remaining items:
- Questions structure (Q1-Q5) not captured as missions
- GitHub push not captured as mission
- Items mentioned but not formalized

## Impact

- Items lost between sessions
- User frustration
- Broken continuity
- Trust degradation

## Root Cause

- Focus on immediate tasks over completeness
- No systematic check before closure
- "Session complete" used too liberally
- Assumption that mentioned items are "captured"

## Correction

1. Added HARD STOP rule #6 in CLAUDE.md:
   > "NEVER say 'session complete' without capturing ALL remaining items as missions. Even minor/non-blocking items must be captured."

2. Will implement /end skill with guardrails (Mission: session-commands)

## Prevention

Before ANY session closure:
- [ ] Check for uncaptured items (scan conversation)
- [ ] Create missions for ALL remaining work
- [ ] Verify git status is clean
- [ ] Update CHANGELOG.md if changes made
- [ ] Archive completed missions

## Related

- Mission: `2025-12-21-session-commands` (implements /end guardrails)
- Mission: `2025-12-21-behavior-fix` (this lesson)

---

_Lesson documented by Claude Code | 2025-12-21_
_Archived as part of mission behavior-fix | 2025-12-22_
