# ADR-0036 — Release-specific hosted QA disposition for v3.9.0

**Date:** 2026-10-24  
**Status:** ACCEPTED — OPTION B, `V3_9_0_MANUAL_HOSTED_SUSPENSION_DISPOSITION` / LIMITED TO v3.9.0  
**Scope:** FRAMEWORK v3.9.0 ONLY; release governance, not runtime adoption  
**Decision owner:** Framework maintainer

## Context and source identity

The public framework v3.9.0 *source candidate* was merged via [PR #26](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/26) from exact reviewed head `9de04f0d30d3d335bcc894babcefd03ac432ac47` into main at merge commit `a749a9c8cdd24b99571b252cb49e9842a7e31efe`. A readback at that checkpoint showed no file changes between the reviewed candidate and main (merge-only history delta). **Neither merge nor this proposed decision creates a v3.9.0 GitHub Release.**

Operator-attributed Windows/Python 3.12.10 evidence on the exact PR #26 candidate recorded **nine official workflow commands successful, with one Windows symlink subtest SKIPPED**; the separate later administrator-elevated execution of `test_current_state.py` recorded **8/8 PASS, 0 SKIPPED**, including the symlink containment case, and an unchanged clean checkout. See [nine-command receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/26#issuecomment-6386757066) and [elevated symlink receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/26#issuecomment-6387381168). These results are **operator-supplied local evidence**, not hosted CI, verified Linux execution or validation of independent agents.

The `.github/workflows/static-qa.yml` definition remains present with nine Python 3.12 steps. At the reviewed SHA the GitHub connector returned no traditional status checks or pull-request-triggered workflow runs. These endpoints do not establish an exhaustive repository-wide absence of runs, so classification remains **HOSTED_CI=NOT VERIFIED / no execution evidenced**, not PASS. Hosted automation was previously kept suspended under [ADR-0034](ADR-0034-scoped-local-validation-consolidation.md), expressly limited to v3.8.0. The older [ADR-0022](ADR-0022-hosted-ci-disposition.md) requires positive runner-zero evidence and other conditions not established for this v3.9.0 candidate. Neither is a transferable waiver.

## Temporary QA procedure acceptance (separate from v3.9.0 exception)

The maintainer has now approved a **temporary controlled local QA process** pending their notice of GitHub billing/access regularization. This procedure is separately recorded as **[ADR-0037](ADR-0037-temporary-local-qa-fallback.md), ACCEPTED / CONDITIONAL PROCEDURE**, with runbook [LOCAL_QA_FALLBACK](../LOCAL_QA_FALLBACK.md) and candidate `scripts/qa_local.ps1`. **This does not accept option B below and does not authorize release.** The wrapper itself needs executable QA on its own final SHA before acceptance. The unknown hosted root cause and all historical CI `NOT RUN` claims remain unchanged.

## Options for a new release-specific maintainer decision

**A — preferred when available:** the maintainer explicitly authorizes reactivation or an execution path for hosted QA, confirms account/security/cost conditions, and obtains actual workflow step logs and results on the final publish SHA. Do not silently reactivate workflows or incur account charges.

**B — narrowly scoped alternative subject to acceptance:** the maintainer explicitly accepts **`V3_9_0_MANUAL_HOSTED_SUSPENSION_DISPOSITION`** for this release only, acknowledging the hosted QA remains `NOT RUN / NOT VERIFIED`. This is a **risk acceptance**, never a CI PASS or a finding that ADR-0022's runner-zero predicate was met. The release must carry all caveats and independently satisfy the remaining gates.

**C — defer publication:** keep v3.9.0 source in main without creating a tag/release or changing private adopter pins until hosted QA becomes available or a valid, release-specific risk acceptance is completed.

**Original proposal (historical):** if option A remains unavailable, prepare option B for the maintainer's *specific recorded decision*. This text was a proposal before the separate human acceptance recorded below. Broad authorization alone is not a hosted QA waiver.

## 2026-10-24 — Maintainer acceptance of Option B, before release authorization

**New attributable owner decision:** the maintainer was asked explicitly whether they approved **Option B** — `V3_9_0_MANUAL_HOSTED_SUSPENSION_DISPOSITION` — with its risk limited to v3.9.0, and then approved following that recommendation and authorized the related steps. Original-language acceptance and scope were recorded in the framework-owning repository: [PR #27 owner decision receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/27#issuecomment-6389104284).

**Approved scope:** `V3_9_0_MANUAL_HOSTED_SUSPENSION_DISPOSITION = ACCEPTED_WITH_DOCUMENTED_RISK` applies **only to the v3.9.0 release gate**. It allows the separately reviewed release process to rely on fully attributed exact-SHA local QA while GitHub-hosted QA remains unverified. **`HOSTED_CI=NOT VERIFIED`, not PASS**; no actual hosted run or runner-zero condition is inferred, no historical `NOT RUN` is rewritten and the cause of hosted nonexecution is not established. v3.8.0/v3.7.0 exceptions are not reused, and no general waiver for a later version follows.

**Evidence at acceptance checkpoint, not a license to skip later QA:** public source SHA `c9c30ebefeea00a9ff187f862914acccc10adebf`; operator-executed Windows Python 3.12.10 controlled PowerShell QA with `9/9` official commands PASS, `SKIPPED_TESTS=0`, `SYMLINK_CAPABILITY=READY`, `CURRENT_STATE_TESTS=8/8_PASS`, clean detached checkout. [Exact-SHA QA receipt](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/27#issuecomment-6389077593). GitHub commit status and PR workflow-run queries returned no verified hosted QA on that source. The reviewed v3.8.0 → candidate diff covers 24 public paths, with bounded pattern/rights screening only; not a comprehensive confidentiality, rights or security guarantee.

**Still a distinct required decision:** this risk acceptance **does not create or approve** the `v3.9.0` tag/GitHub Release, decide the final source SHA, accept the final release notes, or change any private adopter pin or product/operator state. The maintainer must separately authorize **publication of the exact final tested SHA and notes** after final tree/diff/rightfulness review, with rollback/correction procedure and independent release readback.

**Publication readiness after this ADR is written:** writing the decision to a branch creates a **different candidate SHA**. The older `c9c30e...` QA receipt is authentic only for that original tree; require fresh exact-SHA QA of this documentary candidate and further review/merge before any prospective `v3.9.0` tag. Do not present the branch as released or assume this risk decision itself authorizes a merge without applicable review.

## Mandatory gates even if option B is accepted

1. Verify the final immutable source SHA, branch and complete actual release delta. Any new metadata/documentation commit must receive the QA/readback required by the governing release contract; do not present tests on an earlier SHA as execution on a new SHA.
2. Retain the exact nine-step local QA receipt and separate 8/8 symlink receipt with truthful provenance/skip classification; independently review the final public diff/tree for privacy, attribution, licensing and source provenance. A pattern screen is not unlimited privacy or legal certification.
3. Identify the exact source SHA to tag, approval owner, final release notes, public license constraints (PolyForm Noncommercial 1.0.0 and CC BY-NC 4.0), limitations of synthetic fixtures, rollback/correction procedure and immutable release/readback evidence.
4. Record **separate explicit maintainer approvals** for (i) hosted CI option A or B and (ii) creating the v3.9.0 tag/GitHub Release. No prior decision or source merge supplies either approval.
5. After publication, verify tag-to-SHA identity, release content and link; then and only then change public documentation from candidate to published. Private project adoption is separately project-owned and must use a three-way sync, preservation and explicit pin decision.

## Boundaries

This proposal does not modify the canonical Master, runtime scripts/schemas, licenses, optional pilot status, hosted workflow configuration, a real external agent, any private runtime/Workstream, Product, Figma, UI Kit or reports. No background monitoring or hidden scheduling is introduced.

**Decision record owner:** this public framework; index in `DECISION_LOG.md`; active candidate/release-gate readback in `docs/RELEASE_3_9_0.md`. Preserve historical receipts and the fact that v3.8.0 remains the published baseline until an actual later GitHub Release is verified.
