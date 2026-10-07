# Runtime startup

Use this file as the canonical entrypoint for a Project Runtime.

## 1. Resolve startup intent before selecting a Workstream

Classify the user's intent as exactly one of:

### CONTINUE_WORKSTREAM

Use when the user explicitly wants to resume existing work.

Load the selected/current Workstream HANDOFF + state, relevant Session Records, then reconcile current artifact/tool state before continuing from NEXT ACTION.

### START_NEW_WORKSTREAM

Use when the user starts a new task, journey, flow, initiative, artifact scope or materially independent objective **inside the same project**.

Do not auto-continue the currently active Workstream.

Instead:

1. load the base runtime contract;
2. inspect the Workstream registry for overlap;
3. resolve the artifact / mutation scope;
4. create a new `WS-YYYYMMDD-NNN-<slug>` entry;
5. create its HANDOFF.md and state.json from templates;
6. create/update the material Session Record;
7. inspect current artifact/evidence state;
8. begin mutation only after ownership/governance is resolved.

### START_NEW_PROJECT

Use when the user is starting a different product/client/project whose operational history should not share this runtime.

Do not reuse populated operators, sessions, evidence, reports, project Decisions or Workstreams from another project.

Instantiate a new private Project Runtime from the generic `runtime/` package, configure project identity/governance, then create the first Workstream.

## 2. Load base runtime contract

Read `runtime-manifest.json` from the canonical main ref first.

Classify access as:

- `READ_WRITE`
- `READ_ONLY`
- `UNAVAILABLE`

Then load `bootstrap_files` in manifest order, skipping this entry point when encountered.

Resolve Human operator, Operator alias and Chat label separately.

## 3. Base operation rules

Regardless of startup intent:

- chat/model memory is not canonical project state;
- primary evidence remains authoritative at its original source;
- current inspected artifact state outranks stale runtime snapshots;
- check for overlapping ACTIVE mutation scopes before mutation;
- resolve mutation owner and owner-scoped Change History before meaningful mutation;
- use Session Records for material chat history, not full transcripts;
- keep HANDOFF/state current after material checkpoints;
- do not silently broaden scope;
- follow Conventional Commits and persistent Decision records for significant runtime changes.

## 4. Daily reports

Resolve report commands, language and requirement from the manifest.

DRAFT never advances the reporting cursor.

Confirmed SENT advances to the frozen interval_end.

WAIVED does not advance the cursor.

## 5. Runtime synchronization

Before updating shared files, run `scripts/runtime_sync.py` against an independently fetched immutable framework checkout.

Configured files require review; never overwrite project data from templates.

Keep stable and candidate framework pins distinct.
