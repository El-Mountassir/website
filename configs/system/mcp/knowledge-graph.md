# Knowledge Graph — MCP Integration

> **Persistent relational memory** for cross-session knowledge retention.
> Part of MCP_DOCKER toolkit.

**Last updated**: 2025-12-22

---

## Overview

The Knowledge Graph provides a **persistent, relational memory system** that survives across Claude Code sessions. Unlike ephemeral conversation context, entities and relations stored here remain accessible to future instances.

---

## Current State

### Entities (as of 2025-12-22)

| Name | Type | Key Observations |
|------|------|------------------|
| `DefinitionOfDone` | Principle | Ne JAMAIS déclarer terminé sans vérifier |
| `DisciplineCloture` | Principle | Section 15 CLAUDE.md, cleanup protocol |
| `SkillDefinitionOfDone` | Skill | Location: `.claude/skills/definition-of-done/` |
| `Three I's Framework` | Knowledge | Ingestion, Injection, Inception |
| `El Mountassir Team Structure` | Design | 5-team model proposal |
| `MCP Catalog Reference` | Knowledge | ~180+ MCP servers available |

### Relations

```
DisciplineCloture --IMPLEMENTS--> DefinitionOfDone
SkillDefinitionOfDone --ENFORCES--> DisciplineCloture
Omar --REQUIRES--> DisciplineCloture
Claude --USES--> Three I's Framework
Claude --USES--> MCP Catalog Reference
Symbiosis --CONTAINS--> Three I's Framework
Symbiosis --CONTAINS--> El Mountassir Team Structure
El Mountassir Team Structure --USES--> Three I's Framework
```

---

## Tools Reference

### Reading

| Tool | Purpose |
|------|---------|
| `read_graph` | Get all entities and relations |
| `open_nodes` | Get specific entities by name |
| `search_nodes` | Search by query string |

### Writing

| Tool | Purpose |
|------|---------|
| `create_entities` | Create new entities with observations |
| `add_observations` | Add observations to existing entity |
| `create_relations` | Create relations between entities |

### Deleting

| Tool | Purpose |
|------|---------|
| `delete_entities` | Remove entities and their relations |
| `delete_observations` | Remove specific observations |
| `delete_relations` | Remove specific relations |

---

## Entity Types (Convention)

| Type | Usage |
|------|-------|
| `Principle` | Core rules, values, behaviors |
| `Knowledge` | Frameworks, concepts, learnings |
| `Design` | Architecture, structure proposals |
| `Skill` | Claude Code skills |
| `Person` | People (Omar, clients, etc.) |
| `Project` | Projects (Thaifa, Gagliano, etc.) |
| `Decision` | Important decisions made |
| `Pattern` | Reusable patterns discovered |

---

## Usage Patterns

### Storing a new learning

```javascript
create_entities({
  entities: [{
    name: "LearningName",
    entityType: "Knowledge",
    observations: [
      "Key insight 1",
      "Key insight 2",
      "Source: where it came from"
    ]
  }]
})
```

### Creating a relation

```javascript
create_relations({
  relations: [{
    from: "EntityA",
    to: "EntityB",
    relationType: "USES"  // Active voice
  }]
})
```

### Searching for context

```javascript
search_nodes({ query: "team structure" })
```

---

## Relation Types (Convention)

Use **active voice** for relation types:

| Relation | Meaning |
|----------|---------|
| `USES` | A uses B |
| `IMPLEMENTS` | A implements B |
| `REQUIRES` | A requires B |
| `CONTAINS` | A contains B |
| `ENFORCES` | A enforces B |
| `DEPENDS_ON` | A depends on B |
| `CREATED` | A created B |
| `OWNS` | A owns B |

---

## Best Practices

1. **Check before creating**: Search first to avoid duplicates
2. **Use consistent types**: Follow the entity type conventions
3. **Be specific**: Observations should be actionable
4. **Include sources**: Add provenance for knowledge
5. **Keep relations simple**: One relation per concept
6. **Active voice**: Relations should read naturally (A USES B)

---

## Integration with Local Files

| Use Case | Knowledge Graph | Local Files |
|----------|-----------------|-------------|
| Cross-session memory | Yes | No (unless @-referenced) |
| Version control | No | Yes |
| Complex documents | No | Yes |
| Quick facts/principles | Yes | Overkill |
| Relationships | Yes | Hard to express |

**Rule**: Use Knowledge Graph for **relational facts**, local files for **detailed documents**.

---

_configs/system/mcp/knowledge-graph.md — Living document_
