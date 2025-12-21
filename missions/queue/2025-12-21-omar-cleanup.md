# Mission: Omar Directory Cleanup

```yaml
mission_id: 2025-12-21-omar-cleanup
status: QUEUED
assigned_to: Claude Code
created: 2025-12-21
assigned: 2025-12-21
completed:
archived:
```

---

## Context

The `omar/` directory was initially set up with project-style state management (`omar/context/state/`), which is over-engineered for personal context. Additionally, `omar/model/` and `omar/tools/` are empty placeholders without documented intent.

**Related skill**: `.claude/skills/reorganizing-directories/` — Use checklist before executing.

**Why this matters:**
- Simpler structure = easier for future Claude instances to understand
- Documented empty directories signal future intent
- Removes confusion about what belongs where

**Related discussion:** User confirmed keeping `omar/` separate from `admin/` (identity ≠ functions).

---

## Objectives

- [x] **O1**: ~~Remove over-engineered state management files from git~~ — ALREADY DONE (moved to templates/)
- [ ] **O2**: Document intent for `omar/model/` directory
- [ ] **O3**: Document intent for `omar/tools/` directory
- [ ] **O4**: Verify CLAUDE.md reference to `omar/context/README.md` works
- [ ] **O5**: Commit all changes atomically

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | `omar/context/state/` files removed from git | ✅ | Already moved to templates/ in commit aaf799e |
| 2 | `omar/model/README.md` exists with purpose | ⬜ | File content includes intent |
| 3 | `omar/tools/README.md` exists with purpose | ⬜ | File content includes intent |
| 4 | CLAUDE.md `@omar/context/README.md` works | ⬜ | File still readable |
| 5 | Single atomic commit with all changes | ⬜ | Commit hash |

---

## Constraints

- **Do not delete**: `omar/context/README.md` (referenced by CLAUDE.md)
- **Do not modify**: `omar/context/README.md` content
- **Preserve git history**: Use `git rm` for deletions

---

## Execution Steps

### Step 1: Verify State Files Already Removed

> **NOTE**: State files were already moved to `templates/state/` in a previous commit.
> No action needed here — just verify.

```bash
# Verify state/ directory no longer exists in omar/
ls omar/context/
# Should show only README.md, no state/ subdirectory

# Verify templates have the state structure
ls templates/state/
# Should show README.md, baseline/, current/, etc.
```

### Step 2: Create omar/model/README.md

```markdown
# Omar Model

**Status**: Placeholder
**Purpose**: Future - Omar's mental models, decision frameworks, thinking patterns

---

## Intended Content

When populated, this directory will contain:
- Decision-making frameworks Omar uses
- Mental models for business and life
- Thinking patterns and heuristics

---

_Not yet populated. Keep for future use._
```

### Step 3: Create omar/tools/README.md

```markdown
# Omar Tools

**Status**: Placeholder
**Purpose**: Future - Personal tools, scripts, or utilities specific to Omar

---

## Intended Content

When populated, this directory will contain:
- Personal automation scripts
- Custom tools for Omar's workflow
- Utilities not shared with projects

---

_Not yet populated. Keep for future use._
```

### Step 4: Verify CLAUDE.md Reference

```bash
# Confirm file exists and is readable
cat omar/context/README.md

# Check reference in CLAUDE.md
grep "omar/context" CLAUDE.md
```

### Step 5: Commit

```bash
git add omar/model/README.md omar/tools/README.md
git commit -m "$(cat <<'EOF'
chore(omar): document intent for model/ and tools/ directories

- Add README.md to omar/model/ (future: mental models, frameworks)
- Add README.md to omar/tools/ (future: personal utilities)
- Note: state/ cleanup already done (moved to templates/ in aaf799e)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"
```

### Step 6: Archive Mission

After successful execution:

```bash
mkdir -p history/2025/Q4/missions/omar-cleanup
# Move mission.md, create execution-log.md, deviations.md
rm missions/queue/2025-12-21-omar-cleanup.md
# Update missions/README.md
```

---

## Execution Log

> Append-only. Add entries as work progresses.

### 2025-12-21

- **Queued**: Mission created and placed in queue

---

## Deviations

### 2025-12-21: State files already moved

**Expected**: `git rm omar/context/state/*.md` (6 files)
**Actual**: Files already moved to `templates/state/` in commit aaf799e
**Resolution**: Skip deletion step, verify templates exist instead
**Impact**: None — cleanup already complete, mission simplified

---

## Lessons Learned

_To be filled after execution._

---

_Mission v0.0.1-alpha.0_
