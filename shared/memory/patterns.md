# Patterns — Reusable Approaches

> **What works. How to do things. Proven solutions.**
> Generalized from specific experiences.

---

## Format

```markdown
## Pattern: [Name]

**Author**: [Who documented this]
**Confidence**: [✅🟢🟡🟠⚠️]
**Source**: [Where this was learned]

### Problem

What problem this pattern solves.

### Solution

How to apply the pattern.

### Example

Concrete example of usage.

### Anti-Pattern

What NOT to do.
```

---

## Patterns

### Pattern: Recognition → Action (R→A)

**Author**: Claude Code + Omar
**Confidence**: ✅ Certitude (95%)
**Source**: 2025-12-22 cognitive overload incident

#### Problem

Agent acknowledges something ("Noted", "Good point") but takes no action. Words without follow-through.

#### Solution

After every recognition/acknowledgment:

1. **What should I DO about this?**
2. **Is the action obvious?** → ACT, don't ask
3. **Should future instances know?** → Document NOW

#### Example

```
BAD:  "Noted that you prefer X" → (nothing happens)
GOOD: "Noted that you prefer X" → (update preferences.md) → (apply X going forward)
```

#### Anti-Pattern

Empty acknowledgment without action.

---

### Pattern: Obvious Actions Table

**Author**: Claude Code
**Confidence**: 🟢 Recommandation (90%)
**Source**: 2025-12-22 anti-patterns documentation

#### Problem

Agent asks for permission/direction when the next step is obvious.

#### Solution

Maintain a table of obvious actions that should never require asking:

| Situation           | Obvious Action   |
| ------------------- | ---------------- |
| Task completed      | Archive it       |
| Changes made        | Commit them      |
| Learning recognized | Document it      |
| Error pattern found | Create guardrail |
| Next step is clear  | Continue         |

#### Example

```
BAD:  "Mission complete. What should I do next?"
GOOD: (Archive mission) → (Commit changes) → "Mission archived and committed."
```

#### Anti-Pattern

Cognitive overload — asking about obvious things.

---

### Pattern: Confidence-Based Autonomy

**Author**: Omar + Claude
**Confidence**: 🟢 Recommandation (85%)
**Source**: 2025-12-22 architecture discussion

#### Problem

When should agents act autonomously vs. ask for confirmation?

#### Solution

Map confidence level to behavior:

| Confidence | Behavior                                             |
| ---------- | ---------------------------------------------------- |
| ✅ ≥95%    | Act autonomously                                     |
| 🟢 80-94%  | Act, inform human                                    |
| 🟡 60-79%  | Propose, wait for confirmation (important decisions) |
| 🟠 40-59%  | Ask before acting                                    |
| ⚠️ <40%    | Don't act, gather information                        |

#### Example

```
✅ 95%: "File exists" → Just read it
🟢 85%: "This architecture is better" → Implement it, explain why
🟡 70%: "This might fix the bug" → Propose, wait for OK
🟠 50%: "Could be a permissions issue" → Ask before changing permissions
```

#### Anti-Pattern

Acting with low confidence. Asking with high confidence.

---

### Pattern: Split by Access Scope

**Author**: Omar
**Confidence**: 🟢 Recommandation (85%)
**Source**: 2025-12-22 architecture restructuring

#### Problem

Where should files live in a multi-agent system?

#### Solution

Split by who needs access:

| Access Scope         | Location              |
| -------------------- | --------------------- |
| One specific agent   | `.{agent}/`           |
| All agents           | `shared/`             |
| Human only (private) | `{human}/`            |
| Project-specific     | `projects/{project}/` |

#### Example

```
Claude Code settings    → .claude/settings.json
Organization decisions  → shared/memory/decisions.md
Omar's personal goals   → omar/context/goals.md
Thaifa project state    → projects/thaifa/state/
```

#### Anti-Pattern

Putting shared resources in agent-specific folders (lock-in).

---

### Pattern: Migrate with Move, Not Copy

**Author**: Omar
**Confidence**: ✅ Certitude (95%)
**Source**: 2025-12-22 migration discussion

#### Problem

Using `cp` for migrations creates duplicates. Original location still has files.

#### Solution

Always use `mv` for migrations:

```bash
mv source/ destination/
```

#### Example

```bash
# BAD: Creates duplicate
cp docs/standards/ shared/standards/

# GOOD: Single source of truth
mv docs/standards/ shared/standards/
```

#### Anti-Pattern

Copying instead of moving during restructuring.

---

### Pattern: Triple-Check Before Deletion

**Author**: Omar
**Confidence**: ✅ Certitude (100%)
**Source**: 2025-12-22 near-miss incident

#### Problem

Deleting something without proper verification can destroy hours of work. Even if human clicks "yes" by accident.

#### Solution

Before ANY deletion (rm, rmdir, git reset, etc.), verify THREE times:

| Check             | Question                              | How to Verify             |
| ----------------- | ------------------------------------- | ------------------------- |
| **1. Content**    | Is it truly empty/unused?             | `ls -la`, `grep`, `find`  |
| **2. References** | Are there references that will break? | `grep -r "path/to/thing"` |
| **3. Backup**     | Can we recover if wrong?              | Git status, commit state  |

Only proceed if ALL THREE checks pass with ✅ 100% confidence.

#### Example

```bash
# Before: rmdir docs/standards/

# Check 1: Is it empty?
ls -la docs/standards/  # → Only . and ..  ✅

# Check 2: Are there references?
grep -r "docs/standards" . --include="*.md"  # → Found in CLAUDE.md! ❌

# Check 3: Can we recover?
git status  # → Uncommitted changes ⚠️

# RESULT: Do NOT delete yet. Fix references first.
```

#### Anti-Pattern

Quick deletion without verification. Trusting that human will catch mistakes.

---

### Pattern: Document for the Collective

**Author**: Omar
**Confidence**: ✅ Certitude (95%)
**Source**: Partnership framework

#### Problem

Current instance learns something but future instances lose it.

#### Solution

Before ending any significant interaction, ask:

> "Would my next instance want to know this?"

If YES → Document in shared/memory/ or rules IMMEDIATELY

#### Example

```
Learned: "Omar prefers tables over prose"
Action: Add to shared/user/preferences.md
```

#### Anti-Pattern

Individual vs. collective thinking — learning dies with session.

---

### Pattern: Pre-Release Versioning During Drafts

**Author**: Omar + Claude
**Confidence**: ✅ Certitude (100%)
**Source**: 2025-12-22 version bump error — jumped to v0.0.5 instead of alpha.4

#### Problem

During drafting/alpha phase, incrementing PATCH (0.0.1 → 0.0.2) instead of PRE-RELEASE (alpha.0 → alpha.1) causes version inflation. By the time actual content changes warrant a PATCH bump, version is already at v0.0.10+.

#### Solution

**During alpha/drafting**: Increment the PRE-RELEASE identifier ONLY.

| Change Type              | Version Pattern                       | Example                              |
| ------------------------ | ------------------------------------- | ------------------------------------ |
| **Drafting iterations**  | `x.y.z-alpha.N` → `x.y.z-alpha.N+1`   | `0.0.1-alpha.3` → `0.0.1-alpha.4`    |
| **Ready for review**     | `x.y.z-alpha.N` → `x.y.z-rc.0`        | `0.0.1-alpha.7` → `0.0.1-rc.0`       |
| **Stable release**       | `x.y.z-rc.N` → `x.y.z`                | `0.0.1-rc.1` → `0.0.1`               |

**PATCH/MINOR/MAJOR only bump when**:
- PATCH: Actual bug fix or backward-compatible change in STABLE content
- MINOR: New feature added (after stable release)
- MAJOR: Breaking change

#### Example

```
✅ CORRECT (marathon mindset):
0.0.1-alpha.0  → Initial draft
0.0.1-alpha.1  → Added section A
0.0.1-alpha.2  → Added section B
0.0.1-alpha.3  → Refined section A
0.0.1-alpha.4  → Added section C
0.0.1-rc.0     → Ready for review
0.0.1          → Stable release

❌ WRONG (sprint mindset):
0.0.1-alpha.0  → Initial draft
0.0.2-alpha.0  → Added section A  ← WRONG! Still drafting same scope
0.0.3-alpha.0  → Added section B  ← Version 10 before even stable!
```

#### Anti-Pattern

Speed-running versions. Bumping PATCH for every draft iteration. Forgetting that **this is a marathon, not a sprint**.

#### Key Insight

> **There is SO MUCH more to learn and integrate.** PAC, TAC, Agentic Horizon from IndyDevDan, and more from Omar. Stay in `alpha.N` until the scope is actually complete.

---

### Pattern: Docker Hub Account Not Discoverable via CLI

**Author**: Claude Code
**Confidence**: ✅ Certitude (100%)
**Source**: 2025-12-23 Docker investigation

#### Problem

When investigating Docker subscriptions, Docker Hub account details (email, username, subscription plan) cannot be retrieved via CLI commands like `docker info`, `docker system info`, or `docker scout config`.

#### Solution

When documenting Docker subscriptions or platform configs:

1. **Don't assume CLI will reveal account info** — it won't
2. **Ask user directly** for Docker Hub credentials:
   - Email
   - Username
   - Subscription plan
3. **Check Docker Desktop UI** — subscription details visible in Settings → General or docker.com/billing

#### What CLI CAN Reveal

| Info | Command |
|------|---------|
| Docker Desktop version | `docker version` |
| Engine version | `docker info` |
| MCP Toolkit status | `docker mcp server ls` |
| MCP catalog | `docker mcp catalog show docker-mcp` |
| Plugins | `docker info \| grep Plugins` |

#### What CLI CANNOT Reveal

| Info | Where to Get It |
|------|-----------------|
| Docker Hub email | Ask user or Docker Desktop UI |
| Docker Hub username | Ask user or Docker Desktop UI |
| Subscription plan | Ask user or docker.com/billing |
| Billing details | docker.com/billing |

#### Example

```
❌ WRONG: Assume docker info will show account
✅ CORRECT: Ask user: "What's your Docker Hub email, username, and plan?"
```

#### Anti-Pattern

Trying multiple CLI commands hoping to find account info, wasting time.

---

### Pattern: Never Assume Context Completeness

**Author**: Claude Code + Omar
**Confidence**: ✅ Certitude (100%)
**Source**: 2025-12-23 Google accounts merge incident

#### Problem

Agent receives partial information and assumes it's complete. Makes modifications based on assumptions rather than explicit confirmation. Result: data loss, account confusion, overwrites.

**Real example**: Omar mentioned Google Workspace with omar@el-mountassir.com. Agent assumed omar.mountassir@gmail.com was just a linked personal email, not a separate Google account. Rewrote documentation, losing distinction between two accounts.

#### Solution

**Context is ALWAYS partial.** Before modifying factual data:

| Question | Why |
|----------|-----|
| Is this the ONLY thing, or could there be multiple? | Avoid conflating distinct items |
| Am I REPLACING or ADDING? | Preserve existing information |
| Did user explicitly request this change? | Avoid overreach |
| Could I be making an assumption? | Catch hidden biases |

#### Confidence for Data Modifications

| Type | Minimum Confidence | Action |
|------|-------------------|--------|
| Account/subscription changes | 🟠 40-59% | Ask first |
| Structural rewrites | 🟡 60-79% | Propose, don't act |
| Any data modification | — | Treat as important decision |

#### Example

```
User: "We have Google Workspace with omar@el-mountassir.com"

❌ WRONG:
"I'll update google.md from Personal to Workspace"
→ Assumes one account, overwrites all

✅ CORRECT:
"I see you have Google Workspace. Is this the only Google account,
or do you also have a personal Gmail account (like omar.mountassir@gmail.com)
that should be documented separately?"
→ Asks before assuming
```

#### Anti-Pattern

Acting on 🟢 80% confidence when data modifications require 🟠 50% verification threshold.

---

### Pattern: Client Booking Page Setup

**Author**: Claude Code + Omar
**Confidence**: ✅ Certitude (95%)
**Source**: 2025-12-23 Google Calendar Booking Pages mission

#### Problem

Need a professional, frictionless way for clients to schedule meetings. Manual back-and-forth email scheduling wastes time and projects unprofessional image.

#### Solution

Use **Google Calendar Appointment Schedules** with:

| Setting | Recommendation | Rationale |
|---------|---------------|-----------|
| **Durations** | 30 min + 60 min (separate pages) | Different meeting types |
| **Availability** | Business hours, Mon-Fri | Professional boundaries |
| **Buffer time** | 15 minutes | Prep + notes between meetings |
| **Min notice** | 24 hours | No last-minute surprises |
| **Max advance** | 28 days | Reasonable planning horizon |
| **Conferencing** | Google Meet (auto) | Zero friction for remote |
| **Timezone** | Set explicitly | Avoid confusion with international clients |

#### When to Use Which Duration

| Situation | Duration |
|-----------|----------|
| Initial discovery / deep dive | 60 min |
| Quick follow-up / status | 30 min |
| Project kickoff | 60 min |
| Simple question | 30 min |

#### Example Share Message

```
Pour planifier notre réunion, utilisez mes pages de réservation :
- 30 minutes : [URL]
- 60 minutes : [URL]

For scheduling our meeting, please use my booking page:
- 30 minutes: [URL]
- 60 minutes: [URL]
```

#### Calendar Integration Tips

| Tip | Why |
|-----|-----|
| Block personal time as "Busy" | Prevents booking conflicts |
| Create recurring focus blocks | Protects deep work time |
| Set clear availability end time | Prevents late evening bookings |

#### SSOT Location

Booking page configuration is documented in: `admin/time/booking-pages.md`

#### Anti-Pattern

- Single duration for all meeting types (forces awkward fits)
- No buffer time (back-to-back meetings = burnout)
- Very short notice period (stress from last-minute prep)
- No timezone specification (confusion with international clients)

---

### Pattern: Evaluate Client Strategic Value

**Author**: Claude Code + Omar
**Confidence**: ✅ Certitude (100%)
**Source**: 2025-12-23 Gagliano priority correction

#### Problem

Agent evaluates tasks in isolation, missing the bigger picture. Labels client-related tasks as "Medium" when they're actually CRITICAL. Underestimates revenue potential, portfolio impact, and strategic relationships.

#### Solution

Before prioritizing ANY client-related task, ask:

| Question | Why |
|----------|-----|
| **What's the total potential value?** | First project might be gateway to more |
| **What's the portfolio impact?** | 1 project vs 50 projects = different priority |
| **What's the relationship risk?** | Friction now = lost opportunity later |
| **Is this a reference/portfolio client?** | Social proof value beyond revenue |

#### Client Value Tiers

| Tier | Characteristics | Priority |
|------|-----------------|----------|
| **Strategic** | High value potential, portfolio gateway, reference client | 🔴 CRITICAL |
| **Standard** | Normal project, clear scope, one-off | 🟡 Medium |
| **Low-touch** | Small, routine, maintenance | 🟢 Low |

#### Example

```
❌ WRONG (task in isolation):
"Prepare invoice for Cash Depot" → 🟡 Medium (just admin work)

✅ CORRECT (strategic context):
"Prepare invoice for Cash Depot (gateway to 50 sites, $15k potential)" → 🔴 CRITICAL
```

#### Real Case: Gagliano

| Factor | Value |
|--------|-------|
| First project | Cash Depot demo |
| Potential | 50 websites |
| Revenue | ~$15,000 |
| Impact | Payment friction = could block entire portfolio |
| Correct priority | 🔴 CRITICAL, not 🟡 Medium |

#### Anti-Pattern

- Labeling client admin as "paperasse" when it's actually "unlocking strategic value"
- Looking at immediate task, not relationship trajectory
- Treating first-project clients same as one-off clients

---
