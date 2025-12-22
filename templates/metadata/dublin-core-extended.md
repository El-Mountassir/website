# Dublin Core Metadata — Extended Template

> Use this template for **standards** and **managed documents** with versioning and lifecycle.
> Copy the YAML block below into your markdown file.

---

## Template

```yaml
# Dublin Core Metadata (ISO 15836)
Title: [Document title]
Creator: [Person or org responsible]
Subject: [Topic keywords, comma-separated]
Description: [Brief summary]
Date: YYYY-MM-DD
Type: Text
Format: Markdown
Identifier: [Relative path from repo root]
Language: en
Rights: Internal Team Standard

# Extended Metadata (El-Mountassir Standards)
Version: 0.0.1-alpha.0
Status: DRAFT                    # DRAFT | VISION | ACTIVE | DEPRECATED | ARCHIVED
Dimension: [Category]            # Work | Time | State | Project | Reference
Maturity: Declared               # Declared | Tested | Proven
Automation_Target: false         # true if automation planned
Integration_Required: None       # Comma-separated systems (e.g., "Linear, Google Calendar")
```

---

## Core Fields (Dublin Core)

| Field | Required | Description |
|-------|----------|-------------|
| Title | Yes | Human-readable document name |
| Creator | Yes | Author(s) |
| Subject | Yes | Keywords for discoverability |
| Description | Yes | One-sentence purpose |
| Date | Yes | Creation or last major update |
| Type | Yes | "Text" for markdown |
| Format | Yes | "Markdown" |
| Identifier | Yes | Unique path from repo root |
| Language | Yes | ISO 639-1 code |
| Rights | Yes | Access/usage rights |

---

## Extended Fields (Our Standards)

| Field | Required | Description | Values |
|-------|----------|-------------|--------|
| Version | Yes | SemVer 2.0.0 | "0.0.1-alpha.0", "1.0.0-osr.1" |
| Status | Yes | Document lifecycle | DRAFT, VISION, ACTIVE, DEPRECATED, ARCHIVED |
| Dimension | Yes | Category in our taxonomy | Work, Time, State, Project, Reference |
| Maturity | Yes | How proven is this? | Declared (idea), Tested (tried), Proven (works) |
| Automation_Target | No | Is automation planned? | true/false |
| Integration_Required | No | Systems to integrate | "Linear", "Google Calendar", etc. |

---

## Status Values

| Status | Meaning |
|--------|---------|
| `DRAFT` | Work in progress, not ready for use |
| `VISION` | Defined but not yet implemented |
| `ACTIVE` | In use, being followed |
| `DEPRECATED` | Being phased out |
| `ARCHIVED` | No longer maintained |

---

## Maturity Levels

| Level | Meaning | Evidence |
|-------|---------|----------|
| `Declared` | Written down, not yet tested | Document exists |
| `Tested` | Used at least once | Execution log, example |
| `Proven` | Used multiple times successfully | Multiple examples, metrics |

---

## When to Use

- Standards documents (`docs/standards/`)
- Management protocols (missions, time, work)
- Any document requiring version tracking
- Documents with automation/integration roadmap

For simple docs without lifecycle, use the **Standard** template.

---

## Optional: Project-Specific Fields

For complex standards, you may add:

```yaml
# Project-Specific (optional)
Future_Agents: [Agent names that will use this]
Dependencies: [Other standards this depends on]
Supersedes: [Previous document this replaces]
```

---

_Template v1.0.0_
