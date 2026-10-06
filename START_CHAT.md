# START CHAT
## AI-Assisted Design Engineering Operating System

Use this file as the shortest entry point for a new AI session.

## Persistence model

Do not treat chat memory as the canonical project state.

When a persistent private project runtime repository exists, it is the canonical source for:

- project operating context;
- project governance;
- project decisions;
- workstream coordination;
- current handoffs;
- session records;
- machine-readable runtime state.

Current inspectable design/tool state still outranks stale runtime snapshots when the two diverge.

Primary evidence remains authoritative at its original source.

---

## Files to load

Always read:

1. `PROMPT_OPERACIONAL_MASTER.md`

Then, when a persistent project runtime exists, resolve and load its bootstrap contract. At minimum load when available:

2. project context;
3. project governance;
4. project decision index;
5. artifact / file registry;
6. evidence index;
7. active workstream registry;
8. the selected workstream's `HANDOFF.md`;
9. the selected workstream's machine-readable state when present;
10. the latest relevant session record only when needed for reconciliation.

If no persistent project runtime exists, load when available:

2. `PROJECT_CONTEXT.local.md`
3. `HANDOFF_CURRENT.local.md`

Do not ask the user to re-explain information already available in persistent sources.

---

## Startup behavior

### If a persistent project runtime exists

1. identify the human operator;
2. identify or confirm the session alias and chat label when available;
3. load project governance and the active-workstream registry;
4. verify that no other active workstream owns an overlapping mutation scope;
5. resolve the requested/current workstream;
6. load its current handoff and state;
7. inspect the current design/tool state whenever possible;
8. treat the handoff and state as snapshots, not absolute truth;
9. reconcile divergences without silently overwriting newer work;
10. continue from `NEXT ACTION` only when it remains valid.

### If only `PROJECT_CONTEXT.local.md` exists

1. load the project context;
2. load the current handoff if available;
3. validate the current tool state whenever direct inspection is possible;
4. treat handoff content as a snapshot, not absolute truth;
5. reconcile any differences before mutating;
6. continue from `NEXT ACTION`.

### If no project context exists

Start in generic mode.

Ask for only the minimum initial context:

1. Product / project name
2. Primary stakeholder / decision-maker
3. Journey / flow
4. Organization / client — optional
5. Work Package / initiative — optional
6. Design System / UI Kit name and URL — if one exists
7. Primary work file name and URL

Collect additional context just in time.

---

## Session identity

When supported by project governance, distinguish:

- **Human operator** — accountable person;
- **Session alias** — stable operator/agent alias;
- **Chat label** — individual conversation identifier;
- **Workstream** — persistent unit of work that survives chat changes.

Do not infer a human operator solely from a chat title.

---

## Continuous handoff

A workstream handoff is continuously maintained state, not a document written only when a chat ends.

After meaningful checkpoints, update the workstream handoff/state when persistence is available.

Material sessions should create an append-only session record using `SESSION_RECORD_TEMPLATE.md`.

A session record documents what happened in one session; it does not replace the current handoff.

---

## Context-limit trigger

If the interface reports that the conversation reached its maximum duration/context and may continue in a new chat — or presents an equivalent limit warning — treat it as a mandatory continuity trigger.

Do not start a new significant mutation.

Instead:

1. complete or safely stop the current atomic operation;
2. validate the latest completed checkpoint;
3. update the workstream `HANDOFF.md`;
4. update machine-readable runtime state when used;
5. synchronize the active-workstream registry;
6. create/update the material session record;
7. persist the repository checkpoint using Conventional Commits;
8. finish with exactly one `NEXT ACTION`.

The next chat must run this startup protocol again and re-inspect the real tool state before continuing.

---

## Git contract

All repository commits made under this operating model must follow **Conventional Commits 1.0.0**:

https://www.conventionalcommits.org/en/v1.0.0/

Significant commits must reference the relevant persistent Decision ID in the commit body or footer.

---

## Communication

Use the user's language unless they request another one.

Prefer concise operational responses:

### STATUS
Where the work currently stands.

### EVIDENCE
What supports the conclusion.

### ACTION
What was done or what will be done.

### QA
Validation result.

### NEXT
The next concrete action.

---

## Continuity shorthand

If the user says only:

> continue

or:

> seguir

execute the Startup Protocol and continue autonomously when scope and evidence are sufficient.

---

**Do not provide a generic introduction. Start operating.**
