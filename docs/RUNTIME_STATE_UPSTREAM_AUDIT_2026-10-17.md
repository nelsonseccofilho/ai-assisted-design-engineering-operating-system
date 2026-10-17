# Bounded runtime-state upstream audit — 2026-10-17

**Baseline:** released framework 3.7.0. **Candidate decision:** [ADR-0032](decisions/ADR-0032-typed-state-and-current-handoff.md), PROPOSED. This delta audit does not replace the earlier [methodology audit](METHODOLOGY_AUDIT.md) or change its catalog counts.

## Scope and evidence

Compare the public state/manifest/registry seeds, package ownership, synchronization, evidence, decision and validation contracts against a bounded private-adopter selection: state-repair/proposal/adoption documents, validators, regression sources and merge readback. Exact source revisions, hashes and topic mappings remain in a restricted receipt. This is not a new whole-repository or media audit, nor a claim that every possible private lesson has been transferred.

Prior adopter static/regression results were inspected as attributed evidence, not rerun or counted as public tests. Proposal review preceded separately approved activation. Current representation and historical-format criteria have distinct outcomes. Public additions are independently authored from generic requirements using newly invented fictional inputs. No populated project profile, record or locator is copied.

## Topic dispositions

| Topic | Disposition | Destination / treatment |
|---|---|---|
| Public/private ownership and sanitization | ALREADY_COVERED | [Synchronization](FRAMEWORK_RUNTIME_SYNC.md) and [documentation ownership](../runtime/docs/contracts/DOCUMENTATION_OWNERSHIP.md). |
| Configured values, unknown fields and immutable pins | ALREADY_COVERED | Synchronization and separate project migration review. |
| Evidence validity, proportional tests and scoped closure | ALREADY_COVERED | [GOV-VAL-001](../runtime/docs/contracts/VALIDATION_AND_CLOSURE.md). |
| Mandatory base and exact typed extensions, including boolean/integer distinction | REUSABLE_GAP_ADDRESSED | [State contract](../runtime/docs/contracts/CURRENT_STATE_AND_HANDOFF.md), optional checker and fictional regressions. |
| Artifact variants, nullable/structured values and legitimate same-type evolution | REUSABLE_GAP_ADDRESSED | State contract/checker; outer types do not validate nested product semantics. Baseline hashes remain review provenance. |
| Manifest/registry-selected handoff, action alignment and entry gates | REUSABLE_GAP_ADDRESSED | State contract/checker, legacy and current-route fixtures; historical handoffs retained. |
| Historical audit separate from prospective current criteria | REUSABLE_GAP_ADDRESSED | State contract and migration seed; retain original findings/tools/inputs privately. |
| Source-backed metadata repair and exact before-images | REUSABLE_GAP_ADDRESSED | [Migration seed](../runtime/docs/templates/CURRENT_STATE_MIGRATION.md); distinguish observed, inferred and unresolved facts. |
| Proposal versus accountable scoped adoption/activation | REUSABLE_GAP_ADDRESSED | Contract, seed and ADR-0032; a profile declaration cannot verify consent. |
| Populated profiles, ownership constraints, routes, identities, locators and operational history | PRIVATE_ONLY | Excluded; no lightly renamed export. |
| Human usability, live product/native behavior, provider onboarding and productivity comparisons | PILOTS_OR_SEPARATE_EVIDENCE_PENDING | Retain earlier scoped observations and pending gates; no effectiveness claim or pilot promotion. |

Eleven topics: three already covered, six reusable gaps addressed, one private-only exclusion and one group of separately pending evidence. These are documentary dispositions, not a percentage improvement or overall runtime-health claim.

## Acceptance before testing

Require usable destinations or justified exclusions for all topics; unchanged schemas/base fields/bootstrap/aliases/pins; a read-only optional checker with nonzero failures and no authority; affected fictional positive/negative cases; the six existing workflow steps; full-content privacy review; and immutable changed-file readback. Candidate results belong in its PR.

Mandatory new cases cover exact extensions/types, identity/version/operator/references, malformed JSON and unsafe paths, mixed/duplicate/stale action markers, manifest/registry disagreement, legitimate value evolution, artifact variants and selected-scope reporting. Existing package checks retain their obligations. The new tests are wired into the workflow definition; hosted execution remains suspended, so local success is not hosted PASS.

Reuse unaffected evidence only within its original scope under GOV-VAL-001. No unchanged pilot campaign is repeated. There is no new efficiency measurement, provider/clean-machine result, human acceptance, product authority, project activation or publication. No private repository or design artifact changes.

## Next decision

Review the exact tested PR revision. Merge needs separate explicit approval. ADR acceptance, project adoption and release retain their own gates; optional distribution cannot grant them. Installed dependencies and default validation remain unchanged.
