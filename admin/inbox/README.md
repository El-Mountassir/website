# Human Inbox

> **A dropbox for agents to communicate with Omar.**
> Items needing human attention, decisions, reminders, FYIs.

---

## Purpose

Omar doesn't read everything agents write. This inbox provides a dedicated place for:

| Type | Description |
|------|-------------|
| **Action Required** | Omar needs to DO something |
| **Decision Needed** | Omar needs to CHOOSE between options |
| **FYI** | Information Omar should KNOW (no action needed) |
| **Reminder** | Something to remember for later |

---

## How It Works

### For Agents

1. **When to use**: When you identify something that needs Omar's attention
2. **Where to write**: Add to `pending.md` in this folder
3. **Format**: Use the template below

### For Omar

1. **Check regularly**: Review `pending.md` at session start/end
2. **Process items**: Mark as done or move to archive
3. **Respond**: Agents will see your decisions in next session

---

## Item Template

```markdown
## [YYYY-MM-DD] Title

**Priority**: 🔴 High | 🟡 Medium | 🟢 Low
**Type**: Action Required | Decision Needed | FYI | Reminder
**From**: [Agent name]

Description of what needs attention.

**Context**: (optional) Why this matters
**Suggested action**: (optional) What the agent recommends
**Deadline**: (optional) If time-sensitive
```

---

## Priority Guide

| Priority | When to use |
|----------|-------------|
| 🔴 **High** | Blocking work, time-sensitive, financial impact |
| 🟡 **Medium** | Important but not urgent, quality improvement |
| 🟢 **Low** | Nice-to-know, minor improvements |

---

## File Structure

```
admin/inbox/
├── README.md      # This file
├── pending.md     # Current items needing attention
└── archive/       # Processed items (optional)
```

---

## Rules

1. **Agents**: Only add items that truly need human attention
2. **Don't duplicate**: Check if item already exists before adding
3. **Be specific**: Clear description, actionable recommendations
4. **Respect priority**: Don't mark everything as 🔴 High

---

_Created: 2025-12-23 — admin/inbox/README.md_
