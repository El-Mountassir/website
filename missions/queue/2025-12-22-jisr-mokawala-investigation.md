# Mission: Go Siyaha Eligibility & Jisr Portal Investigation

```yaml
mission_id: 2025-12-22-jisr-mokawala-investigation
status: QUEUED
assigned_to: Claude Code
created: 2025-12-22
assigned: 2025-12-22
claimed_at:
claimed_by:
completed:
archived:
priority: P2  # Elevated - potential 90% subsidy
project: thaifa
```

---

## 🔴 DÉCOUVERTE: Go Siyaha = Opportunité Business Majeure

> **Recherche 2025-12-22** — Cette mission a gagné en importance.

| Élément | Détail |
|---------|--------|
| **Programme** | Go Siyaha (MarocPME) |
| **Budget total** | 720M DH |
| **Cible** | 1700+ entreprises touristiques |
| **Financement** | Jusqu'à **90%** des coûts digitalisation (plafonné 1M DH) |
| **HotelRunner** | Partenaire officiel CNT Maroc (via HWS) |

### Connexion découverte

```
Villa Thaifa → éligible Go Siyaha → candidature via Jisr → subvention 90% → finance HotelRunner/digitalisation
```

### Sources

- [Go Siyaha - MarocPME](https://marocpme.gov.ma/gosiyaha/)
- [Démarches Maroc - Go Siyaha](https://www.demarchesmaroc.com/go-siyaha/)
- [HotelRunner Morocco Partnership](https://hoteltechreport.com/news/hotelrunner-morocco)

---

## Context

Villa Thaifa (client) seeks to reduce dependency on Booking.com (~40% commission) by increasing direct bookings.

**NEW**: Go Siyaha program could finance up to 90% of digitalization costs, including HotelRunner setup and operations.

The portal **Jisr l'Mokawala** appears to be built on **Atlassian Jira Service Management**. We have client credentials (stored securely, not in this file).

**Security**: Zero secrets in outputs. Use environment variables.

---

## Objectives

### 🔴 Priority 0: Go Siyaha Eligibility (NEW)
- [ ] Confirm Villa Thaifa eligibility criteria for Go Siyaha
- [ ] Identify required documents for application
- [ ] Estimate potential subsidy amount (up to 90% of digitalization costs)
- [ ] Determine application deadlines/windows

### Business Objectives
- [ ] Reduce Booking.com dependency (increase direct bookings)
- [ ] Improve net margin and ROI
- [ ] Implement KPI tracking (conversion rate, acquisition cost, OTA vs direct)
- [ ] **NEW**: Use Go Siyaha subsidy to finance HotelRunner & digitalization

### Technical Objectives
- [ ] Verify if Jisr portal is API-integrable (Jira Service Management)
- [ ] Map portal endpoints and authentication methods
- [ ] Design fallback strategies (Email Plan B, RPA Plan C)
- [ ] Propose agentic architecture for automation

---

## Success Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Feasibility memo (1-2 pages) delivered | ⬜ | Document exists |
| 2 | API endpoints mapped (or confirmed inaccessible) | ⬜ | Technical report |
| 3 | Architecture diagram (text) for MVP | ⬜ | Document exists |
| 4 | Implementation plan (2-6 weeks) | ⬜ | Milestones defined |
| 5 | Client questions list (tech + business + security) | ⬜ | Questions documented |

---

## Constraints

- French language for deliverables
- Zero secrets in any output
- Respect portal CGU and security
- Client consent required for automation
- Execution-oriented approach

---

## Work Breakdown

### Phase 1: Functional Qualification
- Describe user journey (login, application creation, uploads, status)
- Clarify scope (applications/subsidies only? any booking flows?)
- List questions for client

### Phase 2: Technical Mapping
- Confirm Jira Service Management stack
- Identify endpoints (`/rest/servicedeskapi/`, `/rest/api/2/`)
- Document anti-bot mechanisms (CSRF, CAPTCHA, MFA, rate limits)

### Phase 3: API Feasibility (Priority 1)
- Non-intrusive exploration
- Test REST API accessibility
- Document authentication options
- Map permissions

### Phase 4: Plan B - Email Automation (Priority 2)
- Email listener architecture
- Parsing, deduplication, correlation
- Minimal data model

### Phase 5: Plan C - RPA (Last Resort)
- Playwright approach if needed
- Risks and governance

### Phase 6: Agentic Architecture Design
- Connectors layer
- Orchestrator layer
- Agents layer
- Knowledge base
- Observability
- Security

---

## Deliverables

1. Feasibility memo (Go/No-Go recommendation)
2. Architecture diagram (text format)
3. Implementation plan with milestones
4. Client questions list

---

## Source Brief

Full brief available at: `projects/thaifa/projects/jisr-mokawala/brief.md` (to be migrated)

---

## Execution Log

> Append-only. Add entries as work progresses.

### 2025-12-22

- Mission created from existing investigation brief

---

## Deviations

_None yet_

---

## Lessons Learned

_To be filled after completion_

---

_Mission v0.0.1-alpha.0_
