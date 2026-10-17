# 3.7.0 — publication finalization for review

**Preparation date:** 2026-10-17.
**Status:** hosted exception accepted on 2026-10-17; final publication approval and execution pending.
**Integrated candidate:** [PR #17](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/pull/17), main `e91a785a33b9628a555df2332f97dc76357a1af1`, tree `21283bd35ec23a3bc2e399eaa36512c5a44094ff`.

## Deliverable

Prepare the final distributable source and [release-note text](releases/v3.7.0.md), plus the explicitly accepted [release-specific decision](decisions/ADR-0031-scoped-3-7-0-manual-ci-release-decision.md). No tag, GitHub Release, hosted reactivation, private mutation or pilot promotion occurs here.

Package version 3.7.0 identifies the contents. Temporary candidate-only labels/JSON fields are removed without inserting a claim that publication occurred. [GitHub Releases](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/releases) and its immutable tag target are the distribution record; branch presence and a version header are not publication or adoption. Historical candidate metadata/QA remain in the [preparation record](RELEASE_3_7_0.md), PR #17 and Git history.

## Scope and evidence applicability

The candidate's six local steps, 740 package checks, three candidate-label negative cases and eleven-file readback remain evidence for its exact tree, not for this finalization. This revision changes publication metadata, its validator and documentation; actual finalization QA and changed-file readback must be recorded in its own PR. Candidate-specific guards are replaced by version/parity checks and a check that publication is an external record, without weakening runtime or privacy checks.

Against the integrated candidate, retain all runtime inventory entries, schemas/states, bootstrap, configured seeds, lock pins, accepted/proposed ADR statuses, catalog classifications and license bytes. The Master and exact mirror change only publication metadata. JSON operational policy stays identical. The finalization PR must demonstrate these protected invariants before integration.

Earlier core cross-chat, live-artifact reconciliation and report-cycle observations remain attributed historical evidence. This finalization introduces no live operational interface change, so it supplies no new live result and does not automatically invalidate those scoped observations. The earlier GOV-VAL-001 package evidence remains reusable for unchanged policy content. If review identifies a material changed live dependency or missing mandatory criterion, publication blocks and the affected check becomes necessary.

The 35-topic catalog and seven optional pilots remain unchanged. Human comprehension, individual native annotation collapse/expanded occupancy and cross-file published-library adoption remain unverified. B1–B8 remain NOT RUN; delivery-efficiency comparison remains DEFERRED. Preserve recorded neutral/negative findings. These limits exclude stronger claims; they are not promoted into whole-release blockers for a delivery that makes no such claims. Required security, privacy, integrity and applicable live gates remain binding.

## Finite gate sequence

| Stage | Required disposition |
|---|---|
| Finalization preparation | Six local workflow steps, relevant publication/version guard regressions, full privacy/rights/protected-file review and immutable changed-file readback at the finalization head. Results in its PR. |
| Finalization integration | PR #18 was explicitly approved and integrated as `8c00cec3f510579329794312f30af49e9f5890e0`; its actual main tree matched the tested finalization. Acceptance-record integration/readback belongs to its own reviewed PR. |
| Hosted release decision | ADR-0031 explicitly ACCEPTED by the maintainer on 2026-10-17 for v3.7.0 only. Its conditions remain binding. Hosted QA was not executed because of manual suspension; no hosted PASS or ADR-0022 runner-zero eligibility is inferred. |
| Governance record | Acceptance scope, accountable owner, approval date and reviewed baseline are recorded in ADR-0031/index. Validate and read back this recording change before its separate integration decision. ADR-0022 and ADR-0024–0028/0030 remain unchanged. |
| Publication authorization | Present the actual final immutable commit/tree and final note text, QA/privacy/readback, hosted disposition and limitations for explicit approval. No open-ended permission for future revisions/releases. |
| Publish and verify | Create v3.7.0 tag and GitHub Release only after authorization. Read back the exact tag target, release status/notes and source identity; report the actual result. Do not claim completion from a pending request. |
| Private adoption | Separate project PR and reviewed three-way reconciliation using the actually published immutable pin. Preserve configured data/history; no private update is performed by this record. |

Do not create a chain of release candidates merely for elapsed time or renewed model limits. Reuse still-valid evidence under GOV-VAL-001. A source or acceptance change supplies the concrete reason for affected validation; a missing owner decision stays a decision, not another experiment.

## Publication payload

Use `v3.7.0` as the intended tag and `Framework v3.7.0 — evidence-based validation and reusable design methods` as the intended title, subject to the final explicit decision. Copy the scoped sections of [release notes](releases/v3.7.0.md), then append actual final commit/tree, local QA/readback identity, accountable hosted-gate disposition and decision record. Do not publish placeholders or pending approvals as completed evidence.

The notes retain supplemental/proposed methodology scope and the noncommercial/source-available licensing. No original project records, transcripts, recordings, identities or operational URLs belong in this payload.
