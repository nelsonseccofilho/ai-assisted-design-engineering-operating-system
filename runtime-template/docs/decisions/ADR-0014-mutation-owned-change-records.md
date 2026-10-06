# ADR-0014 — Mutation owners own persistent change records

**Date:** 2026-10-06  
**Status:** `ACCEPTED`  
**Scope:** `GOVERNANCE`  
**Decision owner:** Framework maintainer  
**Supersedes:** N/A  
**Superseded by:** N/A

## Context

The Master defines governance, Change History, decisions and handoff, but a single project-level history location does not specify which artifact owns a mutation record. This can route consumer changes into a shared library merely because it already has Governance.

## Evidence

FACT: Master sections 23 and 27 previously allowed a governance baseline and project-level decision/change history location without an explicit per-artifact routing contract. Project Context exposed one combined decision/change history field. ADR-0010 requires persistent significant decisions; ADR-0013 requires implementing commits to reference them. The current package has manual publication QA and a JSON derivative, but no formal JSON Schema, automated tests or CI. These are repository observations, not copied project evidence.

## Decision

**THE FILE / ARTIFACT THAT OWNS THE MUTATION OWNS THE CHANGE RECORD**

Adopt the owner routing and append-only correction contract in Master section 27. Register each owner's history location and namespace in Project Context. Significant mutations require persistent records at every actually mutated owner and links between multi-owner records. Read-only inspection creates no dependency record. Consumer evidence can support a library change without a consumer mutation; local adoption can cite a library without a library mutation. No central fallback log is permitted.

Establish missing owner history before significant-change finalization. An explicit durable owner-scoped companion is allowed when inline history is unsupported, with a registered owner pointer. Preserve the three existing context layers and their just-in-time onboarding.

Historical misrouting is corrected by adding a canonical owner copy and reciprocal correction references, preserving the original as archived/pointer evidence. Handoff/workstream/chat memory cannot replace persistent records.

## Why

Mutation ownership makes history auditable without confusing shared dependency authority with the artifact actually changed. Linking records retains cross-artifact coordination without centralizing consumer histories.

## Alternatives considered

- Central shared-library log: rejected because it misattributes consumer mutations and hides missing owner governance.
- Record every inspected artifact: rejected because evidence collection does not imply mutation.
- Handoff or Git alone: rejected because continuity snapshots and implementation history do not provide all persistent owner history and rationale.
- Require inline history in every file format: rejected because some artifacts require explicit owner-scoped companions.

## Impact

This is an additive clarification of the existing governance contract, not a redesign of the operating model. Existing project-level fields remain summaries; active runtime contexts gain registry rows just in time before significant-change finalization. Historical records remain intact.

The Master, startup, context/handoff templates, JSON derivative, examples, rationale, README, decision index and publication QA are aligned. Framework source changes remain traceable through Git, with framework release history in CHANGELOG.md; external consumer histories remain with their owners. Released 3.3.0 metadata is retained while the addition is Unreleased.

## Validation / QA

Run `python scripts/validate_framework.py` plus `docs/PUBLICATION_CHECKLIST.md`. Validate local Markdown references, ADR indexing, JSON/Master metadata and governance parity, bootstrap order, required template fields and generic positive/negative ownership scenarios. Manually review scope, evidence accuracy, append-only correction and privacy.

Implementing commit must use Conventional Commits and `Decision: ADR-0014`. No merge is authorized by this record.

## Supersession

N/A. This extends ADR-0010 and ADR-0013; neither is superseded. Accepted prior ADRs are preserved unchanged.

## Revisit triggers

Revisit if artifact formats require new companion mechanisms, automated runtime validation is introduced, or owner identity/namespace collisions appear.
