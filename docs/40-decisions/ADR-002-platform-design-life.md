---
record_id: ADR-002
title: Platform Design Life
revision: 1.0
status: accepted
decision_authority: Spiros Netos
decision_date: 2026-07-09
baseline: B0
---

# ADR-002 — Platform Design Life

## Context

The desired ownership horizon warrants lifecycle decisions based on durability, replaceability, documentation, and long-term support rather than minimum initial cost.

## Decision

Design the solarChaser platform for at least 20 years of normal recreational use with scheduled maintenance. Individual wear items and electronic modules may have shorter lives but must be replaceable without architectural redesign where practical.

## Consequences

- Durable cable systems, connectors, labels, structural interfaces, and corrosion protection are preferred.
- Lifecycle class, access, obsolescence, and replacement strategy influence component selection.
- Configuration records and service information are maintained as part of the product.
- Short-lived components must not be trapped behind permanent construction.

## Traceability

- Requirement: [NFR-039](../10-requirements/SC-100-001-system-requirements.md)
- Project charter: [SC-000-001](../00-project/SC-000-001-project-charter.md)
- Risks: [R-004](../50-risk/SC-950-001-risk-register.md)
