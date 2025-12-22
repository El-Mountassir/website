# Changelog

All notable changes to the El-Mountassir organization repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
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
