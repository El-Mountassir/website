# Pattern Extraction — Thaifa Migration

## Extracted Patterns

### Pattern 1: SSOT State Management

- **Observed In**: Both OLD and NEW paths
- **Underlying Principle**: All authoritative data lives in one location (state/)
- **Structure**: baseline/ → planned/ → execution/ → current/ → historical/
- **Generalization Test**: Would apply in any project? → YES
- **Confidence**: High
- **Action**: Already implemented correctly. KEEP as-is.

### Pattern 2: Language Separation

- **Observed In**: OLD (French), NEW (English)
- **Underlying Principle**: Code/configs in English for AI performance; client comms in French
- **Generalization Test**: Would apply to all projects? → YES
- **Confidence**: High
- **Action**: NEW path is correct. OLD content needs translation where appropriate.

### Pattern 3: Project-Level CLAUDE.md

- **Observed In**: Both paths, but OLD has more operational detail
- **Underlying Principle**: Project context should be self-contained for AI agents
- **What to Include**:
  - Client overview
  - Communication protocols
  - Key systems & access
  - Folder structure (brief)
  - State management pointer
  - Critical deadlines
  - References to detailed docs
- **Generalization Test**: Would apply to all client projects? → YES
- **Confidence**: High
- **Action**: MERGE - take NEW structure, enrich with OLD operational details

### Pattern 4: Report Output Structure

- **Observed In**: OLD uses `.claude/output/YYYY/QQ/type/topic/`
- **Underlying Principle**: Organized, dated, discoverable outputs
- **Conflict**: El-Mountassir uses `history/YYYY/QQ/reports/`
- **Resolution**:
  - Active project work → project-level `.claude/output/`
  - Completed/archived reports → org-level `history/`
- **Generalization Test**: Apply to all projects? → YES with adaptation
- **Confidence**: Medium

### Pattern 5: Task Tracking Gateway

- **Observed In**: OLD uses `tasks/TODOs.md` as mandatory entry point
- **Underlying Principle**: All work must be tracked for continuity
- **Conflict**: El-Mountassir has Linear integration
- **Resolution**:
  - Tactical tasks → Linear (quick, integrated)
  - Multi-step work packages → missions/
  - Project-specific pending items → can stay in TODOs.md temporarily
- **Generalization Test**: → PARTIAL (Linear preferred for org-level)
- **Confidence**: Medium

### Pattern 6: Protected Admin Data

- **Observed In**: OLD has `admin/credentials.md`, `admin/client/PROFILE.md`
- **Underlying Principle**: Sensitive client data isolated and protected
- **Structure**: `admin/` at project level, not exposed
- **Generalization Test**: → YES for all client projects
- **Confidence**: High
- **Action**: Migrate as-is, ensure .gitignore coverage

---

## Anti-Patterns Identified

### Anti-Pattern 1: Duplicate Data

- **Observed**: state/ exists in BOTH locations with different content
- **Problem**: Violates SSOT principle
- **Fix**: Delete OLD state/, keep only NEW (more recent, English)

### Anti-Pattern 2: Path Drift

- **Observed**: Two project locations for same client
- **Problem**: Confusion, potential data loss, inconsistent work
- **Fix**: Complete migration, delete or archive OLD path

### Anti-Pattern 3: Mixed Language

- **Observed**: OLD path has French state files
- **Problem**: Inconsistent with org standards
- **Fix**: Already fixed in NEW path (English)

### Anti-Pattern 4: Scattered Reports

- **Observed**: Reports in `.claude/output/` (OLD), could also be in `history/` (org)
- **Problem**: Unclear where to find past work
- **Fix**: Define clear rule - active work in project, archived in org history

---

## Migration Principles

Based on patterns, the migration should:

1. **Preserve SSOT** - NEW state/ is authoritative
2. **Consolidate admin/** - Bring client data to NEW path
3. **Enrich CLAUDE.md** - Merge OLD operational wisdom into NEW structure
4. **Archive reports** - Move completed reports to org history/
5. **Convert tasks** - P0/P1 to Linear, rest as missions or archive
6. **Delete duplicates** - After verification, remove OLD path

---

## Priority Matrix

| Content | Action | Priority | Risk |
|---------|--------|----------|------|
| state/ in OLD | DELETE (duplicate) | P0 | Low - NEW is authoritative |
| admin/* | MIGRATE to NEW | P0 | Medium - protected data |
| CLAUDE.md | MERGE (enrich NEW) | P0 | Low |
| docs/lessons-learned.md | MIGRATE | P0 | Low |
| tasks/TODOs.md | CONVERT to Linear/missions | P1 | Medium |
| .claude/output/ reports | ARCHIVE to history/ | P1 | Low |
| assets/ | MIGRATE | P1 | Low |
| communication/ | MIGRATE | P1 | Low |
| docs/templates/ | MIGRATE | P2 | Low |
| projects/* (sub-missions) | CONVERT to missions/ | P2 | Medium |
| .backup/ | ARCHIVE or DELETE | P3 | Low |
