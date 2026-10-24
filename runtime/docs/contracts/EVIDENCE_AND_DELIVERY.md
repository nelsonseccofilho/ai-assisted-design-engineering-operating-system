# Evidence, authority and verifiable delivery

**Ownership:** SHARED_CONTRACT. **Maturity:** unreleased clarification of existing evidence, bounded-autonomy and completion safeguards. Optional review records do not replace the Operating Master, project governance or the existing task ledger.

## Recover before investigating again

Load every bootstrap file required by the current manifest. Then use the current handoff, state, evidence index, accepted decisions and task owner to locate the smallest relevant body of evidence. A persisted analysis, an original source that exists, and an original source accessible now are different facts. Reopen primary material for a specific gap, contradiction or changed scope; retain the date and limitations of earlier analysis.

Read meetings and comments in context and in chronological relation. A later source supersedes an earlier decision only when its content, authority and scope establish that replacement. Preserve history and explicit supersession links. A pointing phrase needs the relevant visual context; a transcript alone may be insufficient. A resolved comment proves neither implementation nor acceptance. Shared-account authorship requires attribution evidence.

## Keep authority and status dimensions separate

| Dimension | Question |
|---|---|
| Evidence | What is directly observed, inferred, assumed, conflicting or unknown? |
| Decision | Who can decide, what did they actually authorize, and for which scope? |
| Artifact | What exists in the current owning artifact and which version was inspected? |
| Verification | Which criteria passed, failed or were not run, with what limitations? |
| Task | What does the existing authoritative ledger say under its acceptance gates? |

These are review dimensions, not new task statuses. A recommendation, designer consensus, visible frame, static QA pass and product approval are distinct. Never infer permission, functional correctness or DONE from any one of them.

A stakeholder request establishes intent within its authority; it does not establish empirical UX quality. Separate the business WHAT from the proposed HOW. Compare alternatives, including retention of the current behavior, against user goals, accessibility, risks, feasibility and source quality. Cite specific external guidance only when applicable; it does not grant product permissions. Preserve the canonical rule, its scoped application and any proposed improvement as distinct statements.

## Verify access and outcomes on the actual target

A tool catalog or old connection does not prove present access. A successful read proves that read on that target, not write capability. For an authorized mutation, verify both the operation result and subsequent artifact readback. Do not make a dummy mutation to test permissions.

Distinguish unavailable tool, denied access, absent resource and inconclusive failure. A single failed call does not establish its cause. Reconcile material readback differences before reporting completion.

## Select a concrete unit and verify it

Identify the authorized deliverable, owner, acceptance criteria and dependencies before execution. Continue independent authorized work when a local decision is blocked. Do not turn silence into approval or bypass an explicit restriction through a generic continuation request. Reuse existing components and validated evidence. Preparation and reporting support the deliverable; they do not substitute for it.

Verify the actual result against the criteria. A structural screenshot or zero bounding-box collisions is partial evidence; navigation, permissions, accessibility, native annotation visibility and runtime behavior require their own applicable checks. Report PASS, FAIL and NOT RUN per criterion without converting those labels into task state.

Report formal completed tasks as numerator/denominator from the owner ledger. Report candidate coverage separately, with its own denominator and meaning. Do not add them together. A ready-for-review design can be delivered for review while formal acceptance remains pending.

## History and boundaries

Actual mutations use each artifact's existing owner history. Read-only inspection creates no fictitious artifact change. Preserve source material; a missing historical node is not permission to recreate deliberately removed content. Do not send external communications without applicable authorization.

The broader deliverable-first efficiency policy, review-depth tuning and phase sequencing remain pilots in the [promotion guide](../../../docs/METHODOLOGY_PROMOTION.md). This contract does not claim their productivity or end-to-end effectiveness.


For the full source-chain and scenario procedure, see [evidence reconciliation](EVIDENCE_RECONCILIATION.md). Use [review and acceptance](REVIEW_AND_ACCEPTANCE.md) for controlled comparisons, scoped waivers and pilot delivery checks.

## Optional supplied action-claim consistency checker (generic candidate)

The optional, **read-only** `scripts/check_action_claim.py` can compare a
self-reported action classification to a strictly typed JSON statement containing
an operation identifier, target reference, attempted flag, tool-result
classification, attributable tool-response reference, independently cited
readback classification and the claim being reported. The supplied record is
**not** an authenticated tool log: a coherent `VERIFIED` label has meaning
*only within the supplied declarations*. The checker always emits
`observed_execution_verified: false` and `mutation_authorized: false`.
It cannot prove that a tool ran, read an external target, verified a write,
or that the operator had permission; compare actual host traces and independent
target readback under the original authority contract.

After separately reviewing its applicability, from a configured runtime root:

```sh
python -B runtime/scripts/check_action_claim.py --input path/to/reviewed-claim.json
python -B runtime/scripts/check_action_claim.py --input - < reviewed-claim.json
```

The input is one object or a nonempty array with exactly eight fields:
`operation_id`, `target`, `attempted`, `tool_result`,
`tool_response_ref`, `readback_result`, `readback_ref`, and `reported`.
Record only generic references or other privacy-reviewed identifiers.
Do not copy private real tool traces, credentials, client information or
transcripts into the public repository. Strict JSON rejects duplicate keys,
missing/extra fields, invalid outcome combinations, contradictions, duplicate
operation IDs and unjustified `VERIFIED` claims. Nonzero CLI exit indicates
invalid or inconsistent supplied evidence, not necessarily a failed
original operation. A self-consistent declaration does not substitute for
an independent reviewer.

This optional helper adds **no** authority to execute, merge, approve,
publish, or change state; it creates no new status system, Workstream,
Session, memory ledger or report cursor. This candidate requires new
exact-SHA QA, proportionate privacy/licensing review and a separate
human-approved merge. It does not retroactively change v3.8.0, the
current private project pin, proposed ADRs, or optional pilots.
