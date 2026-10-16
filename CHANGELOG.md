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

## 3.6.0 — 2026-10-06

### Zero-chat startup and runtime cleanup
- added explicit startup intents: CONTINUE_WORKSTREAM, START_NEW_WORKSTREAM and START_NEW_PROJECT;
- documented how to start a brand-new chat for new work without inheriting an unrelated NEXT ACTION;
- documented separate-runtime creation for a completely new project/client;
- added `runtime/compat/ALIASES.local.md` as the single place for legacy path/name mappings;
- deprecated scattered compatibility pointer files in operational folders;
- added ADR-0021.

### Release finalization
- promoted the validated Project Runtime capability to public `main` as framework 3.6.0;
- real cross-chat and Daily Report live pilots passed in a private adopter runtime;
- privacy/secret and structural parity checks passed before promotion;
- hosted CI non-execution remains explicitly documented under ADR-0022 and is not represented as CI PASS.

### Release-gate disposition
- added ADR-0022 to distinguish hosted CI non-execution from framework-source failure;
- allows explicit infrastructure disposition only when no runner/steps/logs execute and independent static/live evidence is sufficient;
- this disposition is not a CI PASS and must remain visible in release notes.

## Unreleased

No additional changes are assigned beyond the candidate below.

## 3.7.0 — CANDIDATE (not released)

### Candidate preparation
- consolidated accumulated compatible additions into a separately reviewed minor-release candidate under proposed ADR-0030; candidate labels do not announce publication;
- aligned Master, exact runtime mirror, JSON derivative, README and package QA to candidate version 3.7.0 while retaining the documented 3.6.0 released baseline;
- drafted release notes, compatibility/adoption steps and explicit pending integration, hosted-CI and publication gates in [the candidate record](docs/RELEASE_3_7_0.md);
- preserved historical evidence below, proposed ADR statuses, catalog classifications, seven optional pilots, runtime schemas/states/bootstrap, immutable pins and licensing; no installed runtime is updated.

The entries below retain their original implementation-time evidence and version statements; their inclusion in this candidate does not relabel earlier experiments or mark a release complete.

### Critical adaptation of design methods
- added an optional method-selection guide, original component-behavior seed, fictional recovery/denial specification and source-linked decision-brief example;
- attributed pinned external references, reused existing governance/triage and preserved the distinction between expected behavior, actual evidence and authorization;
- classified only the new seed as configured in the existing inventory under ADR-0025, ADR-0028 and GOV-VAL-001 / ADR-0029; architecture 3.6.0, mandatory bootstrap, licenses and pilot maturity remain unchanged.

### Bounded native annotation and layout evidence
- recorded one fictional local-component lab, including native annotation visible/hidden/restored observations, dependent reflow, preserved overrides and owner-history readback;
- retained overlay obstruction, weak editor-label contrast and prior access failures; visibility toggling does not establish individual collapse behavior or cross-file library adoption;
- updated METH-023/METH-024 evidence scopes under existing ADR-0025 and GOV-VAL-001 / ADR-0029, preserving all pilot classifications, architecture 3.6.0 and separate approval/release gates.

### Downloadable human handoff preparation
- preserved five frozen fictional participant files for online reading and offline download, with external-reader instructions v1.1 and a documented return/review procedure;
- kept answer keys, prior AI responses and participant identities outside the public packet; human execution remains NOT RUN and pilot classifications unchanged;
- linked preparation and fixed comprehension criteria under existing ADR-0025 and GOV-VAL-001 / ADR-0029, without changing core/runtime contracts or releasing a new version.

### Transfer coverage and proportionate next steps
- consolidated the 35-topic catalog into a bounded transfer checkpoint, separating 25 reusable private-origin topics, six existing core topics, three user-requested extensions and one intentional private exclusion;
- recorded each optional pilot's observed evidence and remaining acceptance boundary; deferred the unexecuted delivery-efficiency comparison for the current documentary scope under GOV-VAL-001 / ADR-0029;
- corrected the README catalog count and retained all catalog classifications, proposed ADR statuses, release/private-adoption gates and architecture 3.6.0.

### Fictional local functional MVP
- exercised fifteen predeclared local role/scope, revision-approval, persistence and rollback/recovery cases for METH-020, retaining a prior sandbox setup failure;
- added a reproducible standard-library SQLite lab and bounded report under ADR-0025 and GOV-VAL-001 / ADR-0029; production identity, human/native-editor acceptance and delivery efficiency remain unverified;
- retained pilot maturity, existing core/runtime contracts and the hosted automation suspension.

### GOV-VAL-001 — validation and evidence-based closure
- adopted the maintainer-approved mandatory contract with valid evidence reuse, protected acceptance gates, justified additional tests and scoped closure under ADR-0029;
- aligned the canonical Master/runtime mirror, JSON derivative, shared inventory and existing acceptance seed without changing startup, runtime states, pins or released version;
- added targeted integration guards and a user-requested catalog extension; no efficiency or pilot promotion claim.

### Temporary hosted QA suspension
- recorded the maintainer-requested suspension of this repository's Static QA workflow and the PR #10 infrastructure disposition under ADR-0022;
- preserved the workflow and local validation commands, with explicit restoration steps in [Hosted CI status](docs/HOSTED_CI_STATUS.md); no hosted PASS, release or pilot promotion is claimed.

### Eight-session retrieval comparison
- recorded eight fresh AI sessions and sixteen eligible synthetic recovery/critique observations under frozen protocol v1.1;
- observed explicit index retrieval in every available-index case, with approximately 18.6% more case-source bytes and no avoided case-document reads;
- retained bootstrap repetition, zero-benefit evidence and grading/provider/timing limitations; kept pilot maturity, architecture 3.6.0 and release gates unchanged.

### Prepared retrieval comparison
- added a prespecified, counterbalanced optional-index comparison protocol separating spontaneous choice from guided consultation;
- added local fictional-input preparation, read-only receipt summaries and mechanical regressions, with unreviewed/mechanical runs excluded from efficacy groups;
- reviewed protocol v1.1 to distinguish search inspection from explicit index retrieval, enforce guided order and bind declared design metadata to implementation;
- documented staged human/native-editor evidence needs; no new independent trial, savings, maturity promotion or release is claimed.

### Exploratory pilot validation
- recorded two independent synthetic AI reviews (four case observations), ten local browser checks, and one external-method intake stop decision;
- published portable fictional fixtures, read-only measurement tooling and explicit reproduction/claim limits;
- hardened fixture creation to use only pinned public Git blobs, reject nested destinations and retain manifest authority under Python optimization, with eight local regressions;
- retained all pilot maturity, ADR statuses and architecture 3.6.0; no index savings, human validation, native-editor rollout, merge or release is claimed.

### Bounded methodology audit
- proposed ADR-0028 and a privacy-safe 34-topic methodology catalog, separating file coverage from finding maturity;
- completed eight reusable procedures and five unconfigured seeds for evidence, migration, decision integrity, comparison/acceptance, annotation, canvas/content, editorial and knowledge/efficiency work;
- kept source-level project mappings local/restricted, with immutable blob identities and explicit exclusions;
- added read-only catalog/source-coverage QA and negative regressions, and repaired the runtime validator's premature result block; no original-media replay, live pilot completion, private repair, merge or release is implied.

### AI-assisted onboarding
- repaired the fictional next-action source found by independent review and added a regression separating recovered context from source availability; the original trial record remains historical and no production-readiness gate is inferred;
- recorded one independent Codex conversation recovering fictional persisted context, while preserving unresolved configuration/source blockers and the distinction between contextual recovery and operational readiness;
- added seven isolated fictional-runtime regressions for safe initialization, immutable-pin configuration, read-only fresh-process recovery and failure cases; documented the observed Windows scope and unexecuted independent trials;
- required explicit candidate source selection when onboarding files are absent from the selected released/default ref, completed the documented check list and diagnosed hosted CI non-execution from its run annotation;
- added a provider-neutral copyable setup prompt and an explicit guided/tool-assisted procedure for exploration or private-project initialization;
- linked onboarding from README and START_CHAT, preserving runtime intents, mandatory bootstrap and private configuration;
- documented environment/pin inspection, existing-install preservation, QA and first-session acceptance without claiming unexecuted clean-machine/provider trials;
- proposed ADR-0027 and updated the English repository About description, read back independently from GitHub metadata.

### Methodology promotion candidate
- proposed ADR-0024 and ADR-0025 with a sanitized maturity review, additive evidence/delivery, foundation QA and optional task-ownership contracts, and unconfigured private review seeds;
- kept incomplete UX, handoff, component maturity, canvas, phase sequencing and efficiency pilots optional with explicit limits;
- retained released 3.6.0 metadata, mandatory bootstrap, private pins and all populated/private artifacts;
- proposed ADR-0026 to repair current-manifest QA, documentation pointer classification and premature PASS reporting; added failure regressions and repaired portable ownership links without changing operative rules.

### README and evidence-ingestion documentation
- rewrote the public README as a practical project entrypoint covering problems, architecture, quick start, runtime usage, evidence provenance, QA, privacy, licensing and maintainer context;
- added generic stakeholder-meeting evidence ingestion guidance;
- added an optional local OBS/WhisperX transcription setup guide with CPU/GPU examples and security boundaries;
- expanded the shared runtime evidence archive contract;
- documented the recording → transcript → evidence → requirement → implementation → QA chain without treating machine transcription as automatic truth.

### Documentation ownership boundary
- added ADR-0023 and a shared contract defining FRAMEWORK_OWNED, PROJECT_OWNED, SHARED_CONTRACT and CROSS_REPO_REFERENCE;
- made the public framework the canonical owner of reusable method/history and private runtimes the canonical owners of project evidence/history;
- added the ownership contract to the canonical runtime package inventory;
- corrected stale candidate-branch links in Change Record Ownership guidance;
- documented the release outcome of ADR-0018 without rewriting its historical candidate context.

### Post-release runtime lock cleanup
- allow `candidate_pin: null` after a framework candidate is promoted and no active candidate remains;
- require any non-null stable/candidate lock pin to be a full immutable commit SHA;
- clarify stable-vs-candidate synchronization and consolidate compatibility aliases in `compat/ALIASES.local.md`;
- add regression coverage for released runtimes with no active candidate.


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
