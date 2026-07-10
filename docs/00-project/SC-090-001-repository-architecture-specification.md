---
document_id: SC-090-001
title: Repository Architecture Specification
revision: 1.0
status: approved
owner: Configuration Management
approver: Spiros Netos
approval_date: 2026-07-10
baseline: B0
---

# SC-090-001 Repository Architecture Specification

## 1. Purpose

This specification defines how the `solarChaser` public GitHub repository stores, identifies, reviews, approves, releases, and preserves engineering information over the platform lifecycle.

## 2. Governing principles

1. The repository is the single source of truth.
2. One subject has one authoritative source; other documents link to it.
3. Stable paths represent current controlled information.
4. Git records history; revision-named duplicate folders are prohibited.
5. Approved decisions are preserved even when superseded.
6. Public content excludes secrets, sensitive personal data, and security-sensitive operational material.
7. The structure shall remain understandable to a maintainer unfamiliar with the project.

## 3. Repository structure

| Path | Controlled content |
|---|---|
| `.github/` | Issue forms, pull-request template, and repository automation |
| `docs/00-project/` | Charter, repository architecture, scope, and governance |
| `docs/10-requirements/` | System requirements and traceability |
| `docs/20-architecture/` | System, electrical, mechanical, software, and interface architecture |
| `docs/30-interfaces/` | Interface control documents and interface registers |
| `docs/40-decisions/` | ADRs and trade studies |
| `docs/50-risk/` | Risk register and risk analyses |
| `docs/60-design-reviews/` | Review packages, minutes, actions, and approvals |
| `docs/70-verification/` | Verification strategy and summary records |
| `docs/80-operations/` | Operations and maintenance source documents |
| `docs/90-configuration/` | Configuration-management plan, baselines, and change records |
| `docs/templates/` | Controlled authoring templates |
| `calculations/` | Reproducible engineering calculations, assumptions, and source data |
| `drawings/` | Diagram sources, CAD, exports, and drawing indexes |
| `hardware/` | Hardware design sources, fabrication data, and component integration |
| `software/` | Source code, configuration schemas, diagnostics, and tests |
| `verification/` | Executable procedures, evidence, logs, and test results |
| `operations/` | Field-use artifacts generated or maintained during operation |

Each top-level technical directory contains a README defining admissible content. Empty structure is represented by that README, not `.gitkeep` files.

## 4. Naming conventions

### 4.1 Controlled documents

Use `SC-NNN-NNN-short-title.md`:

- first group: document family;
- second group: document sequence within that family;
- title: lowercase kebab-case.

Examples: `SC-100-001-system-requirements.md`, `SC-400-001-electrical-power-architecture.md`.

### 4.2 Records and identifiers

| Artifact | Pattern | Example |
|---|---|---|
| Functional requirement | `FR-NNN` | `FR-014` |
| Non-functional requirement | `NFR-NNN` | `NFR-039` |
| ADR | `ADR-NNN-short-title.md` | `ADR-001-48v-house-architecture.md` |
| Trade study | `TS-NNN-short-title.md` | `TS-001-house-voltage-architecture.md` |
| Risk | `R-NNN` | `R-002` |
| Interface | `IF-NNN` | `IF-101` |
| Verification case | `VER-NNN` | `VER-007` |
| Design review | `DR-NNN` | `DR-003` |

Identifiers are never reused. Capitalization is preserved in prose; file names remain lowercase.

## 5. Document metadata

Every controlled Markdown document begins with YAML front matter:

```yaml
---
document_id: SC-NNN-NNN
title: Human-readable title
revision: 0.1
status: draft
owner: Responsible role or system
approver: null
approval_date: null
baseline: null
---
```

Allowed statuses are `draft`, `in-review`, `approved`, `superseded`, and `withdrawn`. Revision numbers describe document maturity; Git commits identify exact content. Approval fields must not be populated without Design Authority approval.

## 6. Baseline and release strategy

- `main` is the current controlled state.
- A **baseline** is an approved, immutable project snapshot.
- Baselines use signed or annotated Git tags where possible: `B0`, `B1`, `B2`, and so on.
- A matching GitHub release summarizes scope, approvals, known deviations, residual risks, and included document revisions.
- Planned progression is B0 repository foundation, B1 requirements baseline, B2 architecture baseline, B3 preliminary design baseline, and B4 build baseline. The Design Authority may revise this plan.
- Semantic software versions may coexist under `software/`; they do not replace engineering baselines.
- Corrections after a baseline occur through a new commit and, if the approved snapshot changes, a new baseline. Existing tags are never moved.

## 7. ADR workflow

1. Open an engineering-change issue describing context and affected requirements.
2. Create a proposed ADR for a significant, long-lived, cross-system, difficult-to-reverse, or principle-setting decision.
3. State alternatives, rationale, consequences, risks, and verification implications.
4. Review against requirements and architecture.
5. The Design Authority accepts, rejects, or defers the ADR.
6. Merge the ADR with all affected authoritative documents.
7. To replace a decision, mark it `superseded` and link both old and new ADRs.

Accepted ADRs are not edited to disguise changed reasoning. Minor factual corrections are permitted through normal review.

## 8. Risk workflow

1. Identify risk in cause–event–consequence form.
2. Allocate the next stable `R-NNN` identifier and an owner.
3. Assess probability and impact using the scales defined in the risk register.
4. Define treatments in preference order: eliminate, reduce, detect early, recover, accept.
5. Link mitigations to requirements, design elements, actions, and verification evidence.
6. Record residual probability, impact, and acceptance authority.
7. Review open high or critical risks at each design review.
8. Close a risk only when objective evidence supports closure; preserve its history.

## 9. Issue and pull-request workflow

Issue forms capture engineering changes, risks, and documentation defects. Pull requests describe requirement, architecture, interface, decision, risk, verification, and configuration impacts. Direct changes to `main` are reserved for the owner while the repository is small; branch protection should later require pull requests for significant changes.

## 10. Diagram standards

- Use Mermaid in Markdown for simple functional, sequence, state, and relationship diagrams that GitHub renders natively.
- Store complex editable sources in `drawings/src/`; store reviewable exports in `drawings/export/`.
- A diagram source and export share a stable drawing identifier and title.
- Use left-to-right flow for energy or process by default; label interfaces and units.
- Do not use colour as the only carrier of meaning.
- Include a legend where symbols or states are not self-evident.
- Electrical schematics must use recognized symbols, conductor identifiers, protection references, voltage domains, and revision metadata.
- Generated exports do not replace their editable source.

## 11. Cross-reference rules

- Use relative Markdown links, never links to a moving GitHub web branch when linking inside the repository.
- Link to the authoritative record at first material mention.
- Requirements link to responsible systems and verification methods through the traceability source.
- ADRs link to affected requirements, risks, interfaces, and documents.
- Risks link to mitigations and verification evidence.
- Avoid copying normative text. Quote only a short summary and link to the source.
- Renames must update inbound links in the same change.
- External references include title, owner/publisher, version or access date, and URL where available.

## 12. Configuration control

The [Configuration-Management Plan](../90-configuration/SC-900-001-configuration-management-plan.md) defines authorities, change classes, approvals, records, public-data restrictions, and recovery. GitHub is a configuration-management tool, not a substitute for engineering approval.

## 13. Verification of repository integrity

Before baseline approval:

- confirm working tree and remote state;
- check metadata and identifier uniqueness;
- check relative links and Mermaid rendering;
- confirm no sensitive information or generated clutter is committed;
- ensure changes to requirements, decisions, risks, interfaces, and verification remain synchronized;
- record review approval and create the immutable tag/release.
