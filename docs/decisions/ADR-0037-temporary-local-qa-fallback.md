# ADR-0037 — Temporary controlled local QA during hosted Actions suspension

**Date:** 2026-10-24  
**Status:** ACCEPTED — PROCEDURE ONLY / CONDITIONAL  
**Decision owner:** Framework maintainer  
**Scope:** Generic public-framework source validation while hosted Actions execution is unavailable or intentionally suspended. **No blanket release waiver.**

## Decision and authority

On 2026-10-24, the human maintainer explicitly approved the recommendation to adopt a controlled **local QA process while the GitHub payment/access issue remains unresolved** and committed to report when it is regularized so the process can be revisited. This is permission to prepare and use a temporary validation procedure; it does **not** establish that the payment issue caused the lack of workflow runs, guarantee future platform access, or permit billing changes, workflow reactivation, paid compute or tag/publication without separate decisions.

Adopt [Controlled local QA fallback](../LOCAL_QA_FALLBACK.md) as the reference procedure for release candidates. Implement an opt-in `scripts/qa_local.ps1` wrapper that runs **nine workflow-parity Python 3.12+ commands** against a user-supplied exact immutable SHA in a clean detached checkout, probes actual symlink capability, insists on the eight current-state tests without `SKIPPED`, preserves local output logs outside the checkout and classifies hosted CI as `NOT VERIFIED`. This script and its behavior are **NOT YET RUNTIME VERIFIED** merely because this ADR is accepted; verify on the actual candidate commit before trusting it for any acceptance gate.

**Local-QA PASS is not hosted-QA PASS.** No one may represent operator-supplied shell output as execution by ChatGPT, GitHub Actions or an independent agent. Any failed or skipped test blocks local PASS. Evidence must be bound to the exact source SHA and remain clear about Windows privilege differences, synthetic fixtures and unavailable hosted Linux steps.

## Subsequent accepted release-specific exception — 2026-10-24

The reference below to ADR-0036 as `PROPOSED` describes the state **when this procedure was first adopted**. The framework maintainer later **accepted Option B specifically for v3.9.0**, under `V3_9_0_MANUAL_HOSTED_SUSPENSION_DISPOSITION`; see [attributable decision](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/27#issuecomment-6389104284) and [updated ADR-0036](ADR-0036-scoped-3-9-0-hosted-qa-disposition-proposal.md). Hosted QA remains `NOT VERIFIED`, not PASS. This subsequent approval is **not** a standing procedure waiver, not approval to reenable GitHub Actions, and **not** authorization to create the v3.9.0 tag/GitHub Release or modify a private adopter pin. Any new source SHA after recording this note requires exact-source QA before a publication decision.

## Publication boundary

A distinct, **version-scoped** maintainer risk decision is required before substituting local evidence for the unavailable hosted gate in a particular release. Specifically, v3.9.0's [ADR-0036](ADR-0036-scoped-3-9-0-hosted-qa-disposition-proposal.md) remains **PROPOSED** until the human owner explicitly accepts its documented limitations. Neither this ADR nor v3.8.0-only ADR-0034 satisfies that gate. Even then, tag/GitHub Release needs separate explicit approval with final commit SHA, actual notes, checked diff/tree, rights/privacy and release rollback/readback.

Implementation PRs must independently pass appropriate exact-SHA QA, including the wrapper itself, before merging; changing the source by adding this process invalidates inheritance of earlier candidate QA. Adoption by private project runtimes is out of scope and separately approved.

## Exit and restoration

When the maintainer reports billing/access resolution, reassess actual GitHub Actions availability and workflow state. Request authorization before any account or workflow change. Prefer real hosted Python workflow execution with logs on an identified SHA. Retire the **temporary fallback** for future normal hosted-capable releases only after an actual executed workflow is read back, and retain historical `NOT RUN` results without retroactive promotion.

## Ownership

Public-framework governance owner. Decision index: `DECISION_LOG.md`; procedure: `docs/LOCAL_QA_FALLBACK.md`; code: `scripts/qa_local.ps1`; per-release exceptions belong to their own decisions (v3.9.0: ADR-0036). No private runtime, workstream, Figma/UI Kit, third-party account or release is mutated by this procedure acceptance.
