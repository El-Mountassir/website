# STRUCTURE.md — Auto-Generated

> **This file is automatically updated by Claude Code hooks.**
> Do not edit manually — changes will be overwritten.

**Last updated**: 2025-12-22 03:05:41 UTC

---

```
./
├── admin/
│   ├── finance/
│   │   └── .gitkeep
│   ├── legal/
│   │   └── .gitkeep
│   └── time/
│       └── .gitkeep
├── archive/
│   └── settings.local.json.backup
├── .claude/
│   ├── agents/
│   │   ├── build-agent.md
│   │   ├── docs-scraper.md
│   │   ├── meta-agent.md
│   │   ├── planner.md
│   │   ├── playwright-validator.md
│   │   ├── scout-report-suggest-fast.md
│   │   └── scout-report-suggest.md
│   ├── commands/
│   │   ├── elevate.md
│   │   ├── end.md
│   │   ├── question-w-mermaid-diagrams.md
│   │   ├── start.md
│   │   └── sync.md
│   ├── hooks/
│   │   └── update-structure.sh*
│   ├── input/
│   │   └── 2025-12-22-architecture-clarification.md
│   ├── memory/
│   │   └── README.md
│   ├── rules/
│   │   ├── anti-patterns.md
│   │   ├── behavior.md
│   │   ├── memory-protocol.md
│   │   ├── partnership.md
│   │   ├── taxonomy.md
│   │   ├── templates.md
│   │   └── world-model.md
│   ├── skills/
│   │   ├── creating-commands/
│   │   │   └── SKILL.md
│   │   ├── ending-session/
│   │   │   └── SKILL.md
│   │   ├── meta-skill/
│   │   │   ├── docs/
│   │   │   └── SKILL.md
│   │   ├── reorganizing-directories/
│   │   │   ├── checklist.md
│   │   │   └── SKILL.md
│   │   └── starting-session/
│   │       └── SKILL.md
│   ├── settings.json
│   ├── settings.json.backup
│   ├── settings.local.json
│   └── settings.local.json.backup
├── configs/
│   └── system/
│       ├── agents/
│       ├── mcp/
│       │   ├── knowledge-graph.md
│       │   ├── linear.md
│       │   ├── notion.md
│       │   └── README.md
│       └── prompts/
├── docs/
│   └── reference/
│       ├── guides/
│       │   ├── claude-code-chrome.md
│       │   └── claude-code-permissions.md
│       └── INDEX.md
├── history/
│   └── 2025/
│       └── Q4/
│           ├── missions/
│           └── reports/
├── learning/
│   ├── pac/
│   │   └── .gitkeep
│   ├── tac/
│   │   └── .gitkeep
│   └── zte/
│       └── .gitkeep
├── LESSONS-LEARNED/
│   ├── 2025-12-21-premature-closure.md
│   ├── 2025-12-22-permissions-config.md
│   └── .gitkeep
├── missions/
│   ├── active/
│   │   └── .gitkeep
│   ├── drafts/
│   │   ├── claude-web-sync.md
│   │   └── multi-instance-coordination.md
│   ├── queue/
│   │   ├── 2025-12-22-claude-permissions-fix.md
│   │   ├── 2025-12-22-destructive-operations-guardrails.md
│   │   ├── 2025-12-22-docs-base-alignment.md
│   │   ├── 2025-12-22-jisr-mokawala-investigation.md
│   │   ├── 2025-12-22-M1-rule-deduplication.md
│   │   ├── 2025-12-22-M2-controlled-execution-failure.md
│   │   ├── 2025-12-22-M2-mcp-on-demand.md
│   │   ├── 2025-12-22-M3-orchestrator-pattern.md
│   │   ├── 2025-12-22-M4-subagent-architecture.md
│   │   ├── 2025-12-22-M5-hierarchical-claude-md.md
│   │   ├── 2025-12-22-thaifa-migration-cleanup.md
│   │   ├── 2025-12-22-thaifa-migration-critical.md
│   │   ├── 2025-12-22-thaifa-migration-operational.md
│   │   └── .gitkeep
│   └── README.md
├── omar/
│   ├── context/
│   │   └── README.md
│   ├── model/
│   │   └── README.md
│   └── tools/
│       └── README.md
├── projects/
│   ├── gagliano/
│   │   └── CLAUDE.md
│   └── thaifa/
│       ├── admin/
│       │   ├── client/
│       │   ├── contacts.md
│       │   └── credentials.md
│       ├── assets/
│       │   └── images/
│       ├── .claude/
│       │   ├── input/
│       │   └── output/
│       ├── communication/
│       │   └── whatsapp/
│       ├── docs/
│       │   ├── templates/
│       │   ├── lessons-learned.md
│       │   └── services-transport.md
│       ├── projects/
│       │   ├── booking-hotelrunner/
│       │   └── jisr-mokawala/
│       ├── state/
│       │   ├── baseline/
│       │   ├── current/
│       │   ├── execution/
│       │   ├── historical/
│       │   ├── planned/
│       │   └── README.md
│       └── CLAUDE.md
├── shared/
│   ├── memory/
│   │   ├── decisions.md
│   │   ├── episodes.md
│   │   ├── facts.md
│   │   └── patterns.md
│   ├── standards/
│   │   ├── management/
│   │   │   ├── missions/
│   │   │   ├── time/
│   │   │   └── work/
│   │   ├── confidence-system.md
│   │   ├── INDEX.md
│   │   ├── project-standards.md
│   │   └── state-management.md
│   ├── user/
│   │   └── preferences.md
│   └── INDEX.md
├── templates/
│   ├── commands/
│   │   └── slash-command.md
│   ├── metadata/
│   │   ├── dublin-core-extended.md
│   │   └── dublin-core-standard.md
│   ├── missions/
│   │   └── mission.md
│   ├── projects/
│   │   └── CLAUDE.md
│   ├── state/
│   │   ├── baseline/
│   │   │   └── README.md
│   │   ├── current/
│   │   │   └── README.md
│   │   ├── execution/
│   │   │   └── README.md
│   │   ├── historical/
│   │   │   └── README.md
│   │   ├── planned/
│   │   │   └── README.md
│   │   └── README.md
│   └── README.md
├── CHANGELOG.md
├── CLAUDE.md
├── .gitignore
├── GOVERNANCE.md
├── INDEX.md
├── MANIFESTO.md
├── .mcp.json*
├── README.md
├── ROADMAP.md
└── STRUCTURE.md

87 directories, 109 files
```

---

_Generated by `.claude/hooks/update-structure.sh`_
