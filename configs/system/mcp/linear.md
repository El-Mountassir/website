# Linear Integration — MCP

> **Linear API** via Docker MCP Toolkit for work management.

**Last updated**: 2025-12-23

---

## ⚠️ Server Status

| Status | Details |
|--------|---------|
| **MCP Server** | 🟡 **Available but NOT enabled** |
| **OAuth** | ✅ Authorized (2025-12-22) |
| **To enable** | `docker mcp server enable linear` |

> **Note**: Linear OAuth is configured, but the MCP server is not currently running.
> Active servers: memory, notion, sequentialthinking (verified 2025-12-23).

---

## Connection Details

| Property         | Value                                               |
| ---------------- | --------------------------------------------------- |
| **Server**       | `linear` (Docker MCP)                               |
| **Tools access** | `mcp-exec({ name: "tool_name", arguments: {...} })` |
| **Auth**         | OAuth (authorized 2025-12-22)                       |

---

## Teams

| Team                                  | ID                                     | Purpose         |
| ------------------------------------- | -------------------------------------- | --------------- |
| **El Mountassir**                     | `f1eb8951-8649-456f-ac0c-60e44437b78c` | Main org work   |
| **Engineering**                       | `f5eef874-b2d7-4fb2-a92a-467e60673db3` | Technical tasks |
| **Collaborative Intelligence System** | `d49c0a60-9467-4dea-ba5a-09de10feb1d0` | AI/Agent work   |

---

## Available Tools

### Issues

| Tool                  | Purpose                   |
| --------------------- | ------------------------- |
| `list_issues`         | Query issues with filters |
| `get_issue`           | Get issue details by ID   |
| `create_issue`        | Create new issue          |
| `update_issue`        | Modify issue              |
| `list_issue_statuses` | Get available statuses    |
| `list_issue_labels`   | Get available labels      |
| `create_issue_label`  | Create new label          |

### Projects

| Tool                  | Purpose             |
| --------------------- | ------------------- |
| `list_projects`       | Query projects      |
| `get_project`         | Get project details |
| `create_project`      | Create new project  |
| `update_project`      | Modify project      |
| `list_project_labels` | Get project labels  |

### Teams

| Tool         | Purpose          |
| ------------ | ---------------- |
| `list_teams` | Get all teams    |
| `get_team`   | Get team details |

### Cycles (Sprints)

| Tool          | Purpose               |
| ------------- | --------------------- |
| `list_cycles` | Get cycles for a team |

### Documents

| Tool              | Purpose              |
| ----------------- | -------------------- |
| `list_documents`  | Query documents      |
| `get_document`    | Get document content |
| `create_document` | Create new document  |
| `update_document` | Modify document      |

### Users

| Tool         | Purpose             |
| ------------ | ------------------- |
| `list_users` | Get workspace users |
| `get_user`   | Get user details    |

### Comments

| Tool             | Purpose              |
| ---------------- | -------------------- |
| `list_comments`  | Get issue comments   |
| `create_comment` | Add comment to issue |

### Documentation

| Tool                   | Purpose              |
| ---------------------- | -------------------- |
| `search_documentation` | Search Linear's docs |

---

## Usage Patterns

### Creating an issue

```javascript
create_issue({
  title: "Issue title",
  team: "El Mountassir", // Can use name or ID
  description: "Description in Markdown",
  assignee: "me", // Or user ID/email
  labels: ["bug", "priority-high"],
  project: "Project Name",
});
```

### Querying issues

```javascript
list_issues({
  team: "Engineering",
  assignee: "me",
  state: "In Progress",
  limit: 20,
});
```

### Getting my issues

```javascript
list_issues({
  assignee: "me",
});
```

---

## Issue States (by team)

Use `list_issue_statuses({ team: "Team Name" })` to get available states.

Common states:

- Backlog
- Todo
- In Progress
- In Review
- Done
- Canceled

---

## Priority Mapping

| Priority    | Value | Meaning      |
| ----------- | ----- | ------------ |
| No priority | 0     | Unset        |
| Urgent      | 1     | Critical     |
| High        | 2     | Important    |
| Normal      | 3     | Standard     |
| Low         | 4     | Nice to have |

---

## Integration with Missions

| Concept     | Linear  | Local                  |
| ----------- | ------- | ---------------------- |
| **Mission** | Project | `missions/active/*.md` |
| **Task**    | Issue   | N/A (use Linear)       |
| **Sprint**  | Cycle   | N/A (use Linear)       |

**Workflow**:

1. Missions defined in `missions/` folders
2. Tasks tracked in Linear issues
3. Link Linear project to mission via description

---

## Best Practices

1. **Use team names**: More readable than IDs
2. **Assign to "me"**: Works for current user
3. **Labels by name**: No need to lookup IDs
4. **Link to missions**: Reference mission file in issue description
5. **Use projects**: Group related issues

---

## Migration Status

**Migrated 2025-12-22**: Linear now runs via Docker MCP Toolkit.

- `.mcp.json` is empty
- All MCPs unified under Docker management
- OAuth authorization completed

---

_configs/system/mcp/linear.md — Living document_
