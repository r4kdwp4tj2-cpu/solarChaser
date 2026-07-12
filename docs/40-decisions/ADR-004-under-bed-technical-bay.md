---
record_id: ADR-004
title: Under-Bed Technical Bay
revision: 1.0
status: accepted
decision_authority: Spiros Netos
decision_date: 2026-07-12
baseline: null
---

# ADR-004 — Under-Bed Technical Bay

## Context

The preliminary technical-bay document defined functional zones but left the vehicle location open pending layout work. In EM-002 the Design Authority clarified the intended habitation arrangement:

- the toilet compartment is dry and contains only a Trelino composting toilet and sanitary storage;
- washing and water systems are on the opposite side near the sliding door;
- the technical bay belongs inside the van under a permanent bed, adjacent to the dry toilet;
- large equipment should be reached by lifting the mattress and bed platform;
- routine equipment should be reached through removable ventilated side panels.

The EM-002 draft proposed `ADR-003` for this decision. That identifier was already allocated to the Renault vehicle-platform decision and cannot be reused under configuration-control rules. This record therefore uses the next free identifier, `ADR-004`.

## Decision drivers

- Direct and repeatable maintenance access under NFR-029.
- Major removal path for battery and large power modules.
- Short, inspectable high-current paths within a concentrated technical volume.
- Separation from the remote washing and water-service area.
- Use of otherwise enclosed under-bed volume without consuming primary living space.
- Passive heat rejection without relying immediately on a fan.
- Compatibility with modular mounting, diagnostics, labelling, and a 20-year service life.

## Decision

Locate the technical bay inside the van under a permanent bed, adjacent to the dry toilet compartment.

Provide two complementary access paths:

1. liftable mattress and bed platform for battery replacement, large-module removal, structural inspection, and major work;
2. removable side service panels for routine inspection, isolation, protection access, diagnostics, safe measurement, and designated small-module replacement.

Use passive ventilation as the baseline through a defined low inlet and high outlet connected to the general living-space air volume. Reserve physical and electrical provision for a quiet temperature-controlled extraction fan, but install or require the fan only if thermal analysis and testing justify it.

Do not route toilet plumbing—none exists—or washing/water pipework through or above the technical bay. The remote water-service area near the sliding door interfaces only through intentionally protected power and signal routes.

## Consequences

- The accepted location replaces the earlier open candidate-location decision in SC-402.
- The bed platform becomes a structural and service component requiring a positive open-position support and verified load capacity.
- Side panels require reusable fasteners, guarding, labelling, rattle control, and integrated grilles.
- Mattress, bedding, storage, and decorative panels must not obstruct access or airflow.
- Grille net free area and fan need remain calculation and test outputs rather than arbitrary hole patterns.
- Equipment layout must address sleeping-area noise and structure-borne vibration.
- The dry toilet adjacency removes the earlier assumption of an adjacent wet bathroom but does not eliminate general condensation, spill, exterior-ingress, or remote plumbing risks.
- Exact feasibility remains conditional on measured Renault L2H2 geometry, equipment envelopes, mass distribution, structural restraint, and thermal validation.

## Alternatives considered

### Scattered equipment throughout the vehicle

Rejected because it increases wiring length, fragments diagnostics, complicates access, and weakens the technical-bay service concept.

### Technical bay next to the remote washing/water-service area

Not selected because the agreed under-bed location beside the dry toilet provides better separation from routine plumbing while retaining interior access.

### Top access only

Rejected because routine inspection would require disturbing the bed and mattress.

### Side access only

Rejected because the battery and other large modules may not have an adequate removal path.

### Mandatory forced ventilation from the outset

Deferred because fan need and size must follow a loss budget and thermal test; passive airflow is simpler and avoids an unnecessary dependency if sufficient.

## Risks and mitigations

- **Thermal accumulation:** defined convection path, loss budget, grille calculation, temperature sensing, instrumented testing, optional fan provision, and load derating.
- **Blocked ventilation:** grille placement clear of bedding and storage, guards, inspection, and diagnostic temperature monitoring.
- **Service injury or falling platform:** positive mechanical support and documented isolation/service states.
- **Noise under sleeping area:** low-loss equipment, vibration-isolated mounts where suitable, fan acoustic criteria, and operating-mode tests.
- **Structural or mass-distribution shortfall:** measured layout, vehicle-approved restraint concept, mass budget, axle analysis, and staged weighing.
- **Liquid ingress despite dry adjacency:** remote plumbing, protected cable routes, raised/guarded equipment where justified, and inspection for general cabin ingress sources.

## Verification implications

Before preliminary layout approval:

1. measure and model the selected under-bed volume and removal paths;
2. demonstrate side-panel routine access and top-access major removal with representative envelopes;
3. calculate structural and restraint loads for the bay and bed platform;
4. complete the thermal loss budget and passive-ventilation calculation;
5. test temperature under declared worst credible conditions;
6. check grille obstruction with normal bedding and storage installed;
7. verify mass, centre of mass, axle distribution, and remaining payload;
8. inspect labels, guards, fasteners, and wiring/document traceability.

## Traceability

- Requirements: [FR-014, FR-033 through FR-038, NFR-027 through NFR-029, NFR-035, and NFR-037 through NFR-039](../10-requirements/SC-100-001-system-requirements.md)
- System architecture: [SC-200-001](../20-architecture/SC-200-001-system-architecture.md)
- Technical-bay design: [SC-402-001](../20-architecture/SC-402-001-technical-bay-preliminary-design.md)
- Mechanical architecture: [SC-500-001](../20-architecture/SC-500-001-mechanical-architecture.md)
- Risks: [R-001, R-002, R-006, and R-009](../50-risk/SC-950-001-risk-register.md)
- Meeting: [EM-002](../60-design-reviews/EM-002-technical-bay-and-repository-governance.md)
