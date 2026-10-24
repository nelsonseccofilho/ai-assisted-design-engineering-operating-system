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

## Post-merge checkpoint — 2026-10-24

This dated checkpoint reconciles the **historical PENDING / NOT RUN** table above; it **does not rewrite** what was known when the candidate was initially created.

- **PR #26 source merge:** GitHub independently reported merged on 2026-10-24 at `a749a9c8cdd24b99571b252cb49e9842a7e31efe`. The reviewed source HEAD was `9de04f0d30d3d335bcc894babcefd03ac432ac47`; GitHub compare showed no changed files between reviewed head and merged main at that point. Readback verified identical Master/runtime-mirror blobs, JSON `meta.version=3.9.0`, 65 inventory entries and README explicitly **NOT RELEASED**. [Merge receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/26#issuecomment-6387439570).
- **Exact candidate QA:** operator-supplied Windows/Python 3.12.10 evidence for all nine workflow-equivalent commands on `9de04f0d30d3d335bcc894babcefd03ac432ac47`: nine commands successful **with one symlink test SKIPPED** on the original run. [Original receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/26#issuecomment-6386757066). In a **separate elevated run**, the operator reported a symlink probe READY, targeted security case PASS, full `test_current_state.py` suite **8/8 PASS, 0 SKIPPED**, clean checkout on the **same tested SHA**. [Supplemental receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/26#issuecomment-6387381168). No agent or hosted runner performed these tests for the operator.
- **Rights/privacy:** ten-file release-candidate diff and canonical-source records reviewed; previous pattern screening found no matches among known private-project identifiers, tokens, personal names or URLs tested. This is a **bounded public-source review**, not exhaustive proprietary-rights or security clearance; recheck final release payload.
- **Hosted gate:** no hosted run of the relevant source was independently established by the available GitHub readbacks. `HOSTED_CI=NOT VERIFIED / NO HOSTED PASS`; no waiver for v3.9.0. ADR-0034 covers v3.8.0 only; ADR-0022's runner-zero predicate is not established for v3.9.0. See [proposed ADR-0036](decisions/ADR-0036-scoped-3-9-0-hosted-qa-disposition-proposal.md) for explicit options. **Status: PROPOSED, not accepted.**
- **Tag/release/pin:** no v3.9.0 ref was found during the checkpoint and **none is created by this documentation change**; v3.8.0 remains the verified baseline. Tag and hosted disposition each require a separate actual maintainer authorization. No private adopter/Workstream/pin is modified.

**Next release decision (still open):** choose actual hosted execution with logs **or** explicitly accept a v3.9.0-only manual hosted-suspension risk disposition; then approve release against the **final immutable source SHA** and final public notes, with rollback and post-release readback. Documentation added after PR #26 changes the prospective final SHA and is not automatically covered by tests on the earlier SHA; apply the exact-SHA QA requirements at each later acceptance gate. Until these conditions are met, **do not tag or publish v3.9.0**.

## Temporary local QA transition — 2026-10-24

The framework maintainer authorized **use of a controlled local QA workflow while the hosted GitHub account/access limitation remains unresolved** and undertook to notify when regularized. This approval **adopts a validation procedure**, not a claim that a billing restriction caused hosted non-execution or a waiver for publication. See accepted [ADR-0037](decisions/ADR-0037-temporary-local-qa-fallback.md), [runbook](LOCAL_QA_FALLBACK.md), and newly proposed `scripts/qa_local.ps1`.

**This implementation adds source to the future v3.9.0 tree.** Its own final pull-request SHA must be checked with Python 3.12+ and the complete local procedure before any merge or release decision. PR #26's historical test receipts remain valid **for their original SHA only**. The new wrapper has **NOT BEEN EXECUTED in the operator's Windows environment at this checkpoint**; script existence/static review is not an execution PASS.

Proposed ADR-0036 is still **PROPOSED** for v3.9.0-specific CI risk acceptance. Hosted status remains **NOT VERIFIED**. Final tag/GitHub Release requires a **separate express maintainer decision after complete exact-final-SHA QA, public rights/privacy review and selected hosted disposition**. Never automatically reactivate GitHub Actions when the user later reports payment/access restored: confirm availability and request authorization before altering workflows.
