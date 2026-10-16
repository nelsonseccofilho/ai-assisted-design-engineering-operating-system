# ADR-0030 — Prepare a compatible 3.7.0 release candidate with separate publication gates

**Date:** 2026-10-15
**Status:** PROPOSED
**Scope:** FRAMEWORK RELEASE PREPARATION
**Decision owner:** Framework maintainer

## Context

Public main contains accumulated onboarding, methodology, validation, templates and bounded experiment records beyond the documented 3.6.0 release. Approved PR integration does not publish a release or update an installed project. The maintainer requested preparation of the next candidate and evaluation of downstream adoption.

## Proposed decision

Prepare version 3.7.0 as a compatible minor release candidate. The package adds capabilities and the separately accepted GOV-VAL-001 safeguard without removing existing entrypoints or changing runtime schemas, operational states, mandatory bootstrap, license terms or configured project values. Compatibility here concerns these interfaces; it does not prove every operator or adopter has migrated successfully. A downstream incompatibility found during review must be resolved or explicitly reassessed before publication.

Label candidate sources NOT RELEASED. Keep 3.6.0 as the documented released baseline until publication is separately approved and completed. Preserve historical reports, catalog review metadata, proposed ADR statuses, pending pilots and immutable dependency pins. Distribution of optional guidance does not accept the guidance's proposed ADR or establish effectiveness.

Use the [release candidate record](../RELEASE_3_7_0.md) for scope, drafted notes, evidence requirements and publication/adoption sequence. Reuse valid prior evidence under GOV-VAL-001; run package QA for materially changed release metadata and validator. Do not repeat unchanged human, native, retrieval or functional studies without a new question.

## Gates retained

- Candidate PR integration requires its own reviewed immutable payload and explicit maintainer authorization.
- A tag/GitHub Release requires a separate decision covering the final immutable commit, notes and all applicable release gates.
- The manually suspended workflow is not a fresh runner-zero result. ADR-0022 and previous PR dispositions are not blanket approval. Obtain real hosted evidence or an explicit, documented release-specific decision consistent with the governing requirements; otherwise publication stays blocked.
- Existing required live evidence must be assessed against its original scope and changed contracts. Optional unvalidated pilots may be distributed only with their pending status and claim limits intact.
- Private adoption requires a separate reviewed migration after the released source/pin exists. It must preserve local shared-file divergences for reconciliation and configured values/history. No private pin is changed by this candidate.

## Alternatives

Remain indefinitely at 3.6.0: obscures the accumulated user-facing changes. Patch-only numbering: understates additive capabilities. Major numbering: no removed interface or incompatible schema is identified in the bounded comparison. Publish immediately: skips separate gates.

## Validation and ownership

Require consistent candidate metadata, exact Master/mirror parity, unchanged runtime schemas/inventory/pins/licenses, the six local workflow steps, full publication/privacy review and immutable changed-file readback. Record actual results in the candidate PR, without a self-referential candidate commit inside its own source. Local Windows execution is not hosted Linux execution.

Owner: public framework. Change History: CHANGELOG.md. No external project history is copied here. This proposed ADR records preparation and a decision request; it grants no merge, publication, waiver or private-adoption authority.

## Revisit triggers

Incompatible adopter configuration, new material evidence, changed public content after validation, restored hosted execution or a maintainer publication decision.
