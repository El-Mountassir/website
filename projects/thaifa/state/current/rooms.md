# Current State — Rooms & Pricing

**Last updated**: 2025-12-20
**Source**: HotelRunner (app.hotelrunner.com)
**Booking.com Commission**: 25%

---

## Summary

| Metric | Value |
|--------|-------|
| Total rooms | **12** |
| Room types | **9** |
| Prices configured | **0** (all pending) |
| Pricing formula | `Booking Price = Net margin / 0.75` |

---

## Room ↔ HotelRunner Type Mapping

| Room # | HotelRunner Type | Target Net Margin | Booking Price (calculated) | Palmeraie Market |
|--------|------------------|-------------------|---------------------------|------------------|
| 4, 5 | Double Room Superior | **120€** | **160€** | ✅ €130-180 |
| 1, 3, 8 | Deluxe Triple Room | **150€** | **200€** | ✅ €180-220 |
| 2 | Deluxe Double Room | **150€** | **200€** | ✅ €130-180 |
| 6 | Executive Suite | **180€** | **240€** | ✅ €200-280 |
| 7 | Deluxe King Suite | **330€** | **440€** | ⚠️ Premium |
| 9 | Family Suite | **170€** | **227€** | ✅ €200-280 |
| 10 | Suite | **200€** | **267€** | ✅ €180-250 |
| 11 | Family Suite | **180€** | **240€** | ✅ €200-280 |
| 12 | Presidential Suite | **450€** | **600€** | ⚠️ Very premium |

## Room ↔ HotelRunner Type Mapping - Re-pricing in progress

| Room # | HotelRunner Type | Target Net Margin | Booking Price (calculated) | Palmeraie Market |
|--------|------------------|-------------------|---------------------------|------------------|
| 4 | Double Room Superior | **120€** | **160€** | ✅ €130-180 |
| 5 | Double Room Superior | **120€** | **160€** | ✅ €130-180 |
| 1 | Deluxe Triple Room | **150€** | **200€** | ✅ €180-220 |
| 3 | Deluxe Triple Room | **150€** | **200€** | ✅ €180-220 |
| 8 | Deluxe Triple Room | **150€** | **200€** | ✅ €180-220 |
| 2 | Deluxe Double Room | **150€** | **200€** | ✅ €130-180 |
| 6 | Executive Suite | **180€** | **240€** | ✅ €200-280 |
| 7 | Deluxe King Suite | **330€** | **440€** | ⚠️ Premium |
| 9 | Family Suite | **170€** | **227€** | ✅ €200-280 |
| 10 | Suite | **200€** | **267€** | ✅ €180-250 |
| 11 | Family Suite | **180€** | **240€** | ✅ €200-280 |
| 12 | Presidential Suite | **450€** | **600€** | ⚠️ Very premium |

---

## HotelRunner Configuration

### Interface

- **Navigation**: Calendar → Simple Updates
- **Channel**: Booking.com
- **Platform**: app.hotelrunner.com

### Status by Type

| Type | Rooms | Price configured | Status |
|------|-------|------------------|--------|
| Double Room Superior | 4, 5 | ❌ No | ⏳ Pending |
| Deluxe Triple Room | 1, 3, 8 | ❌ No | ⏳ Pending |
| Deluxe Double Room | 2 | ❌ No | ⏳ Pending |
| Executive Suite | 6 | ❌ No | ⏳ Pending |
| Deluxe King Suite | 7 | ❌ No | ⏳ Pending (premium) |
| Family Suite | 9, 11 | ❌ No | ⏳ Pending |
| Suite | 10 | ❌ No | ⏳ Pending |
| Presidential Suite | 12 | ❌ No | ⏳ Pending (premium) |

---

## Pricing Formula

```
Booking Price = Target Net Margin / (1 - Commission%)
Booking Price = Target Net Margin / 0.75
```

**Example** (Double Room Superior, 120€ margin):

```
Booking Price = 120€ / 0.75 = 160€
Verification: 160€ × 0.75 = 120€ net ✅
```

---

## Premium Decisions Pending

| Room | Type | Calculated price | Omar decision |
|------|------|-----------------|---------------|
| 7 | Deluxe King Suite | **440€** | ⏳ Pending |
| 12 | Presidential Suite | **600€** | ⏳ Pending |

→ These prices are above Palmeraie market. Premium positioning confirmed?

---

## Note

> Booking.com's 25% commission is high (standard = 15%).
> To negotiate mid-term (leverage: volume + good ratings).

---

_Source of truth for rooms and pricing state_
_Updated on 2025-12-20_
