# Pending Items

> **Items needing Omar's attention.**
> Agents add items here. Omar processes them.

**Last checked**: —

---

## [2025-12-23] Linear MCP Server Not Enabled

**Priority**: 🟢 Low
**Type**: FYI
**From**: Claude Code

Linear OAuth is configured but the MCP server is not currently running (not in active server list).

**Current state**:

- OAuth: ✅ Authorized
- MCP Server: 🟡 Available but not enabled
- Active servers: memory, notion, sequentialthinking

**To enable**: Run `docker mcp server enable linear` when needed.

**Impact**: No impact if using Linear via web UI. Only matters if wanting to use Linear tools via MCP.

---

## [2025-12-23] Gagliano Brothers Email Response Pending

**Priority**: 🟡 Medium
**Type**: Action Required
**From**: Claude Code

Omar needs to respond to the Gagliano brothers (Robert & Matthew) email about scheduling a meeting for the Cash Depot project.

**Context**:

- Project: Cash Depot (POS system)
- Last email from Robert (Dec 19): "Was busy week. I know Xmas is next Thursday. Are you free maybe Wednesday or perhaps the week after?"
- Google Calendar Booking Page mission is in queue — once completed, the booking URL can be included in the response

**Suggested action**:

1. Execute the Google Calendar Booking Pages mission first
2. Replace `[BOOKING_LINK]` in draft below with actual URL
3. Send response to Gagliano brothers

**Related mission**: `missions/queue/2025-12-23-google-calendar-booking-pages.md`

---

### Draft Email Response

**To**: Robert Gagliano, Matthew Gagliano
**Subject**: Re: Cash Depot Demo Ready

```
Hi Robert, Matthew,

No worries at all — I know this time of year gets hectic!

Both work for me. Pick whichever fits best:

👉 [BOOKING_LINK]

This will let you choose a time that works on your end. I'm generally available late afternoons and evenings.

Enjoy the holidays, and looking forward to catching up!

Best,
Omar
```

**Notes on draft**:
- Warm but professional tone
- Acknowledges busy period (empathy)
- Uses booking link (reduces back-and-forth)
- Short (~50 words) — respects their time

---

<!-- Add new items above this line -->
