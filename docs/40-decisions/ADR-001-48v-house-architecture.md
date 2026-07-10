---
record_id: ADR-001
title: 48 V House Architecture
revision: 1.0
status: accepted
decision_authority: Spiros Netos
decision_date: 2026-07-09
baseline: B0
---

# ADR-001 — 48 V House Architecture

## Context

Present camper loads could be supported by 12 V, but later induction cooking, larger inverter capacity, HVAC, and useful surplus-energy transfer would create very high 12 V currents. The design also values scalability over its 20-year life.

## Decision

Use a 48 V DC house backbone with a derived 12 V service bus. Do not introduce a 24 V bus unless a future requirement and trade study justify it.

## Alternatives considered

- 12 V backbone: broad component availability and minimum conversion complexity, but poor scalability at high power.
- 24 V backbone: intermediate current and availability, but adds a domain without a demonstrated load requirement.
- Mixed primary buses: flexible but unnecessarily complex for the current architecture.

## Rationale

At a given power, 48 V reduces current to approximately one quarter of the 12 V value. This supports smaller conductors and protection components, lower distribution losses, and practical high-power inverter integration. The accepted additional cost is a 48-to-12 V conversion stage for service loads.

## Consequences

- The battery, main distribution, primary chargers, protection, and high-power inverter interface are designed for the 48 V domain.
- Standard camper loads use a separately protected derived 12 V service bus.
- Converter capacity, redundancy, standby loss, thermal behavior, diagnostics, and replaceability require analysis.
- Voltage-domain boundaries must be explicit in schematics and labels.
- A later change of backbone voltage requires a superseding ADR and full impact analysis.

## Traceability

- Requirements: [FR-014 and NFR-037](../10-requirements/SC-100-001-system-requirements.md)
- Architecture: [SC-200-001](../20-architecture/SC-200-001-system-architecture.md)
- Risks: [R-005 and R-006](../50-risk/SC-950-001-risk-register.md)
