# ADR-0029 — Adopt GOV-VAL-001 for proportionate validation and scoped closure

**Date:** 2026-10-15  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK GOVERNANCE  
**Decision owner:** Framework maintainer  
**Supersedes:** N/A

## Context

Risk classification, postflight, finalization and review contracts already require evidence, but do not collect acceptance planning, evidence reuse and stopping rules into one mandatory operational contract. Unbounded repeat validation can consume effort without changing a decision; premature closure can hide a missing mandatory gate.

## Evidence

FACT: the maintainer supplied GOV-VAL-001 and explicitly adopted it after review of five clarifications: evidence validity context; protection against lowered criteria; possible outcomes instead of confirmation-seeking; preservation of runtime states; and completion limited to its named deliverable. Master sections 22, 26 and 35 and the review contract contain compatible safeguards. No empirical productivity gain is asserted by this decision.

## Decision

Adopt [GOV-VAL-001](../../runtime/docs/contracts/VALIDATION_AND_CLOSURE.md) as mandatory operating policy. Define criteria before tests, distinguish mandatory/triggered/optional/redundant checks, reuse still-valid evidence, justify additional testing by its possible decision effect, and close the authorized scope once sufficient evidence exists.

Keep security, privacy, integrity, compliance and all applicable mandatory gates binding. An AI cannot reduce acceptance criteria or expand waiver/publication authority. Closure assessment labels are not serialized runtime states. Record short supporting notes in existing owner records instead of adding a ledger or mandatory bootstrap file.

## Why

Explicit stopping rules and evidence validity make rigor accountable to the actual decision while preserving risk controls. Normative adoption is separate from pilot validation or any measured efficiency claim.

## Alternatives considered

- Keep the guidance dispersed: leaves the stop/reuse decision implicit.
- Always rerun everything: ignores unchanged evidence and decision value.
- Always choose the cheapest checks: can omit binding safety or acceptance evidence.
- Add new task states or a validation registry: creates unnecessary schema and ownership complexity.

## Impact

Extend the canonical Master and exact runtime mirror, JSON derivative, shared contract inventory, existing acceptance seed and methodology catalog. Preserve architecture/released version 3.6.0, startup order, runtime schemas/statuses, dependency pins, licensing and existing ADR/pilot maturity. The new catalog entry is a user-requested normative extension; existing source-audit findings are not relabeled.

Private adoption, merge, release and reactivation of hosted automation remain separate gates. This ADR records the approved policy, not permission to perform those actions.

## Validation / QA

Acceptance: the Master and runtime mirror agree; the JSON policy and registered canonical contract preserve all safeguards; assessment outcomes do not enter operational states; acceptance records expose criteria, evidence validity and scoped closure; existing full-package and synchronization checks pass. Negative checks must reject weakened mandatory safeguards and incompatible state changes. Run the six existing local workflow steps and the new targeted contract regressions once for the resulting candidate, then privacy/protected-file review and remote readback. Existing unchanged pilot experiments are not rerun.

These are package/contract integration checks. They do not prove universal operator compliance, faster delivery, human acceptance or pilot efficacy. Hosted automation remains under its separately recorded temporary suspension; no new exception is granted here.

## Revisit triggers

Material incidents, evidence-reuse errors, premature closure, unclear transition authority or observations that the policy introduces disproportionate reporting effort.

## Mutation / Change History references

Owner: public framework. Persistent history: CHANGELOG.md, GOV-VAL-001 adoption entry; implementing commit references this ADR. Read-only private-source comparison creates no private mutation record. Existing decisions remain unchanged.
