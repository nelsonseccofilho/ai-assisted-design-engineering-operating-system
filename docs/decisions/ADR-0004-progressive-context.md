# ADR-0004 — Collect project context progressively

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `FRAMEWORK`

## Context

Collecting every possible project field during onboarding creates unnecessary friction and cognitive load.

## Decision

Collect minimum context during first run and request additional fields just in time when they become operationally relevant.

## Why

Context should support work, not delay it.

## Impact

First-run onboarding stays lightweight while the system can still build rich project context over time.
