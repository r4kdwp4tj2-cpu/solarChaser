---
record_id: EM-006
title: Electrical and Solar Preliminary Design
revision: 0.1
status: draft
meeting_authority: Spiros Netos
meeting_date: 2026-07-12
approver: null
approval_date: null
baseline: null
---

# EM-006 — Electrical and Solar Preliminary Design

## Purpose

Continue the engineering work from EM-003 through EM-005 by defining a complete preliminary house-electrical and roof-solar candidate system, its reproducible electrical and mass checks, and the gates required before procurement or installation.

The Design Authority supplied a 200 kg roof-load input. The project carries this value for planning while retaining vehicle-specific Renault/MFK confirmation as an open approval item.

## Engineering findings

1. The approved EM-003 load model requires approximately 2.61 kWh on the higher summer design day and 2.39 kWh on the winter design day.
2. An 800 Wp array at a 70% planning derate yields approximately 2.80 kWh/day under a 5.0 peak-sun-hour summer assumption, 1.68 kWh/day in a shoulder case and 0.84 kWh/day in a 1.5-hour winter case. The vehicle is solar-first, not solar-only.
3. Four compact 200 W modules fit within a 2549 × 1553 mm bounding rectangle before perimeter clearance. Actual roof feasibility remains unverified.
4. A 2S2P arrangement of the selected 31.3 V Vmp modules does not provide robust hot-voltage margin for a 48 V battery. A 4S1P string and 250 V-class MPPT provide the required preliminary voltage envelope.
5. The 4S string is approximately 164 V open circuit at the conservative -25 °C input. PV routing and isolation therefore require explicit high-voltage DC controls.
6. The fixed solar package is approximately 61.24 kg before reserved roof margin. A 75 kg roof allocation leaves 125 kg unallocated against the 200 kg project input, but neither local structure nor dynamic attachment is yet approved.
7. The complete electrical-core candidate is approximately 216.82 kg, including 68 kg of estimated ancillary mass. This materially constrains the 500 kg remaining-payload objective.
8. A 3 kVA / 2400 W continuous inverter candidate covers the current 1500 W AC peak with margin while avoiding the mass and standby burden of the 5 kVA class.
9. Two separate 30 A isolated 12 V converters permit essential/non-essential segregation and graceful degradation.
10. The vehicle-source charging path remains unpopulated; solar and authorized shore charging provide a complete baseline without assuming access to Renault traction HV or OEM 12 V power.

## Proposed decisions

These decisions are proposed for Design Authority review and are not approved by this draft record.

| ID | Proposed decision | Status | Implementation |
|---|---|---|---|
| D-027 | Carry 200 kg as the roof-load planning input while requiring vehicle-specific Renault/MFK evidence before roof release. | Proposed | SC-410; SC-500; NFR-042 |
| D-028 | Use four compact rigid 200 W modules in a 4S1P, 800 Wp packaging baseline. | Proposed | SC-410; calculation |
| D-029 | Use a 250 V MPPT class for the 4S array; carry SmartSolar 250/60-Tr as the packaging candidate. | Proposed | SC-410; BOM |
| D-030 | Carry a 48 V / 3 kVA inverter/charger, specifically MultiPlus-II 48/3000/35-32, as the packaging candidate. | Proposed | SC-410; BOM |
| D-031 | Use separate essential and non-essential 12 V buses, each supplied by an isolated 48/12 V 30 A converter. | Proposed | SC-410; SC-200 |
| D-032 | Use the Victron NG/Lynx/GX ecosystem as the integrated packaging baseline while preserving documented interfaces and requiring an alternate-source review before procurement. | Proposed | SC-410; BOM |
| D-033 | Keep the Renault vehicle-source charger absent from the baseline until written interface and approval evidence exists. | Proposed | SC-410; R-003 |
| D-034 | Set a 75 kg roof-equipment planning allocation for the solar package and roof service reserve within the 200 kg input. | Proposed | SC-410; calculation |

## Derived requirements

TBR-023 through TBR-032 are defined in [SC-410-001](../20-architecture/SC-410-001-electrical-and-solar-preliminary-design.md) and allocated to SC-402. NFR-042 adds the system-level roof-load constraint.

## Repository Update Package RUP-006

| Artifact | Change |
|---|---|
| SC-100-001 | Add roof-load requirement NFR-042 |
| SC-200-001 | Add detailed source/storage/distribution architecture allocation |
| SC-402-001 | Allocate TBR-023 through TBR-032 and candidate equipment envelopes |
| SC-410-001 | Add the complete electrical and solar preliminary design |
| SC-500-001 | Add roof integration and 200 kg planning boundary |
| SC-950-001 | Add roof-PV and high-voltage PV risks; strengthen payload risk |
| Calculations | Add BOM, cable schedule, solar/electrical calculation and generated results |
| Verification | Add executable solar, mass and cable checks |
| Indexes / changelog | Add navigation and change summary |

## Open Action List OAL-006

### Vehicle and compliance

- Obtain the exact CoC/eCoC and VIN-specific Renault body-builder manual.
- Obtain documentary evidence for the 200 kg roof limit and its load-distribution conditions.
- Agree roof mounting, penetrations, intermediate inspections and electrical evidence with MFK/APS.
- Confirm whether any approved vehicle-source charging interface exists.

### Mechanical and solar

- Measure and scan the usable roof surface, ribs, curvature, exclusions, hatch zones and cable route.
- Complete rigid-versus-lightweight module lifecycle and attachment trade study.
- Perform dynamic, aerodynamic uplift, fatigue, corrosion, ingress and service-access analyses.
- Recalculate cold/hot string values with the final module and mission temperature envelope.

### Electrical and safety

- Obtain exact battery prospective short-circuit data and complete fuse coordination.
- Close final conductor ampacity, protection, isolation, grounding and chassis-bonding design.
- Complete qualified 230 V design and Swiss initial-verification route.
- Build the configuration-matched product evidence and alternate-source matrix.
- Complete detailed loss/thermal analysis and technical-bay airflow sizing.

### Mass and packaging

- Replace every estimated BOM mass and cable length with quotation, measurement or drawing data.
- Complete the whole-vehicle itemized mass and axle-load budget before procurement.
- Demonstrate component access and removal using representative envelopes.

## Risks

- The 800 Wp roof rectangle may conflict with roof curvature, hatch/ventilation, safe edge clearance or service access.
- The 200 kg input may not be the applicable vehicle-specific dynamic roof limit.
- The series PV string remains energized at hazardous DC voltage in daylight.
- The complete conversion may not retain 500 kg payload after the approximately 217 kg electrical core.
- A single MPPT/string fault or shading can remove most solar generation.
- Product-family integration may create lifecycle or supplier concentration risk.

## Review status

**Engineering draft ready for Design Authority review.** No proposed decision, component purchase, roof work, wiring work, energization or vehicle-interface connection is approved by this record.
