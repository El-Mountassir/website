# Work Management Protocols

> Extracted from `project-standards.md` for consistency with `missions/` and `time/`.

---

**We** use a characteristic-based framework to select and configure our project management workflows. Instead of relying on industry labels (e.g., "Marketing Template"), **we** analyze **Work Type**, **Iteration Frequency**, and **Constraints** to determine the optimal structure.

## 1. Core Selection Framework

**We** categorize every initiative through a 3-step process:

### Step 1: Work Type

| Type        | Characteristics                     | Default Template Family      |
| ----------- | ----------------------------------- | ---------------------------- |
| **Project** | Has start/end, produces deliverable | Project Mgmt or Software Dev |
| **Process** | Recurring, optimization-focused     | Operations (Kanban)          |
| **Request** | Reactive, queue-based, SLA-driven   | IT Support / Service Desk    |

**Test**: Does your work have a natural "done" state (project), or does it flow continuously (process/request)?

### Step 2: Iteration Frequency

| Frequency        | Description                 | Implication                   |
| ---------------- | --------------------------- | ----------------------------- |
| **Daily/Weekly** | Priorities shift constantly | Kanban (continuous flow)      |
| **Bi-weekly**    | Regular planning cycles     | Scrum/Agile (sprint-based)    |
| **Stable**       | Requirements fixed upfront  | Waterfall (phases/milestones) |

**Test**: If something urgent came in today, would you restructure this week's work?

### Step 3: Constraints (Refinement)

| Constraint           | Adjustment                                                          |
| -------------------- | ------------------------------------------------------------------- |
| **Compliance/Audit** | Add Waterfall-style documentation trail, even if execution is Agile |
| **Multi-department** | Add cross-team visibility (Kanban boards)                           |
| **Client-facing**    | Add milestone tracking, deliverable focus                           |
| **Creative cycles**  | Add review/approval stages                                          |

---

## 2. Definition of Ready (DoR)

**We** verify these criteria before starting any task (based on the INVEST framework):

| Criterion       | Check                                       |
| --------------- | ------------------------------------------- |
| **Independent** | No external blockers; dependencies resolved |
| **Valuable**    | Clear stakeholder value articulated         |
| **Estimable**   | Scope understood enough to estimate         |
| **Small**       | Completable within time-box (sprint/day)    |
| **Testable**    | Acceptance criteria defined                 |

### DoR by Work Type

| Work Type   | Additional DoR Criteria                                           |
| ----------- | ----------------------------------------------------------------- |
| **Project** | Goals, scope, acceptance criteria, dependencies mapped            |
| **Process** | Process flow clear, inputs defined, success metrics known         |
| **Request** | Request is actionable, urgency/impact clear, resources identified |

---

## 3. Definition of Done (DoD)

**We** verify these criteria before marking work complete:

| Category          | Check                                               |
| ----------------- | --------------------------------------------------- |
| **Clarity**       | All tasks completed, acceptance criteria verified   |
| **Quality**       | Meets defined standards (format, content, accuracy) |
| **Documentation** | Relevant outputs captured and attached              |
| **Review**        | Peer/stakeholder review conducted (if required)     |
| **Handoff**       | Ready for next phase or delivery                    |

### DoD by Work Type

| Work Type   | DoD Criteria                                                     |
| ----------- | ---------------------------------------------------------------- |
| **Project** | Deliverables complete, quality gate passed, stakeholder sign-off |
| **Process** | Process executed per standard, outputs verified, documented      |
| **Request** | Request resolved, confirmation from requestor, closed in system  |

### DoD by Deliverable Type (Examples)

| Deliverable Type           | DoD Checklist                                        |
| -------------------------- | ---------------------------------------------------- |
| **Messaging (Copy-Paste)** | TXT format, tone appropriate, recipient-ready        |
| **Formal Report (PDF)**    | Professional styling, structured sections, metadata  |
| **Internal Doc (MD)**      | Dublin Core metadata, proper hierarchy, correct path |

---

## 4. Task Lifecycle

**We** track tasks through these states:

```
[Ready] → [In Progress] → [Review] → [Done]
    ↓           ↓
[Blocked] ← [Blocked]
    ↓
[Escalated]
```

| State       | Entry Criteria              | Exit Criteria                 |
| ----------- | --------------------------- | ----------------------------- |
| Ready       | DoR met                     | Work started                  |
| In Progress | Work started                | Work complete OR blocked      |
| Blocked     | Dependency/issue identified | Blocker resolved OR escalated |
| Review      | Work complete               | Approved OR revision needed   |
| Done        | DoD met + approved          | —                             |
| Escalated   | All alternatives exhausted  | Resolution from escalation    |

### Priority Matrix

| Priority | MoSCoW | Eisenhower       | Action            |
| -------- | ------ | ---------------- | ----------------- |
| P0       | Must   | Urgent+Important | Do immediately    |
| P1       | Must   | Important        | Do today          |
| P2       | Should | Urgent           | Delegate/schedule |
| P3       | Could  | Neither          | Batch for later   |
| P4       | Won't  | —                | Backlog/defer     |
| P5       | —      | —                | Archive           |

---

## 5. Communication Pattern

**We** follow this sequence for stakeholder-facing work:

| Phase         | Purpose                            | Output          |
| ------------- | ---------------------------------- | --------------- |
| **Scout**     | Explore, verify feasibility        | Notes, findings |
| **Rapport**   | Inform stakeholder of discoveries  | Status update   |
| **Questions** | Gather missing info (with context) | Clarifications  |
| **Action**    | Execute when all is clear          | Deliverable     |

**Rule**: Never request information without first reporting what was discovered.

**Anti-pattern**: Asking questions without context ("What's X?") vs. proper form ("I found Y and Z, but need X to proceed because...")

---

## 6. Implementation Guidelines

1. **Trial with Real Data**: **We** validate workflow choices by running a pilot with actual project data for 1-2 weeks before committing.

2. **Pilot → Scale**: **We** roll out to ONE team/project first, document customizations, then scale to others.

3. **Hybrid as Norm**: **We** acknowledge most real work is hybrid (e.g., Waterfall planning + Agile execution). Templates are starting points, not constraints.

4. **Visual Boards Default**: For service-heavy or multi-department coordination, **we** default to Kanban boards with WIP limits.

5. **Review Cadence**: **We** review workflow effectiveness quarterly and adjust as needed.

---

_Extracted from project-standards.md | 2025-12-22_
