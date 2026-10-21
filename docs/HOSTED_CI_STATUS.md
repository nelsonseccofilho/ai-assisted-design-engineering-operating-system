# Hosted CI status

**Recorded:** 2026-10-15.
**Scope:** this public framework repository; existing Static QA workflow.
**Automation:** TEMPORARILY_DISABLED by the maintainer's explicit request.
**PR #10 hosted gate:** DISPOSITIONED_INFRASTRUCTURE under [ADR-0022](decisions/ADR-0022-hosted-ci-disposition.md), using the reviewed local QA and bounded trial evidence. This is not a hosted PASS.

## Evidence and authorized scope

The [hosted retry](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/actions/runs/38758667700) for commit `0c021c320bbce24a272e97af6692cbc23825646e` failed before execution: runner ID 0, empty runner name and zero steps. Its tree is identical to the content reviewed at `50f5cbacacc18949e7e95e19fca52b9945b88dd0`. The restriction is an infrastructure condition; it does not establish a failed framework test.

After that retry, the maintainer requested temporary suspension and integration into the principal branch using local validation. Static QA was disabled through the repository's workflow controls, without deleting or editing [its definition](../.github/workflows/static-qa.yml). The default branch is `main`.

The six existing workflow Python steps passed locally for the trial report package. Seventeen mechanical comparison regressions passed for the unchanged frozen v1.1 tooling. The [trial report](RETRIEVAL_COMPARISON_2026-10-15.md) records the eight-session synthetic evidence and its limits. The final PR description records QA for the added suspension documentation and readback of the resulting candidate.

This disposition applies to PR #10 integration. It does not authorize future merges, waive local QA or review, accept pending pilots, change architecture/version 3.6.0, change private runtimes or authorize a release. Failed hosted records remain historical evidence. Future candidates require their own evidence and owner decision while hosted automation is unavailable.

## Local validation while automation is unavailable

Run all six existing steps from the public framework checkout and retain their actual results:

```text
python scripts/validate_framework.py
python scripts/test_runtime_sync.py
python scripts/test_methodology.py
python scripts/audit_methodology.py --framework .
python scripts/test_audit_methodology.py
python scripts/test_onboarding.py
```

Run relevant example regressions when those tools change. Keep local PASS distinct from hosted non-execution. Review privacy, protected files and the entire candidate, then read back every changed file at the resulting commit before integration.

## Restore normal hosted validation

When hosted execution is available again, the maintainer should:

1. Open [Actions / Static QA](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/actions/workflows/static-qa.yml) and select **Enable workflow**.
2. Run the unchanged workflow through a normal new push or pull request for the current candidate. Re-running an older attempt validates that older revision; it does not validate a newer candidate.
3. Verify an assigned runner, checkout/setup steps and successful execution of all six Python validation steps for the intended revision.
4. Update this status and CHANGELOG.md with the actual run, revision and outcome. Close the temporary suspension only after real hosted execution is verified.

The suspension has no automatic expiry or scheduled reactivation. Repository automation remains disabled until explicitly re-enabled; this document does not repair an account-level restriction. See [GitHub's workflow controls](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows).

## 3.7.0 candidate — separate release decision pending

The [3.7.0 preparation](RELEASE_3_7_0.md) preserves this suspension and the historical PR-specific evidence above. No candidate run or release-specific disposition is asserted by that record. A manually disabled workflow supplies no new runner/step result and is not itself proof of ADR-0022 eligibility. Publication requires real hosted evidence or a documented governing decision for the exact release scope; previous PR approvals are insufficient. Local candidate results belong in its reviewed PR.

## Historical 3.7.0 finalization proposal — before acceptance

[ADR-0031](decisions/ADR-0031-scoped-3-7-0-manual-ci-release-decision.md) proposes a finite, separate publication path for the already manually suspended workflow. It remains PROPOSED and inactive. Manual suspension is not a fresh runner-zero observation and does not itself satisfy ADR-0022. No hosted PASS, release waiver, approval, reactivation or private update is asserted. The [finalization sequence](RELEASE_3_7_0_FINALIZATION.md) requires exact local evidence, review, accountable governance recording and separate publication authorization.

## Current 3.7.0 release-specific decision — accepted 2026-10-17

The framework maintainer explicitly accepted [ADR-0031](decisions/ADR-0031-scoped-3-7-0-manual-ci-release-decision.md) only for v3.7.0 and authorized recording that decision. This supersedes the pending/proposed decision status above, without rewriting the historical PR-specific evidence. Static QA remains manually suspended; hosted QA did not execute, and local Windows PASS is not hosted Linux PASS. ADR-0022 runner-zero eligibility is not inferred. The exception remains conditional on the exact final source, all applicable local/privacy/rights/live evidence and readback, followed by separate explicit publication approval. It grants no standing waiver, tag/release, pilot promotion, private adoption, hosted reactivation or Figma authority.

## Current3.8.0 scoped decision — 2026-10-21

The maintainer explicitly requests continued suspension and local QA with online Git review/consolidation. [ADR-0034](decisions/ADR-0034-scoped-local-validation-consolidation.md) governs this exact3.8.0 candidate only. Hosted QA is NOT RUN, not PASS; no reactivation occurs. Actual local results and immutable candidate/readback belong in the PR and release receipt. Prior exceptions remain scoped history.
