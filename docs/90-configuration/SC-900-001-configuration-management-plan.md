---
document_id: SC-900-001
title: Configuration-Management Plan
revision: 1.0
status: approved
owner: Configuration Management
approver: Spiros Netos
approval_date: 2026-07-10
baseline: B0
---

# SC-900-001 Configuration-Management Plan

## Purpose

This plan controls the identity, status, change, approval, release, preservation, and recovery of solarChaser engineering information and installed configuration.

## Configuration items

Controlled items include requirements, architecture, interfaces, ADRs, trade studies, risks, drawings, calculations, schematics, software, parameter sets, BOMs, verification evidence, manuals, and installed-equipment records.

## Authority

| Action | Authority |
|---|---|
| Approve or change a requirement or architecture | Design Authority |
| Accept residual project or technical risk | Design Authority |
| Accept safety or compliance evidence | Design Authority plus applicable competent authority where required |
| Approve a baseline and release | Design Authority |
| Prepare and verify changes | Assigned engineering owner |
| Administer GitHub repository settings | Repository owner |

## Change classes

| Class | Description | Minimum control |
|---|---|---|
| Editorial | No change to technical meaning | Reviewed commit; link check |
| Minor | Local technical clarification with no architecture or safety impact | Issue or explained commit; affected-document review |
| Major | Requirement, architecture, interface, safety, compliance, performance, weight, or cross-system change | Issue, impact analysis, pull request, Design Authority approval, ADR or trade study where applicable |
| Emergency | Immediate correction needed to protect people or prevent damage | Make the system safe first; record rationale, evidence, and retrospective approval promptly |

## Version and baseline rules

- Controlled documents carry a human-readable revision in metadata.
- Draft revisions normally progress `0.x`; the first approved issue is normally `1.0`.
- Git commit hashes identify exact content.
- Baseline tags identify approved repository snapshots and are never moved or reused.
- GitHub releases describe the approved scope, known deviations, open high risks, and approval.
- Never create full repository copies such as `Repository_Rev0.2` inside the repository.

## Branching and review

The repository begins with direct owner-controlled work on `main`, as explicitly approved for this foundation change. After initial setup, significant changes should use short-lived branches and pull requests. Long-lived `development`, revision, or personal branches are discouraged because they create competing sources of truth.

Recommended branch protection for `main`:

- require a pull request before merging significant changes;
- require at least one approval when an independent reviewer is available;
- dismiss stale approvals after new commits;
- require conversation resolution;
- block force pushes and deletion;
- allow repository-owner bypass only for documented emergency or administrative recovery.

## Public information controls

Never commit:

- API keys, passwords, tokens, private keys, or `.env` files;
- vehicle immobilizer, alarm, access, or security credentials;
- precise private location history or personal contact data;
- unredacted invoices or documents containing account information;
- proprietary supplier material without redistribution rights;
- exploit-ready security details that would create avoidable physical risk.

Use secret storage outside Git. Publish sanitized examples where engineering reproducibility requires configuration shape.

## Installed configuration

Before construction, establish an installed-configuration register containing component ID, manufacturer, part number, serial number where appropriate, firmware, configuration version, lifecycle class, location, mass, interfaces, installation/removal dates, and replacement rationale. Sensitive serial or access data may reside in a private companion record referenced by a public placeholder.

## Backup and recovery

- GitHub is the primary remote.
- Maintain at least one periodically refreshed local clone and one independent release/archive backup.
- Verify that a fresh clone renders documents and contains required source artifacts.
- Large binary design files may require Git LFS after a specific need and quota review; do not enable it pre-emptively.
- Recovery must preserve baseline tags and approved history.

## Baseline procedure

1. Define baseline scope and entry criteria.
2. Close or explicitly disposition review actions.
3. Confirm controlled-document metadata, traceability, risks, links, and verification status.
4. Record Design Authority approval.
5. Merge the approved state to `main`.
6. Create an immutable annotated tag.
7. Publish a matching GitHub release.
8. Archive release artifacts and record the baseline in `CHANGELOG.md`.

Repository organization and naming are defined in the [Repository Architecture Specification](../00-project/SC-090-001-repository-architecture-specification.md).
