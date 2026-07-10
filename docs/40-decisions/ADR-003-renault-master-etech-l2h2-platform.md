---
record_id: ADR-003
title: Renault Master E-Tech Electric L2H2 Vehicle Platform
revision: 1.0
status: accepted
decision_authority: Spiros Netos
decision_date: 2026-07-10
baseline: null
---

# ADR-003 — Renault Master E-Tech Electric L2H2 Vehicle Platform

## Context

The preliminary project material assumed a Fiat E-Ducato L3H2 and later considered a 4.2 t configuration. The Design Authority was informed that the 4.2 t vehicle is governed to 90 km/h and that intended international operation would require C1 driving entitlement. Both consequences are unacceptable to the customer.

The project therefore returns to the original Renault concept using a 3.5 t vehicle. Official Renault Switzerland information current on 2026-07-10 offers the Master E-Tech electric panel van in L2H2, 87 kWh Long Range, 3.5 t configuration.

The Fiat speed and cross-border licence statements are recorded as customer-supplied decision inputs. They have not been independently established here as universal facts for every homologation and jurisdiction; the decision does not depend on retaining the Fiat alternative.

## Decision drivers

- No C1 licence dependency for intended operation.
- Registered permissible gross mass no greater than 3500 kg.
- Suitable electric panel-van package in Switzerland.
- L2H2 size compatible with the intended compact living concept.
- Acceptable driving performance for international motorway travel, to be quantified.
- Ability to retain at least 500 kg remaining payload after conversion.
- Long-term maintainability, body-builder support, and an approved auxiliary-energy interface.

## Decision

Select the **Renault Master E-Tech electric panel van, L2H2, 87 kWh Long Range, 3.5 t** as the SYS-100 vehicle-platform baseline.

Reject the Fiat E-Ducato 4.2 t platform for this project. Fiat-specific assumptions and interfaces are removed from current design documents but remain visible in Git history and this decision rationale.

## Supplier inputs requiring confirmation

Renault Switzerland currently publishes for L2H2:

- 5681 mm overall length;
- 2500 mm overall height;
- 3225 mm maximum load-floor length;
- 1885 mm interior height;
- 10.8 m³ load volume;
- 3500 kg permissible gross mass option;
- average payload range 844–1132 kg across configurations.

None of these values substitutes for the exact ordered vehicle's Certificate of Conformity, registration document, axle limits, running-order mass, or physical measurement.

## Consequences

- All packaging work changes from L3H2 to Renault L2H2 dimensions.
- The shorter 3225 mm load floor materially tightens the bed, toilet, storage, technical-bay, and circulation layout.
- The 3.5 t limit protects the licence objective but makes mass control more demanding.
- NFR-027 requires a conversion mass budget derived from the exact vehicle mass; Renault's generic payload range is insufficient for acceptance.
- Vehicle mounting, HV exclusion zones, roof loading, towing, body penetrations, and auxiliary electrical interfaces must be re-established using Renault-approved information.
- Existing 48 V house architecture remains unchanged unless Renault interface evidence forces a controlled change.
- The technical-bay location study restarts using Renault L2H2 measurements.

## Risks and mitigations

- **Payload shortfall:** obtain the exact base-vehicle mass and option list before purchase; allocate a conversion mass ceiling; preserve contingency; weigh at controlled build stages.
- **Packaging shortfall:** produce a measured 3D layout and validate both permanent beds, toilet, service access, and removal paths before fixing architecture.
- **Vehicle-interface uncertainty:** use only Renault/body-builder-approved interfaces and retain solar plus shore charging as independent sources.
- **Unverified speed capability:** obtain the governed speed and motorway performance in writing for the exact homologated configuration before purchase.
- **Licence interpretation:** confirm the completed registration classification and intended-country entitlement with competent authorities before purchase and travel.

## Verification implications

Before vehicle procurement approval:

1. inspect the exact configuration quotation and Certificate of Conformity data;
2. verify 3500 kg permissible gross mass and category-B compatibility for the intended jurisdictions;
3. verify governed/top speed against an approved quantified requirement;
4. close a preliminary mass budget demonstrating a credible path to NFR-027;
5. validate the L2H2 packaging concept using measured or manufacturer-controlled geometry;
6. identify Renault conversion guidance and approved electrical interfaces.

## Traceability

- Requirements: [NFR-027, NFR-028, and NFR-040](../10-requirements/SC-100-001-system-requirements.md)
- Architecture: [SC-200-001](../20-architecture/SC-200-001-system-architecture.md)
- Technical bay: [SC-402-001](../20-architecture/SC-402-001-technical-bay-preliminary-design.md)
- Risks: [R-001, R-003, R-009, and R-010](../50-risk/SC-950-001-risk-register.md)

## External references

- Renault Switzerland, [Master E-Tech electric L2H2 configurator](https://de.business.renault.ch/business-range-master/kastenwagen-etech-electric/konfigurator.html), accessed 2026-07-10.
- Renault Switzerland, [Master panel-van dimensions](https://de.business.renault.ch/business-range-master/kastenwagen.html), accessed 2026-07-10.
- ASTRA, [Information on the Swiss driving licence](https://www.astra.admin.ch/dam/astra/de/dokumente/abteilung_strassenverkehrallgemein/information-schweizer-fuehrerausweis.pdf.download.pdf/Information%20Schweizer%20F%C3%BChrerausweis.pdf), accessed 2026-07-10.
