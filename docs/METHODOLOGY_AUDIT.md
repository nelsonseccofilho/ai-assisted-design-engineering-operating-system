# Bounded methodology coverage audit

**Status:** unreleased proposal under [ADR-0028](decisions/ADR-0028-traceable-methodology-audit.md).
**Operating baseline:** 3.6.0. This audit proposes generic material; it does not merge, release or update any private dependency.

## What was audited
The authoring audit retrieved every tracked text blob from an immutable private-adopter snapshot and the public candidate, with complete recursive inventories and Git blob-hash verification. Current stable public source was independently checked as the comparison baseline. Policies, inline/standalone decisions, shared/configured files, sessions, workstream handoffs, task ledgers, evidence analyses, tracking, tests and historical records were included.

The source-level ledger contains private paths, blob identities, review dispositions, finding links and source-integrity observations. It remains local/restricted and is not part of this public package. No private evidence excerpts, client names, source locators, original records or unique project values are published.

Review consisted of complete text retrieval and structured per-file content screening, contextual review of policy/decision/incident-bearing material, cross-document chronology and public destination comparison. It was not line-by-line human verification of every historical assertion or replay of original media. Untracked material, inaccessible original recordings and future commits are outside this bounded claim.

## Finding-level coverage
The [machine-readable catalog](methodology-catalog.json) contains 34 generic topics, including two user-requested onboarding/audit extensions identified separately by origin. Existing core capabilities are referenced, repeated observations are consolidated, summary-only methods receive usable procedures/templates, optional pilots retain their limits, and product-specific content is excluded.

| Area | Reusable destination |
|---|---|
| Source inventory, duplicate provenance, chronology and journey coverage | [Evidence reconciliation](../runtime/docs/contracts/EVIDENCE_RECONCILIATION.md) |
| Shared API, slot/control compatibility, publication and adoption | [Design change control](../runtime/docs/contracts/DESIGN_CHANGE_CONTROL.md) |
| Unique decisions, aliases, index completeness and contract fidelity | [Decision integrity](../runtime/docs/contracts/DECISION_INTEGRITY.md) |
| Independent critique, controlled comparison, metrics and scoped acceptance | [Review and acceptance](../runtime/docs/contracts/REVIEW_AND_ACCEPTANCE.md) |
| Concise annotations, ancestry, exact preservation and blind retrieval | [Annotation handoff pilot](../runtime/docs/contracts/ANNOTATION_HANDOFF_PILOT.md) |
| Parentage, dependent reflow, native labels and content stress | [Canvas and content QA](../runtime/docs/contracts/CANVAS_AND_CONTENT_QA.md) |
| Counts, compound indicators, domain labels and actor/effect semantics | [Editorial review](../runtime/docs/contracts/EDITORIAL_REVIEW.md) |
| Comment triage, knowledge relations, selective retrieval and research costs | [Knowledge and efficiency pilots](../runtime/docs/contracts/KNOWLEDGE_AND_EFFICIENCY_PILOTS.md) |

Existing evidence/delivery, owner-task and design-foundation contracts remain their canonical owners; the new procedures add detail through links. Five unconfigured review seeds are classified in the package inventory. They supplement existing owner records rather than establishing new ledgers or mandatory startup documents.

## Reproduce the coverage checks
Run from the public framework checkout:

```text
python scripts/audit_methodology.py --framework .
python scripts/test_audit_methodology.py
```

The public command validates catalog identities, dispositions, target existence and explicit claim limits. It verifies documentation coverage, not effectiveness. For a local restricted audit, additionally provide its inventory and source ledger using the command's private-input options. The command reports counts/errors only and never writes or uploads source data.

A complete source mapping means every inventoried file has findings or a reasoned privacy/configuration/history exclusion, with the expected blob identity. It does not prove that every conceivable methodological inference has been discovered. Finding counts and file counts are separate measures.

## Source integrity versus promotion
The restricted audit records ambiguous historical decision identities, index omissions and installed shared-source/pin differences where observed. It distinguishes inherited public-package QA defects from adopter-specific drift. These observations inform generic integrity procedures; they do not authorize rewriting private governance or presenting historical snapshots as current live authority.

## Remaining gates
- Independent live/behavioral acceptance for each pilot and any necessary local adoption.
- Clean-machine/provider onboarding trials, real design/runtime/keyboard/native-editor tests where relevant.
- Hosted CI execution and explicit review of proposed ADRs.
- Authorized merge/release and a separately governed private pin update.

The audit inspected repository text and actual public authoring readback. It did not mutate design artifacts, send stakeholder messages, restore deleted material or modify a private repository. All maturity and acceptance limits remain explicit.
