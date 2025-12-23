# STRUCTURE.md — Auto-Generated

> **This file is automatically updated by Claude Code hooks.**
> Do not edit manually — changes will be overwritten.

**Last updated**: 2025-12-23 11:46:31 UTC

---

```
./
├── admin/
│   ├── finance/
│   │   ├── subscriptions/
│   │   │   ├── anthropic.md
│   │   │   ├── cloudflare.md
│   │   │   ├── docker.md
│   │   │   ├── github.md
│   │   │   ├── google.md
│   │   │   ├── linear.md
│   │   │   ├── README.md
│   │   │   └── vercel.md
│   │   └── .gitkeep
│   ├── inbox/
│   │   ├── pending.md
│   │   └── README.md
│   ├── legal/
│   │   └── .gitkeep
│   └── time/
│       ├── booking-pages.md
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
│       ├── platforms/
│       │   ├── cloudflare.md
│       │   ├── docker.md
│       │   ├── github.md
│       │   └── vercel.md
│       └── prompts/
├── docs/
│   └── reference/
│       ├── architecture/
│       │   ├── backlog.md
│       │   ├── evaluation.md
│       │   ├── README.md
│       │   └── reference.md
│       ├── guides/
│       │   ├── claude-code-chrome.md
│       │   ├── claude-code-permissions.md
│       │   └── client-communication-best-practices.md
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
│   ├── 2025-12-22-backup-before-edit.md
│   ├── 2025-12-22-permissions-config.md
│   ├── 2025-12-22-rushing-hurricane.md
│   └── .gitkeep
├── missions/
│   ├── active/
│   │   └── .gitkeep
│   ├── drafts/
│   ├── queue/
│   │   ├── 2025-12-22-claude-audit-deduplication.md
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
│   │   ├── 2025-12-22-multi-instance-coordination.md
│   │   ├── 2025-12-22-sync-claude-code-claude-web.md
│   │   └── .gitkeep
│   └── README.md
├── .omar/
│   ├── context/
│   │   └── README.md
│   ├── models/
│   │   └── README.md
│   ├── prompt/
│   └── tools/
│       └── README.md
├── projects/
│   ├── gagliano/
│   │   ├── communication/
│   │   │   └── 2025-12-cash-depot-demo-thread.md
│   │   └── CLAUDE.md
│   └── thaifa/
│       ├── ai/
│       │   ├── agentic/
│       │   ├── analytics/
│       │   ├── knowledge/
│       │   ├── memory/
│       │   ├── rag/
│       │   └── CLAUDE.md
│       ├── archive/
│       │   └── 2025/
│       ├── .claude/
│       │   ├── commands/
│       │   ├── input/
│       │   ├── rules/
│       │   └── settings.local.json
│       ├── data/
│       │   ├── admin/
│       │   ├── communication/
│       │   └── specs/
│       ├── docs/
│       │   ├── briefs/
│       │   ├── templates/
│       │   ├── workflows/
│       │   ├── guest-testimonials.md
│       │   ├── INDEX.md
│       │   ├── lessons-learned.md
│       │   └── services-transport.md
│       ├── infra/
│       │   ├── docker/
│       │   └── envs/
│       ├── project/
│       │   └── TODOs.md
│       ├── src/
│       │   ├── apps/
│       │   ├── packages/
│       │   ├── tools/
│       │   └── CLAUDE.md
│       ├── AGENTS.md
│       ├── CLAUDE.md
│       ├── .gitignore
│       ├── README.md
│       ├── ROADMAP.md
│       └── STRUCTURE.md
├── scripts/
│   └── get/
│       ├── transcript/
│       │   ├── video/
│       │   └── indy_dev_dan_2026_roadmap_transcript.md
│       └── video/
│           └── get_transcript.py
├── shared/
│   ├── books/
│   ├── drafts/
│   │   ├── 2026-tech-stack.md
│   │   ├── enterrpise.md
│   │   └── .md
│   ├── memory/
│   │   ├── decisions.md
│   │   ├── episodes.md
│   │   ├── facts.md
│   │   └── patterns.md
│   ├── philosophy/
│   │   └── 2026-playbook.md
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
│   ├── 52c6a6d8-39f0-5442-aba1-cc7d7174b268.pdf
│   ├── account_activities_202512.csv
│   ├── INDEX.md
│   ├── Invoice-QYCPRZIA-0001.pdf
│   └── s43681-024-00489-4.pdf
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

109 directories, 148 files
```

---

_Generated by `.claude/hooks/update-structure.sh`_
