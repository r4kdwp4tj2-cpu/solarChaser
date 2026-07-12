---
record_id: EM-002
title: Technical Bay Architecture and Repository Governance
revision: 0.1
status: in-review
meeting_authority: Spiros Netos
meeting_date: 2026-07-12
baseline: null
---

# EM-002 — Technical Bay Architecture and Repository Governance

## Purpose

Preserve the accepted engineering decisions developed after repository baseline B0 and define the controlled repository update submitted for Design Authority review.

This record summarizes decisions; it does not reproduce the full conversation. Acceptance of the engineering direction occurred in the project discussion. The pull request remains the Design Authority's review of whether the repository implements those decisions correctly.

## Decisions

| ID | Decision | Status | Authoritative implementation |
|---|---|---|---|
| D-001 | Locate the technical bay inside the van under a permanent bed, adjacent to the dry toilet compartment. | Approved | ADR-004; SC-402; SC-500 |
| D-002 | Define the toilet as a dry compartment with Trelino composting toilet and sanitary storage only; no sink, shower, fresh-water plumbing, or grey-water plumbing. | Approved | FR-003; SC-200; SC-500 |
| D-003 | Locate washing and water-service functions on the opposite side near the sliding door. | Approved | SC-200; SC-402; SC-500 |
| D-004 | Provide top access by lifting the mattress/bed platform for major work and removable side panels for routine service. | Approved | ADR-004; SC-402; SC-500 |
| D-005 | Use defined passive low-inlet/high-outlet ventilation as the baseline and reserve a temperature-controlled fan provision pending thermal justification. | Approved | ADR-004; SC-402; SC-500 |
| D-006 | Treat the technical bay as a professional, accessible, diagnosable, modular service compartment. | Approved | SC-402; SC-500 |
| D-007 | Confirm GitHub as the single source of truth; conversations remain working material. | Approved | SC-000; NFR-041 |
| D-008 | Require each engineering meeting that changes controlled information to produce a repository update and remain open until reviewed. | Approved | SC-000; NFR-041 |
| D-009 | Keep engineering reasoning in the engineering discussion and use GitHub review primarily for implementation correctness, consistency, and traceability. | Approved | This record; repository workflow |

## Identifier reconciliation

The earlier EM-002 draft proposed `ADR-003` for the technical-bay decision and `NFR-040` for repository synchronization. Both identifiers were already allocated in the repository. Configuration control prohibits reuse; therefore:

- the technical-bay decision is `ADR-004`;
- repository synchronization is `NFR-041`.

This is an administrative correction with no change to approved intent.

## Repository Update Package RUP-002

| Artifact | Change |
|---|---|
| SC-000-001 | Clarify meeting-to-repository governance and closure rule |
| SC-090-001 / CONTRIBUTING | Define engineering-meeting identifiers and synchronization workflow |
| SC-100-001 | Clarify FR-003 and add NFR-041 |
| SC-200-001 | Allocate dry toilet, remote water area, and under-bed technical bay |
| SC-402-001 | Implement accepted location, dual access, passive ventilation, interfaces, derived requirements, and open analyses |
| SC-500-001 | Create mechanical architecture for the accepted spatial relationships and service mechanics |
| SC-950-001 | Correct environmental assumptions and add repository-drift risk |
| ADR-004 | Record the accepted under-bed technical-bay decision |
| README / indexes / CHANGELOG | Add navigation, identifiers, and change summary |

## Risks

- R-002: liquid ingress remains credible, but not from plumbing in the adjacent dry toilet.
- R-006: under-bed thermal accumulation and high-power expansion require analysis and testing.
- R-009: selected location remains dimensionally, structurally, thermally, acoustically, and mechanically unverified.
- R-011: repository drift may cause approved decisions to exist only in conversation history.

## Open Action List OAL-002

### Engineering

- Complete the dimensioned Renault L2H2 habitation and technical-bay layout.
- Produce the energy/load and equipment-loss budgets.
- Calculate passive ventilation and define the thermal test plan.
- Develop the bed-platform, battery-restraint, and side-panel mechanical concepts.
- Establish representative battery and power-electronics envelopes.

### Design Authority

- Review the EM-002 pull-request diff for correctness, consistency, and traceability.
- Comment or request changes where the repository does not reflect the approved discussion.
- Approve and merge only when satisfied; do not approve unverified dimensions or thermal sizing merely by accepting the architecture.

## Review status

**Awaiting Design Authority pull-request review.** The meeting closes when the implementation is approved and merged to `main`. Technical calculations and open actions remain open work after meeting closure.
