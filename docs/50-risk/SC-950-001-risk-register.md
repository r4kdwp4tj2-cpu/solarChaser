---
document_id: SC-950-001
title: Risk Register
revision: 0.3
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
| R-002 | Safety / technical | Because plumbing or condensation may introduce water, water may enter the technical bay and damage energized equipment or create a hazardous condition. | Low | Critical | Physical Architecture and Safety | Separate wet and electrical bays; raised equipment; drip shields; sealed penetrations; leak sensor; drain path; inspection; defined isolation response. | Low / High | Open |
| R-003 | Technical / external | Because the Fiat traction system may not expose an approved energy interface, planned house charging or surplus-energy transfer may be infeasible or warranty-sensitive. | Medium | High | Vehicle Interface | Obtain authoritative vehicle interface data; do not modify HV; use approved equipment only; retain solar and commanded shore alternatives; close with interface trade study. | Low / Medium | Open |
| R-004 | Lifecycle | Because electronic products and vendors change during 20 years, replacement components may be unavailable or incompatible. | Medium | Medium | Configuration and Lifecycle | Standard interfaces; modular harnesses and mounts; archived configuration; alternate-source criteria; obsolescence review; replaceable modules. | Low / Medium | Open |
| R-005 | Technical | Because most utility loads are 12 V, failure or undersizing of the 48-to-12 V converter may disable multiple habitation functions. | Medium | High | Electrical Power | Load analysis; protected branch architecture; thermal margin; diagnostics; manual isolation; consider graceful-degradation or spare strategy through trade study. | Low / Medium | Open |
| R-006 | Technical / safety | Because future high-power loads increase thermal and fault energy, the 48 V bay may overheat or require protection beyond preliminary assumptions. | Medium | High | Electrical Power and Safety | Power and thermal budgets; ventilation analysis; temperature monitoring; derating; correctly rated protection and disconnects; staged expansion limits. | Low / Medium | Open |
| R-007 | Project | Because attractive functions can accumulate, scope growth may increase mass, complexity, cost, and software burden. | High | Medium | Design Authority | Require traceability to a need; apply “every feature pays rent”; use change issues and ADRs; maintain reserves and deferred backlog. | Medium / Low | Open |
| R-008 | Technical / lifecycle | Because supervisory and diagnostic software can become complex or unsupported, automation may reduce rather than improve serviceability. | Medium | Medium | Software and Diagnostics | Open formats; local operation; manual fallback; bounded automation; documented interfaces; tests; exportable configuration and logs. | Low / Medium | Open |
| R-009 | Technical / project | Because the living layout and equipment envelopes are not yet measured, premature technical-bay location selection may create inaccessible modules, poor mass distribution, excessive cable routes, or inadequate cooling. | High | High | Physical Architecture | Measure vehicle and habitation envelopes; model removal paths and service clearances; compare candidate locations in TS-002 before drilling, cutting, or fixing furniture interfaces. | Low / Medium | Open |

## Review rules

- Each mitigation action must acquire an issue or verification reference when scheduled.
- High and critical-impact open risks are reviewed at every design review.
- Residual risk acceptance belongs to the Design Authority; safety acceptance must also satisfy applicable legal and technical authority.
- Closed and realized risks remain in the register with evidence and outcome.
