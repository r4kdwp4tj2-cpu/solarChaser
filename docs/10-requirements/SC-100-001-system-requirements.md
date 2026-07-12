---
document_id: SC-100-001
title: System Requirements Specification
revision: 0.5
status: draft
owner: Systems Engineering
approver: null
approval_date: null
baseline: null
---

# SC-100-001 System Requirements Specification

## Status and scope

This draft preserves the accepted requirements captured in the earlier engineering discussion. It is not yet a complete requirements baseline. Unlisted earlier candidate requirements require consolidation, conflict review, verification-method allocation, and Design Authority approval before B1.

## Accepted functional requirements

| ID | Requirement | Primary allocation | Verification concept |
|---|---|---|---|
| FR-001 | The camper shall provide two independent permanent beds, each with a minimum sleeping area of 1800 mm × 700 mm, without requiring daily conversion from another function. | Habitation | Inspection and measurement |
| FR-003 | The camper shall provide a dry toilet compartment containing a Trelino composting toilet and sanitary-item storage, with no sink, shower, fresh-water plumbing, or grey-water plumbing. | Habitation; Water and Sanitary | Inspection |
| FR-004 | The camper shall provide an outside shower. | Water and Sanitary; Body and Openings | Demonstration |
| FR-005 | The camper shall support portable gas cooking without a fixed gas installation. | Cooking and Food; Safety | Inspection and demonstration |
| FR-007 | The camper shall provide usable fresh-water storage of not less than 40 L and not more than 50 L. | Water and Sanitary | Fill-and-measure test |
| FR-008 | The camper shall provide usable grey-water storage of at least 80% of the usable fresh-water capacity. | Water and Sanitary | Fill-and-measure test |
| FR-011 | The camper shall provide 230 V AC shore-power charging whose activation is commanded by the captain rather than used as the normal automatic source. | Electrical Power; Resource Management; Human Interface | Functional test |
| FR-014 | The camper shall use a 48 V DC house electrical backbone with derived lower-voltage buses where required. | Electrical Power | Design inspection and test |
| FR-033 | House batteries shall normally charge from solar energy; when solar is insufficient, charging from an approved vehicle or traction-energy interface shall be possible; shore charging requires captain authorization. | Vehicle Interface; Electrical Power; Resource Management | Scenario-based functional test |
| FR-034 | The camper shall provide an integrated check program that enables the captain to identify failed or degraded systems. | Monitoring and Diagnostics | Fault-insertion demonstration |
| FR-035 | Diagnostics shall provide at least `OK`, `Warning`, and `Fault` health states. | Monitoring and Diagnostics; Human Interface | Functional test |
| FR-036 | Diagnostics shall record active and historical faults with timestamp, affected subsystem, and suggested action. | Monitoring and Diagnostics | Functional test |
| FR-037 | Diagnostics shall support a manually initiated full-system check. | Monitoring and Diagnostics; Human Interface | Demonstration |
| FR-038 | Diagnostics shall distinguish energy-source, storage, distribution, and load faults where practical. | Monitoring and Diagnostics | Fault-insertion test |
| FR-039 | Monitoring shall provide predictive notifications where practical before operational limits are reached. | Resource Management; Monitoring | Scenario test and analysis |
| FR-040 | Resource Management shall use surplus renewable energy whenever practical according to configured policy and available safe storage or consumption options. | Resource Management; Electrical Power | Scenario test |
| FR-041 | Resource Management shall estimate and display remaining operational autonomy for the current operating mode using available energy, recent consumption, and expected generation where practical. | Resource Management; Human Interface | Analysis and scenario test |

## Accepted non-functional requirements

| ID | Requirement | Primary allocation | Verification concept |
|---|---|---|---|
| NFR-001 | Software architecture shall use open and documented interfaces where practical. | Software and Data | Design review |
| NFR-002 | Hardware shall use open or standard interfaces where practical. | All technical systems | Design review |
| NFR-004 | Widely available components shall be preferred. | Configuration and Lifecycle | Trade-study review |
| NFR-007 | Maintenance access shall be simple. | Physical Architecture; Maintenance | Inspection |
| NFR-011 | Reliability shall take precedence over unnecessary complexity. | All systems | Architecture review |
| NFR-013 | Parasitic electrical loads shall be minimized. | Electrical Power; Monitoring | Measurement |
| NFR-017 | Replaceable and serviceable modules shall be preferred. | All technical systems | Inspection and replacement demonstration |
| NFR-021 | The electrical design shall be safe and inspection-ready. | Electrical Power; Safety | Compliance review and test |
| NFR-027 | With permanently installed equipment fitted and operating fluids except fresh water at their defined reference condition, the completed vehicle shall retain at least 500 kg certified available payload under the applicable registration basis. | Vehicle Platform; Weight Management | Certified weighbridge measurement |
| NFR-028 | A weight budget shall record every component over 0.5 kg with mass, mounting location, and cumulative impact. | Weight Management | Record inspection |
| NFR-029 | Electrical and electronic components shall permit safe, direct access for inspection, maintenance, replacement, and troubleshooting without dismantling fixed furniture or unrelated systems. | Electrical Power; Monitoring; Physical Architecture | Inspection and maintenance demonstration |
| NFR-030 | Common faults shall be diagnosable without specialized test equipment; the check program shall identify the affected system or subsystem and, where practical, recommend corrective action. | Monitoring and Diagnostics | Fault-insertion demonstration |
| NFR-031 | Diagnostics shall not prevent manual operation of essential loads unless safety requires shutdown. | Monitoring and Diagnostics; Safety | Fault-insertion test |
| NFR-032 | Diagnostic data shall be stored locally and exportable in a human-readable format. | Software and Data | Inspection and export test |
| NFR-033 | Diagnostic interfaces shall be open or documented where practical. | Software and Data | Design review |
| NFR-034 | Fault messages shall use the same physical component identifiers as wiring and mechanical documentation. | Diagnostics; Configuration Management | Traceability inspection |
| NFR-035 | Major subsystems shall be understandable to a technically competent owner using project documentation without relying on proprietary manufacturer knowledge. | All systems; Documentation | Review and owner demonstration |
| NFR-037 | The electrical architecture shall support future higher-power loads, including a larger inverter and possible induction cooking, without redesigning the complete house electrical system. | Electrical Power | Architecture review and capacity analysis |
| NFR-038 | Each subsystem shall minimize standby power consumption. | All powered systems | Measurement |
| NFR-039 | The platform shall support at least 20 years of normal recreational operation with scheduled maintenance; wear items and electronic components may be replaced without architectural redesign. | All systems; Configuration and Lifecycle | Lifecycle analysis and design review |
| NFR-040 | The completed vehicle shall have a registered permissible gross mass not exceeding 3500 kg and shall be legally operable by the captain without a C1 licence in every intended travel jurisdiction. | Vehicle Platform; Compliance; Weight Management | Registration-document inspection and jurisdiction review |
| NFR-041 | The GitHub engineering repository shall remain synchronized with all approved requirements, architectural decisions, and engineering-meeting outcomes; no approved engineering decision shall exist solely in conversation history. | Configuration Management; Documentation | Meeting-to-repository traceability inspection |

## Proposed non-functional requirements for B1

| ID | Proposed requirement | Primary allocation | Verification concept |
|---|---|---|---|
| NFR-042 | Permanently installed roof equipment shall not exceed the lower of 200 kg and the vehicle-specific allowance confirmed by Renault and the approval authority; its load distribution, attachment, dynamic loading, aerodynamic uplift, fatigue, corrosion resistance and watertightness shall be verified before installation release. | Vehicle Platform; Physical Architecture; Electrical Power; Compliance | Manufacturer/authority evidence, structural analysis, inspection and staged weighing |

## Traceability work required before B1

- Reconcile all earlier candidate FR and NFR entries, including numbering gaps.
- Define terms such as “practical,” “common fault,” “essential load,” and reference payload condition.
- Allocate each requirement to one accountable system owner and all participating systems.
- Establish verification cases and acceptance criteria.
- Identify applicable Swiss vehicle, electrical, gas-storage, and registration constraints using authoritative sources.
- Resolve whether occasional grandchildren sleeping remains a requirement and specify its measurable form.
- Quantify the minimum acceptable governed/top speed and motorway cruise capability; the rejected 90 km/h limit is currently a platform decision driver, not yet a testable requirement.
- Confirm how NFR-027's 500 kg remaining payload is calculated for the Renault 3.5 t registration basis, including occupants, water, optional equipment, and statutory mass definitions.
- Confirm and accept or revise the 200 kg roof-load input and NFR-042 using vehicle-specific Renault and MFK/APS evidence.

Architectural decisions are recorded separately in [ADR-001](../40-decisions/ADR-001-48v-house-architecture.md), [ADR-002](../40-decisions/ADR-002-platform-design-life.md), and [ADR-003](../40-decisions/ADR-003-renault-master-etech-l2h2-platform.md).

The technical-bay physical concept is recorded in [ADR-004](../40-decisions/ADR-004-under-bed-technical-bay.md) and allocated through [SC-402-001](../20-architecture/SC-402-001-technical-bay-preliminary-design.md) and [SC-500-001](../20-architecture/SC-500-001-mechanical-architecture.md).

The proposed electrical and roof-solar design is controlled in [SC-410-001](../20-architecture/SC-410-001-electrical-and-solar-preliminary-design.md) and [EM-006](../60-design-reviews/EM-006-electrical-and-solar-preliminary-design.md).
