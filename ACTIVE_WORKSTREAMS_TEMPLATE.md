# ACTIVE WORKSTREAMS — TEMPLATE

Use this registry when a project runtime supports concurrent work.

## Status values

- `PLANNED`
- `ACTIVE`
- `PAUSED`
- `BLOCKED`
- `READY_FOR_QA`
- `FINAL`
- `ARCHIVED`

## Registry

| Workstream ID | Human operator | Session alias | File / scope | Mutation scope | Status | Handoff | State | Latest session | Last validated |
|---|---|---|---|---|---|---|---|---|---|
| `WS-...` | <person> | <alias / N/A> | <artifact/scope> | <owned mutation scope> | `ACTIVE` | <path> | <path/N/A> | <path/N/A> | <timestamp> |

## Ownership rule

Two `ACTIVE` workstreams must not own overlapping mutation scopes.

When overlap is detected:

1. stop new mutation;
2. identify the current owner;
3. merge, re-scope, pause, or transfer ownership;
4. update this registry;
5. only then continue.

Read-only inspection may proceed without mutation ownership.

A workstream persists across chat/session changes.
