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
