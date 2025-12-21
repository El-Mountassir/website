# Calendar Standards & Time Management

```yaml
# Dublin Core Metadata
Title: Calendar Standards & Time Management
Creator: Omar El Mountassir + Claude Web
Subject: Time Management, Calendar Configuration, Appointment Standards
Description: Standards for managing time through Google Calendar, optimized for a solo founder orchestrating AI agents
Date: 2025-12-21
Type: Text
Format: Markdown
Identifier: docs/standards/time-management.md
Language: en
Rights: Internal Team Standard

# Extended Metadata
Version: 0.0.2-alpha.0
Status: VISION
Dimension: Time
Maturity: Declared (not yet proven)
Automation_Target: true
Integration_Required: Google Calendar, Linear
Future_Agents: Time Management Agent, Scheduling Agent
```

---

## 1. Philosophy

> **Protect deep work. Batch shallow work. Never context-switch without intention.**

| Principle                     | Implementation                                              | Automation Potential                           |
| ----------------------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| Time is finite                | Default to NO for meetings. Require justification.          | Agent can auto-decline meetings without agenda |
| Context-switching kills       | Batch similar meetings on same days                         | Agent can suggest optimal meeting clustering   |
| Deep work > shallow work      | Protect focus blocks for creation                           | Agent can enforce focus time protection        |
| Async > sync                  | Prefer Loom/email over calls when possible                  | Agent can suggest async alternatives           |
| Energy management             | Match task type to energy level                             | Agent can learn energy patterns over time      |
| Time is the scarcest resource | Every calendar event = commitment of irreplaceable resource | Agent must justify time allocation             |

---

## 2. Appointment Duration Tiers

### 2.1 Tier Overview

| Tier         | Code     | Duration | Color     | Google Calendar Color | Purpose                                 |
| ------------ | -------- | -------- | --------- | --------------------- | --------------------------------------- |
| Micro        | `MICRO`  | 15 min   | 🟡 Yellow | Banana                | Quick sync, single decision             |
| Standard     | `STD`    | 30 min   | 🔵 Blue   | Blueberry             | Focused discussion, status update       |
| Working      | `WORK`   | 60 min   | 🟢 Green  | Sage                  | Deep discussion, problem-solving        |
| Extended     | `EXT`    | 90 min   | 🟠 Orange | Tangerine             | Complex topics, workshops               |
| Client Block | `CLIENT` | 2-4h     | 🔴 Red    | Tomato                | On-site client work, major deliverables |

### 2.2 Tier Details

| Tier                | Best For                                       | Agenda Required            | Buffer After | Max Per Day | Notes                            |
| ------------------- | ---------------------------------------------- | -------------------------- | ------------ | ----------- | -------------------------------- |
| Micro (15 min)      | Quick status, single decision, unblock request | No (but topic clear)       | 0 min        | 4           | If goes over → schedule Standard |
| Standard (30 min)   | Regular check-ins, 2-3 decisions, simple demo  | Light (3 bullets)          | 5 min        | 3           | Default for external calls       |
| Working (60 min)    | Problem-solving, strategy, technical deep-dive | Required                   | 10 min       | 2           | Clear objective mandatory        |
| Extended (90 min)   | Workshops, planning, training, retrospectives  | Required + time allocation | 15 min       | 1           | Break at 45 min recommended      |
| Client Block (2-4h) | On-site work, major deliverables, full audits  | Required + deliverables    | 30 min       | 1           | Include travel + breaks          |

### 2.3 Client Block Composition

| Component            | Duration  | Purpose                       | Example (Thaifa RDV) |
| -------------------- | --------- | ----------------------------- | -------------------- |
| Pre-buffer (travel)  | 30 min    | Travel to location + margin   | 09:30-10:00          |
| Core meeting         | 2-4h      | Actual work/meeting           | 10:00-14:00          |
| Break (if >3h)       | 30-60 min | Lunch/recharge                | Built into core      |
| Post-buffer (travel) | 30 min    | Return + decompression        | 14:00-14:30          |
| **Total block**      | **3-5h**  | **Full calendar reservation** | **09:30-14:30**      |

---

## 3. Daily Structure

### 3.1 Current Reality (Night Owl)

| Time Block  | Duration | Type         | Activity                        | Automation                 |
| ----------- | -------- | ------------ | ------------------------------- | -------------------------- |
| 09:00-10:00 | 1h       | Wake-up      | Morning routine, breakfast      | —                          |
| 10:00-10:30 | 30 min   | Planning     | Review calendar, set priorities | Agent: Daily briefing      |
| 10:30-13:00 | 2.5h     | Deep Work    | Building, coding, creating      | Agent: Block protection    |
| 13:00-14:30 | 1.5h     | Break        | Lunch + recharge                | Agent: No meetings         |
| 14:30-18:00 | 3.5h     | Meeting Zone | Client calls, syncs allowed     | Agent: Schedule here       |
| 18:00-19:00 | 1h       | Execution    | Deliverables, follow-ups        | Agent: Task completion     |
| 19:00-19:30 | 30 min   | Wrap-up      | Capture notes, prep tomorrow    | Agent: Daily summary       |
| 21:00-00:00 | 3h       | Night Focus  | Deep work (high energy period)  | Agent: Optional protection |

### 3.2 Target State (Early Bird Transition)

| Time Block  | Duration | Type         | Activity                            | Transition Priority |
| ----------- | -------- | ------------ | ----------------------------------- | ------------------- |
| 06:00-06:30 | 30 min   | Wake-up      | Morning routine                     | Phase 3             |
| 06:30-09:00 | 2.5h     | Deep Work    | Building, coding, creating (sacred) | Phase 3             |
| 09:00-09:30 | 30 min   | Planning     | Review calendar, set priorities     | Phase 2             |
| 09:30-12:30 | 3h       | Meeting Zone | Client calls, syncs allowed         | Phase 1             |
| 12:30-14:00 | 1.5h     | Break        | Lunch + recharge                    | Phase 1             |
| 14:00-17:00 | 3h       | Execution    | Client work, deliverables           | Phase 1             |
| 17:00-17:30 | 30 min   | Wrap-up      | Capture notes, prep tomorrow        | Phase 1             |
| 22:00-06:00 | 8h       | Sleep        | Recovery                            | Phase 2             |

### 3.3 Transition Plan

| Phase   | Wake Time | Sleep Time | Focus                       | Timeline |
| ------- | --------- | ---------- | --------------------------- | -------- |
| Current | ~09:00    | ~01:00+    | Stabilize current rhythm    | Now      |
| Phase 1 | 09:00     | 00:00      | Consistent bedtime          | Week 1-4 |
| Phase 2 | 08:00     | 23:00      | Earlier wake, earlier sleep | Week 5-8 |
| Phase 3 | 07:00     | 22:30      | Target early bird           | Week 9+  |

---

## 4. Weekly Rhythm

| Day       | Focus                | Meeting Preference | Max Meetings | Deep Work Hours |
| --------- | -------------------- | ------------------ | ------------ | --------------- |
| Monday    | Planning, priorities | Internal only      | 2            | 4h              |
| Tuesday   | Client work          | Client meetings OK | 3            | 2h              |
| Wednesday | Client work          | Client meetings OK | 3            | 2h              |
| Thursday  | Building, learning   | Minimize meetings  | 1            | 5h              |
| Friday    | Wrap-up, admin       | Quick syncs only   | 2            | 3h              |
| Saturday  | OFF                  | Emergency only     | 0            | 0h              |
| Sunday    | OFF                  | Emergency only     | 0            | 0h              |

---

## 5. Buffer System

### 5.1 Post-Meeting Buffers

| Meeting Type      | Buffer Duration | Buffer Purpose          | Calendar Implementation        |
| ----------------- | --------------- | ----------------------- | ------------------------------ |
| Micro (15 min)    | 0 min           | No decompression needed | End at :15, :30, :45, :00      |
| Standard (30 min) | 5 min           | Quick notes capture     | Use "Speedy meetings" (25 min) |
| Working (60 min)  | 10 min          | Notes + mental reset    | Use "Speedy meetings" (50 min) |
| Extended (90 min) | 15 min          | Full decompression      | Schedule 90 min + 15 min block |
| Client Block      | 30 min          | Travel + full reset     | Include in total block         |

### 5.2 Travel Buffers

| Travel Type        | Pre-Buffer | Post-Buffer | Total Addition |
| ------------------ | ---------- | ----------- | -------------- |
| Same building      | 5 min      | 5 min       | 10 min         |
| Same city (nearby) | 15 min     | 15 min      | 30 min         |
| Same city (far)    | 30 min     | 30 min      | 60 min         |
| Different city     | 60+ min    | 60+ min     | 120+ min       |

---

## 6. Meeting Request Evaluation

### 6.1 Decision Matrix

| Question                        | YES Action    | NO Action                  |
| ------------------------------- | ------------- | -------------------------- |
| Can this be async (email/Loom)? | Suggest async | Continue evaluation        |
| Is there a clear objective?     | Continue      | Decline or ask for clarity |
| Is the duration appropriate?    | Continue      | Suggest shorter tier       |
| Does it fit in Meeting Zone?    | Accept        | Propose alternative time   |
| Is decision-maker present?      | Accept        | Decline or reschedule      |
| Is prep shared beforehand?      | Accept        | Request prep first         |

### 6.2 Acceptance Criteria

| Criterion              | Required | Nice to Have | Red Flag                      |
| ---------------------- | -------- | ------------ | ----------------------------- |
| Clear objective        | ✅       | —            | Missing = decline             |
| Appropriate duration   | ✅       | —            | Over-scoped = negotiate       |
| In Meeting Zone        | ✅       | —            | Deep Work conflict = move     |
| Agenda provided        | —        | ✅           | "Let's catch up" = clarify    |
| Decision-maker present | —        | ✅           | Too many attendees = question |
| Async prep shared      | —        | ✅           | No context = request          |

### 6.3 Response Templates

| Situation          | Response Template                                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Declining          | "Thanks for thinking of me. Can we handle this via email/Loom instead? If a call is essential, I have [specific slot] available." |
| Shortening         | "I can do 30 minutes. Let's focus on [specific objective]. If we need more time, we can schedule a follow-up."                    |
| Rescheduling       | "My mornings are reserved for deep work. I have availability [afternoon slots]. Would any of those work?"                         |
| Requesting clarity | "Happy to meet. To make the best use of our time, could you share the main objective and any prep materials?"                     |

---

## 7. Naming Convention

### 7.1 Format

```
[TYPE] - [CLIENT/PROJECT] - [TOPIC/PERSON]
```

### 7.2 Type Prefixes

| Prefix   | Meaning                      | Color     | Example                                    |
| -------- | ---------------------------- | --------- | ------------------------------------------ |
| `RDV`    | Rendez-vous (client meeting) | 🔴 Red    | `RDV - Villa Thaifa - avec M. Said Thaifa` |
| `SYNC`   | Internal sync                | 🔵 Blue   | `SYNC - El Mountassir - Weekly review`     |
| `WORK`   | Working session              | 🟢 Green  | `WORK - Gagliano - Demo prep`              |
| `FOCUS`  | Deep work block              | 🟣 Purple | `FOCUS - Deep work block`                  |
| `ADMIN`  | Administrative task          | ⚫ Gray   | `ADMIN - Invoicing`                        |
| `LEARN`  | Learning/training            | 🟣 Purple | `LEARN - TAC Course`                       |
| `TRAVEL` | Travel time                  | ⚫ Gray   | `TRAVEL - To Villa Thaifa`                 |
| `BREAK`  | Break/lunch                  | ⚫ Gray   | `BREAK - Lunch`                            |

---

## 8. Color Coding System

| Google Color | Color Name | Usage                   | Event Types                |
| ------------ | ---------- | ----------------------- | -------------------------- |
| 🍅 Tomato    | Red        | Critical, client-facing | `RDV`, `CLIENT` blocks     |
| 🍊 Tangerine | Orange     | Extended meetings       | `EXT` tier                 |
| 🍌 Banana    | Yellow     | Quick meetings          | `MICRO` tier               |
| 🌿 Sage      | Green      | Working sessions        | `WORK` tier                |
| 🫐 Blueberry | Blue       | Standard meetings       | `STD` tier, `SYNC`         |
| 🍇 Grape     | Purple     | Learning, focus         | `LEARN`, `FOCUS`           |
| ite Graphite | Gray       | Personal, admin, travel | `ADMIN`, `TRAVEL`, `BREAK` |
| 🌸 Flamingo  | Pink       | Reminders, deadlines    | Tasks, reminders           |

---

## 9. Automation & AI Integration

### 9.1 Current State (Manual)

| Task                      | Current Owner | Pain Point                        |
| ------------------------- | ------------- | --------------------------------- |
| Scheduling meetings       | Omar          | Time-consuming, context-switching |
| Protecting focus time     | Omar          | Often forgotten or overridden     |
| Travel buffer calculation | Omar          | Easy to forget                    |
| Daily planning            | Omar          | Inconsistent                      |
| Meeting prep reminders    | Omar          | Often missed                      |

### 9.2 Target State (AI-Assisted)

| Task                      | Future Owner | Implementation                                 |
| ------------------------- | ------------ | ---------------------------------------------- |
| Scheduling meetings       | Time Agent   | Auto-suggest optimal slots based on rules      |
| Protecting focus time     | Time Agent   | Auto-decline or defer meetings in focus blocks |
| Travel buffer calculation | Time Agent   | Auto-add buffers based on location             |
| Daily planning            | Time Agent   | Morning briefing with priorities               |
| Meeting prep reminders    | Time Agent   | 24h and 1h reminders with context              |

### 9.3 Integration Requirements

| System            | Access Level | Purpose                        |
| ----------------- | ------------ | ------------------------------ |
| Google Calendar   | Read/Write   | Event management, availability |
| Linear            | Read/Write   | Task → Calendar sync           |
| Email (Gmail)     | Read         | Meeting request parsing        |
| Location services | Read         | Travel time calculation        |

### 9.4 Automation Triggers

| Trigger                      | Action                                   | Agent Responsibility |
| ---------------------------- | ---------------------------------------- | -------------------- |
| New Linear task created      | Suggest calendar block                   | Time Agent           |
| Meeting request received     | Evaluate against rules, suggest response | Time Agent           |
| Focus block approaching      | Send prep reminder, activate DND         | Time Agent           |
| Meeting ending               | Prompt for notes capture                 | Time Agent           |
| Daily wrap-up time           | Generate summary, prep tomorrow          | Time Agent           |
| Work session with AI started | Reserve calendar block                   | Time Agent           |

### 9.5 Council-AI Work Session Protocol

| Step | Action                          | Calendar Impact                   |
| ---- | ------------------------------- | --------------------------------- |
| 1    | Omar initiates work with Claude | Time Agent creates `WORK` block   |
| 2    | Estimated duration set          | Block sized appropriately         |
| 3    | Work in progress                | Block protected from interruption |
| 4    | Work complete                   | Block closed, notes prompted      |
| 5    | Follow-up needed                | New block scheduled               |

---

## 10. Implementation Checklist

| Task                                        | Priority | Status  | Owner       | Automation         |
| ------------------------------------------- | -------- | ------- | ----------- | ------------------ |
| Set up "Speedy meetings" in Google Calendar | P1       | ⬜ TODO | Omar        | Manual             |
| Create recurring "Deep Work" blocks         | P1       | ⬜ TODO | Omar        | Future: Time Agent |
| Create recurring "Lunch" blocks             | P1       | ⬜ TODO | Omar        | Future: Time Agent |
| Set default meeting duration to 30 min      | P1       | ⬜ TODO | Omar        | Manual             |
| Apply color coding to existing events       | P2       | ⬜ TODO | Omar        | Manual             |
| Review and clean up recurring meetings      | P2       | ⬜ TODO | Omar        | Manual             |
| Share availability preferences with clients | P2       | ⬜ TODO | Omar        | Manual             |
| Document current sleep/wake patterns        | P2       | ⬜ TODO | Omar        | Future: Time Agent |
| Set up Linear ↔ Calendar integration        | P3       | ⬜ TODO | Claude Code | Automation         |
| Create Time Agent specification             | P3       | ⬜ TODO | Council     | Future             |

---

## Changelog

| Version       | Date       | Changes                                                                                                                           |
| ------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0.0.2-alpha.0 | 2025-12-21 | Added Dimension metadata, realistic daily structure (night owl), transition plan, travel buffers, automation section, more tables |
| 0.0.1-alpha.0 | 2025-12-21 | Initial draft                                                                                                                     |

---

_Status: VISION — Declared standards to be tested and refined through practice. Future automation by Time Management Agent._
