# Patterns — Reusable Approaches

> **What works. How to do things. Proven solutions.**
> Generalized from specific experiences.

---

## Format

```markdown
## Pattern: [Name]

**Author**: [Who documented this]
**Confidence**: [✅🟢🟡🟠⚠️]
**Source**: [Where this was learned]

### Problem
What problem this pattern solves.

### Solution
How to apply the pattern.

### Example
Concrete example of usage.

### Anti-Pattern
What NOT to do.
```

---

## Patterns

### Pattern: Recognition → Action (R→A)

**Author**: Claude Code + Omar
**Confidence**: ✅ Certitude (95%)
**Source**: 2025-12-22 cognitive overload incident

#### Problem
Agent acknowledges something ("Noted", "Good point") but takes no action. Words without follow-through.

#### Solution
After every recognition/acknowledgment:
1. **What should I DO about this?**
2. **Is the action obvious?** → ACT, don't ask
3. **Should future instances know?** → Document NOW

#### Example
```
BAD:  "Noted that you prefer X" → (nothing happens)
GOOD: "Noted that you prefer X" → (update preferences.md) → (apply X going forward)
```

#### Anti-Pattern
Empty acknowledgment without action.

---

### Pattern: Obvious Actions Table

**Author**: Claude Code
**Confidence**: 🟢 Recommandation (90%)
**Source**: 2025-12-22 anti-patterns documentation

#### Problem
Agent asks for permission/direction when the next step is obvious.

#### Solution
Maintain a table of obvious actions that should never require asking:

| Situation | Obvious Action |
|-----------|---------------|
| Task completed | Archive it |
| Changes made | Commit them |
| Learning recognized | Document it |
| Error pattern found | Create guardrail |
| Next step is clear | Continue |

#### Example
```
BAD:  "Mission complete. What should I do next?"
GOOD: (Archive mission) → (Commit changes) → "Mission archived and committed."
```

#### Anti-Pattern
Cognitive overload — asking about obvious things.

---

### Pattern: Confidence-Based Autonomy

**Author**: Omar + Claude
**Confidence**: 🟢 Recommandation (85%)
**Source**: 2025-12-22 architecture discussion

#### Problem
When should agents act autonomously vs. ask for confirmation?

#### Solution
Map confidence level to behavior:

| Confidence | Behavior |
|------------|----------|
| ✅ ≥95% | Act autonomously |
| 🟢 80-94% | Act, inform human |
| 🟡 60-79% | Propose, wait for confirmation (important decisions) |
| 🟠 40-59% | Ask before acting |
| ⚠️ <40% | Don't act, gather information |

#### Example
```
✅ 95%: "File exists" → Just read it
🟢 85%: "This architecture is better" → Implement it, explain why
🟡 70%: "This might fix the bug" → Propose, wait for OK
🟠 50%: "Could be a permissions issue" → Ask before changing permissions
```

#### Anti-Pattern
Acting with low confidence. Asking with high confidence.

---

### Pattern: Split by Access Scope

**Author**: Omar
**Confidence**: 🟢 Recommandation (85%)
**Source**: 2025-12-22 architecture restructuring

#### Problem
Where should files live in a multi-agent system?

#### Solution
Split by who needs access:

| Access Scope | Location |
|--------------|----------|
| One specific agent | `.{agent}/` |
| All agents | `shared/` |
| Human only (private) | `{human}/` |
| Project-specific | `projects/{project}/` |

#### Example
```
Claude Code settings    → .claude/settings.json
Organization decisions  → shared/memory/decisions.md
Omar's personal goals   → omar/context/goals.md
Thaifa project state    → projects/thaifa/state/
```

#### Anti-Pattern
Putting shared resources in agent-specific folders (lock-in).

---

### Pattern: Migrate with Move, Not Copy

**Author**: Omar
**Confidence**: ✅ Certitude (95%)
**Source**: 2025-12-22 migration discussion

#### Problem
Using `cp` for migrations creates duplicates. Original location still has files.

#### Solution
Always use `mv` for migrations:
```bash
mv source/ destination/
```

#### Example
```bash
# BAD: Creates duplicate
cp docs/standards/ shared/standards/

# GOOD: Single source of truth
mv docs/standards/ shared/standards/
```

#### Anti-Pattern
Copying instead of moving during restructuring.

---

### Pattern: Triple-Check Before Deletion

**Author**: Omar
**Confidence**: ✅ Certitude (100%)
**Source**: 2025-12-22 near-miss incident

#### Problem
Deleting something without proper verification can destroy hours of work. Even if human clicks "yes" by accident.

#### Solution
Before ANY deletion (rm, rmdir, git reset, etc.), verify THREE times:

| Check | Question | How to Verify |
|-------|----------|---------------|
| **1. Content** | Is it truly empty/unused? | `ls -la`, `grep`, `find` |
| **2. References** | Are there references that will break? | `grep -r "path/to/thing"` |
| **3. Backup** | Can we recover if wrong? | Git status, commit state |

Only proceed if ALL THREE checks pass with ✅ 100% confidence.

#### Example
```bash
# Before: rmdir docs/standards/

# Check 1: Is it empty?
ls -la docs/standards/  # → Only . and ..  ✅

# Check 2: Are there references?
grep -r "docs/standards" . --include="*.md"  # → Found in CLAUDE.md! ❌

# Check 3: Can we recover?
git status  # → Uncommitted changes ⚠️

# RESULT: Do NOT delete yet. Fix references first.
```

#### Anti-Pattern
Quick deletion without verification. Trusting that human will catch mistakes.

---

### Pattern: Document for the Collective

**Author**: Omar
**Confidence**: ✅ Certitude (95%)
**Source**: Partnership framework

#### Problem
Current instance learns something but future instances lose it.

#### Solution
Before ending any significant interaction, ask:
> "Would my next instance want to know this?"

If YES → Document in shared/memory/ or rules IMMEDIATELY

#### Example
```
Learned: "Omar prefers tables over prose"
Action: Add to shared/user/preferences.md
```

#### Anti-Pattern
Individual vs. collective thinking — learning dies with session.

---
