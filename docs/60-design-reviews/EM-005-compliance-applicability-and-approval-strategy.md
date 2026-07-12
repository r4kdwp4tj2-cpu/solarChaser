---
record_id: EM-005
title: Compliance Applicability and Approval Strategy
revision: 0.1
status: draft
meeting_authority: Spiros Netos
meeting_date: 2026-07-12
approver: null
approval_date: null
baseline: null
---

# EM-005 — Compliance Applicability and Approval Strategy

## Purpose

Implement the first controlled response to A-402-005 by distinguishing governing Swiss vehicle approval, habitation electrical design standards, EMC evidence, battery product evidence, dangerous-goods transport evidence, and vehicle-specific authority decisions.

The result is [SC-095-001 Compliance Applicability Register](../00-project/SC-095-001-compliance-applicability-register.md). It defines preliminary applicability, evidence owners, eight approval gates, and the questions that require written authority answers.

## Findings

1. The conversion approval route is vehicle- and canton-specific. It shall be agreed with the responsible cantonal road-traffic authority before irreversible work.
2. The exact CoC/eCoC, registration category, body designation, Renault body-builder constraints, mass/axle data, and conversion scope are controlling inputs.
3. IEC 60364-7-721:2017 is the appropriate preliminary design baseline for fixed habitation-purpose circuits, but the project must confirm the applicable Swiss NIN adoption, inspection, and installer route.
4. UN R10 and the ASTRA electrical-safety/EMC guidance inform component and completed-vehicle EMC evidence. Component approval does not by itself validate the integrated installation.
5. UN R100 primarily addresses electric-powertrain energy storage. The Renault HV system remains OEM-controlled; house-battery applicability must be decided by the authority rather than assumed.
6. IEC 62619 product evidence and UN 38.3 transport-test evidence are useful battery screening inputs but do not approve the under-bed installation.
7. As-built workmanship, restraint, mass, drawings, settings, labels, tests, photographs, deviations, and qualified sign-offs are approval evidence in their own right.

## Proposed decisions

| ID | Decision | Status | Authoritative implementation |
|---|---|---|---|
| D-020 | Control compliance applicability and evidence through SC-095-001 rather than informal checklists. | Proposed | SC-095-001 |
| D-021 | Obtain a written pre-application approval strategy from the responsible canton and any required ASTRA-recognized test centre before layout freeze or irreversible modification. | Proposed | CA-001/002; CG-01 |
| D-022 | Use IEC 60364-7-721:2017 as the preliminary design baseline for fixed habitation-purpose electrical circuits, subject to confirmation of the current Swiss implementation and inspection route. | Proposed | CA-004/005; CG-03 |
| D-023 | Require an EMC evidence matrix and completed-system change-impact assessment; do not treat individual E-marks or declarations as proof of integrated compatibility. | Proposed | CA-006/007; CG-05 |
| D-024 | Keep the OEM traction-HV system outside the house architecture and treat UN R100 as conditional/supporting evidence for the separate house battery unless the authority decides otherwise. | Proposed | CA-008; SC-402 |
| D-025 | Require a current UN 38.3 test summary for the exact battery type as transport evidence while explicitly rejecting it as installed-system approval. | Proposed | CA-010; CG-04 |
| D-026 | Prohibit layout-dependent procurement and concealed installation until the applicable approval gate is closed with configuration-matched evidence. | Proposed | SC-095-001 |

## Proposed derived requirements

| ID | Proposed requirement | Verification concept |
|---|---|---|
| TBR-018 | The project shall obtain and retain the written approval strategy, evidence list, and inspection stages agreed with the responsible Swiss authority before irreversible conversion work. | Record inspection |
| TBR-019 | The fixed 230 V habitation installation shall be designed, installed, inspected, and tested against the confirmed Swiss implementation of the applicable caravan/motor-caravan electrical standard by qualified persons. | Design review and installation certificate |
| TBR-020 | Every safety- or approval-relevant electrical product shall have configuration-matched evidence covering exact part number, firmware/BMS, accessories, environmental limits, mounting, and certificate scope. | Evidence-matrix audit |
| TBR-021 | EMC compliance shall be assessed for the completed conversion and shall include component evidence, installation controls, change-impact analysis, and testing where required by the approval authority. | EMC dossier review |
| TBR-022 | The as-built approval dossier shall include drawings, configuration, protection settings, labels, torque/inspection records, electrical tests, mass/axle evidence, photographs, deviations, and required sign-offs. | Dossier audit |

## Repository Update Package RUP-005

| Artifact | Change |
|---|---|
| SC-095-001 | Add controlled applicability matrix, approval gates, authority questions, sources, and open items |
| SC-402-001 | Reference the compliance register, allocate derived requirements, and update A-402-005 |
| SC-950-001 | Add approval-path and evidence-scope risk |
| README / indexes / CHANGELOG | Add navigation and change summary |

## Risks

- Legal or standards applicability can change with vehicle category, canton, installation configuration, and submission date.
- A component certificate may not cover the installed part number, firmware, accessories, mounting, or environment.
- A safe design may still be unregistrable if inspection sequencing or evidence is agreed too late.
- A product marketed for industrial, marine, stationary, or automotive use may not be acceptable for this specific house-battery installation.
- Concealed work may have to be reopened if intermediate inspection evidence is missing.

## Open Action List OAL-005

### Engineering

- Obtain the exact ordered-vehicle CoC/eCoC, VIN-specific data, and current Renault body-builder documentation.
- Identify the responsible cantonal road-traffic authority and submit the seven SC-095 pre-application questions with concept drawings.
- Ask the authority whether and when an ASTRA-recognized test centre must be engaged.
- Obtain the current Swiss NIN/IEC requirements through a qualified electrical designer or inspector and define the fixed 230 V verification plan.
- Build the configuration-matched component and evidence matrix before candidate-product down-selection.
- Update SC-095 with written authority responses and exact current legal clauses.

### Design Authority

- Review the applicability classes, approval gates, authority questions, proposed decisions, and derived requirements.
- Accept, correct, or reject RUP-005.
- After acceptance, merge the synchronized pull request to close the meeting's repository action.

## Review status

**Implementation complete; awaiting Design Authority review and external authority confirmation.** Approval establishes the project compliance strategy; it does not represent legal advice, authority acceptance, or installation certification.
