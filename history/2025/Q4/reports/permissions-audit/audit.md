# Permissions Audit

**Date**: 2025-12-22
**Current Config**: `.claude/settings.json`

---

## Current State Analysis

### ALLOW (43 entries)

| Category | Patterns | Status |
|----------|----------|--------|
| **Core Tools** | Read, Write, Edit, Grep, Glob, TodoWrite | ✅ Complete |
| **File Ops** | ls, tree, find, cat, wc, sort, mv, mkdir, chmod, du, xargs, grep | ✅ Complete |
| **Version Control** | git, gh | ✅ Complete |
| **Package Managers** | npm, pnpm, uv | ✅ Complete |
| **Runtimes** | python3, docker | ✅ Complete |
| **Tools** | pandoc, typst, wkhtmltopdf, claude, md5sum, getfacl, getent | ✅ Complete |
| **MCP** | firecrawl, code-execution, MCP_DOCKER, linear | ✅ Complete |
| **Web/Skills** | WebFetch, WebSearch, Skill, SlashCommand | ✅ Complete |

### DENY (10 entries)

| Category | Patterns | Status |
|----------|----------|--------|
| **.env files** | Read/Write .env, .env.local, .env.* | ✅ Good |
| **Secrets dir** | Read/Write ./secrets/** | ✅ Good |
| **AWS** | Read ~/.aws/** | ✅ Good |
| **SSH** | Read ~/.ssh/** | ✅ Good |

---

## Gap Analysis

### Missing ALLOW (Productivity)

| Command | Why Needed | Recommendation |
|---------|------------|----------------|
| `Bash(cp:*)` | Copy files | ✅ ADD |
| `Bash(rm:*)` | Remove files (with care) | ⚠️ CONSIDER (risky) |
| `Bash(touch:*)` | Create empty files | ✅ ADD |
| `Bash(head:*)` | View file starts | ✅ ADD |
| `Bash(tail:*)` | View file ends, logs | ✅ ADD |
| `Bash(diff:*)` | Compare files | ✅ ADD |
| `Bash(less:*)` | View files | ✅ ADD (non-interactive fails) |
| `Bash(which:*)` | Find executables | ✅ ADD |
| `Bash(whereis:*)` | Find binaries | ✅ ADD |
| `Bash(file:*)` | Identify file types | ✅ ADD |
| `Bash(stat:*)` | File statistics | ✅ ADD |
| `Bash(ln:*)` | Create symlinks | ✅ ADD |
| `Bash(realpath:*)` | Resolve paths | ✅ ADD |
| `Bash(dirname:*)` | Extract directory | ✅ ADD |
| `Bash(basename:*)` | Extract filename | ✅ ADD |
| `Bash(pwd:*)` | Current directory | ✅ ADD |
| `Bash(echo:*)` | Output text | ✅ ADD |
| `Bash(printf:*)` | Formatted output | ✅ ADD |
| `Bash(date:*)` | Date/time | ✅ ADD |
| `Bash(env:*)` | Environment vars (careful) | ⚠️ CONSIDER |
| `Bash(export:*)` | Set env vars | ❌ SKIP (risky) |
| `Bash(source:*)` | Source scripts | ❌ SKIP (risky) |
| `Bash(tar:*)` | Archive operations | ✅ ADD |
| `Bash(zip:*)` | Compression | ✅ ADD |
| `Bash(unzip:*)` | Decompression | ✅ ADD |
| `Bash(gzip:*)` | Compression | ✅ ADD |
| `Bash(gunzip:*)` | Decompression | ✅ ADD |
| `Bash(curl:*)` | HTTP requests | ⚠️ CONSIDER (WebFetch preferred) |
| `Bash(wget:*)` | HTTP downloads | ⚠️ CONSIDER (WebFetch preferred) |
| `Bash(ssh:*)` | Remote access | ❌ SKIP (security) |
| `Bash(scp:*)` | Secure copy | ❌ SKIP (security) |
| `Bash(rsync:*)` | Sync files | ⚠️ CONSIDER (useful for backups) |
| `Bash(sed:*)` | Stream editing | ✅ ADD (common tool) |
| `Bash(awk:*)` | Text processing | ✅ ADD (common tool) |
| `Bash(cut:*)` | Column extraction | ✅ ADD |
| `Bash(tr:*)` | Character translation | ✅ ADD |
| `Bash(tee:*)` | Pipe + write | ✅ ADD |
| `Bash(id:*)` | User identity | ✅ ADD |
| `Bash(whoami:*)` | Current user | ✅ ADD |
| `Bash(hostname:*)` | System hostname | ✅ ADD |
| `Bash(uname:*)` | System info | ✅ ADD |
| `Bash(ps:*)` | Process list | ✅ ADD |
| `Bash(pgrep:*)` | Process grep | ✅ ADD |
| `Bash(pkill:*)` | Kill processes | ⚠️ CONSIDER (risky) |
| `Bash(kill:*)` | Kill process | ⚠️ CONSIDER (risky) |
| `Bash(killall:*)` | Kill by name | ❌ SKIP (too risky) |
| `Bash(nohup:*)` | Background tasks | ✅ ADD |
| `Bash(timeout:*)` | Command timeout | ✅ ADD |
| `Bash(time:*)` | Measure duration | ✅ ADD |
| `Bash(sleep:*)` | Delay | ✅ ADD |
| `Bash(yes:*)` | Auto-confirm | ❌ SKIP (dangerous) |
| `Bash(node:*)` | Node.js | ✅ ADD |
| `Bash(npx:*)` | npm execute | ✅ ADD |
| `Bash(yarn:*)` | Yarn package manager | ✅ ADD |
| `Bash(pip:*)` | Python packages | ✅ ADD |
| `Bash(pip3:*)` | Python 3 packages | ✅ ADD |
| `Bash(poetry:*)` | Python poetry | ✅ ADD |
| `Bash(cargo:*)` | Rust package manager | ✅ ADD |
| `Bash(go:*)` | Go commands | ✅ ADD |
| `Bash(make:*)` | Build tool | ✅ ADD |
| `Bash(cmake:*)` | CMake build | ✅ ADD |
| `Bash(pytest:*)` | Python tests | ✅ ADD |
| `Bash(jest:*)` | JS tests | ✅ ADD |
| `Bash(vitest:*)` | Vite tests | ✅ ADD |
| `Bash(playwright:*)` | Browser testing | ✅ ADD |
| `Bash(eslint:*)` | JS linting | ✅ ADD |
| `Bash(prettier:*)` | Code formatting | ✅ ADD |
| `Bash(tsc:*)` | TypeScript | ✅ ADD |
| `Bash(bun:*)` | Bun runtime | ✅ ADD |
| `Bash(deno:*)` | Deno runtime | ✅ ADD |

### Missing DENY (Security)

| Pattern | Why Needed | Priority |
|---------|------------|----------|
| `Read(~/.gcp/**)` | GCP credentials | ✅ ADD |
| `Read(~/.azure/**)` | Azure credentials | ✅ ADD |
| `Read(~/.config/gcloud/**)` | GCP config | ✅ ADD |
| `Read(~/.kube/**)` | Kubernetes config | ✅ ADD |
| `Read(~/.docker/config.json)` | Docker credentials | ✅ ADD |
| `Read(./config/credentials.*)` | App credentials | ✅ ADD |
| `Read(./*.pem)` | Private keys | ✅ ADD |
| `Read(./*.key)` | Private keys | ✅ ADD |
| `Write(~/.ssh/**)` | Protect SSH keys | ✅ ADD |
| `Write(~/.aws/**)` | Protect AWS creds | ✅ ADD |

---

## Recommendation Summary

### High-Value ALLOW Additions (35 patterns)

File operations, text processing, system info, dev tools, package managers, testing tools.

### Security DENY Additions (10 patterns)

Cloud credentials (GCP, Azure, Kube), Docker creds, private keys, SSH write protection.

### Skip List (High Risk)

- `rm:*` - Prefer specific patterns or ask
- `export:*`, `source:*` - Env manipulation
- `ssh:*`, `scp:*` - Remote access
- `killall:*`, `yes:*` - Too dangerous
