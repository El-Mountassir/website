# Baseline — Booking.com Promotions (Dec 20, 2025)

**Snapshot date**: 2025-12-20 ~17:00 (before execution)
**Hotel ID**: 5446847
**Source**: Booking.com Extranet

---

## Context

This snapshot captures the state of promotions **BEFORE** executing the cleanup plan.
The promotions listed below were identified as problematic.

---

## Promotions State (8 total)

| # | Promotion | Discount | Stay period | Performance | Planned action |
|---|-----------|----------|-------------|-------------|----------------|
| 1 | Basic Deal | 30% | Dec 8, 2025 → Nov 30, 2026 | -- | P1: Reduce to **10%** |
| 2 | Basic Deal | 33% | Dec 8, 2025 → Nov 30, 2026 | 1 booking, 10 nights, €118.50 | P1: Reduce to **15%** |
| 3 | Basic Deal | **38%** | Dec 8, 2025 → Nov 30, 2026 | 3 bookings, 9 nights, €102.92 | P0: **DEACTIVATE** |
| 4 | Geo-targeted Europe | **10%** | Always active | -- | P0: **DEACTIVATE** |
| 5 | Geo-targeted Morocco | **10%** | Always active | -- | P0: **DEACTIVATE** |
| 6 | Early Booker Deal | **40%** | Dec 8, 2025 → Nov 30, 2026 | -- | P0: **DEACTIVATE** |
| 7 | Late Escape Deal | **43%** | Oct 1, 2025 → Jan 7, 2026 | -- | P0: **DEACTIVATE** |
| 8 | Late Escape Deal | **42%** | Oct 1, 2025 → Jan 7, 2026 | -- | P0: **DEACTIVATE** |

---

## Impact Analysis (before correction)

| Metric | Value | Problem |
|--------|-------|---------|
| Active promotions | **8** | Too many |
| Maximum discount | **43%** | Destructive |
| Promotions > 30% | **5** | Negative margins |
| Max combined impact | **~58%** | Commission + discount |

---

## ROI Impact (Example: 200€ room)

| Scenario | Client price | 25% Commission | Villa Net | vs Target 120€ |
|----------|-------------|----------------|-----------|----------------|
| No promo | 200€ | -50€ | **150€** | +30€ ✅ |
| Basic Deal 38% | 124€ | -31€ | **93€** | **-27€** ❌ |
| Early Booker 40% | 120€ | -30€ | **90€** | **-30€** ❌ |
| Late Escape 43% | 114€ | -28.5€ | **85.5€** | **-34.5€** ❌ |

---

## Note

> This snapshot is a historical reference.
> Current state is in [../current/promotions.md](../current/promotions.md).
> Changes made are in [../execution/2025-12-20/promotions.md](../execution/2025-12-20/promotions.md).

---

_Baseline snapshot created on 2025-12-20_
_Immutable file — do not modify_
