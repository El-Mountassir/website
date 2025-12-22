# Template Management Rule

> **SSOT Principle**: Templates live in `templates/`, standards reference them via hyperlinks.

---

## The Pattern

```
INLINE TEMPLATE (in docs/standards/)  →  EXTRACT to templates/  →  HYPERLINK back
```

| Location | Purpose |
|----------|---------|
| `templates/` | Single Source of Truth for template content |
| `docs/standards/` | Explains WHEN and WHY to use templates |

---

## When to Extract

| Condition | Action |
|-----------|--------|
| Template exists inline in a standard/README | Extract to `templates/` |
| Template is referenced in multiple places | Must be in `templates/` |
| Creating a new reusable structure | Create directly in `templates/` |

---

## How to Extract

1. **Create** the template in appropriate `templates/` subdirectory
2. **Replace** inline content with hyperlink:
   ```markdown
   > **Template location**: [`templates/xxx/template.md`](relative/path/to/template.md)
   ```
3. **Keep** explanation of template purpose/usage in the standard
4. **Update** version/changelog in the standard

---

## Directory Structure

```
templates/
├── README.md              # Index of all templates
├── missions/              # Mission templates
│   └── mission.md
├── projects/              # Project structure templates
│   └── CLAUDE.md
├── state/                 # State management templates
│   └── {category}/README.md
└── commands/              # Slash command templates
    └── slash-command.md
```

---

## Anti-Pattern: Duplication

| BAD | GOOD |
|-----|------|
| Template inline in README.md | Template in templates/, README links to it |
| Same template in 2+ places | One template, multiple hyperlinks |
| Copy-paste between projects | Reference shared template |

---

## Verification

When reviewing standards, check:
- [ ] Are there code blocks that look like templates?
- [ ] Is the same structure defined in multiple places?
- [ ] Could this be reused across projects?

If YES to any → Extract to `templates/`

---

_Rule v1.0.0 — Created 2025-12-22 after mission template extraction_
