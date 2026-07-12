---
record_id: EM-003
title: Preliminary Electrical Load and Energy Budget
revision: 0.1
status: draft
meeting_authority: Spiros Netos
meeting_date: 2026-07-12
approver: null
approval_date: null
baseline: null
---

# EM-003 — Preliminary Electrical Load and Energy Budget

## Purpose

Implement the first reproducible electrical load budget for the accepted 48 V house architecture and provide planning inputs for the technical-bay converter, inverter, protection, thermal, and battery trade studies.

This is a preliminary envelope. It records estimates and explicit exclusions; it does not select products, battery capacity, inverter rating, solar capacity, cable sizes, or protective devices.

## Implemented analysis

The controlled CSV input and standard-library Python calculation are in [`calculations/`](../../calculations/README.md). The calculation:

- validates identifiers, voltage domains, non-negative inputs, and peak-versus-continuous consistency;
- refers 12 V, 48 V, and 230 V loads to the 48 V source side using declared planning efficiencies;
- reports summer and winter daily energy;
- reports conservative arithmetic sums of worst-continuous and peak branch loads;
- calculates a two-day battery-planning value using 10% contingency and 80% usable energy;
- generates a reviewable Markdown result from the controlled CSV source.

Automated verification checks the controlled input and sizing arithmetic.

## Preliminary results

| Result | Planning value | Disposition |
|---|---:|---|
| Summer daily source energy | 2.61 kWh/day | Higher seasonal design day in this first model |
| Winter daily source energy | 2.27 kWh/day | Excludes electrical space and water heating |
| Worst-continuous arithmetic sum | 1.56 kW | Conservative envelope; diversity not yet applied |
| Arithmetic peak upper bound | 2.26 kW | Requires transient and coincidence study |
| Two-day nominal battery-planning energy | 7.17 kWh | Trade-study input, not selected capacity |

## Proposed decisions

| ID | Decision | Status | Authoritative implementation |
|---|---|---|---|
| D-010 | Use the reproducible CSV-and-Python load model as the controlled source for preliminary electrical sizing. | Proposed | Calculation package |
| D-011 | Use 2.61 kWh/day as the current design-day estimate until mission profiles and selected equipment replace the assumptions. | Proposed | Generated results |
| D-012 | Carry 1.56 kW continuous and 2.26 kW arithmetic peak as conservative analysis envelopes; do not treat them as final nameplate selections. | Proposed | Generated results; SC-402 |
| D-013 | Carry 7.17 kWh nominal as a battery trade-study input only, based on two days, 10% contingency, and 80% usable energy. | Proposed | Generated results; SC-402 |
| D-014 | Exclude space heating, water heating, air conditioning, fixed electric cooking, and traction energy until requirements approve those loads. | Proposed | Controlled load input and result limits |

## Assumptions and exclusions

- Inputs are engineering estimates, not supplier guarantees or measured installed performance.
- The 12 V, 48 V, and 230 V planning efficiencies are 90%, 98%, and 88% respectively.
- The inverter is assumed normally disabled; only limited enabled-idle energy is included.
- The extraction fan has zero daily energy in the baseline but remains in the continuous envelope as a reserved provision.
- The arithmetic continuous and peak sums intentionally assume no diversity. Product selection needs a defensible coincidence model and transient data.
- Solar and charger sizing are outside this package because generation, location, season, shading, and mission profiles are not yet controlled.

## Repository Update Package RUP-003

| Artifact | Change |
|---|---|
| Electrical load CSV | Add auditable preliminary branch-load assumptions |
| Python calculation | Add deterministic validation and source-side aggregation |
| Generated result | Add human-readable calculation output |
| Verification test | Add input-integrity and sizing-arithmetic checks |
| SC-402-001 | Reference the preliminary envelope and update A-402-003 status |
| SC-950-001 | Reference the load budget in converter and future-load mitigations |
| README / indexes / CHANGELOG | Add navigation and change summary |

## Risks

- R-005 remains open because the 48-to-12 V converter topology, diversity, transient behavior, thermal derating, and graceful degradation are not selected.
- R-006 remains open because future higher-power loads and technical-bay heat rejection are not yet analyzed.
- R-007 remains open because adding excluded loads can materially increase energy, mass, cost, and system complexity.
- Estimated duty cycles may understate real expedition use until mission profiles and measurements are available.

## Open Action List OAL-003

### Engineering

- Obtain Design Authority agreement on the included loads, exclusions, autonomy days, contingency, and usable-energy assumption.
- Define at least summer, winter, travel, storage, and degraded-power mission profiles.
- Replace estimates with supplier data and measurements when candidate products exist.
- Complete load-coincidence, motor-start, inverter-surge, temperature-derating, and protection studies.
- Perform the battery chemistry/capacity trade study using the planning value as one input.
- Perform solar and charging energy-balance studies against controlled locations and mission profiles.
- Convert accepted architecture-level limits into allocated requirements and verification cases.

### Design Authority

- Review the assumptions, exclusions, proposed decisions, and generated result.
- Accept, correct, or reject RUP-003.
- After acceptance, merge the synchronized pull request to close the meeting's repository action.

## Review status

**Implementation complete; awaiting Design Authority review.** The analysis is suitable for preliminary planning only. Approval of EM-003 would approve the stated calculation basis and interim envelopes, not final equipment ratings or procurement.
