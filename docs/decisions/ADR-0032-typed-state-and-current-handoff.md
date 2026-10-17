# ADR-0032 — Optional typed state and explicit current handoff

**Date:** 2026-10-17
**Status:** PROPOSED
**Scope:** compatible public candidate; no project activation or release.

## Context and evidence

An earlier bounded transfer established generic runtime preservation rules. A later focused private-adopter review found reusable implementation details: strict declared extensions, legitimate value evolution, explicit current routing, source-backed repair and separate historical criteria. Restricted static adoption and regression evidence supports those representation methods in one adopter; no raw records or identifiers belong here. See the [bounded delta audit](../RUNTIME_STATE_UPSTREAM_AUDIT_2026-10-17.md) for coverage and limits.

## Proposed decision

Distribute [GOV-RUNTIME-STATE-001](../../runtime/docs/contracts/CURRENT_STATE_AND_HANDOFF.md), an unconfigured migration seed and a dependency-free read-only checker. Add fictional format/behavior examples. Preserve all fourteen base fields, schemas, ordered bootstrap, status enums, existing seeds, aliases, dependency pins and framework version 3.7.0. The generic checker is independently implemented from requirements, not a copied project validator.

Keep opt-in scope explicit; the default package checker remains unchanged. Profiles declare exact additional keys/types and artifact variants. Manifest, registry, state and current handoff agree for selected Workstreams. Historical records remain intact; current structural success cannot rewrite old findings or supply execution authority. A declared ACCEPTED status is not verified consent.

## Why and alternatives

Allowing arbitrary extras loses integrity; dropping them destroys evidence. A single forced artifact shape loses valid legacy data. Picking the latest marker confuses accumulated history with current intent. Freezing live values to review hashes blocks legitimate updates. Explicit typed profiles, routes and prospective approval address these risks while keeping old projects compatible.

Documentation alone would leave format and failure behavior ambiguous. Automatically replacing installed validation would exceed the evidence and authority available; therefore the checker stays optional and selected-scope only.

## Validation / QA

Before integration: six existing workflow steps, the focused checker regressions, full-content privacy review, unchanged compatibility/authority boundaries and immutable remote readback. Test malformed/unknown/missing/type/reference/route inputs and same-type evolution using fictional files only. Results belong in the reviewed PR, not a claim of hosted execution. GOV-VAL-001 excludes redundant private, live and pilot reruns.

## Impact, adoption and supersession

New shared contract/checker and one configured review seed require package inventory classification. Distribution is not project adoption. A project must separately approve and record its contract version, migration, activation and rollback, preserving existing mandatory checks. This proposal accepts no pending ADR, promotes no pilot and changes no installed runtime, release, license or hosted-CI disposition. Existing accepted decisions prevail. Rollback removes unadopted candidate additions or restores affected project selections from reviewed before-images without deleting history.
