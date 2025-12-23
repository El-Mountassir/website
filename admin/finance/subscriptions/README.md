# Subscriptions Tracker

> **All active subscriptions for El Mountassir operations.**
> Includes both paid and free-tier services.

**Last updated**: 2025-12-23

---

## Summary

### Monthly Costs

| Service        | Plan                          | Monthly | Yearly    | Currency | Status    |
| -------------- | ----------------------------- | ------- | --------- | -------- | --------- |
| **Anthropic**  | Max 20x                       | $200.00 | $2,400.00 | USD      | 🟢 Active |
| **Google**     | Workspace Business + AI Ultra | €17.58  | €210.96   | EUR      | 🟢 Active |
| **Cloudflare** | Free + Domain                 | $0.87   | $10.46    | USD      | 🟢 Active |

### Total Estimated Costs

| Currency | Monthly | Yearly  |
| -------- | ------- | ------- |
| **USD**  | ~$220   | ~$2,640 |
| **EUR**  | ~€202   | ~$2,424 |

> **Note**: Google billed in EUR (€17.58). Total USD estimate uses ~1.09 USD/EUR exchange rate.

---

### Free Tier Services

| Service    | Plan             | Limits                          | Status    |
| ---------- | ---------------- | ------------------------------- | --------- |
| **Vercel** | Hobby (Free)     | 100GB bandwidth, 6000 build min | 🟢 Active |
| **GitHub** | Free             | Unlimited public repos          | 🟢 Active |
| **Linear** | Business (Trial) | Full features until Jan 10      | 🟡 Trial  |
| **Docker** | Personal         | Desktop + MCP Toolkit           | 🟢 Active |

---

## Cost Breakdown

### 2025-2026 Projection

| Category           | Monthly | Yearly    | Notes                       |
| ------------------ | ------- | --------- | --------------------------- |
| **AI/LLM**         | $200.00 | $2,400.00 | Anthropic Max 20x           |
| **Productivity**   | €17.58  | €210.96   | Google Workspace + AI Ultra |
| **Infrastructure** | $0.87   | $10.46    | Cloudflare domain           |

### Per-Service Details

| Service                     | Details                                            |
| --------------------------- | -------------------------------------------------- |
| [Anthropic](anthropic.md)   | Claude Max 20x Plan ($200/mo)                      |
| [Google](google.md)         | Workspace Business Standard + AI Ultra (€17.58/mo) |
| [Cloudflare](cloudflare.md) | Domain + Free Plan ($10.46/year)                   |
| [Vercel](vercel.md)         | Hobby (Free)                                       |
| [GitHub](github.md)         | Free                                               |
| [Linear](linear.md)         | Business Trial (Free until Jan 10)                 |
| [Docker](docker.md)         | Personal (Free)                                    |

---

## Billing Calendar

| Service        | Billing Cycle | Next Due    | Payment Method |
| -------------- | ------------- | ----------- | -------------- |
| **Anthropic**  | Monthly       | —           | Card           |
| **Google**     | Monthly       | Jan 1, 2026 | Card           |
| **Cloudflare** | Yearly        | ~Dec 2026   | Card           |

---

## Upcoming Decisions

| Service    | Decision                            | Deadline            | Impact                    |
| ---------- | ----------------------------------- | ------------------- | ------------------------- |
| **Linear** | Keep Business or fall back to Free? | ⚠️ **Jan 10, 2026** | +$18/mo if kept           |
| **Google** | Discount ends Dec 4, 2026           | Dec 2026            | +€1.62/mo (€14.58→€16.20) |

> **Linear Action**: Evaluate Business features usage by Jan 5, 2026. See [linear.md](linear.md) for criteria.

---

## Discount Tracker

| Service              | Current Discount           | Ends        | Post-Discount Price |
| -------------------- | -------------------------- | ----------- | ------------------- |
| **Google Workspace** | 10% off (€14.58 vs €16.20) | Dec 4, 2026 | €16.20/mo           |

---

## Notes

- USD prices for Anthropic, Cloudflare
- EUR prices for Google Workspace
- Free tier services tracked for awareness and capacity planning
- Platform configs: `configs/system/platforms/`
- MCP configs: `configs/system/mcp/`

---

_admin/finance/subscriptions/README.md v1.1.0_
_Updated: 2025-12-23 — Added Google Workspace Business Standard + AI Ultra as paid subscription_
