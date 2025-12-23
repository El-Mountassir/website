# GitHub Platform Account

> **Status**: 🟢 Active
> **Purpose**: Version control, collaboration, CI/CD

---

## Account Details

| Field                | Value                        |
| -------------------- | ---------------------------- |
| **Personal Account** | github.com/omar-elmountassir |
| **Organization**     | github.com/El-Mountassir     |
| **Email**            | omar@el-mountassir.com       |

---

## CLI Configuration

| Field            | Value                                  |
| ---------------- | -------------------------------------- |
| **CLI**          | GitHub CLI (gh)                        |
| **Auth Status**  | ✅ Logged in                           |
| **Protocol**     | SSH                                    |
| **Account**      | omar-elmountassir                      |
| **Token Scopes** | admin:public_key, gist, read:org, repo |

```bash
# Verify connection
gh auth status
# → ✓ Logged in to github.com account omar-elmountassir
# → Git operations protocol: ssh
```

---

## Organization Access

| Org               | Role  | Access                      |
| ----------------- | ----- | --------------------------- |
| **El-Mountassir** | Owner | Full (via personal account) |

---

## MCP Access (via Docker MCP Toolkit)

| MCP Server | Purpose                         | Status       |
| ---------- | ------------------------------- | ------------ |
| **github** | GitHub API (issues, PRs, repos) | 🟡 On-demand |

> **Access**: `mcp-add({ name: "github", activate: true })`

---

_Created: 2025-12-23_
