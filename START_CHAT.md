# START CHAT
## AI-Assisted Design Engineering Operating System

Use this file as the shortest entry point for a new AI session.

## Persistence model

Do not treat model/chat memory as the canonical project database.

The framework supports two modes:

1. **Persistent Project Runtime** — preferred for long-running, multi-chat or multi-operator work.
2. **Local minimal mode** — `PROJECT_CONTEXT.local.md` + `HANDOFF_CURRENT.local.md` when no persistent runtime exists.

A Project Runtime is a versioned, project-specific operational memory. It does **not** replace live artifact state or primary evidence.

---

## Always load

1. `PROMPT_OPERACIONAL_MASTER.md`

---

## If a Persistent Project Runtime is configured

### Runtime access

Classify access first:

- `READ_WRITE`
- `READ_ONLY`
- `UNAVAILABLE`

The normal stable bootstrap ref is `main` unless project governance explicitly defines another canonical ref.

### Load

Load when available:

1. project context;
2. project governance;
3. project decision index;
4. artifact / owner registry;
5. evidence index;
6. Workstream registry;
7. selected Workstream `HANDOFF.md`;
8. selected Workstream `state.json`;
9. only the relevant Session Record(s) needed for reconciliation.

Then:

10. identify the Human operator;
11. resolve the stable Operator alias;
12. resolve the current Chat label when available;
13. verify no other ACTIVE Workstream owns an overlapping mutation scope;
14. inspect current live tool/artifact state;
15. resolve mutation owners and owner-scoped Change History;
16. reconcile live state against runtime snapshots;
17. continue from exactly one `NEXT ACTION` only when it remains valid.

A Workstream survives chat and operator changes.

A Session Record represents one material chat and may reference multiple Workstreams.

---

## If only local minimal mode exists

Load when available:

2. `PROJECT_CONTEXT.local.md`
3. `HANDOFF_CURRENT.local.md`

Then:

1. validate current tool state whenever possible;
2. resolve target mutation owners and read-only dependencies;
3. load relevant governance / persistent decision / Change History records;
4. treat the handoff as a snapshot;
5. reconcile divergence before mutation;
6. continue from `NEXT ACTION` when still valid.

---

## If no project context exists

Start in generic mode.

Ask only for the minimum useful context:

1. Product / project name
2. Primary stakeholder / decision-maker
3. Journey / flow
4. Organization / client — optional
5. Work Package / initiative — optional
6. Design System / UI Kit name and URL — if one exists
7. Primary work file name and URL

Collect more context just in time.

---

## Runtime degraded mode

### READ_WRITE

Normal operation. Persist meaningful checkpoints.

### READ_ONLY

Inspection, analysis and reconciliation may continue.

Do not perform significant project mutation whose safe continuity depends on writing the Project Runtime. A deliberate exception requires explicit human authorization, owner-scoped artifact logging, and a pending runtime-sync record.

### UNAVAILABLE

Do not reconstruct project state from chat/model memory.

Safe generic analysis may continue, but reconnect the Project Runtime before project mutation.

---

## Session identity

Keep these separate:

- **Human operator** — accountable person;
- **Operator alias** — stable alias across chats;
- **Chat label** — individual conversation identifier;
- **Workstream ID** — stable unit of continuing work.

Do not encode a mutable operator identity into a Workstream ID.

Recommended Workstream ID:

`WS-YYYYMMDD-NNN-<slug>`

Recommended Session Record path:

`sessions/<OPERATOR_ALIAS>/<YYYY>/<MM>/<YYYY-MM-DD>_<chat-label>.md`

---

## Context-limit continuity trigger

If the interface reports that the conversation reached its maximum duration/context and may continue in a new chat — or shows equivalent wording — treat it as a mandatory continuity trigger.

Do not start new significant scope.

Instead:

1. complete or safely stop the current atomic operation;
2. validate the latest completed checkpoint;
3. update the current Workstream handoff;
4. update machine-readable state when used;
5. synchronize the Workstream registry;
6. update/close the material Session Record;
7. persist the repository checkpoint;
8. end with exactly one `NEXT ACTION`.

The next chat runs this startup protocol again and reinspects live tool state before continuing.

---

## Mutation record attribution

Persistent owner-scoped Change History remains governed by ADR-0014.

When session attribution is relevant, a meaningful mutation record should include:

- offset-aware timestamp;
- timezone;
- Human operator;
- Operator alias;
- Chat label;
- Workstream ID.

---

## Git contract

All framework and adopting Project Runtime repositories use **Conventional Commits 1.0.0** unless stricter project governance says otherwise:

https://www.conventionalcommits.org/en/v1.0.0/

Significant commits reference the relevant persistent Decision ID.

---

## Communication

Use the user's language unless requested otherwise.

Prefer:

`STATUS → EVIDENCE → ACTION → QA → NEXT`

If the user says only `continue` or `seguir`, execute this startup protocol and continue autonomously when scope and evidence are sufficient.

---

**Do not provide a generic introduction. Start operating.**


## Operator daily-report command contract

A Project Runtime may define operator-specific report commands.

Recommended command convention:

- `<operator_alias_lower>_report` — generate a report DRAFT;
- `<operator_alias_lower>_report_sent` — confirm actual sending and advance the reporting cursor.

When project governance marks daily reporting as required, a DRAFT does not satisfy the obligation.

### Generation

A report generator should:

1. read the operator's report state;
2. use the last confirmed reporting cursor when available;
3. otherwise use the project's configured bootstrap baseline;
4. inspect persistent Session Records and relevant mutation records after the cursor;
5. load current Workstream handoff/state for planned work and blockers;
6. summarize outcomes rather than internal technical logs;
7. use project-configured languages and destination format;
8. persist DRAFT when runtime write access exists;
9. never advance the cursor during generation.

### Sent confirmation

The sent-confirmation command should:

1. locate the latest DRAFT;
2. confirm it was actually sent when sending was manual;
3. mark it SENT;
4. persist sent timestamp;
5. advance the last confirmed reporting cursor.

Do not invent blockers. Distinguish blockers from dependencies.

A Project Runtime may make one SENT-or-WAIVED report per reporting day mandatory for operators with material project activity.
