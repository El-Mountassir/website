# Step-Back Analysis — Mission Coordination

**Date**: 2025-12-22
**Request**: Design a mechanism so Claude instances know when another instance is working on a mission

---

## Problem Statement

Multiple Claude Code instances can unknowingly work on the same mission because there's no signaling mechanism to indicate "this mission is claimed by another instance."

---

## Incident That Triggered This

Omar asked me (current instance) about the Thaifa migration status. I didn't know another instance was already executing those missions. The missions were in `queue/` with `status: QUEUED` and `assigned_to: Claude Code` — but no indication that work had started.

---

## Success Criteria

1. **Visibility**: Any instance can see at a glance if a mission is being worked on
2. **Claim mechanism**: An instance can "claim" a mission before starting
3. **Handoff support**: If an instance crashes, another can resume
4. **Minimal friction**: The mechanism shouldn't add significant overhead
5. **Conflict prevention**: Two instances shouldn't claim the same mission

---

## Current System Gap

The standard at `docs/standards/management/missions/README.md` defines:

| Element | Exists | Problem |
|---------|--------|---------|
| `status: QUEUED/ACTIVE` | Yes | Not updated when work starts |
| `assigned_to` | Yes | Says "Claude Code" generically, not specific instance |
| Move to `active/` | Yes (protocol) | Not enforced, often skipped |
| Execution log | Yes | Not used as claim mechanism |
| Instance ID | **NO** | No way to identify which instance |
| Timestamp of claim | **NO** | No way to know when claimed |

---

## Domain Concepts

- **Claim**: Declaring intent to work on a mission, preventing others
- **Lock**: Preventing concurrent access (stronger than claim)
- **Instance**: A single Claude Code session (ephemeral, no persistent ID)
- **Session**: A conversation within an instance (can be resumed)
- **Handoff**: Transferring work from one instance to another
