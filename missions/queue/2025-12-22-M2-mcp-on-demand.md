# Mission: MCP On-Demand Strategy

**ID**: M2-2025-12-22
**Status**: QUEUED
**Priority**: HIGH
**Estimated effort**: 20 min

---

## Objective

Finalize MCP configuration so all servers are 100% on-demand, reducing baseline context from 44k to 0 tokens.

## Context

Current state:
- Linear migrated to Docker MCP (2025-12-22)
- 4 servers active: memory, notion, sequentialthinking, linear
- All load at startup, consuming ~44k tokens

Target state:
- 0 MCP servers at startup
- Add via `mcp-add` when needed
- Remove via `mcp-remove` when done

## Success Criteria

- [ ] Document which MCPs to load for which task types
- [ ] Configure Docker MCP for on-demand activation
- [ ] Test workflow: start clean → add MCP → use → remove
- [ ] Update configs/system/mcp/README.md

## Tasks

1. [ ] Analyze which tasks need which MCPs
2. [ ] Create MCP activation patterns guide
3. [ ] Configure Docker MCP defaults
4. [ ] Test on-demand workflow
5. [ ] Update documentation

## Execution Log

(To be filled during execution)

---

_Created: 2025-12-22_
