# CHANGELOG

All notable changes to the operating framework are documented here.

## 3.4.0 — 2026-10-06

### Framework/runtime product parity
- added manifest, governance, artifact/evidence registry, backlog, QA and dependency templates;
- added explicit instance assembly and upstream promotion mapping with ADR-0018;
- aligned Workstream state schema 1.1 with runtime version metadata;
- made project report configuration and schema extension boundaries explicit.

### Consolidation QA
- repaired executable QA regular expressions and strengthened link, JSON and report-state validation;
- clarified frozen report coverage, delivery timestamps, waiver and idempotent confirmation;
- synchronized report template mappings, session closure and private runtime ignore paths.

### Project Runtime
- added generic Operator Daily Report contracts with report cursors, DRAFT/SENT semantics and project-configurable mandatory mode;
- added report/state templates and ADR-0017;
- added a persistent Project Runtime model for multi-chat / multi-operator continuity;
- separated Operational Runtime truth from current artifact, Design System and evidence authority;
- added Operator / Session / Workstream identity boundaries;
- added operator-independent Workstream IDs and global Session Record paths;
- added continuous handoff and mandatory conversation-limit continuity triggers;
- added READ_WRITE / READ_ONLY / UNAVAILABLE runtime access modes;
- added Project Runtime / Workstream / Session / Operator templates;
- added ADR-0015 and ADR-0016;
- retained ADR-0014 mutation-owned Change History and added optional timestamp/timezone + session provenance fields.

## 3.5.0 — 2026-10-06

### Canonical runtime root
- replaced the candidate `runtime-template/` tree with canonical `runtime/`;
- made framework and project instances use identical runtime-relative paths;
- added classified `runtime/package.index.json`;
- added generic evidence archive surface and metadata template;
- separated Project Runtime decision templates from framework ADR history;
- added explicit compatibility area and runtime READMEs;
- added ADR-0020.

## Unreleased

### Governance
- added [ADR-0014](docs/decisions/ADR-0014-mutation-owned-change-records.md): mutation owners own persistent change records;
- integrated owner history routing, artifact registry, append-only ownership correction, startup and completion checks across the Master, templates and JSON derivative;
- added generic ownership scenarios and executable package QA; existing three-layer architecture and released version metadata remain unchanged for this unreleased addition.
- adopted Conventional Commits 1.0.0 as the mandatory commit-message convention;
- added `ADR-0012`;
- added `CONTRIBUTING.md` with commit types, scopes, examples, and commit discipline;
- added `ADR-0013` requiring significant commits to reference their Decision ID;
- added commit-to-decision traceability to the Master and publication checklist.

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
## Candidate 3.4.0 — canonical runtime package

- ADR-0019 adds runtime-template/, classified inventory, compatibility parity and read-only synchronization QA. Live release gates remain pending.
