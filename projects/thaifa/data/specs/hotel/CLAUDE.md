# Hotel Configuration — CLAUDE.md

> **Domain**: Villa Thaifa room & property configuration
> **Parent context**: `../../CLAUDE.md` (inherits all project rules)

---

## This Directory

| File | Purpose |
|------|---------|
| `rooms.md` | Room inventory, pricing, capacities |
| `reservations.md` | Current reservation state |

---

## Key Rules

| Rule | Description |
|------|-------------|
| **SSOT** | This is the Single Source of Truth for hotel data |
| **No calculation** | Always use exact platform values, never calculate |
| **Backup first** | Before modifying, create backup in `archive/` |

---

## Data Integrity

Before modifying any file in this directory:

1. **Verify source** — Is the data from HotelRunner or Booking.com?
2. **Create baseline** — `cp file.md archive/YYYY/QQ/snapshots/file-YYYY-MM-DD.md`
3. **Validate after** — Cross-check with platform

---

_Hierarchical context for data/specs/hotel/_
