# ADR-0035 — Prepare an additive v3.9.0 framework candidate with distinct publication and adopter gates

**Date:** 2026-10-24
**Status:** PROPOSED
**Scope:** FRAMEWORK RELEASE PREPARATION — no publication
**Decision owner:** Framework maintainer

## Context

The released and immutable public v3.8.0 remains the last actual publication. Subsequent public main integrated three additive, opt-in generic runtime scripts through [PR #23](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/23), [PR #24](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/24) and [PR #25](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/25). Their provenance, review and exact-SHA Windows package checks were recorded for **those source trees**, with a Windows symlink subtest SKIPPED, GitHub-hosted QA NOT VERIFIED and no independent actual-agent effectiveness claim. The optional pilot catalog remains unchanged. Merging feature code is neither versioned distribution nor downstream adoption.

## Proposed decision

Prepare a **v3.9.0 minor-release candidate** with only metadata consistency changes and documented additive feature notes. The original Master and exact runtime mirror change by version header only; its operative rules, bootstrap and state schemas do not change. Keep the derivative JSON policy constant except for the version field and preserve the 65-entry runtime inventory, aliases, configured seeds, local private pins, report cursors and historical candidate/release records. The README must distinguish `**Framework version:** 3.9.0` **candidate** from the actually **published v3.8.0**.

The new methods remain opt-in: bounded source transport does not establish reading by an agent; a consistent evidence declaration is not an authenticated tool log; the cycle-focus packet does not autonomously recover an objective or authorize action. No proposed ADR status or optional pilot classification is promoted through this release candidate.

## Gates and limitations

1. **Candidate PR integration:** independently read back exact changed Git blobs and verify Master/mirror equality, versioned derivative/README/validator consistency, runtime inventory, schemas/locks/bootstrap/licensing and all nine official Python workflow commands **on the new candidate SHA**. Record any `SKIPPED` and failures without promotion to PASS. Confirm clean worktree and proportionate full-content public privacy/rights review. Human owner review and permission to merge are separately required.
2. **Release publication:** a GitHub tag/release requires a **new and separate explicit maintainer decision**, identifying final immutable SHA, versioned release-note text, publish/rollback plan and the disposition of hosted QA. Earlier ADR-0031/ADR-0034 and any PR #22–#25 local acceptance **do not** waive hosted requirements for v3.9.0. Manually suspended hosted Actions are `NOT RUN` unless actual runs exist; no fictitious Linux PASS.
3. **Private adopter upgrade:** after a real public release exists, a project-owned decision and three-way shared-file audit must protect pinned source, configured values, original local modifications and records. Newly shared package paths are manually reviewed; no copied private Sessions/Workstreams/transcripts, and no automatic private pin write.
4. **Pilot/live behavior:** cross-chat agent recovery, original transcript and video review, actual tool readback and optional pilots remain bounded by their own source and human authority. These are not implicitly verified by fictional Python unit tests.

## Alternatives and impact

Patch-only numbering understates three independent additive tools. Major numbering is unsupported without an identified incompatible interface. Immediate tag/release skips independent candidate QA and hosted publication decision. Deferring preparation forever obscures an accumulated reviewed source tree. This **PROPOSED** decision requests preparation and later review, not unconditional integration/publication authority.

Mutation owner: public framework; framework history `CHANGELOG.md`, decision index `DECISION_LOG.md`, candidate package record `docs/RELEASE_3_9_0.md`. No private owner, Figma, Product or UI Kit is mutated.
