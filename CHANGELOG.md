# CHANGELOG

All notable changes to the operating framework are documented here.

## Unreleased

### Governance
- adopted Conventional Commits 1.0.0 as the mandatory commit-message convention;
- added `ADR-0012`;
- added `CONTRIBUTING.md` with commit types, scopes, examples, and commit discipline.

## 3.3.0 — 2026-10-05

### Decision governance
- added `DECISION_LOG.md` as the permanent index of significant framework decisions;
- added ADR records under `docs/decisions/`;
- added `ADR_TEMPLATE.md`;
- documented the major architectural, privacy, workflow, naming, licensing, and governance decisions made while building the framework;
- added a mandatory Decision Documentation Protocol to the Master;
- integrated decision references into Handoff and Project Context templates;
- added decision-governance checks to the public-release checklist;
- documented why decision history must be preserved separately from handoffs and changelogs;
- documented the public repository identity and publication decision in `ADR-0011`;
- synchronized framework version metadata to `3.3.0` across canonical files.

## 3.2.0 — 2026-10-05

### Licensing
- added `LICENSE` using PolyForm Noncommercial License 1.0.0 for framework/software-like materials;
- added `LICENSE-DOCS.md` applying CC BY-NC 4.0 to documentation and editorial material;
- added `COMMERCIAL-LICENSE.md` reserving commercial use for separate written licensing;
- identified Nelson Secco Filho as copyright holder;
- documented that the repository is source-available for noncommercial use and is not OSI Open Source;
- added licensing checks to the public-release checklist;
- added structured licensing metadata to `prompt-operacional.json`.

## 3.1.0 — 2026-10-05

### Added
- `docs/RATIONALE.md` documenting the problem, design rationale, architecture, intended usage, consulting hypothesis and potential product evolution.
- explicit explanation of why a prompt alone is insufficient for persistent AI-assisted design work.
- rationale for evidence hierarchy, bounded autonomy, parity-before-evolution, tool-state reconciliation and human-first communication.

### Changed
- README now links directly to the framework rationale.

## 3.0.0 — 2026-10-05

### Architecture
- converted the framework from a project-derived operating prompt into an organization-agnostic operating system;
- separated stable operating rules from persistent project context and volatile handoff state;
- introduced `PROJECT_CONTEXT_TEMPLATE.md`;
- moved real project values to ignored local runtime files;
- introduced fictional public examples;
- introduced a public-release privacy checklist.

### First-run onboarding
- added generic-mode startup;
- added minimum contextual onboarding;
- added organization/client, project, primary stakeholder, Work Package, journey, Design System/UI Kit, and primary work file fields;
- added just-in-time context collection to reduce human cognitive load.

### Privacy
- removed the historical project archive from the public package;
- removed real organization, stakeholder, Figma, Design System, work-package, journey, node, and change-record references from the public framework;
- added `.gitignore` protection for real runtime context;
- added mandatory public-release scanning guidance.

### Product direction
- positioned the repository as personal research and an evolving consulting framework for AI-Assisted Design Engineering;
- preserved the principle that the public repository documents the method while project/client context remains private.

## 2.x

Pre-3.0 versions were internal working iterations used to discover and validate the operating model. They are intentionally not included in the public repository because they contained project-specific context.
