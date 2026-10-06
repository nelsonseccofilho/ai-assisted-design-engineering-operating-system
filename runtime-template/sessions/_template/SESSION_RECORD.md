# SESSION RECORD — TEMPLATE

A Session Record represents one material AI-assisted chat.

**Date:** YYYY-MM-DD  
**Started:** <offset-aware timestamp + timezone>  
**Ended:** <offset-aware timestamp + timezone | OPEN>  
**Human operator:** <person>  
**Operator alias:** <stable alias>  
**Chat label:** <exact label | UNRESOLVED>  
**Status:** `OPEN | CLOSED`

## Workstreams touched

- `WS-...` — <role in this session>

A single Session Record may reference multiple Workstreams.

## Starting state

- <runtime/handoff/state/checkpoint loaded>

## Inspected

- <source / artifact>

## Completed

- <material delta>

## Persistent changes

- <owner Change record / Git commit / document mutation>

## Decisions

- <Decision ID / none>

## QA

### Passed
- <...>

### Pending
- <...>

## Divergence / reconciliation

- <... / none>

## Continuity outcome

**Workstream handoffs updated:** <paths / none>  
**Registry updated:** yes/no  
**Git checkpoint:** <commit / pending>

**NEXT ACTION:** <exactly one concrete action>

Do not store the full chat transcript.

An OPEN record may be updated during the live session. A CLOSED record is immutable except for explicit append-only correction notes.

Close only at actual conversation end, context-limit trigger or explicit human handoff. A Git checkpoint or PR merge alone is not session closure.
