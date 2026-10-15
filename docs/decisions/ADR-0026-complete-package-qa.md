# ADR-0026 — Evaluate the complete current package before reporting PASS

**Date:** 2026-10-15
**Status:** PROPOSED
**Scope:** compatibility and QA repair

## Context
Baseline QA reproduced three existing defects: the validator expects a removed template_sources mapping and manifest schema 1.0 although the canonical manifest is 1.1; documentation references are incorrectly classified as exact mirrors; the final runtime/startup checks occur after the validator's failure/PASS block.

## Decision
Validate the current canonical inventory and manifest without changing the manifest, bootstrap or released metadata. Distinguish documentation pointers from byte-identical aliases and check their canonical link. Move final failure/PASS evaluation after all package checks. Cover late-gate failure and pointer/alias differences with negative regressions.

## Consequences
Previously hidden or premature success becomes an explicit failure. Root documentation entrypoints keep their URLs and link to canonical contracts. Preserve the full ownership workflow in its canonical contract; repair stale branch links and make Master links portable across root and runtime without changing operative rules. The synchronization tool remains read-only; it does not migrate installed runtimes. New optional metadata is additive within inventory schema 2.0.

## Validation
Run the complete package checks, existing synchronization cases, pointer drift/missing-pointer cases and a subprocess regression proving the final startup gate fails without printing PASS. Verify that Master changes only repair link destinations, and compare the unchanged JSON derivative, manifest, state templates, locks and bootstrap against baseline.

## Supersession
None. This repairs enforcement of the existing architecture.
