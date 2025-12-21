# Templates — El-Mountassir Organization

> Reusable templates for projects, state management, and documentation.

---

## Available Templates

| Template | Location | Purpose |
|----------|----------|---------|
| **State Management** | [state/](state/) | Track project/context state (current, baseline, planned, execution, historical) |
| **Project CLAUDE.md** | [projects/CLAUDE.md](projects/CLAUDE.md) | Project-specific context for Claude Code |

---

## Usage

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

## Related Standards

- [State Management Standard](/docs/standards/state-management.md)

---

_Templates v0.1.0_
_El-Mountassir Organization_
