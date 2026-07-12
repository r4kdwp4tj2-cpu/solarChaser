---
document_id: SC-950-001
title: Risk Register
revision: 0.7
status: draft
owner: Systems Engineering
approver: null
approval_date: null
baseline: null
---

# SC-950-001 Risk Register

## Scales

Probability is `Low`, `Medium`, or `High`. Impact is `Low`, `Medium`, `High`, or `Critical`. Safety risks are not accepted solely through this qualitative matrix; applicable analysis and regulation govern.

## Active risks

| ID | Category | Risk statement | P | I | Owner | Mitigation and detection | Residual target | Status |
|---|---|---|---|---|---|---|---|---|
| R-001 | Project / technical | Because conversion mass can grow incrementally, the completed vehicle may fail to retain 500 kg payload, reducing mission capability or compliance margin. | Medium | High | Weight Management | Live mass budget; record items over 0.5 kg; reserve unallocated margin; weigh after major build stages; final certified weighing. | Low / High | Open |
| R-002 | Safety / technical | Although the adjacent toilet compartment is dry, cabin condensation, spills, exterior ingress, or migration from the remote washing/water area may introduce liquid into the under-bed technical bay and damage energized equipment or create a hazardous condition. | Low | Critical | Physical Architecture and Safety | Keep all pipework, joints, pumps, filters, fills, and drains outside and not above the bay; protect cable crossings against liquid tracking; position and guard equipment using the credible liquid-path analysis; inspect for condensation and exterior ingress; define detection and isolation response where justified. | Low / High | Open |
| R-003 | Technical / external | Because the Renault Master E-Tech may not expose an approved auxiliary or traction-energy interface for conversion use, planned house charging or surplus-energy transfer may be infeasible or warranty-sensitive. | Medium | High | Vehicle Interface | Obtain Renault/body-builder interface data; do not modify HV; use approved equipment only; retain solar and commanded shore alternatives; close with interface trade study. | Low / Medium | Open |
| R-004 | Lifecycle | Because electronic products and vendors change during 20 years, replacement components may be unavailable or incompatible. | Medium | Medium | Configuration and Lifecycle | Standard interfaces; modular harnesses and mounts; archived configuration; alternate-source criteria; obsolescence review; replaceable modules. | Low / Medium | Open |
| R-005 | Technical | Because most utility loads are 12 V, failure or undersizing of the 48-to-12 V converter may disable multiple habitation functions. | Medium | High | Electrical Power | Maintain the EM-003 load model; validate diversity, transients, and derating; use protected branch architecture, thermal margin, diagnostics, and manual isolation; consider graceful-degradation or spare strategy through trade study. | Low / Medium | Open |
| R-006 | Technical / safety | Because future high-power loads increase thermal and fault energy, the 48 V bay may overheat or require protection beyond preliminary assumptions. | Medium | High | Electrical Power and Safety | Use the EM-003 preliminary power envelope; add product loss and future-load cases; complete ventilation analysis; provide temperature monitoring, derating, correctly rated protection and disconnects, and staged expansion limits. | Low / Medium | Open |
| R-007 | Project | Because attractive functions can accumulate, scope growth may increase mass, complexity, cost, and software burden. | High | Medium | Design Authority | Require traceability to a need; apply “every feature pays rent”; use change issues and ADRs; maintain reserves and deferred backlog. | Medium / Low | Open |
| R-008 | Technical / lifecycle | Because supervisory and diagnostic software can become complex or unsupported, automation may reduce rather than improve serviceability. | Medium | Medium | Software and Diagnostics | Open formats; local operation; manual fallback; bounded automation; documented interfaces; tests; exportable configuration and logs. | Low / Medium | Open |
| R-009 | Technical / project | Because the accepted under-bed technical-bay location and equipment envelopes are not yet measured or tested, the location may create inaccessible modules, poor mass distribution, excessive cable routes, noise, inadequate structure, or insufficient cooling. | High | High | Physical Architecture | Measure the Renault and habitation envelopes; model top and side access, removal paths, restraints, and service clearances; complete mass/axle and thermal analyses; use representative mock-ups before drilling, cutting, purchasing layout-dependent equipment, or fixing furniture interfaces. | Low / Medium | Open |
| R-010 | Project / compliance | Because published Renault payload and dimensional data cover multiple configurations, the selected 3.5 t vehicle may not provide sufficient exact payload, packaging, speed capability, or conversion approvals for the mission. | Medium | High | Vehicle Platform | Before purchase, verify exact CoC/configuration, running-order and axle masses, governed speed, body-builder rules, HV exclusion zones, and conversion mass budget; make procurement conditional on NFR-027 and NFR-040 feasibility. | Low / Medium | Open |
| R-011 | Project / configuration | Because engineering decisions are developed in conversation before controlled documents are updated, the repository may lag behind approved intent, causing omissions, conflicting identifiers, or reliance on non-authoritative history. | Medium | High | Configuration Management | Apply NFR-041; issue an RUP for each engineering meeting that changes controlled information; reconcile identifiers before authoring; use a working branch and pull request; close the meeting only after Design Authority review and merge; audit meeting-to-repository traceability at baselines. | Low / Medium | Open |
| R-012 | Safety / technical | Because a high-energy lithium house battery is installed inside the occupied vehicle beneath a bed, internal failure, external heating, overcharge, sub-zero charging, mechanical damage, or propagation may release heat, flammable or toxic gases, fire, or fault current into the habitation space. | Low | Critical | Energy Storage and Safety | Apply the approved EM-004 LFP baseline; select only an eligible documented battery system; provide independent BMS and hardware protection, low-temperature charge inhibition, temperature monitoring, manual isolation, fault-current protection, structural restraint, controlled venting/thermal concept, service access, and applicable compliance evidence; verify by analysis, inspection, fault testing, and supplier instructions. | Low / High | Open |

## Review rules

- Each mitigation action must acquire an issue or verification reference when scheduled.
- High and critical-impact open risks are reviewed at every design review.
- Residual risk acceptance belongs to the Design Authority; safety acceptance must also satisfy applicable legal and technical authority.
- Closed and realized risks remain in the register with evidence and outcome.
