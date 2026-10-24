# Framework v3.9.0 — source candidate preparation, NOT RELEASED

**Preparation date:** 2026-10-24
**Decision:** [ADR-0035](decisions/ADR-0035-3-9-0-additive-tools-candidate.md), **PROPOSED**.
**Published baseline:** [v3.8.0](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/releases/tag/v3.8.0), immutable source `0d0b8ffffa3a640d937e97c54062c517c5b88029`.
**Candidate code baseline before version metadata:** public main `a4b20cffbd6919414113e79470f6d02efb32521a`, after PRs #22–#25.
**Status:** candidate for exact-source QA and maintainer review; **no tag, GitHub Release or private adopter update**.

## Scope and compatibility rationale

The integrated features are three independent **opt-in**, shared Python helpers for bounded contextual transport, supplied tool evidence-claim consistency and explicit read-only cycle-focus packets. This is additive to GOV-CTX-001 and preserves the already published core. Recommend minor v3.9.0 rather than 3.8.1; no breaking interface has been established that would justify major v4.0. The package index has 65 entries (the released v3.8.0 index had 62); all existing 62 entries and classifications remain in place. No hosted service, background scheduler, embedded private commands or automatic project acceptance is added.

**Metadata touched only for candidate preparation:** the canonical Master and exact runtime mirror must differ from prior main only by `3.8.0→3.9.0` version header; the JSON derivative only by `meta.version`, README framework version plus candidate notice, validator exact expected version, changelog candidate record, decision index and these release-preparation artifacts. All underlying operational policy stays intact. `runtime/runtime-manifest.json`, `runtime/framework-lock.json`, all runtime schemas, default bootstraps and `docs/methodology-catalog.json` remain byte-identical to reviewed prior main.

## Acceptance gates

| Gate | Required evidence | Current disposition |
|---|---|---|
| Candidate version/compatibility | Diff scope, full Git tree, Master/mirror bytes and JSON derivative parity, 65/65 package index paths, 35 methodology subjects / seven optional pilots, correct changelog/README and licenses | **PENDING exact candidate SHA readback** |
| Candidate package QA | All **nine** `.github/workflows/static-qa.yml` commands on exact candidate SHA using Python 3.12+, attributed logs, successful commands, any skipped subcase identified, clean worktree | **NOT RUN** |
| Public rights/privacy | Full scope-appropriate review of changed files, public attribution/license/decision consistency, no private client/workstream data; include diff and source readback | **PENDING** |
| Candidate merge | Maintainer acceptance of exact tested tree, scope, security and any symlink/hosted execution caveats; GitHub merge + independent readback | **NOT AUTHORIZED** |
| Hosted release disposition | For v3.9.0, actual hosted PASS or separately documented release-specific authority satisfying the applicable release constraints; ADR-0034 is v3.8.0-only | **NOT VERIFIED / NO WAIVER** |
| Tag + GitHub Release | Explicit new release decision specifying immutable main/tag SHA, signed-off release notes and post-tag/release readback | **NOT AUTHORIZED** |
| Private adopter upgrade | Release source confirmed, owner-only project review, exact three-way sync and preservation of installed modifications/configured data, explicit pin approval and QA | **NOT AUTHORIZED** |

## Evidence reuse and limitations

The nine local QA commands passed on **each earlier feature PR's distinct tested tree** under owner-supplied Windows Python evidence, but no result is inherited as an execution of this candidate's new version-metadata tree. The Windows symlink subtest was SKIPPED, hosted QA absent, and fictional tests do not validate independent agent objective reconstruction, actual tool receipts or practical cost savings. Historical six private INDETERMINATE, transcript/audio limitations, optional method trials and product-side acceptance remain outside this framework source release. Avoid repeating expensive native pilots without a changed decision question; do not label them passed.

## Publication boundary

[Draft release notes](releases/v3.9.0.md) are descriptive and **not an announcement**. Do not create tag/release, activate public candidate in private Git, accept ADR-0035 automatically, alter licenses or bump private pins. After a verified release, project-owned adoption follows [framework sync](FRAMEWORK_RUNTIME_SYNC.md), preserving existing configured files and required shared-file differences.
