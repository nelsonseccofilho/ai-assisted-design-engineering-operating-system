# ADR-0018 — Promote reusable runtime learnings to the framework

**Date:** 2026-10-06  
**Status:** ACCEPTED within the candidate; release remains gated

## Context

A configured runtime can accumulate operational capabilities that are missing from generic templates. A candidate PR can also make private operation appear ahead of the public stable main. Both require explicit ownership and promotion tracking.

## Evidence

Repository parity inspection identified missing generic manifest, governance, artifact/evidence index, backlog, QA and dependency templates alongside existing Operator, Session, Workstream and report contracts.

## Decision

The framework is the canonical source of reusable method. Runtime instances pilot that method and configure project policy. Promote reusable capabilities through generic templates, contracts, schemas and QA. Track candidate/stable refs separately, then update private pins after framework promotion.

Use docs/FRAMEWORK_RUNTIME_SYNC.md as the assembly and promotion mapping. Keep populated runtime data private. Preserve declared live validation gates.

## Why

This prevents private-only generic evolution and makes the product usable for new projects without copying another project's confidential instance.

## Impact

Adds the missing generic template surface, schema migration guidance, parity checks and a repeatable dependency/promotion process. Does not assert live pilot completion.

## Validation / QA

Validate every template mapping, manifest defaults, schema/version relationships, decision index, documentation references and public privacy/secret patterns. Report actual results separately from pending live gates.

## Supersession

Extends ADR-0015, ADR-0016 and ADR-0017; does not supersede them.
