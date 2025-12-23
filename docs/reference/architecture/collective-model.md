# Extended C4 Model for The Collective

> Architecture documentation using C4 with C0 (Collective Context) extension.
> Inspired by [Leeds University Process Documentation Levels](https://deliveringresults.leeds.ac.uk/a-practical-guide-to-documenting-and-designing-processes/process-documentation/levels-of-documentation/).

**Date**: 2025-12-23
**Status**: Active

---

## The Extended Model

Standard C4 starts at "System Context" but ignores **who operates the system and why**. We extend it with **C0 (Collective Context)** as the shared foundation.

| Level  | Name               | Audience   | Description                                          |
| ------ | ------------------ | ---------- | ---------------------------------------------------- |
| **C0** | Collective Context | Everyone   | Organizational foundation (shared with process docs) |
| **C1** | System Context     | Technical  | External integrations and system boundaries          |
| **C2** | Containers         | Technical  | Repos, services, data stores                         |
| **C3** | Components         | Developers | Skills, commands, modules                            |
| **C4** | Code               | Developers | Implementation details (often auto-generated)        |

---

## The Bifurcation Model

C0/L0 is the **shared foundation** for both architecture (C1-C4) and process (L1-L3) documentation:

```text
                    C0 / L0
            (Shared Foundation)
         Collective Context Layer
         ┌─────────────────────┐
         │ Substrate Layer     │
         │ Three-Layer Model   │
         │ NORTH STAR          │
         └──────────┬──────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
    C1-C4                   L1-L3
 (Architecture)          (Processes)
 This document           processes/
```

---

## C0: Collective Context (Foundation)

> **This layer is documented in [architecture.md](architecture.md) Sections 0-1.**
> Do not duplicate — reference the source of truth.

| Section       | Content                                     | Link                                                                                         |
| ------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Section 0** | Substrate Layer (Carbon-Silicon Foundation) | [architecture.md#0-substrate-layer-foundation](architecture.md#0-substrate-layer-foundation) |
| **Section 1** | Three-Layer Model                           | [architecture.md#1-three-layer-model](architecture.md#1-three-layer-model)                   |

### What C0 Contains

| Element        | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| **Actors**     | Omar (51% decision weight), Claude Code, Claude Web, Future Agents         |
| **Governance** | Decision authority matrix, veto rules                                      |
| **Philosophy** | NORTH STAR (outcome), Synergy (mechanism), symbiosis principle, Hard Stops |
| **Boundaries** | What's in scope, what's external                                           |

For **process documentation** (L1-L3), see [processes/](../processes/).

---

## C1: System Context

The highest C4 level shows how The Collective interacts with external systems.

### External Integrations

| System              | Purpose                            | Status          |
| ------------------- | ---------------------------------- | --------------- |
| **Linear**          | Work management (issues, projects) | Connected (MCP) |
| **GitHub**          | Version control, repos             | Connected       |
| **Google Calendar** | Time management, scheduling        | Connected       |
| **Vercel**          | Deployment platform                | Pending         |
| **Cloudflare**      | Domain (el-mountassir.com)         | Owned           |

---

## C2: Containers

High-level technical building blocks within The Collective's system.

| Container          | Type         | Purpose                           |
| ------------------ | ------------ | --------------------------------- |
| **El-Mountassir/** | Mono-repo    | Digital headquarters, org context |
| **thaifa/**        | Project repo | Villa Thaifa client project       |
| **gagliano/**      | Project repo | Gagliano client project           |
| **.claude/**       | Config       | Claude Code configuration         |
| **shared/**        | Data store   | Cross-agent resources             |

---

## C3: Components

Internal components within containers (skills, commands, modules).

### Example: `.claude/` Container

| Component   | Type           | Purpose                             |
| ----------- | -------------- | ----------------------------------- |
| `commands/` | Slash commands | User-invoked actions (/start, /end) |
| `skills/`   | Agent skills   | Reusable capabilities               |
| `agents/`   | Sub-agents     | Specialized task handlers           |
| `rules/`    | Behavior rules | Instance configuration              |

---

## C4: Code

Implementation details — often auto-generated or too granular for documentation.

Refer to source files directly when needed.

---

## Structurizr Implementation

For implementing this model as diagrams-as-code using [Structurizr](https://structurizr.com/).

### Recommended Directory Structure

```text
/project-root/
├── workspace.dsl              # Root — includes everything else
├── model/
│   ├── people.dsl             # Global users/actors
│   └── systems/
│       ├── payment-system.dsl # System A definition
│       └── order-system/      # Complex system with subdirectory
│           ├── containers.dsl # Level 2 (C2) details
│           └── components/    # Level 3 (C3) details
├── docs/                      # ADRs & documentation
└── views/                     # Visual layout definitions
```

### The `!include` Mechanism

| Type          | Syntax                      | Effect                             |
| ------------- | --------------------------- | ---------------------------------- |
| **File**      | `!include model/people.dsl` | Imports specific elements          |
| **Directory** | `!include model/systems/`   | Imports all `.dsl` files in folder |

### Identity Inheritance

Enable `!identifiers hierarchical` for scoped naming:

| Level          | Identifier Example                          |
| -------------- | ------------------------------------------- |
| Root (System)  | `MySystem`                                  |
| Container (C2) | `MySystem.WebApplication`                   |
| Component (C3) | `MySystem.WebApplication.PaymentController` |

### Summary of Inheritance Types

| Inheritance      | Purpose                     | Implementation              |
| ---------------- | --------------------------- | --------------------------- |
| **Directory**    | Team ownership & modularity | `!include <path>`           |
| **Identifier**   | Uniqueness & scoping        | `!identifiers hierarchical` |
| **Relationship** | Reducing clutter            | Implied Relationships       |
| **Visual**       | Consistent branding         | Tag-based styling           |

---

## References

### Official Resources

- [C4 Model Official Site](https://c4model.com/)
- [Structurizr Documentation](https://docs.structurizr.com/)
- [Structurizr DSL](https://docs.structurizr.com/dsl)

### Conceptual Foundation

- [Leeds University - Levels of Documentation](https://deliveringresults.leeds.ac.uk/a-practical-guide-to-documenting-and-designing-processes/process-documentation/levels-of-documentation/)
- [Leeds University - Organisational Context Model (Level 0)](https://deliveringresults.leeds.ac.uk/a-practical-guide-to-documenting-and-designing-processes/process-documentation/levels-of-documentation/organisational-context-model-level-0/)

### Guides & Tutorials

- [C4 Model - Wikipedia](https://en.wikipedia.org/wiki/C4_model)
- [Understanding the C4 Model (Medium)](https://alirezafarokhi.medium.com/understanding-the-c4-model-a-clear-path-to-documenting-software-architecture-88c9ee618a08)
- [C4 Model Architecture with Structurizr (Devōt)](https://devot.team/blog/c4-model)

---

_Created 2025-12-23 — Council Decision: Extended C4 with C0/L0 bifurcation model_
