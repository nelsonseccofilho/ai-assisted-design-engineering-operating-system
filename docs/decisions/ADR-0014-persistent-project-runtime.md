# ADR-0014 — Use a persistent private project runtime as the operational source of truth

**Date:** 2026-10-06  
**Status:** ACCEPTED

## CONTEXT

Long-running AI-assisted design work spans multiple conversations, tools, days, and operators. Conversational context and model memory are bounded and cannot safely serve as the only durable state store.

## EVIDENCE

- Existing handoff and project-context separation already reduces conversational dependence.
- Git provides version history, diffs, rollback, traceability, review, and deterministic files.
- Live design/tool state can diverge from stored conversational or runtime snapshots.

## DECISION

When a project needs multi-session continuity, use a persistent private project runtime repository as the canonical source for **operational state and continuity**.

The runtime may persist project context, governance, decisions, workstreams, handoffs, session records, registries, evidence indexes, QA metadata, and optional machine-readable state.

This does not make Git the universal source of truth.

Authority remains separated:

1. primary requirements/evidence — authoritative at the original evidence source;
2. current design/tool artifact state — authoritative when directly inspected;
3. current canonical Design System — authoritative for shared system state;
4. persistent private runtime — authoritative for operational continuity, governance, coordination, and recorded decisions;
5. chat/model memory — non-authoritative convenience only.

Confidential project runtimes must remain private.

## WHY

The model preserves durable memory without creating false authority over artifacts that can change outside the repository. It also lets a new AI session recover work without replaying entire chat histories.

## IMPACT

- project runtimes may intentionally track private project-specific Markdown/JSON files;
- new sessions should bootstrap from the persistent runtime when available;
- stale runtime state must be reconciled against current inspectable tool state;
- public generic repositories remain project-agnostic;
- adopting runtime repositories must use governed Git history.

## STATUS

ACCEPTED
