# solarChaser Engineering Repository

`solarChaser` is an open, maintainable, and explainable electric expedition camper platform designed for a 20-year service life.

This repository is the project's **single source of truth**. Approved requirements, architecture, decisions, risks, interfaces, designs, verification evidence, and operating information belong here. Chat discussions and external files are inputs until their decisions are recorded in this repository.

## Current status

| Item | Value |
|---|---|
| Lifecycle phase | Preliminary design |
| Repository baseline | B0 — Repository foundation |
| Default branch | `main` |
| Design authority | Spiros Netos |
| Architecture status | 48 V house backbone accepted; 12 V service bus derived |

The earlier project discussion recorded PDR approval. The present repository foundation preserves that decision while identifying the detailed requirements and review evidence as work to be completed.

## Start here

- [SC-000-001 Project Charter](docs/00-project/SC-000-001-project-charter.md)
- [SC-090-001 Repository Architecture Specification](docs/00-project/SC-090-001-repository-architecture-specification.md)
- [SC-100-001 System Requirements Specification](docs/10-requirements/SC-100-001-system-requirements.md)
- [SC-200-001 System Architecture Specification](docs/20-architecture/SC-200-001-system-architecture.md)
- [Decision records](docs/40-decisions/README.md)
- [Risk register](docs/50-risk/SC-950-001-risk-register.md)
- [Configuration-management plan](docs/90-configuration/SC-900-001-configuration-management-plan.md)
- [Contributing and review workflow](CONTRIBUTING.md)

## Repository map

```text
.github/          GitHub issue and pull-request workflows
calculations/     Controlled engineering analyses and source data
docs/             Approved and working engineering documents
drawings/         Diagrams, CAD exports, and drawing sources
hardware/         Hardware-specific design artifacts
operations/       Operating and maintenance material
software/         Monitoring, diagnostics, and automation software
verification/     Plans, procedures, results, and evidence
```

Do not create revision-named copies of the repository or documents. Git preserves history; approved snapshots are identified by baseline tags and GitHub releases.

## Public-repository notice

Do not commit credentials, personal information, vehicle keys, private location history, supplier-confidential data, or security-sensitive configuration. See the [configuration-management plan](docs/90-configuration/SC-900-001-configuration-management-plan.md).

## Licence

No licence has yet been approved. Until one is added, copyright remains with the repository owner and normal GitHub viewing/forking permissions do not grant reuse rights.
