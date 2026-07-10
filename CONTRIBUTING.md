# Contributing to solarChaser

## Authority and scope

Spiros Netos is the Design Authority and approves requirements, baselines, architectural decisions, and accepted risk. Contributions are welcome, but a proposal becomes authoritative only after it is merged into `main` and, where applicable, included in an approved baseline.

## Working model

- `main` contains the current controlled project state.
- Small, low-risk documentation corrections may be committed directly by the repository owner.
- Significant engineering changes should use a short-lived branch and pull request once branch protection is enabled.
- Do not create branches or folders named after document revisions.
- Use issues for proposed work, defects, risks, requirement changes, and decisions needing analysis.

## Change process

1. Identify the need and the affected requirements, systems, interfaces, risks, and documents.
2. Open the appropriate issue template.
3. Perform analysis or a trade study when alternatives or material consequences exist.
4. Create or update an ADR for a significant architectural decision.
5. Update authoritative documents and cross-references in the same change.
6. State verification performed and residual risks in the pull request.
7. Obtain Design Authority approval for controlled changes.
8. Merge without rewriting approved history.

## Document rules

- Use lowercase kebab-case file names.
- Controlled documents use `SC-NNN-NNN-short-title.md`.
- ADRs use `ADR-NNN-short-title.md`; trade studies use `TS-NNN-short-title.md`.
- Requirement IDs are stable: `FR-NNN` and `NFR-NNN`.
- Risk IDs are stable: `R-NNN`.
- Use relative Markdown links for repository content.
- Never reuse or silently renumber an allocated identifier.
- Mark superseded records as such and link to their replacement; do not delete approved rationale.

## Commit guidance

Use an imperative, scoped subject, for example:

```text
docs: establish repository baseline B0
adr: accept 48 V house backbone
risk: add technical-bay water-ingress controls
```

## Review checklist

- The change serves an approved requirement or clearly proposes a new one.
- Metadata and status are current.
- IDs and links resolve.
- Requirement, architecture, ADR, risk, and verification impacts are addressed.
- No secrets or sensitive personal data are included.
- The change remains understandable to the 2046 maintainer.
