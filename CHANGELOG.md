# Changelog

All notable changes to the El-Mountassir organization repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Auto-update hook for STRUCTURE.md (`.claude/hooks/update-structure.sh`)
- Project settings hook configuration (`.claude/settings.json`)
- Live structure reference in CLAUDE.md (`@STRUCTURE.md`)
- CHANGELOG.md following Keep a Changelog standard
- Project standards documentation (`docs/standards/project-standards.md`)

### Changed
- CLAUDE.md REPOSITORY STRUCTURE now includes missions/, history/, .claude/
- GitHub repo renamed: El-Mountassir/El-Mountassir → El-Mountassir/website

### Fixed
- .gitignore now protects admin/finance/ and admin/legal/

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
