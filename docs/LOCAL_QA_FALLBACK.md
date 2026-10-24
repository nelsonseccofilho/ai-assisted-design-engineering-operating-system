# Controlled local QA fallback — temporary hosted Actions suspension

**Scope:** public AI-Assisted Design Engineering framework, release candidate validation.  
**Status:** temporary **operator-authorized QA procedure**, **not** a hosted CI PASS or blanket release waiver.  
**Related governance:** [ADR-0037](decisions/ADR-0037-temporary-local-qa-fallback.md) and release-specific [ADR-0036](decisions/ADR-0036-scoped-3-9-0-hosted-qa-disposition-proposal.md).

## Purpose

When GitHub Actions execution cannot currently be verified or is deliberately suspended, avoid blocking ordinary source development while preserving exact-SHA, complete, auditable testing. The maintainer has directed use of controlled local validation **until they report that the GitHub billing/access issue is regularized**. Billing has **not** been independently confirmed as the root cause; a manually suspended workflow is an alternative explanation. Do not silently alter billing, enable workflows, execute paid services or claim the platform's behavior was diagnosed.

A local PASS is **not** a hosted GitHub Actions PASS, not a Linux runner result, not independent external-agent testing and not an unconditional authorization to tag or publish a version.

## Requirements

1. Fetch a **fresh detached checkout** of the exact full 40-character commit SHA under review. Use Python **3.12+** and **PowerShell 7.4+** on Windows. Never use a mutable branch label in place of the expected SHA; do not run unreviewed or untrusted code with administrator privileges. Enable the Windows symlink capability with appropriate authorization, or use a previously authorized elevated PowerShell session when needed. The script must **fail** rather than accept a skipped symlink case.
2. Run **all nine** commands in `.github/workflows/static-qa.yml`, in their declared order, checking both exit status and skip reports. The runner verifies parity with the workflow's Python commands and rejects any drift. It also verifies the exact HEAD, detached state, symlink support, the complete 8-test current-state suite including the path containment test, and clean worktree before/after.
3. Keep the complete, generated log **outside the repository**. Record exact commit SHA, Python version, exit statuses, per-step results, SKIPPED count, environment/limitations, log location, operator and date. Review and **redact** local user names/paths, machine identifiers, credentials and any potentially private data before sharing or citing log excerpts in the public repository. Do not upload unfiltered logs automatically.
4. Independently read back remote PR/head, protected files and public diff/privacy/licensing/source provenance. Confirm the tested SHA is still the prospective release source and no material change occurred. A documentation change creates a new SHA and triggers renewed exact-source QA; test evidence does not jump between different source trees.
5. Record a **release-specific** decision whether absent hosted QA can be dispositioned with accepted limitations. A release still needs its own final immutable SHA, approved notes and explicit human tag/release authorization; no general exception grants automatic publication or private runtime adoption.
6. If any command fails, is skipped, has missing output, reports stale source, or changes the checkout: `LOCAL_QA_RESULT=FAIL`; do not merge/publish under a claimed PASS until diagnosed and rerun on the correct source.

## One-command invocation (Windows)

For operator-facing commands and diagnostic snippets, also follow the [PowerShell execution-context contract](POWERSHELL_EXECUTION_CONTEXT.md): select the absolute expected checkout directory with `Set-Location -LiteralPath`, confirm Git root/origin/exact SHA before QA, and restore the original directory in `finally`. The example below assumes the operator has already established that context; a runnable handoff to an operator must include these checks even when paths are absolute.

From a **detached checkout** of the candidate SHA (not the private project repository):

```powershell
# Verify detached HEAD and determine the exact source identity.
git rev-parse HEAD
git status --porcelain=v1 --untracked-files=all

# Substitute the exact 40-character SHA from git rev-parse HEAD:
pwsh -NoProfile -File .\scripts\qa_local.ps1 -ExpectedSha '<full-40-character-sha>'
```

The script finds the repository from its own path. It does not create branches/commits, edit tracking files, run GitHub workflows or enable machine settings. It writes its log under the operating-system temporary directory. For Windows, if symlink privileges are missing, it fails clearly; after separate admin/developer-mode authorization, rerun the **same exact SHA**. Do not consider a failed first attempt PASS.

Expected terminal markers **only after actual success**:

```text
WORKFLOW_PARITY=9/9_MATCH
SYMLINK_CAPABILITY=READY
STEP_1=PASS
...
STEP_9=PASS
CHECKOUT_AFTER=CLEAN
LOCAL_WORKFLOW_COMMANDS=9/9_PASS
CURRENT_STATE_TESTS=8/8_PASS
SKIPPED_TESTS=0
LOCAL_QA_RESULT=PASS
HOSTED_CI=NOT_VERIFIED
QA_LOG=<local-temporary-log-path>
```

A completed script verifies **local** results, not hosted status. Where possible, an additional **independent Linux** run with Python 3.12 is useful because GitHub's defined workflow uses `ubuntu-latest`, but local Linux is also not GitHub-hosted evidence. If running Linux QA with symlinks, use an equivalent auditable harness; this particular script requires PowerShell 7.4+ and focuses on the operator's Windows setup.

## Release gates and reactivation

**Suspended/unknown hosted period:** keep GitHub Actions `NOT RUN / NOT VERIFIED`. The maintainer may explicitly accept a **version-scoped risk disposition** only after the equivalent local testing and required public-source reviews, without representing runner-zero or paid-account infrastructure hypotheses as observed facts. Prior release exemptions do not automatically transfer. Release owner separately accepts/rejects the precise immutable version payload and authorizes tag/publication.

**When the maintainer reports billing/access is regularized:** first inspect GitHub account/workflow status, permissions and billing as authorized; do not assume Actions automatically work. Request explicit authorization before re-enabling or dispatching hosted workflows. Run the nine official steps in GitHub Actions on a controlled exact commit and capture job/step logs. Verify an actual hosted PASS before retiring this temporary fallback or updating the next release's gate. Preserve all prior local receipts and non-execution classifications; never rewrite historical hosted `NOT RUN` to PASS.

**Project adoption stays separate:** a public release never writes a private runtime pin, changes live Workstreams or accepts methods/agent effectiveness without its own project-owner and preservation checks.
