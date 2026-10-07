# ADR-0021 — Resolve startup intent before selecting a Workstream

**Date:** 2026-10-06  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK

## Context

A new AI chat can mean three materially different things: continue existing work, start new work inside the same project, or start a completely different project.

Treating every new chat as continuity risks carrying the wrong NEXT ACTION, scope or project history into unrelated work.

Compatibility pointer files can also make a clean runtime look duplicated even when they contain no canonical state.

## Decision

Require startup intent classification before Workstream selection:

- `CONTINUE_WORKSTREAM`
- `START_NEW_WORKSTREAM`
- `START_NEW_PROJECT`

New work inside the same project creates a new Workstream when the objective/mutation scope is independent.

A new project creates a separate private Project Runtime and must not reuse populated operational history from another project.

Consolidate legacy runtime path aliases into one configured `compat/ALIASES.local.md` file rather than scattering compatibility pointer files through operational folders.

## Why

This keeps new chats safe by default, makes "start from zero" explicit, and reduces structural ambiguity.

## Validation

README and runtime startup documentation must include zero-chat examples. Package QA must require the alias registry and startup intent tokens.
