# Claude Code CLI + Chrome Integration

```yaml
Title: Claude Code Chrome Integration Guide
Creator: Omar El Mountassir + Claude Web
Subject: Browser Automation, Claude Code, Chrome Integration
Description: Guide for using Claude Code CLI with Chrome browser automation
Date: 2025-12-21
Type: Text
Format: Markdown
Identifier: guides/claude-code-chrome.md
Language: en
Version: 0.0.1-alpha.0
Status: REFERENCE
Dimension: Tools
```

---

## 1. Overview

| Aspect                       | Detail                                  |
| ---------------------------- | --------------------------------------- |
| **Feature**                  | Claude Code ↔ Chrome browser automation |
| **Status**                   | Beta                                    |
| **Launch Command**           | `claude --chrome`                       |
| **Requirement: Claude Code** | Version 2.0.73+                         |
| **Requirement: Extension**   | Claude in Chrome v1.0.36+               |

---

## 2. What It Can Do

| Capability      | Description                    | Example                                   |
| --------------- | ------------------------------ | ----------------------------------------- |
| **Navigate**    | Open URLs, switch tabs         | "Open calendar.google.com"                |
| **Click**       | Click buttons, links, elements | "Click the 'Create' button"               |
| **Type**        | Fill forms, input fields       | "Type 'Meeting with Thaifa' in the title" |
| **Read**        | Extract text, DOM state        | "What events are on my calendar today?"   |
| **Console**     | Read browser console logs      | Debug web apps                            |
| **Screenshots** | Capture page state             | Visual verification                       |
| **Record**      | Record workflows as shortcuts  | Reusable automation                       |

---

## 3. Built-in Platform Knowledge

| Platform            | Claude Knows How To                    |
| ------------------- | -------------------------------------- |
| **Google Calendar** | Navigate, create events, view schedule |
| **Gmail**           | Read, compose, manage emails           |
| **Google Docs**     | Edit documents                         |
| **Slack**           | Send messages, navigate channels       |
| **GitHub**          | Navigate repos, issues, PRs            |

---

## 4. Setup Steps

| Step | Action                    | Command/Note                         |
| ---- | ------------------------- | ------------------------------------ |
| 1    | Check Claude Code version | `claude --version` (need 2.0.73+)    |
| 2    | Install Chrome extension  | Chrome Web Store: "Claude in Chrome" |
| 3    | Pin extension             | Click puzzle icon → pin              |
| 4    | Sign in extension         | Use Claude account                   |
| 5    | Launch Claude Code        | `claude --chrome`                    |
| 6    | Verify connection         | `/chrome` in Claude Code             |

---

## 5. Important Limitations

| Limitation              | Impact                              | Workaround                   |
| ----------------------- | ----------------------------------- | ---------------------------- |
| **No headless mode**    | You see Chrome actions in real-time | Feature, not bug             |
| **Modal dialogs block** | JS alerts interrupt flow            | Dismiss manually             |
| **Tab state**           | Tabs can become unresponsive        | Ask Claude to create new tab |
| **Chrome only**         | Brave, Arc not supported            | Use Chrome                   |
| **WSL not supported**   | Linux users need native             | Use Pop!\_OS native          |

---

## 6. Security Considerations

| Risk                 | Mitigation                             |
| -------------------- | -------------------------------------- |
| **Prompt injection** | Malicious sites can trick Claude       |
| **Session access**   | Claude sees your logged-in state       |
| **Sensitive data**   | Don't automate banking, personal email |

**Best Practice:** Use for development/automation, not sensitive browsing.

---

## 7. Example Commands for Calendar

| Task                  | Command to Claude Code                                              |
| --------------------- | ------------------------------------------------------------------- |
| View today's schedule | "Show me my calendar for today"                                     |
| Create event          | "Create a meeting called 'RDV Thaifa' tomorrow at 10am for 4 hours" |
| Find free time        | "When am I free next week for a 1-hour meeting?"                    |
| Color code event      | "Change the color of tomorrow's meeting to red"                     |
| Set reminder          | "Add a 30 minute reminder to my 10am meeting"                       |
| Create recurring      | "Create a weekly review every Friday at 5pm"                        |

---

## 8. Workflow: Configure Calendar Standards

| Step | Claude Code Task                       |
| ---- | -------------------------------------- |
| 1    | Navigate to calendar.google.com        |
| 2    | Go to Settings (gear icon)             |
| 3    | Set default meeting duration to 30 min |
| 4    | Enable "Speedy meetings"               |
| 5    | Create Focus Time blocks (recurring)   |
| 6    | Create Lunch blocks (recurring)        |
| 7    | Apply color coding to existing events  |

---

## 9. CLAUDE.md for Calendar Configuration

```markdown
# CLAUDE.md — Calendar Configuration Mission

## Context

Omar's Google Calendar needs configuration per Calendar Standards v0.0.2-alpha.0.

## Mission

Configure Google Calendar settings and create protected time blocks.

## Chrome Required

This mission requires browser automation. Launch with: `claude --chrome`

## Tasks

### Task 1: Calendar Settings

- [ ] Open calendar.google.com
- [ ] Go to Settings → General → Event settings
- [ ] Set default duration: 30 minutes
- [ ] Enable "Speedy meetings" (25/50 min instead of 30/60)
- [ ] Set default notification: 10 minutes before

### Task 2: Create Recurring Blocks (Current Schedule - Night Owl)

Create these recurring events starting Monday 2024-12-23:

| Event                    | Days    | Time  | Duration | Color    |
| ------------------------ | ------- | ----- | -------- | -------- |
| FOCUS - Morning Planning | Mon-Fri | 10:00 | 30 min   | Grape    |
| FOCUS - Deep Work        | Mon-Fri | 10:30 | 2.5h     | Grape    |
| BREAK - Lunch            | Mon-Fri | 13:00 | 1.5h     | Graphite |
| FOCUS - Wrap-up          | Mon-Fri | 19:00 | 30 min   | Grape    |

### Task 3: Color Existing Events

- Apply Tomato (Red) to client meetings
- Apply Grape (Purple) to focus/learning blocks

## Verification

After each task, confirm completion before proceeding.

## Safety

- Do NOT delete any existing events
- Do NOT modify events with attendees
- Ask before any destructive action
```

---

## Changelog

| Version       | Date       | Changes       |
| ------------- | ---------- | ------------- |
| 0.0.1-alpha.0 | 2025-12-21 | Initial guide |
