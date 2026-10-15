# ADR-0028 — Close methodology promotion gaps through a bounded source audit

**Date:** 2026-10-15
**Status:** PROPOSED
**Scope:** reusable methodology coverage and audit integrity

## Context
A topic summary can mention a private-adopter practice without making its procedure reusable. Method also appears in historical sessions, QA, migrations and incidents. Completeness must be bounded to an immutable source snapshot and cannot be inferred from a few policy documents.

## Decision
Audit every tracked text artifact at fixed public/private source commits, verify fetched blob hashes, assign a source-level disposition, and separately track distinct reusable findings. Preserve detailed source locators and project payloads locally/private. Publish only generic methods, maturity limits, reusable seeds and a privacy-safe catalog.

Complete previously summary-only guidance for evidence reconciliation, compatible component migration, decision-ID integrity, scoped acceptance/comparison, contextual annotation, canvas/content QA, editorial context and measured efficiency pilots. Keep existing core references instead of duplicating them.

## Validation and boundaries
Catalog entries identify real candidate paths and explicit evidence/maturity limits. Automated checks cover target presence, unique IDs, dispositions and source-mapping completeness for a local restricted ledger. Negative cases must reject missing sources, unsupported claims and private references in public catalog data. The audit also found the runtime validator reporting before its last startup checks; move its final result after all checks, consistent with ADR-0026, and cover that failure path.

A covered source has a documented disposition; it does not mean all original media were replayed, all pilots passed or all private governance defects were repaired. Historical records and configured private/shared files remain unchanged. Source integrity issues are recorded separately from transferable method.

## Compatibility
Additive shared procedures and unconfigured seeds use the existing runtime inventory. No new mandatory bootstrap, task state, model dependency, private pin update or release. Proposed ADRs remain reviewable in Draft.

## Supersession
None.
