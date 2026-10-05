# ADR-0002 — Keep project/client context local and private

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `GOVERNANCE`

## Context

The public framework may be reused across consulting clients, but real project context can include confidential company names, stakeholders, design files, internal references, and evidence.

## Decision

Real project context must live in local/runtime files such as:

- `PROJECT_CONTEXT.local.md`
- `HANDOFF_CURRENT.local.md`

These files must be ignored by Git by default.

## Why

The public framework should teach the method without exposing client information.

## Impact

Public distribution remains generic while real work can still use rich contextual information locally.
