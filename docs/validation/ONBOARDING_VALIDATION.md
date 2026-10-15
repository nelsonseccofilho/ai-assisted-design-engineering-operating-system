# Scoped onboarding validation record

**Date:** 2026-10-15  
**Status:** candidate evaluation; not release acceptance  
**Decision:** [ADR-0027](../decisions/ADR-0027-ai-assisted-onboarding.md)

## Source and environment

The trial used a new public Git checkout at commit `6b516feddb5620e955493070bfe5a3aef1e11134`, plus the follow-up guide/test changes committed alongside this record. The independently fetched stable baseline was `2910154799ed28416475a359a9ea536599f38451`; the declared framework version remains **3.6.0**. Final committed-head verification belongs in the PR validation summary to avoid a self-referential commit pin.

The available Windows environment already had Git 2.55.0.windows.3 and Python 3.12.10. This was a tool-assisted checkout/configuration test with fictional temporary projects. It did not install prerequisites on a clean machine, test source archives, or establish universal platform/provider compatibility.

## Observed scope

| Check | Outcome | Evidence and limits |
|---|---|---|
| New public checkout and immutable commit inspection | PASS | Local Git HEAD and fetched stable object inspected separately |
| Fictional runtime seed initialization | PASS | Only generic runtime seeds copied to an absent temporary project destination; no public Git history or populated source project copied |
| Existing destination preservation | PASS | Initialization refused an existing fixture destination; before/after file digests matched |
| Local configuration | PASS | Fictional identity, operator profile, governance scope, dependency/lock/manifest pins, registry, handoff, state, session and owner record created/read back |
| Bootstrap and policy preservation | PASS | Eight-file order retained; report requirement false; live-report and cross-chat gates remain PENDING |
| Runtime structure and read-only parity | PASS | Runtime validator passed; configured changes retained for review; generic shared sources retained |
| Fresh-process recovery | PASS | A new Python process read the persisted runtime and recovered the same owner, alias, ACTIVE Workstream and one next action; validation/recovery did not change fixture content |
| Negative recovery scenarios | PASS | Missing handoff, mismatched pins, reversed bootstrap and inconsistent next action blocked recovery |
| Independent AI / separate conversation recovery | NOT RUN | Fresh-process data readback does not establish assistant behavior or cross-chat continuity |
| Clean-machine Windows/macOS/Linux trials | NOT RUN | Existing Windows prerequisites were reused |
| Independent ChatGPT/Gemini guided onboarding | NOT RUN | No independent provider/session trial |
| External integrations, live report sending and production/design mutation | NOT RUN | Outside the fictional setup scope; no evidence of those capabilities is claimed |

Reproduce the six integration scenarios with `python scripts/test_onboarding.py`. That mode uses synthetic pins. For a real checkout trial, independently verify a full stable commit and supply `--stable-pin <full-commit>`; the script resolves both Git objects locally and uses actual HEAD for the candidate. Fixture creation/readback supports READ_WRITE only for those authorized local operations. It does not imply access to another runtime, remote or design file.

## Hosted CI disposition

The [candidate Actions run](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/actions/runs/38696409868) failed before any job steps were started. The GitHub run annotation reported an account lock caused by a billing issue. This explains the absent runner/steps for that run; it is not a test failure diagnosis for code that never ran.

The account owner must resolve that external condition, then rerun hosted QA on the reviewed head. No account/billing setting was changed, no payment was made, and no CI waiver is inferred. Local passing checks do not replace the hosted gate. See [ADR-0022](../decisions/ADR-0022-hosted-ci-disposition.md) for the existing gate policy.

## Follow-up and boundaries

The copyable prompt now requires explicit source selection when a guide is absent from the selected released/default source. The guide lists the audit and onboarding checks supplied by this candidate.

Keep the PR in Draft until the outstanding gates are reviewed. A later independent conversation trial should receive only the initialized runtime location, selected Workstream and startup request; recover persisted state without importing the originating conversation. If no separate session is run, retain NOT RUN and PENDING. Merge, release and adoption by an existing private project are separately governed actions.
