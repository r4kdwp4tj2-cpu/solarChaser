---
record_id: EM-004
title: Battery Capacity and Chemistry Trade Study
revision: 0.1
status: draft
meeting_authority: Spiros Netos
meeting_date: 2026-07-12
approver: null
approval_date: null
baseline: null
---

# EM-004 — Battery Capacity and Chemistry Trade Study

## Purpose

Implement A-402-004 by selecting a preferred house-battery chemistry baseline and a packaging capacity envelope derived directly from the approved EM-003 load model.

This trade study does not select a product or authorize procurement. It narrows the design space for technical-bay geometry, mass, thermal management, BMS architecture, protection, and compliance work.

## Method

The controlled chemistry scores and weighted calculation are in [`calculations/`](../../calculations/README.md). Scores use 1 (least favorable) through 5 (most favorable). Criteria reflect an occupied, payload-constrained expedition vehicle with a 20-year service objective:

| Criterion | Weight | Reason |
|---|---:|---|
| Thermal safety | 25% | The battery is inside the occupied vehicle beneath a bed |
| Lifecycle | 15% | Supports the accepted 20-year platform objective and replaceable-module strategy |
| Mass and volume | 20% | Payload margin and technical-bay volume are constrained |
| Cold operation | 10% | Expedition use includes cold storage and operation |
| 48 V integration | 15% | Open, serviceable BMS and power-system integration are required |
| Power performance | 10% | Must support the EM-003 load envelope and charging sources |
| Availability and cost | 5% | Important, but subordinate to safety and feasibility at this stage |

Weights and scores are engineering judgments. They expose the decision logic; they are not safety certification or proof that any representative product is suitable for road-vehicle installation.

## Evidence and score rationale

### LFP — lithium iron phosphate

- Experimental abuse testing found LFP cells reacted later and at higher temperatures than NMC/NCA cells; pack-level design remains decisive and LFP can still vent or enter thermal runaway.
- A representative current 51.2 V LFP module provides 5.12 kWh at an estimated 37 kg, 2500 cycles to at least 80% capacity at 80% depth of discharge, and 100 A continuous discharge.
- That representative module permits discharge from -20 °C but charging only from +5 °C, making low-temperature charge inhibition and possibly controlled warming mandatory design concerns.
- Its BMS, serviceability, 48 V voltage range, and mounting provisions make LFP comparatively straightforward to integrate, but several listed safety certifications are pending and ECE R10 is EMC evidence rather than battery installation approval.

### LTO — lithium titanate

- Toshiba's representative 48 V industrial LTO pack is 1.113 kWh and approximately 16 kg, with a stated -30 °C to +45 °C use range and integrated protection.
- Toshiba publishes cell-dependent claims of at least 20,000 cycles, strong low-temperature charging, and low internal-short-circuit escalation risk.
- The representative pack has excellent cold and power performance but only about 70 Wh/kg before system-level installation; reaching the EM-003 energy target would require many packs, and approved parallel/system configuration is not established.
- The available representative product is described for industrial/AGV use, not accepted here as a road-vehicle house-battery solution.

### NMC — nickel manganese cobalt

- NMC offers the most favorable cell-level energy density and therefore the best mass/volume score.
- Comparative abuse testing shows earlier and more severe thermal-runaway behavior than LFP in the tested cells.
- No current 48 V NMC pack with documented serviceability, open integration, cold-charge control, and suitable vehicle-installation evidence has been established for this design.
- The energy-density advantage does not offset the occupied under-bed installation risk and lifecycle/integration penalties for the baseline.

## Ranked result

| Rank | Chemistry | Weighted score | Disposition |
|---:|---|---:|---|
| 1 | LFP | 4.20 / 5 | Preferred baseline |
| 2 | LTO | 3.75 / 5 | Retain as an extreme-cold alternative |
| 3 | NMC | 3.15 / 5 | Reject for the habitation baseline |

The result is robust to modest weight changes between LFP and NMC. LTO can overtake LFP only if extreme-cold operation and cycle life are assigned substantially more value than payload, volume, integration, and availability.

## Capacity result

EM-003 provides 2.608 kWh/day as the current governing load and 7.173 kWh as the minimum nominal planning energy for two days, 10% contingency, and 80% usable energy. At 51.2 V nominal, the minimum is approximately 140 Ah.

A representative packaging envelope of two 51.2 V, 100 Ah LFP modules gives:

| Parameter | Envelope value |
|---|---:|
| Nominal energy | 10.24 kWh |
| Battery-only mass | 74 kg |
| Usable-energy operating duration with 10% load contingency | 2.86 days |
| EM-003 arithmetic peak current at nominal voltage | 44.1 A |

This envelope deliberately rounds up to a plausible modular arrangement. The 10.24 kWh value is not a capacity requirement or product decision. The weight budget must also include BMS, isolation, protection, busbars, cables, enclosure, restraint, thermal provisions, and service clearances.

## Proposed decisions

| ID | Decision | Status | Authoritative implementation |
|---|---|---|---|
| D-015 | Use LFP as the preferred house-battery chemistry baseline. | Proposed | Trade calculation; SC-402 |
| D-016 | Retain LTO only as an alternative if controlled mission requirements make sub-zero charging dominant enough to justify its mass, volume, integration, and availability penalties. | Proposed | This record |
| D-017 | Reject NMC as the baseline for the occupied under-bed technical bay. | Proposed | This record; R-012 |
| D-018 | Carry 7.173 kWh / 140 Ah at 51.2 V as the minimum nominal planning result and 10.24 kWh / 74 kg battery-only as the representative two-module packaging envelope. | Proposed | Generated result; SC-402 |
| D-019 | Require independent low-temperature charge inhibition, temperature monitoring, hardware protection, manual isolation, and a controlled thermal/venting concept before battery layout approval. | Proposed | SC-402; R-012 |

## Compliance boundary

- IEC 62619:2022 addresses industrial secondary-lithium battery safety and explicitly excludes road vehicles when a vehicle-specific standard applies; it is useful evidence but not automatically sufficient.
- UN Regulation No. 100 addresses rechargeable energy storage associated with electric powertrains. Applicability to a conversion-installed auxiliary house battery must be determined rather than assumed.
- ECE R10 evidence addresses electromagnetic compatibility, not the full mechanical, electrical, fire, thermal, or installation safety case.
- UN transport testing, Swiss vehicle requirements, body-builder rules, insurer expectations, installation standards, and product-specific certifications remain part of A-402-005.

## Sources

- Victron Energy, [Lithium NG 51.2 V technical data](https://www.victronenergy.com/media/pg/Lithium_NG_battery_51%2C2_V/en/technical-data.html), accessed 2026-07-12.
- Toshiba, [SCiB industrial pack specifications](https://www.global.toshiba/ww/products-solutions/battery/scib/product-next/product/module/sip.html), accessed 2026-07-12.
- Toshiba, [SCiB product catalogue](https://www.global.toshiba/content/dam/toshiba/ww/products-solutions/battery/scib/pdf/SCiB_toshiba_en.pdf), accessed 2026-07-12.
- IEC, [IEC 62619:2022 scope and publication data](https://webstore.iec.ch/en/publication/64073), accessed 2026-07-12.
- UNECE, [UN Regulation No. 100 Revision 3](https://unece.org/transport/documents/2022/03/standards/regulation-no-100-rev3), accessed 2026-07-12.
- Koch et al., [Thermal and Mechanical Safety Assessment of Type 21700 Lithium-Ion Batteries with NMC, NCA and LFP Cathodes](https://doi.org/10.3390/batteries9050237), 2023.

## Repository Update Package RUP-004

| Artifact | Change |
|---|---|
| Battery chemistry CSV | Add auditable trade scores and dispositions |
| Python calculation | Add deterministic weighted ranking and capacity derivation from EM-003 |
| Generated result | Add human-readable ranking and capacity envelope |
| Verification test | Add ranking and cross-calculation consistency checks |
| SC-402-001 | Add chemistry and capacity planning baseline; update A-402-004 |
| SC-950-001 | Add house-battery thermal, venting, and low-temperature charging risk |
| README / indexes / CHANGELOG | Add navigation and change summary |

## Open Action List OAL-004

### Engineering

- Confirm mission minimum and maximum battery temperatures, storage states, and required sub-zero behavior.
- Determine applicable Swiss/EU installation, transport, EMC, fire, and vehicle requirements under A-402-005.
- Establish at least two eligible LFP product families with verified certifications, BMS behavior, interfaces, serviceability, mounting orientation, parallel limits, and supplier support.
- Measure or model the 10.24 kWh / 74 kg representative envelope in the technical bay, including removal path and installed ancillary mass.
- Develop low-temperature charge inhibition and, if justified, controlled pre-heating without depending solely on supervisory software.
- Perform cell-to-pack thermal propagation, vent-gas routing, fault-current, isolation, and emergency-response analyses.
- Update capacity after controlled mission profiles, candidate equipment, solar/charging studies, and payload analysis mature.

### Design Authority

- Review the criteria, weights, evidence, proposed decisions, and representative capacity envelope.
- Accept, correct, or reject RUP-004.
- After acceptance, merge the synchronized pull request to close the meeting's repository action.

## Review status

**Implementation complete; awaiting Design Authority review.** Approval would select LFP as the chemistry baseline and accept the stated planning envelope and safety constraints, but would not select a supplier, product, or procurement configuration.
