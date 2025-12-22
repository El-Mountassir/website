# Villa Thaifa — Project Context

# Claude & Omar El Mountassir -> Villa Thaifa

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

### Pattern

```
1. SCOUT    → Explore, verify feasibility
2. REPORT   → Inform client of discoveries
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

> **NEVER ask for information without first reporting what was discovered.**

> **Détails**: Voir `docs/lessons-learned.md`

---

## State Management

**Source of Truth**: `state/`

| State      | Location            |
| ---------- | ------------------- |
| Current    | `state/current/`    |
| Baseline   | `state/baseline/`   |
| Planned    | `state/planned/`    |
| Execution  | `state/execution/`  |
| Historical | `state/historical/` |

> **Structure complète**: Voir `state/README.md`

---

## Key Systems

| System               | Purpose                     | URL                 |
| -------------------- | --------------------------- | ------------------- |
| HotelRunner          | Channel management, pricing | app.hotelrunner.com |
| Booking.com Extranet | Promotions, reservations    | admin.booking.com   |

> **CRITICAL**: Lire `admin/credentials.md` AVANT d'accéder aux plateformes.

| Rule                | Description                                   |
| ------------------- | --------------------------------------------- |
| **Default account** | Use **Admin Omar** (`omar@el-mountassir.com`) |
| **Client account**  | Do NOT use unless explicitly requested        |

---

## Folder Structure

| Folder           | Content                               |
| ---------------- | ------------------------------------- |
| `admin/`         | Credentials, client profile, contacts |
| `state/`         | **Centralized states (SSOT)**         |
| `docs/`          | Documentation, lessons-learned        |
| `.claude/rules/` | Platform operation rules              |

---

## Key Rules

| Rule            | Description                                   |
| --------------- | --------------------------------------------- |
| **Resilience**  | Never abandon silently. Fallback → Escalate.  |
| **Anti-Dodge**  | Install/resolve, don't work around.           |
| **SSOT**        | All state data in `state/`, never duplicate.  |
| **Formal tone** | Vouvoiement mandatory with M. Thaifa          |
| **STOP & ASK**  | When not highly confident → STOP and ASK Omar |

### ⚠️ Platform Operations

> **CRITICAL**: Voir `.claude/rules/platform-operations.md`

4 règles obligatoires:

1. **Confidence-Based Action** — Si < 90% confiance → STOP
2. **Date/Detail Verification** — Répéter les détails avant exécution
3. **Exact System Values** — Jamais calculer, toujours copier
4. **State File Protection** — Demander avant modification destructive

---

## Important References

| Document                               | Purpose                       |
| -------------------------------------- | ----------------------------- |
| `docs/lessons-learned.md`              | Past errors and corrections   |
| `admin/client/PROFILE.md`              | Full client profile           |
| `ROADMAP.md`                           | Strategic phases & milestones |
| `.claude/rules/platform-operations.md` | Platform operation rules      |

> **READ `docs/lessons-learned.md` BEFORE any client action**

---

## Contacts

| Role        | Name               | Contact                 |
| ----------- | ------------------ | ----------------------- |
| Owner       | M. Said Thaifa     | See `admin/contacts.md` |
| Admin       | Omar El Mountassir | omar@el-mountassir.com  |
| HWS Support | Ikram              | See `admin/contacts.md` |

---

_Villa Thaifa Project — El-Mountassir Organization_
