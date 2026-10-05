# ADR-0005 — Current inspectable tool state outranks stale snapshots

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `TOOLING`

## Context

A handoff is a snapshot. The actual design/tool state may have changed after the handoff was written.

## Decision

When the current tool state can be inspected, it takes precedence over stale conversational snapshots. Divergences must be investigated rather than silently overwritten.

## Why

Continuing from outdated context can introduce incorrect mutations.

## Impact

The system becomes more resilient to concurrent changes and stale handoffs.
