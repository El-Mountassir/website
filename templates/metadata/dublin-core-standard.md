# Dublin Core Metadata — Standard Template

> Use this template for general documentation files.
> Copy the YAML block below into your markdown file.

---

## Template

```yaml
# Dublin Core Metadata (ISO 15836)
Title: [Document title]
Creator: [Person or org responsible - e.g., "Omar El Mountassir + Claude Code"]
Subject: [Topic keywords, comma-separated]
Description: [Brief summary of the document's purpose]
Date: YYYY-MM-DD
Type: Text
Format: Markdown
Identifier: [Relative path from repo root - e.g., "docs/reference/guides/example.md"]
Language: en
Rights: Internal Team Standard
```

---

## Field Descriptions

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| Title | Yes | Human-readable document name | "Calendar Standards" |
| Creator | Yes | Author(s) | "Omar El Mountassir + Claude Code" |
| Subject | Yes | Keywords for discoverability | "Time Management, Calendar, Appointments" |
| Description | Yes | One-sentence purpose | "Standards for calendar integration and time management" |
| Date | Yes | Creation or last major update | "2025-12-22" |
| Type | Yes | Resource category | "Text" (always for markdown) |
| Format | Yes | File format | "Markdown" (always for .md) |
| Identifier | Yes | Unique path | "docs/standards/time/README.md" |
| Language | Yes | ISO 639-1 code | "en" or "fr" |
| Rights | Yes | Access/usage rights | "Internal Team Standard" |

---

## When to Use

- General documentation
- Reference guides
- How-to articles
- Any standalone markdown document

For standards with versioning and lifecycle tracking, use the **Extended** template instead.

---

## Reference

- [Dublin Core Metadata Initiative](https://www.dublincore.org/)
- [ISO 15836 Standard](https://www.dublincore.org/specifications/dublin-core/dces/)

---

_Template v1.0.0_
