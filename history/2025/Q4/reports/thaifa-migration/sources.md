# Source Triangulation — Thaifa Migration

## Sources Compared

### Source 1: OLD Path (Documents)

- **Location**: `/home/omar/Documents/projects/clients/external/dossiers/villa-thaifa/`
- **Type**: Original working directory
- **Evidence**: 88 files, 7.1 MB, French, last updated 2025-12-20 19:10
- **Key Claims**: Complete operational project with full context
- **Bias**: May contain outdated patterns, pre-organization structure

### Source 2: NEW Path (El-Mountassir)

- **Location**: `/home/omar/Work/El-Mountassir/projects/thaifa/`
- **Type**: Organization-integrated project
- **Evidence**: 20 files, 116 KB, English, last updated 2025-12-22 00:15
- **Key Claims**: Standards-compliant, translated state/, minimal CLAUDE.md
- **Bias**: Incomplete - only state/ was migrated

---

## CLAUDE.md Comparison

| Aspect | OLD (256 lines) | NEW (50 lines) | Action |
|--------|-----------------|----------------|--------|
| Client info | Age, relation type, context | Basic overview | MERGE - keep old details |
| Communication protocol | Vouvoiement, WhatsApp patterns, Scout→Report→Action | Formal mention only | MERGE - keep old workflow |
| Folder structure | Full documentation | Not documented | MERGE - adapt to new structure |
| State/ documentation | Detailed with examples | Links only | KEEP NEW - simpler |
| Credentials handling | Full rules + warning | Not mentioned | ADD to new |
| Lessons-learned ref | Referenced | Not mentioned | ADD reference |
| Task workflow | TODOs.md pattern | Not mentioned | DECIDE - Linear vs file |
| PDF generation | Full command + CSS | Not mentioned | ADD to new |
| Deadlines | RDV 22 Dec 10:00 | Not mentioned | ADD to new |

---

## Content Mapping: What's Missing in NEW

| OLD Content | Size | Priority | Migration Strategy |
|-------------|------|----------|-------------------|
| `admin/client/PROFILE.md` | 412 lines | **P0** | Migrate as-is |
| `admin/credentials.md` | ~20 lines | **P0** | Migrate as-is (protected) |
| `admin/contacts.md` | ~15 lines | **P1** | Migrate as-is |
| `admin/audit.md` | ~10 lines | **P2** | Migrate or archive |
| `.claude/output/2025/Q4/reports/` | 7 dirs, 39 files | **P1** | Migrate to history/ |
| `assets/images/` | 4 PNGs | **P1** | Migrate as-is |
| `communication/whatsapp/` | 4 files | **P1** | Migrate as-is |
| `docs/lessons-learned.md` | Key file | **P0** | Migrate to docs/ |
| `docs/templates/` | CSS + MD | **P1** | Migrate as-is |
| `docs/services-transport.md` | Reference | **P2** | Migrate as-is |
| `projects/2025-12_booking-hotelrunner/` | Active mission | **P0** | Migrate or convert to mission format |
| `projects/jisr-mokawala/` | Exploratory | **P2** | Archive or migrate |
| `tasks/TODOs.md` | 231 lines | **P0** | Migrate to Linear OR keep file |
| `.backup/` | 2 files | **P3** | Archive |

---

## state/ Comparison

**Finding**: Same data, different language (FR → EN)

| File | OLD (FR) | NEW (EN) | Verdict |
|------|----------|----------|---------|
| `current/reservations.md` | French | English | **KEEP NEW** (more recent, EN standard) |
| `current/promotions.md` | French | English | **KEEP NEW** |
| `current/rooms.md` | French | English | **KEEP NEW** |
| `current/blockers.md` | French | English | **KEEP NEW** |
| `baseline/*` | French | English | **KEEP NEW** |
| `planned/*` | French | English | **KEEP NEW** |
| `execution/*` | French | English | **KEEP NEW** |
| `historical/*` | French | English | **KEEP NEW** |

---

## Convergence Analysis

| Pattern | OLD | NEW | Confidence |
|---------|-----|-----|------------|
| State management (SSOT) | AGREE | AGREE | High |
| English for code/configs | DISAGREE (FR) | AGREE (EN) | High - NEW wins |
| Folder structure | Custom | Template-based | Medium - adapt OLD |
| Task tracking | File-based | Not specified | Decision needed |
| Report output | `.claude/output/` | `history/YYYY/QQ/` | Medium - adapt to org standard |

---

## Decision Points

### 1. Tasks/TODOs

**Options**:
- A) Migrate TODOs.md as-is (simple, continuity)
- B) Convert to Linear issues (integrated, standard)
- C) Convert to missions/ (if multi-step)

**Recommendation**: B for tactical items, C for strategic work

### 2. Reports Output Location

**Options**:
- A) Keep `.claude/output/` structure (project-specific)
- B) Move to `history/YYYY/QQ/reports/thaifa-*` (org-level)

**Recommendation**: B for completed reports, A for active work

### 3. Admin Structure

**Options**:
- A) Keep `admin/` in project (simple)
- B) Use `configs/` or parent admin (org pattern)

**Recommendation**: A - project-specific client data stays in project
