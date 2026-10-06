# ADR-0015 — Use append-only session records and continuous handoff with a mandatory context-limit trigger

**Date:** 2026-10-06  
**Status:** ACCEPTED

## CONTEXT

Writing a handoff only after a long conversation reaches its limit creates a fragile final-minute reconstruction problem. Creating a full handoff per chat also duplicates current state and causes competing snapshots.

## EVIDENCE

- One current handoff is useful for continuation.
- Chat histories are too verbose to reload as persistent memory.
- Material sessions may contain evidence, QA, or mutations that should remain auditable after the handoff evolves.
- User interfaces may explicitly warn that the conversation reached its maximum duration/context and must continue in a new chat.

## DECISION

Use three complementary persistence layers when supported:

1. **Workstream** — persistent unit of work that survives conversation changes.
2. **HANDOFF.md** — continuously maintained compressed current state for that workstream.
3. **Session record** — append-only record for each material session, excluding full chat transcripts.

Optionally maintain a machine-readable runtime state projection for deterministic agent startup.

Session identity distinguishes human operator, stable session alias, individual chat label, and workstream ID.

A conversation-limit warning, including wording equivalent to “the conversation reached its maximum duration and may continue in a new chat,” is a mandatory continuity trigger.

At the trigger the agent must not begin new significant scope. It must safely close the atomic operation, validate the latest checkpoint, synchronize handoff/state/registry/session record, persist the repository checkpoint, and end with exactly one `NEXT ACTION`.

The next chat reloads persistent state and reinspects the current tool state before continuing.

## WHY

This provides incremental memory without forcing every new session to load every prior conversation or every historical session record.

## IMPACT

- a workstream is not recreated merely because a chat ended;
- session records become historical execution evidence rather than competing current-state documents;
- handoffs are maintained incrementally;
- context-limit continuity becomes deterministic;
- session records are required only for material operational sessions, avoiding repository noise.

## STATUS

ACCEPTED
