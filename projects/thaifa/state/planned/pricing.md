# Planned — HotelRunner Pricing Configuration

**Last updated**: 2025-12-20
**Status**: Awaiting configuration
**Interface**: HotelRunner → Calendar → Simple Updates

---

## Prices to Configure

| Type                   | Rooms   | Target margin | Booking Price | Market          | Status             |
| ---------------------- | ------- | ------------- | ------------- | --------------- | ------------------ |
| Double Room Superior   | 4, 5    | 120€          | **160€**      | ✅ €130-180     | ⏳ Pending         |
| Deluxe Triple Room     | 1, 3, 8 | 150€          | **200€**      | ✅ €180-220     | ⏳ Pending         |
| Deluxe Double Room     | 2       | 150€          | **200€**      | ✅ €130-180     | ⏳ Pending         |
| Executive Suite        | 6       | 180€          | **240€**      | ✅ €200-280     | ⏳ Pending         |
| **Deluxe King Suite**  | 7       | 330€          | **440€**      | ⚠️ Premium      | 🟡 Decision needed |
| Family Suite           | 9, 11   | 170-180€      | **227-240€**  | ✅ €200-280     | ⏳ Pending         |
| Suite                  | 10      | 200€          | **267€**      | ✅ €180-250     | ⏳ Pending         |
| **Presidential Suite** | 12      | 450€          | **600€**      | ⚠️ Very premium | 🟡 Decision needed |

---

## Formula

```
Booking Price = Target Net Margin / (1 - Commission%)
Booking Price = Target Net Margin / 0.75  (25% commission)
```

---

## Pending Premium Decisions

### Room 7 — Deluxe King Suite

| Option | Description                               |
| ------ | ----------------------------------------- |
| A      | **440€** — Assumed premium positioning    |
| B      | Adjust toward market (280€ = 210€ margin) |

**Omar decision**: `[WRITE HERE]`

### Room 12 — Presidential Suite

| Option | Description                                 |
| ------ | ------------------------------------------- |
| A      | **600€** — Assumed very premium positioning |
| B      | Adjust toward market (350€ = 262€ margin)   |

**Omar decision**: `[WRITE HERE]`

---

## Execution Method (once validated)

1. Access HotelRunner (app.hotelrunner.com)
2. Navigate to Calendar → Simple Updates
3. For each room type:
   - Select Booking.com channel
   - Enter calculated price
   - Save
4. Verify synchronization with Booking.com

---

_Source of truth for planned pricing configuration_
_Updated on 2025-12-20_
