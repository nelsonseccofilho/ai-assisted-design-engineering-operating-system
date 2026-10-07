# ADR-0016 — Separate Operator, Session and Workstream topology

**Date:** 2026-10-06  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK

## Context

Stable operator identity, individual chats and continuing Workstreams change at different rates.

A Workstream may change operator. A chat may touch multiple Workstreams. Therefore paths that bind Workstreams to operators or Session Records to exactly one Workstream create false ownership or duplication.

## Evidence

- Operator aliases persist across multiple chats;
- Workstreams are designed to survive chat changes;
- multi-workstream sessions are operationally plausible;
- context limits require deterministic transfer between chats.

## Decision

Use independent identities:

- Human operator;
- Operator alias;
- Chat label;
- Workstream ID.

Recommended Workstream ID:

`WS-YYYYMMDD-NNN-<slug>`

Recommended Session Record path:

`sessions/<OPERATOR_ALIAS>/<YYYY>/<MM>/<YYYY-MM-DD>_<chat-label>.md`

A Session Record may reference multiple Workstreams.

Maintain one current handoff/state per Workstream.

Treat conversation-limit warnings as mandatory continuity triggers.

Support runtime access modes:

- READ_WRITE;
- READ_ONLY;
- UNAVAILABLE.

When session provenance is relevant to a persistent mutation record, include offset-aware timestamp/timezone, Human operator, Operator alias, Chat label and Workstream ID.

## Why

Stable paths should depend on stable identities. History should model the chat itself; current state should model the Workstream.

## Impact

New public templates define Workstream registries, Session Records, runtime state and operator profiles.

## Validation

Package QA plus real Project Runtime pilots.
