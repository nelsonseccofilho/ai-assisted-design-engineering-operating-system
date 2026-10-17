# ADR-0031 — Accepted release-specific treatment of manually suspended hosted QA

**Date:** 2026-10-17
**Status:** ACCEPTED
**Scope:** VERSION 3.7.0 PUBLICATION ONLY
**Decision owner:** Framework maintainer (@nelsonseccofilho)
**Accepted:** 2026-10-17, explicit maintainer approval; exception limited to v3.7.0
**Related:** ADR-0022, ADR-0029, ADR-0030

## Context

The maintainer requested temporary manual suspension of Static QA and separately approved reviewed integrations using local evidence. PR #17 integrated the 3.7.0 preparation, but expressly excluded release, proposed-ADR acceptance and private adoption. A disabled workflow does not supply a fresh job with runner ID zero. It would be incorrect to claim that manual suspension alone satisfies ADR-0022's observed-run criteria.

## Acceptance record

On 2026-10-17 the framework maintainer explicitly accepted and authorized recording this exception only for v3.7.0, using the reviewed local QA while Actions remains suspended, preserving all other mandatory criteria. The approval expressly excluded tag/GitHub Release creation, pilot promotion and private-runtime mutation. Publication still requires approval of the actual final immutable commit and notes. This records an accountable decision; it is not publication authorization or automatic satisfaction of the conditions below.

The reviewed baseline was integrated [PR #18](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/18), main `8c00cec3f510579329794312f30af49e9f5890e0`, tree `2ddad238697012c94380e65d1b4dc217a98be0aa`. Its six local workflow steps, 760 package checks, three publication-guard negative cases and twelve-file readback remain evidence for that exact payload. The decision-record change requires its own applicable package/privacy/readback evidence in its PR; it does not relabel baseline runs as new results.

## Accepted decision — conditional publication path

For version 3.7.0 only, permit the maintainer to make a separate publication decision while the previously requested manual suspension remains in effect, provided every condition below is satisfied and documented. This is a new, narrowly scoped release exception for manual suspension, not an assertion that ADR-0022's runner/step criteria have been met. ADR-0022 remains unchanged and continues governing its original non-executing-job case.

1. Independently observe and record `disabled_manually` and preserve the inspectable workflow definition. Do not re-enable it or start paid/hosted work without authorization.
2. Bind the exact final commit/tree to actual PASS results for all six existing local workflow commands, full-content privacy/secret/rights review, protected contracts and immutable changed-file readback. Record local environment and any harness/setup failure; local Windows evidence is not hosted Linux evidence.
3. Review applicability of the earlier core live evidence against the current changes. Preserve its original revision/scope. A material live-contract change, missing required evidence or known blocker cannot be waived by this decision. Optional/pending pilots remain excluded from validated-capability claims.
4. Distribute accepted GOV-VAL-001 as adopted policy; retain ADR-0024–0028 and ADR-0030 as PROPOSED and their supplemental/experimental scope. Neither distribution nor merge accepts those ADRs or promotes pilots.
5. Review final version metadata, notes, licensing and absence of private/configured material. A version string alone is not publication or installed adoption.
6. Explicit accountable acceptance of this exception is recorded above. PR integration, publication and private adoption remain separate decisions; an approval must name the actions it covers. Acceptance does not waive evidence conditions or authorize integration of an unreviewed record.
7. Obtain explicit publication authorization for the actual final immutable commit and notes after integration/readback. Create no release based only on acceptance of this exception or an earlier PR approval.
8. In the release notes record hosted QA as **not executed because of manual suspension**, local QA separately, exception decision/owner and remaining limits. Never label this hosted PASS or silently copy the previous `DISPOSITIONED_INFRASTRUCTURE` label into new observed evidence.

## Limits and expiry

The exception applies only to the approved 3.7.0 release payload. It does not change security/privacy/integrity requirements, waive local QA, authorize another release, enable automation, accept pilots, change private pins or authorize any Figma work. A material payload change invalidates its evidence binding and requires affected validation and renewed decision. Restore ordinary hosted evidence when the maintainer authorizes reactivation and actual execution becomes available; retain failures and prior limits.

## Alternatives

Restore hosted QA: preferred when available and authorized. Defer publication: remains valid if final publication is declined or required evidence is insufficient. Treat a disabled workflow as a runner-zero PASS: rejected because it fabricates execution/eligibility. Use an indefinite waiver: rejected because it removes the specific release decision.

## Validation and ownership

This decision adds no runtime state, package path, operational ledger or executable waiver. It is public framework release governance. Index it in DECISION_LOG.md and record preparation in CHANGELOG.md. The [finalization record](../RELEASE_3_7_0_FINALIZATION.md) identifies reviewed evidence and pending gates; the final PR supplies its exact immutable identity and actual QA/readback results. Maintainer acceptance is recorded here; actual publication, final evidence binding and private adoption remain separately pending. Historical PROPOSED text remains visible in Git and PR #18.
