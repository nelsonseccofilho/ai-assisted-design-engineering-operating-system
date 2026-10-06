# Project Runtime

A **Project Runtime** is a project-specific, persistent operational memory for AI-assisted work.

It solves a different problem from the public Operating System.

```text
Operating System
= how the workflow should operate

Project Runtime
= where one project's operational state persists

Artifact tools
= where current design / implementation state lives

AI session
= temporary executor
```

## Why it exists

Conversation memory is bounded and session-local. Long-running work needs a durable place for:

- governance;
- project decisions;
- artifact / mutation-owner registry;
- evidence indexes;
- Workstreams;
- handoffs;
- deterministic state;
- operator identity;
- Session Records;
- QA / continuity checkpoints.

## Source-of-truth boundaries

A Project Runtime is canonical for operational continuity.

It does not replace:

- primary evidence at its original source;
- current inspected artifact state;
- the current canonical Design System.

Chat/model memory is non-authoritative convenience only.

## Recommended topology

```text
project-runtime/
├── README.md
├── governance...
├── operators/
│   └── <OPERATOR_ALIAS>.md
├── sessions/
│   └── <OPERATOR_ALIAS>/<YYYY>/<MM>/<session>.md
├── workstreams/
│   ├── WS-YYYYMMDD-NNN-<slug>/
│   │   ├── HANDOFF.md
│   │   └── state.json
│   └── ...
├── reports/daily/
│   ├── _template/
│   └── <OPERATOR_ALIAS>/
│       ├── state.json
│       └── <YYYY>/<MM>/<report>.md
└── workstream registry
```

## Stable entities

### Operator

Who is accountable.

### Operator alias

Stable alias across chats.

### Session Record

One material chat. May touch multiple Workstreams.

### Workstream

Continuing unit of work. Survives chats and may transfer between operators.

## Canonical ref

For a Git-backed Project Runtime, prefer `main` as the stable bootstrap ref.

Use feature branches for runtime changes under review.

## Access modes

### READ_WRITE
Normal operation.

### READ_ONLY
Analysis/reconciliation allowed; avoid significant project mutation whose safe continuity requires runtime writes.

### UNAVAILABLE
Do not use chat memory as a substitute Project Runtime. Reconnect before project mutation.

## Context-limit trigger

A conversation-limit warning triggers controlled continuity: close the atomic operation, synchronize Workstream state, Session Record and registry, persist a checkpoint, and finish with exactly one NEXT ACTION.

## Complete template surface and upstreaming

Use [framework/runtime synchronization](FRAMEWORK_RUNTIME_SYNC.md) for deterministic assembly, manifest configuration, template mapping, schema compatibility and promotion of reusable pilot learnings. Runtime-specific values remain private; reusable rules belong in the framework.
