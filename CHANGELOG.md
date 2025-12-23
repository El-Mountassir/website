# Changelog

All notable changes to the El-Mountassir organization repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Architecture Reference document (`docs/reference/architecture.md`) — 7 sections:
  - **Substrate Layer** (NEW) — Carbon-Silicon Partnership foundation
  - Three-Layer Model (Human Control Plane + Agent Harness + Conventions)
  - Everything-as-Code (EaC) philosophy
  - Hybrid Multi-Repo Architecture (for 10+ clients)
  - Current Mono-Repo Structure (3-Level Rule)
  - Agent Harness Components (6 from Parallel.ai)
  - Core Four framework (IndyDevDan) — Context + Model + Prompt + Tools
- Decisions captured in `shared/memory/decisions.md`:
  - Three-Layer Model
  - Everything-as-Code (EaC) Philosophy
  - Multi-Repo Hybrid for 10+ Clients
  - Agentic ⊂ Digital Transformation positioning
  - ROADMAP.md as Single Source of Priority
- Patterns captured in `shared/memory/patterns.md`:
  - Reference over Inline (@imports)
  - Agent Depth Limitation (3-Level Rule)
  - Explicit Delegation in Agentic Systems
- ROADMAP.md: Added OPERATIONAL PRIORITIES section (NOW/NEXT/LATER/DONE)
- Time Management: Google Calendar booking pages documentation (`admin/time/booking-pages.md`)
- Time Management: Client Meeting booking URLs (30 min + 60 min)
- Pattern: "Client Booking Page Setup" in `shared/memory/patterns.md`
- Pattern: "Evaluate Client Strategic Value" in `shared/memory/patterns.md`
- User Preferences: Time Management section with booking config
- Subscriptions documentation (`admin/finance/subscriptions/`)
- Platform configs (`configs/system/platforms/`)
- Gagliano: Cash Depot email thread documentation

### Changed
- **Structural: `omar/` → `.omar/`** — A2A protocol alignment (all agents use `.{agent}/` pattern)
- Architecture Reference: Added Section 0 "Substrate Layer" — Carbon-Silicon Partnership (v1.3.0)
- Architecture Reference: Migrated all ASCII diagrams to Mermaid (8 diagrams total)
- Architecture Reference: Enriched Core Four with INPUT → PROCESS → OUTPUT → FEEDBACK flow
- Architecture Reference: Unified agent directories in File Access Pattern diagram (v1.4.0)
- Thaifa project: Major restructure (archive/, data/, docs/, src/, ai/)
- User preferences updated to v1.1.0 with booking pages

### Added (previous)
- Villa Thaifa: Booking.com data file (`projects/thaifa/state/current/booking-com-data.md`)
- Villa Thaifa: Guest testimonials for marketing (`projects/thaifa/docs/guest-testimonials.md`)
- Villa Thaifa: State File Protection guardrail in CLAUDE.md (FULL STOP before destructive edits)
- Unified mission template with 6 types (`templates/missions/mission.md`)
- Dublin Core metadata templates (`templates/metadata/dublin-core-*.md`)
- Template extraction rule (`.claude/rules/templates.md`)
- P0 Mission: Destructive operations guardrails (`missions/queue/2025-12-22-destructive-operations-guardrails.md`)
- Shared resources directory (`shared/`) with INDEX, memory, standards, user preferences
- Permissions audit with expanded allow patterns (92 patterns)
- Reports: permissions-audit, agentic-cognitive-gaps (`history/2025/Q4/reports/`)
- Thaifa project files: reports, templates, assets, communication logs
- Auto-update hook for STRUCTURE.md (`.claude/hooks/update-structure.sh`)
- Project settings hook configuration (`.claude/settings.json`)
- Live structure reference in CLAUDE.md (`@STRUCTURE.md`)
- CHANGELOG.md following Keep a Changelog standard
- Project standards documentation (`docs/standards/project-standards.md`)
- Mission: omar-cleanup in queue (`missions/queue/2025-12-21-omar-cleanup.md`)
- Skill: reorganizing-directories (`.claude/skills/reorganizing-directories/`)

### Changed
- Villa Thaifa: PROFILE.md expanded with detailed Booking.com review scores, breakfast info
- Villa Thaifa: rooms.md now shows both HotelRunner (9) and Booking.com (8) room types
- Villa Thaifa: contacts.md with languages spoken (Arabic, French, English, Dutch)
- Villa Thaifa: lessons-learned.md with date confusion pattern
- /end command now ZERO TOLERANCE (all guardrails BLOCKING, no warnings)
- Mission standard: inline template extracted to `templates/missions/`
- Project standards: Dublin Core section links to templates
- CLAUDE.md: Added SHARED RESOURCES section, standards moved to `shared/standards/`
- CLAUDE.md REPOSITORY STRUCTURE now includes missions/, history/, .claude/
- GitHub repo renamed: El-Mountassir/El-Mountassir → El-Mountassir/website

### Fixed
- .gitignore now protects admin/finance/ and admin/legal/
- STRUCTURE.md manually updated (hook not triggering automatically)

## [0.0.1-alpha.0] - 2025-12-21

### Added
- Initial repository structure
- CLAUDE.md organizational context (NORTH STAR, WHO WE ARE, HARD STOPS)
- Mission management system (drafts/, queue/, active/)
- Project templates (state/, projects/)
- Thaifa project with full state management
- Gagliano project placeholder
- Standards documentation (missions, time, versioning)
- Learning directories (TAC, PAC, ZTE)
- Admin structure (time, finance, legal)
- Omar context and profile

---

[Unreleased]: https://github.com/El-Mountassir/El-Mountassir/compare/v0.0.1-alpha.0...HEAD
[0.0.1-alpha.0]: https://github.com/El-Mountassir/El-Mountassir/releases/tag/v0.0.1-alpha.0
