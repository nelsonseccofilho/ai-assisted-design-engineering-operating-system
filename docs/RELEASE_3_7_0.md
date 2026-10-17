# Framework 3.7.0 — historical candidate preparation

**Update — 2026-10-17:** candidate preparation was integrated through [PR #17](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/17), merge `e91a785a33b9628a555df2332f97dc76357a1af1`. The original checklist and labels below are preserved as that preparation snapshot, not current package metadata. See [publication finalization](RELEASE_3_7_0_FINALIZATION.md) for the next deliverable and pending release-specific decision. This update does not announce a release.

**Status:** CANDIDATE — NOT RELEASED.
**Documented released baseline:** 3.6.0.
**Preparation baseline:** public main `bb003bb84a5f6cabfedc17597a4ce0f3e837e471`.
**Proposal:** [ADR-0030](decisions/ADR-0030-framework-3-7-0-release-candidate.md).
This record prepares publication; no tag, GitHub Release, private migration or pilot promotion is performed by it.

## Scope and version rationale

3.7.0 is recommended for accumulated compatible additions since documented 3.6.0: AI-assisted setup, evidence/delivery and methodology guidance, configured review seeds, executable QA/fictional labs, and accepted GOV-VAL-001. Existing runtime schemas, startup intents/order, access modes, paths, compatibility aliases, private configuration, licensing and authority boundaries remain. Package version and runtime/schema versions are independent.

The new metadata identifies this checkout as a candidate. Historical 3.6.0 experiment reports and frozen fixtures are not rewritten as 3.7.0 evidence. The catalog's `baseline_version` and per-entry `UNRELEASED_REVIEW` values describe the retained methodology review snapshot, not the current package distribution status. Publishing the package will not accept proposed ADRs or promote their entries. A later promotion must update the specific finding through its own decision.

The latest documented QA for the unchanged method-adaptation baseline is six local workflow steps, including 723 package checks, and nine-file readback. Those counts describe that baseline, not this candidate. Actual final-candidate revision, command results, privacy/protected-file review and remote readback belong in its PR validation record.

## Draft release notes — not yet published

### Added

- Provider-neutral AI-assisted onboarding instructions and fictional fresh-process regressions, with explicit source/pin selection and existing-install preservation.
- Generic evidence/delivery, foundation QA and methodology procedures, a 35-topic bounded catalog and a transfer checkpoint separating public coverage from operational maturity.
- Optional method-selection guidance, a component-behavior template, fictional failure/recovery specification and derived decision brief, with pinned external attribution and reuse limits.
- Reproducible fictional pilot tools and bounded reports, including a downloadable human-reading packet and local/native observations.

### Operating policy and QA

- Accepted GOV-VAL-001 / ADR-0029: risk-proportionate validation, reuse of valid evidence, protected mandatory gates and closure limited to the evidenced deliverable.
- Current-package validation, synchronization, methodology, catalog and onboarding regressions; source/derivative/alias consistency remains required.
- Evidence-ingestion and optional local transcription documentation. Recordings, transcripts, project requirements and populated operational data remain private.

### Compatibility and adoption

- Retain the v3.6 runtime architecture/interfaces, mandatory bootstrap and existing schema/state values. No automated update of installed runtimes or configured files.
- After approval/publication, adopters must verify the immutable released source and use the existing [synchronization procedure](FRAMEWORK_RUNTIME_SYNC.md). Review newly classified paths and configured seeds manually.
- Compare shared content against both its installed immutable source and the target. Preserve unexplained local shared-file differences; reconcile generalized upstream changes and project-specific overrides before replacing any file.

### Known limits

- The seven optional pilots remain optional/pending. Human comprehension, individual native annotation collapse/expanded occupancy and cross-file published-library adoption remain unverified.
- Fifteen local functional cases establish bounded fictional behavior, not production identity/authorization or product acceptance. The new component-specification cases B1–B8 are NOT RUN.
- Eight-session synthetic retrieval observations showed approximately 18.6% more case-source bytes and no avoided case-document reads. No token/cost saving or productivity gain is claimed; the delivery-efficiency comparison remains DEFERRED.
- AI-assisted setup is not a clean-machine or cross-provider acceptance result. Prior live core evidence remains attributed to its original scope.
- Static QA is temporarily manually disabled. Local PASS is not hosted PASS. A release-specific hosted-gate decision is pending; earlier integration exceptions do not authorize this publication.
- Licensing remains PolyForm Noncommercial 1.0.0 for framework/software-like materials and CC BY-NC 4.0 for documentation. This is source-available, not OSI Open Source.

## Acceptance and gate checklist

| Gate | Required evidence / current disposition |
|---|---|
| Metadata and compatibility | Version 3.7.0 and CANDIDATE agree across Master, mirror, derivative and README; protected inventory, schemas, enums, bootstrap and pins remain unchanged. Final candidate review required. |
| Package QA | Run the six unchanged commands in [hosted CI status](HOSTED_CI_STATUS.md) for the immutable candidate. Preserve failures and actual environment. Final results belong in the PR. |
| Privacy and rights | Apply the full [publication checklist](PUBLICATION_CHECKLIST.md), review generic/fictional content, filenames, metadata and external attribution; read back every changed file at the tested revision. |
| Live evidence relevance | Existing core live reports are historical scoped evidence. No changed live interface is intended here. Review applicability; any material contract change or missing mandatory evidence blocks publication. Optional pilots are excluded from validated-capability claims. |
| ADR disposition | ADR-0029 is ACCEPTED. ADR-0024–0028 and ADR-0030 remain PROPOSED. Publication must explicitly retain optional/proposed scope or obtain separate accountable acceptance; merge is not acceptance. |
| Hosted execution | PENDING RELEASE-SPECIFIC DECISION. Manual suspension does not itself satisfy ADR-0022's runner/step observations. Real hosted PASS or a properly scoped governing decision is required before publication. |
| Integration | PENDING explicit approval for this candidate PR. |
| Tag / GitHub Release | NOT CREATED. PENDING separate approval of the final commit, notes and gate dispositions. |
| Installed project adoption | NOT PERFORMED. Separate project migration and review after a released immutable pin exists. |

Candidate preparation and publication are separate deliverables. Preparation can close with documented limitations once its own QA/readback criteria pass; publication remains blocked while applicable gates are unresolved. Cost alone cannot waive a mandatory check.

## Publication sequence after review

1. Review candidate evidence and decide its PR integration separately.
2. Resolve and record the release-specific hosted gate and proposed-ADR scope; confirm final notes, privacy/rights and live-evidence applicability.
3. Remove candidate-only labels consistently through a reviewed finalization change. Revalidate affected metadata/package checks; confirm the final commit/tree, with no unreviewed payload changes.
4. Obtain explicit publication authorization for that final immutable commit and notes. Create a version tag and GitHub Release pointing at it; read back tag target, release metadata and source contents before reporting success.
5. Prepare each adopter migration separately. Do not move a private stable pin to an unreleased candidate or silently overwrite configured records/history.

No paid service, additional chat, Figma edit or repeated efficacy experiment is required to prepare this candidate.
