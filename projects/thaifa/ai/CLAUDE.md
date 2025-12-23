# AI Systems — CLAUDE.md

> **Domain**: Agentic AI infrastructure for Villa Thaifa
> **Parent context**: `../CLAUDE.md` (inherits all project rules)

---

## Directory Structure

```
ai/
├── agentic/        # Agentic AI core
│   └── core/       # The "Core Four"
│       ├── contexts/   # Domain contexts
│       ├── models/     # Agent configurations
│       ├── prompts/    # System/user prompts
│       └── tools/      # Tool definitions
├── rag/            # Retrieval-Augmented Generation
│   ├── pipelines/  # RAG pipelines
│   ├── embeddings/ # Embedding configs
│   └── chunking/   # Document chunking
├── knowledge/      # Knowledge graphs
│   ├── graphs/     # Graph definitions
│   ├── entities/   # Entity types
│   └── relationships/ # Relationship types
├── memory/         # Persistent memory
│   ├── vector/     # Vector stores
│   └── strategies/ # Memory strategies
└── analytics/      # Business intelligence
    ├── dashboards/ # Dashboard configs
    └── insights/   # Analytical reports
```

---

## The Core Four (Agentic)

| Component | Purpose |
|-----------|---------|
| **Contexts** | Domain-specific knowledge |
| **Models** | Agent behavior configurations |
| **Prompts** | System and user prompts |
| **Tools** | HotelRunner, Booking.com, Communication |

---

## Future Development

This infrastructure supports:
- Autonomous reservation management
- Dynamic pricing decisions
- Guest communication automation
- Performance analytics

---

_Hierarchical context for ai/_
