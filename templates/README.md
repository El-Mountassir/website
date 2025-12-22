# Templates — El-Mountassir Organization

> Reusable templates for projects, state management, and documentation.

---

## Available Templates

| Template | Location | Purpose | Standard |
|----------|----------|---------|----------|
| **Mission** | [missions/mission.md](missions/mission.md) | Multi-step work packages (supports 6 types) | [Mission Standard](../docs/standards/management/missions/README.md) |
| **State Management** | [state/](state/) | Track project/context state | [State Standard](../docs/standards/state-management.md) |
| **Project CLAUDE.md** | [projects/CLAUDE.md](projects/CLAUDE.md) | Project-specific context for Claude Code | — |
| **Slash Command** | [commands/slash-command.md](commands/slash-command.md) | Custom Claude Code commands | — |

---

## Mission Types

The unified mission template supports multiple types via HTML comment sections:

| Type | Use Case | Special Sections |
|------|----------|------------------|
| `STANDARD` | General multi-step work | — |
| `ELEVATE` | /elevate outputs | Pipeline Progress, Promotion Decision |
| `FIX` | Bug fixes | Root Cause Analysis |
| `FEATURE` | New features | — |
| `RESEARCH` | Investigation | Pipeline Progress, Promotion Decision |
| `MIGRATION` | System/data migrations | Migration Checklist |

---

## Usage

### New Mission

```bash
# Copy template
cp templates/missions/mission.md missions/drafts/{slug}.md

# Edit and fill in details
# Uncomment type-specific sections as needed
```

### New Project Setup

```bash
# 1. Create project directory
mkdir -p projects/{project-name}/state

# 2. Copy state templates
cp -r templates/state/* projects/{project-name}/state/

# 3. Copy project CLAUDE.md
cp templates/projects/CLAUDE.md projects/{project-name}/

# 4. Customize copied files with project-specific data
```

---

## Template Extraction Rule

> **SSOT Principle**: Templates live here, standards reference via hyperlinks.

See: [`.claude/rules/templates.md`](../.claude/rules/templates.md)

When you find inline templates in documentation:
1. Extract to appropriate `templates/` subdirectory
2. Replace inline content with hyperlink
3. Update this index

---

## Future Candidates

Templates identified but not yet extracted:

| Candidate | Current Location | Priority |
|-----------|------------------|----------|
| Dublin Core (Standard) | 5 docs | Low (metadata, not content) |
| Dublin Core (Extended) | 3 docs | Low (metadata, not content) |

---

## Related Standards

- [Mission Management Standard](../docs/standards/management/missions/README.md)
- [State Management Standard](../docs/standards/state-management.md)

---

_Templates v0.2.0_
_El-Mountassir Organization_
