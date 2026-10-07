# ADR-0023 — Classify documentation ownership across framework and project runtimes

**Date:** 2026-10-07  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK GOVERNANCE

## Context

The Project Runtime capability was developed while a real private runtime and the generic framework evolved in parallel.

That produced useful traceability, but some historical project records also described framework architecture in detail. Without an explicit boundary, future work could duplicate framework history inside private runtimes or accidentally treat project-specific records as reusable method.

## Decision

Classify every durable documentation record as exactly one of:

- `FRAMEWORK_OWNED`;
- `PROJECT_OWNED`;
- `SHARED_CONTRACT`;
- `CROSS_REPO_REFERENCE`.

The public framework is the canonical owner of reusable method, framework ADRs, framework CI/release history, templates, schemas and generic QA.

A private Project Runtime is the canonical owner of project context, stakeholder requirements, proprietary evidence, project Decisions and populated operational records.

Shared contracts are authored upstream in the public framework and consumed by pinned runtimes.

Cross-repository references link canonical owners without duplicating their full history.

Historical accepted records are preserved. Where an older private project ADR overlaps framework architecture later promoted upstream, append an ownership/adoption note rather than deleting or silently rewriting the record.

## Why

Ownership should follow the subject of the durable record. This keeps framework evolution reusable, project history confidential, and cross-repository traceability explicit without maintaining two competing canonical histories.

## Impact

Adds the shared `runtime/docs/contracts/DOCUMENTATION_OWNERSHIP.md` contract, updates runtime inventory, and requires future promotion/adoption work to identify canonical documentation ownership.

## Validation

- framework ADRs/release notes remain public-owned;
- project evidence and populated history remain private-owned;
- shared contracts stay synchronized;
- promotion links use cross-repo references instead of copied histories;
- privacy scan remains clean.

## Supersession

None.
