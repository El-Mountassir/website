# Villa Thaifa — Project Context

> **Project-specific context for Villa Thaifa management.**

---

## Project Overview

| Attribute      | Value                             |
| -------------- | --------------------------------- |
| **Client**     | M. Said Thaifa (78 years old)     |
| **Type**       | Hospitality / Property Management |
| **Location**   | Palmeraie, Marrakech, Morocco     |
| **Channels**   | Booking.com (via HotelRunner)     |
| **Rooms**      | 12                                |
| **Commission** | 25% Booking.com                   |
| **Admin**      | Omar El Mountassir                |

---

## Communication Protocol

| Audience  | Register          | Language       |
| --------- | ----------------- | -------------- |
| M. Thaifa | **Formal (vous)** | French         |
| Guests    | Formal            | French/English |

### Communication Pattern

```
1. SCOUT    → Explore, verify feasibility
2. REPORT   → Inform client of discoveries
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

> **NEVER ask for information without first reporting what was discovered.**

### WhatsApp Rules

| Situation                | Approach               |
| ------------------------ | ---------------------- |
| First message of day     | Greeting + signature   |
| Follow-up (same thread)  | Direct, no re-greeting |
| Important/formal message | Greeting + signature   |

---

## State Management

**Source of Truth**: [state/](state/)

| State              | Location                               |
| ------------------ | -------------------------------------- |
| Current state      | [state/current/](state/current/)       |
| Baseline snapshots | [state/baseline/](state/baseline/)     |
| Planned actions    | [state/planned/](state/planned/)       |
| Execution logs     | [state/execution/](state/execution/)   |
| Historical records | [state/historical/](state/historical/) |

---

## Key Systems

| System               | Purpose                     | URL                 |
| -------------------- | --------------------------- | ------------------- |
| HotelRunner          | Channel management, pricing | app.hotelrunner.com |
| Booking.com Extranet | Promotions, reservations    | admin.booking.com   |

### Credentials

> **READ `admin/credentials.md` BEFORE accessing platforms**

| Rule                | Description                                   |
| ------------------- | --------------------------------------------- |
| **Default account** | Use **Admin Omar** (`omar@el-mountassir.com`) |
| **Client account**  | Do NOT use unless explicitly requested        |
| **Reason**          | Avoid disturbing client with notifications    |

---

## Folder Structure

| Folder   | Content                               |
| -------- | ------------------------------------- |
| `admin/` | Credentials, client profile, contacts |
| `state/` | **Centralized states (SSOT)**         |
| `docs/`  | Documentation, lessons-learned        |

---

## Important References

| Document                    | Purpose                         |
| --------------------------- | ------------------------------- |
| `docs/lessons-learned.md`   | Past errors and corrections     |
| `admin/client/PROFILE.md`   | Full client profile (412 lines) |
| `state/current/blockers.md` | Active blockers                 |

> **Read `docs/lessons-learned.md` BEFORE any client action**

---

## Key Rules

| Rule            | Description                                  |
| --------------- | -------------------------------------------- |
| **Resilience**  | Never abandon silently. Fallback → Escalate. |
| **Anti-Dodge**  | Install/resolve, don't work around.          |
| **SSOT**        | All state data in `state/`, never duplicate. |
| **Formal tone** | Vouvoiement mandatory with M. Thaifa         |

---

## Contacts

| Role  | Name               | Contact                 |
| ----- | ------------------ | ----------------------- |
| Owner | M. Said Thaifa     | See `admin/contacts.md` |
| Admin | Omar El Mountassir | omar@el-mountassir.com  |

---

_Villa Thaifa Project — El-Mountassir Organization_
