# ADR-0017 — Derive Operator Daily Reports from persistent runtime evidence

**Date:** 2026-10-06  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK

## Context

Long-running Project Runtimes can preserve operational state across chats, but daily team/client status communication can still force operators to reconstruct activity manually.

## Decision

Add a generic Operator Daily Report capability.

Use persistent reporting cursors.

Generation creates DRAFT and never advances the cursor.

Confirmed external sending creates SENT and advances the cursor.

Projects configure language, timezone, command aliases and whether daily reporting is mandatory.

Recommended commands:

- `<operator_alias_lower>_report`
- `<operator_alias_lower>_report_sent`

When mandatory mode is enabled, an operator with material project activity must end the reporting day as SENT or explicitly WAIVED.

## Why

Status communication should be reproducible from the same persistent evidence used for operational continuity.

## Impact

Adds report templates, report state and runtime/master/startup contracts.

Daily report state remains independent from artifact QA and Workstream status.

## Validation

Verify cursor semantics, first-report baseline, evidence grounding, blocker accuracy and fresh-session generation.
