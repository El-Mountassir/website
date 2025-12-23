# Booking Pages Configuration

> **SSOT** for Omar's professional booking pages.
> Last updated: 2025-12-23

---

## Active Booking Pages

### El Mountassir Consulting - Client Meeting

| Duration | URL | Use Case |
|----------|-----|----------|
| **30 min** | https://calendar.app.google/i1Q4t8G8Zg328caE8 | Quick sync, follow-up, simple questions |
| **60 min** | https://calendar.app.google/B9jKSicLyqcD8zkw5 | Deep dive, discovery, complex discussions |

---

## Configuration Details

| Setting | Value | Rationale |
|---------|-------|-----------|
| **Account** | omar@el-mountassir.com | Professional Google Workspace |
| **Availability** | Mon-Fri 1:30pm - 7:30pm | Afternoon/evening work hours |
| **Timezone** | Africa/Casablanca (GMT+01:00) | Morocco Time |
| **Buffer time** | 15 minutes | Preparation + notes between meetings |
| **Min notice** | 24 hours | No last-minute bookings |
| **Max advance** | 28 days | Reasonable planning horizon |
| **Conferencing** | Google Meet (auto-generated) | Video call link in confirmation |

---

## Calendar Integration

### Blocking Events

These calendar events affect booking availability:

| Event | Time | Effect |
|-------|------|--------|
| FOCUS - Deep Work Block | 9:30am - 1:30pm | Blocks morning (outside availability anyway) |
| BREAK - Lunch | ~1:00pm - 2:30pm | May block early afternoon slots |
| FOCUS - Night Deep Work | 7:30pm - 11:20pm | Blocks evening (outside availability) |

### Availability Math

| Duration | Last Possible Slot | Calculation |
|----------|-------------------|-------------|
| 30 min | 6:45pm | 6:45 + 30min meeting + 15min buffer = 7:30pm |
| 60 min | 6:30pm | 6:30 + 60min meeting = 7:30pm |

---

## Booking Form Fields

| Field | Required | Purpose |
|-------|----------|---------|
| First name | Yes | Personalization |
| Last name | Yes | Identification |
| Email address | Yes | Confirmation + calendar invite |
| Phone number | No | Backup contact |
| Email verification | Yes | Prevent spam bookings |

---

## For Future Enhancement

| Feature | Status | Notes |
|---------|--------|-------|
| Custom intake questions | Not configured | Could add: "What would you like to discuss?" |
| Company field | Not configured | Could add for B2B context |
| Cancellation policy | Default | Consider adding custom policy |
| Reminder emails | Default | Google sends automatic reminders |

---

## Usage Guidelines

### When to Share Which Link

| Situation | Link to Share |
|-----------|---------------|
| Initial discovery call | 60 min |
| Quick follow-up | 30 min |
| Project kickoff | 60 min |
| Status update | 30 min |
| Complex technical discussion | 60 min |
| Simple question/clarification | 30 min |

### How to Share

```
For scheduling a meeting, please use my booking page:
- 30 minutes: https://calendar.app.google/i1Q4t8G8Zg328caE8
- 60 minutes: https://calendar.app.google/B9jKSicLyqcD8zkw5
```

---

## History

| Date | Change | By |
|------|--------|-----|
| 2025-12-23 | Initial setup, both booking pages created | Omar (manual) + Claude Code (verification) |
| 2025-12-23 | Availability adjusted to 1:30pm-7:30pm | Omar |
| 2025-12-23 | Night Deep Work moved to 7:30pm-11:20pm | Omar |

---

_Created 2025-12-23 as part of Google Calendar Booking Pages mission_
