# ADR-0001 — Separate Operating Model, Project Context, and Current Handoff

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `FRAMEWORK`

## Context

A single large prompt mixed stable operating rules, project-specific context, and rapidly changing task state. This increased cognitive load, reduced portability, and made stale context more likely.

## Evidence

- stable rules changed slowly;
- project identity changed between clients/projects;
- current task state changed frequently;
- long conversations eventually reached context limits.

## Decision

Separate the system into three layers:

1. Operating Model — persistent working method.
2. Project Context — project/client environment.
3. Handoff — current operational state.

## Why

Each layer has a different lifecycle and should be maintained independently.

## Impact

The framework becomes reusable across projects and easier to hand off between AI sessions.

## Validation / QA

A new session should be able to load the Master + Project Context + Current Handoff without requiring the entire previous conversation.
