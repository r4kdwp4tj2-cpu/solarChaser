# Changelog

This file records repository-level baselines and noteworthy engineering-package changes. Detailed file history remains in Git.

## [Unreleased]

### Added

- EM-006 and SC-410-001 electrical and solar preliminary design covering an 800 Wp 4S roof array, 48 V storage/distribution, dual 12 V buses, 3 kVA inverter/charger, shore control, monitoring and approval gates.
- Reproducible solar voltage/yield, electrical-core mass and cable voltage-drop calculations with an 18-line component BOM, 11-circuit cable schedule and automated verification.
- Proposed NFR-042 controlling the Design Authority's 200 kg roof-load input through vehicle-specific structural, dynamic, aerodynamic and approval evidence.
- SC-700-001 German-language MFK certification-evidence chapter and project-lifecycle evidence register for the cargo-van-to-motor-caravan conversion.
- EM-005 compliance applicability and approval strategy with a controlled Swiss/EU evidence register and eight approval gates.
- SC-095-001 Compliance Applicability Register distinguishing governing, conditional, supporting, and insufficient evidence.
- EM-004 reproducible battery chemistry and capacity trade study, generated results, and automated verification.
- EM-003 reproducible preliminary electrical load and energy budget, generated results, and automated verification.
- EM-002 record covering the technical-bay architecture and repository-governance decisions.
- ADR-004 accepting the under-bed technical-bay location, dual-access concept, and passive-ventilation baseline.
- SC-500-001 Mechanical Architecture establishing the dry toilet, under-bed technical bay, and opposite-side washing/water-service allocations.
- NFR-041 requiring synchronization of approved engineering decisions into the GitHub single source of truth.
- Engineering-meeting record and handover rules in the repository architecture and contribution guidance.
- ADR-003 selecting the Renault Master E-Tech electric L2H2, 87 kWh, 3.5 t as the vehicle platform.
- NFR-040 constraining registered permissible gross mass to 3500 kg and requiring licence compatibility for intended travel jurisdictions.
- SC-402-001 Technical Bay Preliminary Design, including zoning, serviceability, thermal, routing, diagnostic, safety, and verification concepts.
- Repository Architecture Specification.
- Stable repository structure and controlled-document metadata.
- Configuration-management and contribution guidance.
- GitHub issue and pull-request templates.
- ADR, risk, trade-study, document, and design-review templates.
- Initial requirements, architecture, decision, and risk records migrated from the Rev. 0.1 upload.

### Changed

- Raised the payload-growth risk because the preliminary complete electrical core is approximately 216.82 kg, including 68 kg of estimated ancillary installation mass.
- Added roof-solar attachment/ingress and approximately 164 V daylight-PV safety risks, and allocated TBR-023 through TBR-032 to the technical-bay design.
- Recorded Design Authority approval of SC-700-001 MFK Certification Evidence.
- Added proposed technical-bay compliance requirements for authority strategy, habitation electrical verification, configuration-matched product evidence, EMC assessment, and the as-built dossier.
- Established LFP as the approved house-battery chemistry baseline and accepted a 10.24 kWh / 74 kg representative packaging envelope without selecting a product.
- Added preliminary source-side planning envelopes for daily energy, continuous and peak load, and two-day nominal battery energy without selecting equipment.
- Clarified FR-003 as a dry Trelino toilet compartment without sink, shower, or plumbing.
- Allocated the technical bay under a permanent bed adjacent to the dry toilet, with top access for major work and removable side panels for routine service.
- Established passive low-inlet/high-outlet ventilation as the baseline while retaining a thermally justified fan provision.
- Corrected the EM-002 draft identifiers: the technical-bay decision is ADR-004 and repository synchronization is NFR-041 because ADR-003 and NFR-040 were already allocated.
- Replaced the rejected Fiat E-Ducato 4.2 t platform assumption with the Renault Master E-Tech electric L2H2 3.5 t baseline.
- Updated technical-bay measurement inputs and vehicle-interface risk for the Renault platform.
- Replaced the revision-named wrapper directory with stable authoritative paths.

## B0 — Repository foundation — 2026-07-10

- Established the repository as the project single source of truth.
- Preserved the accepted 48 V backbone and 20-year design-life decisions.

[Unreleased]: https://github.com/r4kdwp4tj2-cpu/solarChaser/compare/B0...HEAD
