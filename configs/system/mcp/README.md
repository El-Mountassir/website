# MCP Architecture — El Mountassir

> **Model Context Protocol (MCP)** enables Claude Code to interact with external services.
> This document describes our active MCP infrastructure.

**Last updated**: 2025-12-22

---

## Architecture Overview

```
Claude Code
    │
    └── Docker MCP Toolkit (Unified)
        │
        ├── memory ──────────────────► Knowledge Graph
        │                               └── Persistent relational memory
        │
        ├── notion ──────────────────► Notion API
        │                               └── Omar's Workspace
        │
        ├── sequentialthinking ──────► Structured Reasoning
        │                               └── Multi-step problem decomposition
        │
        ├── linear ──────────────────► Linear API
        │                               └── Work management (issues, projects)
        │
        └── [On-demand: ~180+ servers available]
            ├── github
            ├── playwright
            ├── puppeteer
            └── ...
```

> **Migration completed 2025-12-22**: All MCPs now unified under Docker MCP Toolkit.
> `.mcp.json` is empty — kept for future project-specific overrides if needed.

---

## Active Servers

### Always Active (Core)

| Server               | Tools Access         | Purpose         |
| -------------------- | -------------------- | --------------- |
| `memory`             | `mcp-exec` or direct | Knowledge Graph |
| `notion`             | `mcp-exec` or direct | Documentation   |
| `sequentialthinking` | `mcp-exec` or direct | Reasoning       |
| `linear`             | `mcp-exec`           | Work management |

> **Note**: All tools accessible via `mcp__MCP_DOCKER__mcp-exec` with tool name as parameter.
> Direct tools (memory, notion, sequentialthinking) also available as `mcp__MCP_DOCKER__*`.

### On-Demand (Available in catalog)

| Server                         | Description             | Required Setup        |
| ------------------------------ | ----------------------- | --------------------- |
| `github`                       | GitHub API              | Personal access token |
| `playwright`                   | Browser automation      | None                  |
| `puppeteer`                    | Browser automation      | None                  |
| `arxiv-mcp-server`             | Research papers         | Storage path config   |
| `cloudflare-browser-rendering` | Web fetch + screenshots | None                  |
| ...                            | ~180+ more              | Varies                |

---

## Context Window Strategy

> **Problem**: Each MCP server adds tools to the context window, consuming tokens.

### Solution: Core + On-Demand

```
CORE (Always active)          ON-DEMAND (Add when needed)
─────────────────────         ─────────────────────────────
• memory                      • github (for repo tasks)
• sequentialthinking          • playwright (for browser)
• notion                      • arxiv (for research)
• linear                      • etc.
```

### Token Impact Estimates

| Server             | Approximate Token Cost |
| ------------------ | ---------------------- |
| memory             | ~500-800 tokens        |
| notion             | ~1500-2000 tokens      |
| linear             | ~1500-2000 tokens      |
| sequentialthinking | ~300-500 tokens        |

**Rule**: Keep total MCP overhead under 5000 tokens (< 3% of context).

---

## Managing On-Demand Servers

### Finding servers

```javascript
mcp - find({ query: "github" });
// Returns matching servers from catalog
```

### Adding a server

```javascript
mcp - add({ name: "github", activate: true });
// Adds and activates tools immediately
```

### Configuring secrets

```javascript
mcp -
  config -
  set({
    server: "github",
    key: "personal_access_token",
    value: "ghp_xxx",
  });
```

### Removing a server

```javascript
mcp - remove({ name: "github" });
// Removes from active session
```

---

## Server Details

### Linear (Docker MCP)

**Connection**: OAuth via Docker MCP Toolkit
**Tools access**: `mcp-exec({ name: "list_issues", arguments: {...} })`

| Capability | Key Tools                                     |
| ---------- | --------------------------------------------- |
| Issues     | `list_issues`, `create_issue`, `update_issue` |
| Projects   | `list_projects`, `create_project`             |
| Teams      | `list_teams`, `get_team`                      |
| Documents  | `list_documents`, `create_document`           |

**Teams configured**:

- El Mountassir (main)
- Engineering
- Collaborative Intelligence System

→ See: [linear.md](linear.md)

### Memory (Docker MCP)

**Type**: Knowledge Graph
**Tools prefix**: `mcp__MCP_DOCKER__*`

| Operation | Tools                                                        |
| --------- | ------------------------------------------------------------ |
| Read      | `read_graph`, `open_nodes`, `search_nodes`                   |
| Write     | `create_entities`, `add_observations`, `create_relations`    |
| Delete    | `delete_entities`, `delete_observations`, `delete_relations` |

→ See: [knowledge-graph.md](knowledge-graph.md)

### Notion (Docker MCP)

**Type**: Notion API
**Workspace**: Omar El Mountassir's Space
**Tools prefix**: `mcp__MCP_DOCKER__API-*`

| Operation | Tools                                        |
| --------- | -------------------------------------------- |
| Pages     | `post-page`, `retrieve-a-page`, `patch-page` |
| Databases | `create-a-database`, `post-database-query`   |
| Blocks    | `get-block-children`, `patch-block-children` |
| Search    | `post-search`                                |

→ See: [notion.md](notion.md)

### Sequential Thinking (Docker MCP)

**Type**: Reasoning assistant
**Tool**: `mcp__MCP_DOCKER__sequentialthinking`

Used for complex, multi-step problem decomposition with:

- Thought tracking
- Revision support
- Branch exploration
- Hypothesis verification

---

## Best Practices

1. **Minimize active MCPs**: Only core servers always-on
2. **Add on-demand**: Use `mcp-add` for task-specific servers
3. **Remove when done**: `mcp-remove` to free context
4. **Document additions**: Update this file for new permanent servers
5. **Check duplicates**: Don't enable same server in both systems

---

## Related Files

| File                 | Purpose                        |
| -------------------- | ------------------------------ |
| `.mcp.json`          | Project-level MCP config       |
| `knowledge-graph.md` | Knowledge Graph schema & usage |
| `notion.md`          | Notion workspace & conventions |
| `linear.md`          | Linear teams & workflows       |

---

## Quick Reference

```bash
# Docker MCP CLI (from terminal)
docker mcp server ls              # List enabled servers
docker mcp server enable <name>   # Enable server
docker mcp server disable <name>  # Disable server
docker mcp secret set <key> <val> # Set secret

# MCP Tools (from Claude Code)
mcp-find({ query: "..." })        # Search catalog
mcp-add({ name: "..." })          # Add server
mcp-remove({ name: "..." })       # Remove server
mcp-config-set({ ... })           # Configure server
```

---

_configs/system/mcp/README.md v0.0.2 — Living document_
