# ADR-0010 — Require explicit documentation for every significant decision

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `GOVERNANCE`

## Context

The framework depends on continuity, traceability, and explicit evidence. Undocumented decisions can disappear between sessions or become impossible to audit later.

## Decision

Every significant decision must be documented in a persistent decision record.

Framework-level decisions use ADRs under `docs/decisions/`.

Project/client decisions should use an equivalent private decision log when they contain contextual or confidential information.

A decision record must contain at minimum:

- context;
- evidence;
- decision;
- rationale;
- impact;
- status.

Where relevant it should also contain:

- alternatives considered;
- QA/validation;
- supersession links;
- revisit triggers.

## Why

Decision history is part of the operating system, not auxiliary documentation.

## Impact

The framework gains durable institutional memory and makes changes explainable across sessions and versions.

## Validation / QA

A release or significant workflow change is incomplete if its corresponding decision record is missing.
