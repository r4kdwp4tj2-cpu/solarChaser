---
document_id: EM-007
title: EcoFlow Minimal Electrical Alternative Review
revision: 0.1
status: draft
owner: Electrical Power
approver: null
approval_date: null
baseline: null
---

# EM-007 EcoFlow Minimal Electrical Alternative Review

## Review question

Can a minimal, predominantly EcoFlow fixed power system serve the specified camper loads while charging solar-first, then from shore, with Renault Master E-Tech 230 V V2L as backup?

## Finding

Yes as a draft alternative, subject to vehicle, roof, protection and installation gates. The selected packaging baseline is one EcoFlow Power Hub 5 kVA, one 5.12 kWh LFP battery, the EcoFlow AC/DC panel and touchscreen, four EcoFlow 175 W rigid panels in two independent 2S strings, and the 45 L EcoFlow GLACIER refrigerator.

The load model returns 1.894 kWh/day from the battery, 922 W arithmetic continuous load and 972 W arithmetic peak. One battery provides 1.97 planning days. The 700 Wp array is adequate for the modeled average summer day but requires shore or V2L support in shoulder and winter planning cases.

## Material and mass finding

The complete listed material estimate is CHF 12,089 and 154.35 kg, including the requested loads and physical installation materials but excluding labour, engineering, testing, certification, delivery and contingency. CHF 10,330 and 123.75 kg belong to the power/solar/interface core including the conditional 12 V branch; CHF 1,759 and 30.60 kg belong to habitation loads and the existing MacBook charger.

EcoFlow lacks several specified loads and mandatory integration devices. The “all EcoFlow” requirement cannot safely be literal: the 10 L boiler, six installed USB-C lights, underfloor heater, blanket, charge outlets, roof attachment, AC changeover, RCD/MCB and wiring/protection must be third-party.

## Principal findings and actions

| Finding | Consequence | Required action |
|---|---|---|
| Shore and Renault V2L both use the single Power Hub AC input | Direct connection could parallel or back-feed sources | Provide a two-pole mechanically interlocked source selector and verify PE/RCD behavior |
| Published Renault V2L capability is up to 3.5 kW | Capability is promising but not configuration approval | Confirm exact option, socket, current, runtime and low-SOC behavior for the purchased vehicle |
| Renault auxiliary 12 V interface is not yet approved | Starter-battery depletion, vehicle faults or warranty impact are possible | Keep EF-018 conditional and capped at 20 A until written upfitter approval |
| One 5.12 kWh battery gives 1.97 planning days | It does not provide a full two-day requirement after contingency | Accept as the explicitly minimal configuration or add a second battery after mass/cost review |
| Two independent 2S PV strings reduce common shade/fault loss | One shaded module still limits its partner in the same string | Perform roof shade survey and keep strings on separate MPPT inputs |
| Winter solar covers approximately 39% of the modeled day | V2L/shore charging will be routine in poor winter solar | Validate seasonal mission profile and traction-range impact |
| Price and mass inputs mix official data with allowances | Procurement totals can change materially | Replace allowances with selected-part quotations and measured harness/mounting data |

## Proposed disposition

Retain SC-411-001 as a draft alternative on its branch. Do not supersede the existing SC-410-001/Victron preliminary design or buy components until the Design Authority reviews the energy behavior, roof packaging, mass, vendor concentration and Renault interface evidence.

## Evidence

- [`ecoflow-minimal-load-budget.csv`](../../calculations/ecoflow-minimal-load-budget.csv)
- [`ecoflow-core-bom.csv`](../../calculations/ecoflow-core-bom.csv)
- [`ecoflow_minimal_design.py`](../../calculations/ecoflow_minimal_design.py)
- [`ecoflow-minimal-design-results.md`](../../calculations/ecoflow-minimal-design-results.md)
- [`SC-411-001`](../20-architecture/SC-411-001-ecoflow-minimal-electrical-design.md)
