# Docker Platform Account

> **Status**: 🟢 Active
> **Purpose**: Container runtime + MCP Toolkit (core agentic infrastructure)

---

## Account Details

| Field | Value |
|-------|-------|
| **Email** | omar.mountassir@gmail.com |
| **Username** | skrillll |
| **Plan** | Docker Personal (Free) |
| **Docker Desktop** | ✅ v4.54.0 |
| **MCP Toolkit** | ✅ v0.28.0 |

---

## MCP Toolkit

The Docker MCP Toolkit is the **primary integration layer** for Claude Code.

### Status

| Component | Status | Description |
|-----------|--------|-------------|
| **MCP Gateway** | 🟢 Connected | Routes tool calls to servers |
| **Dynamic MCP** | 🟢 Available | On-demand server loading |
| **OAuth** | 🟢 Configured | Authentication for third-party services |
| **Catalog** | 🟢 312 servers | Searchable server marketplace |

### Active Servers

| Server | Purpose | Status |
|--------|---------|--------|
| **memory** | Knowledge graph persistence | 🟢 Active |
| **notion** | Notion API integration | 🟢 Active |
| **sequentialthinking** | Chain-of-thought reasoning | 🟢 Active |

---

## How to Use MCP Servers

### Find Available Servers

```
mcp-find({ query: "search term" })
```

Example: `mcp-find({ query: "cloudflare" })` → Returns 6 Cloudflare MCPs

### Add a Server

```
mcp-add({ name: "server-name", activate: true })
```

- `activate: true` → Tools immediately available
- `activate: false` → Added but not activated

### Configure a Server

```
mcp-config-set({ server: "server-name", key: "config-key", value: "value" })
```

### Execute a Tool

```
mcp-exec({ name: "tool-name", arguments: { ... } })
```

---

## Available Server Categories

| Category | Examples |
|----------|----------|
| **Productivity** | notion, linear, google-calendar, slack |
| **Cloud** | cloudflare-*, aws-*, gcp-* |
| **AI/LLM** | sequentialthinking, memory |
| **Dev Tools** | github, gitlab, docker |
| **Data** | postgres, mysql, mongodb |

---

## OAuth-Enabled Services

Services requiring OAuth authentication:

| Service | OAuth Flow |
|---------|------------|
| **Notion** | ✅ Configured |
| **Linear** | 🟡 Available (not active) |
| **Google** | 🟡 Basic (Calendar) |
| **GitHub** | 🟡 Available |
| **Slack** | 🟡 Available |

---

## Best Practices

| Practice | Description |
|----------|-------------|
| **On-demand loading** | Add servers only when needed |
| **Check availability** | Use `mcp-find` before assuming a server exists |
| **Activate wisely** | Too many active servers = slower responses |

---

## References

- Subscription: `admin/finance/subscriptions/docker.md`
- MCP configs: `configs/system/mcp/`
- Tech Stack: `shared/drafts/2026-tech-stack.md`

---

_Created: 2025-12-23_
