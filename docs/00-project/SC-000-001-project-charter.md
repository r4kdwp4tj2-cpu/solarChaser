---
document_id: SC-000-001
title: Project Charter
revision: 0.4
status: in-review
owner: Design Authority
approver: null
approval_date: null
baseline: null
---

# SC-000-001 Project Charter

## Vision

Create an electric expedition camper platform that remains understandable, maintainable, reliable, and enjoyable throughout a 20-year design life.

## Mission

Develop an open, modular, professionally engineered platform that supports independent travel while keeping the captain in command of every critical system, except where safety protection must override operator action.

The current vehicle implementation baseline is the **Renault Master E-Tech electric L2H2, 87 kWh, 3.5 t**, selected in [ADR-003](../40-decisions/ADR-003-renault-master-etech-l2h2-platform.md).

## Roles

| Role | Authority or responsibility |
|---|---|
| Product Owner, Design Authority, Chief Engineer, Captain | Spiros Netos; approves requirements, architecture, trade-offs, baselines, and accepted risk |
| Systems Architect and Implementation Engineer | Codex-assisted engineering; proposes, analyzes, documents, implements, and verifies under Design Authority review |

## Engineering principles

1. The captain remains in command; the camper observes, informs, recommends, and protects.
2. Simplicity and reliability take precedence over unnecessary features.
3. Every important component is understandable, diagnosable, maintainable, and replaceable.
4. Open and documented interfaces are preferred.
5. Every feature must provide value relative to cost, complexity, weight, and maintenance burden.
6. Safety overrides convenience and cannot be defeated by ordinary operator override.
7. Documentation is a product and the repository is its single source of truth.
8. Requirements describe intent; architecture enables alternatives; implementations remain replaceable.
9. Significant decisions and their rationale are recorded.
10. Design debt is explicitly recorded, justified, owned, and resolved.
11. Technical challenge addresses ideas, not people.

## Success criteria

- The captain can understand the system and diagnose common failures without external help.
- Common field-replaceable modules can be serviced using the onboard toolkit within the target maintenance time where practical.
- Minor subsystem failures permit safe degraded operation.
- Hardware can evolve without invalidating the platform architecture.
- Requirements, design elements, risks, and verification evidence remain traceable.

## Governance

The [Repository Architecture Specification](SC-090-001-repository-architecture-specification.md) governs engineering information. The [Configuration-Management Plan](../90-configuration/SC-900-001-configuration-management-plan.md) governs changes and baselines.

GitHub is the authoritative engineering record. Chat discussions and meeting conversations are working material until their approved decisions are synchronized into the repository. Each engineering meeting that changes controlled information produces an implementation record identifying decisions, affected artifacts, risks, actions, and review status. A meeting is not closed until the corresponding repository change has been reviewed and accepted by the Design Authority.
