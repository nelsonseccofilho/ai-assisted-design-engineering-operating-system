# ADR-0015 — Use a persistent Project Runtime for operational continuity

**Date:** 2026-10-06  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK

## Context

Long-running AI-assisted work spans multiple chats, tools, operators and days. Chat/model memory is bounded and cannot safely serve as the only durable project state store.

## Evidence

- handoffs already reduce context loss but remain fragile when they are reconstructed only at chat end;
- Git/versioned storage provides history, diffs, rollback and traceability;
- live artifact state can legitimately diverge from stored snapshots.

## Decision

Support a persistent **Project Runtime** as the preferred operational-memory layer for long-running work.

The Project Runtime is canonical for operational continuity, governance, coordination and recorded decisions.

It does not replace primary evidence, current inspected artifact state, or the canonical Design System.

For Git-backed runtimes, prefer `main` as the stable bootstrap ref.

## Why

This preserves continuity without promoting chat transcripts or model memory into a project database.

## Impact

The framework supports both:

- Persistent Project Runtime mode;
- local minimal mode for simpler use cases.

## Validation

A real new-chat bootstrap must recover current work from persistent state, reinspect the live artifact, reconcile divergence and continue without the human rebuilding prior conversational context.
