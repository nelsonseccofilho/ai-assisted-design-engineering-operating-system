# WORKSTREAM REGISTRY — TEMPLATE

Use this registry when a Project Runtime supports persistent or concurrent Workstreams.

## Status values

- `PLANNED`
- `ACTIVE`
- `PAUSED`
- `BLOCKED`
- `READY_FOR_QA`
- `FINAL`
- `ARCHIVED`

## Registry

| Workstream ID | Current Human operator | Operator alias | Latest Chat label | Artifact / scope | Mutation scope | Status | Handoff | State | Last validated |
|---|---|---|---|---|---|---|---|---|---|
| `WS-YYYYMMDD-NNN-<slug>` | <person> | <alias> | <label> | <artifact> | <explicit scope> | `ACTIVE` | <path> | <path> | <timestamp> |

## ID contract

Use:

`WS-YYYYMMDD-NNN-<slug>`

Do not encode the current operator into the ID.

## Ownership rule

Two ACTIVE Workstreams must not own overlapping mutation scopes.

If overlap exists, stop new mutation and resolve ownership first.

Read-only inspection may continue.
