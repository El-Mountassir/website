# Omar El Mountassir — State Index

**Last updated**: 2025-12-20 22:30
**Structure**: Centralized SSOT (Single Source of Truth) Management

---

## Quick Navigation

| Category       | Description               | Link                       |
| -------------- | ------------------------- | -------------------------- |
| **Current**    | WHAT IS NOW               | [current/](current/)       |
| **Baseline**   | WHAT WAS (before changes) | [baseline/](baseline/)     |
| **Planned**    | WHAT WILL BE (objectives) | [planned/](planned/)       |
| **Execution**  | WHAT WAS DONE (logs)      | [execution/](execution/)   |
| **Historical** | CHANGES/CORRECTIONS       | [historical/](historical/) |

---

## Current State — Snapshot (Dec 20, 2025)

### Booking.com Promotions

| Metric                   | Value       |
| ------------------------ | ----------- |
| Active promotions        | **5**       |
| Maximum discount         | **15%**     |
| All within optimal range | ✅ (10-15%) |

→ [Details](current/promotions.md)

### Reservations

| Metric                     | Value         |
| -------------------------- | ------------- |
| Confirmed reservations     | **11**        |
| Rooms to assign            | **10**        |
| Revenue forecast           | **€8,008.85** |
| Peak occupancy (Dec 29-31) | **50%**       |

→ [Details](current/reservations.md)

### Rooms

...
→ [Details](current/rooms.md)

### Blockers

...

→ [Details](current/blockers.md)

---

## Conventions

### File Structure

```
state/
├── README.md                    # This index
├── current/                     # Current states (live)
├── baseline/                    # Initial states (before changes)
├── planned/                     # Planned states (objectives)
├── execution/                   # Execution logs by date
└── historical/                  # Complete history + changelogs
```

### Updates

- `current/` files are updated on each state change
- `baseline/` files are dated snapshots (do not modify)
- `execution/` files are logs (append-only)
- `historical/` files are changelogs (append-only)

### Links from Other Documents

All reports and documents point to this folder for state data:

```markdown
> **Source of truth**: [state/current/promotions.md](../state/current/promotions.md)
```

---

_Index created on 2025-12-20_
_Omar El Mountassir — Centralized State Management_
