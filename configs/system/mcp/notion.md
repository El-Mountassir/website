# Notion Integration — MCP

> **Notion API** via Docker MCP Toolkit for collaborative documentation.

**Last updated**: 2025-12-22

---

## Connection Details

| Property | Value |
|----------|-------|
| **Server** | `notion` (Docker MCP) |
| **Tools prefix** | `mcp__MCP_DOCKER__API-*` |
| **Bot name** | Claude Code MCP |
| **Workspace** | Omar El Mountassir's Space |
| **Workspace ID** | `0e69d401-8d1a-810b-a489-0003f162ff47` |

---

## Available Tools

### Pages

| Tool | Purpose |
|------|---------|
| `API-post-page` | Create a new page |
| `API-retrieve-a-page` | Get page by ID |
| `API-patch-page` | Update page properties |
| `API-retrieve-a-page-property` | Get specific property |

### Databases

| Tool | Purpose |
|------|---------|
| `API-create-a-database` | Create new database |
| `API-retrieve-a-database` | Get database schema |
| `API-post-database-query` | Query database entries |
| `API-update-a-database` | Update database schema |

### Blocks (Content)

| Tool | Purpose |
|------|---------|
| `API-retrieve-a-block` | Get block by ID |
| `API-get-block-children` | Get child blocks |
| `API-patch-block-children` | Append content |
| `API-update-a-block` | Modify block |
| `API-delete-a-block` | Remove block |

### Search & Discovery

| Tool | Purpose |
|------|---------|
| `API-post-search` | Search by title |

### Comments

| Tool | Purpose |
|------|---------|
| `API-create-a-comment` | Add comment to page |
| `API-retrieve-a-comment` | Get comments |

### Users

| Tool | Purpose |
|------|---------|
| `API-get-self` | Get bot user info |
| `API-get-user` | Get user by ID |
| `API-get-users` | List all users |

---

## Current State

As of 2025-12-22:
- **Pages**: None found via search (workspace may be empty or access limited)
- **Access level**: Workspace-wide (bot has full access)

---

## Usage Patterns

### Creating a page

```javascript
API-post-page({
  parent: { page_id: "parent-page-uuid" },
  properties: {
    title: [{ text: { content: "Page Title" } }]
  }
})
```

### Searching for content

```javascript
API-post-search({
  query: "search term",
  filter: { property: "object", value: "page" }
})
```

### Adding content to a page

```javascript
API-patch-block-children({
  block_id: "page-or-block-id",
  children: [{
    type: "paragraph",
    paragraph: {
      rich_text: [{ type: "text", text: { content: "Content here" } }]
    }
  }]
})
```

---

## Integration Strategy

### What goes in Notion

| Content Type | Notion | Local Files |
|--------------|--------|-------------|
| Collaborative docs | Yes | No |
| Client-facing | Yes | No |
| Meeting notes | Yes | No |
| Standards/Specs | No | Yes (version controlled) |
| CLAUDE.md files | No | Yes |
| Code documentation | No | Yes |

### Sync considerations

- Notion is **not version controlled**
- Use for **living documents** that need collaboration
- Keep **authoritative specs** in git

---

## Access & Permissions

The bot has access to:
- All pages shared with the integration
- All databases shared with the integration
- Comments on accessible pages

To grant access to new content:
1. Open the page/database in Notion
2. Click "..." menu → "Connections"
3. Add "Claude Code MCP"

---

## Limitations

| Limitation | Impact |
|------------|--------|
| No file uploads | Can't attach files via API |
| Rate limits | ~3 requests/second |
| Block size | Max 2000 characters per block |
| Search scope | Only titles, not content |

---

_configs/system/mcp/notion.md — Living document_
