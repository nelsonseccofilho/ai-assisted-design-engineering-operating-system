# Fictional current-state fixture

Every identity, value, path and narrative in [fixture.json](fixture.json) was newly invented for this example. It is not an anonymized project export. `files` maps runtime-relative paths to JSON objects or UTF-8 text, materialized only in disposable tests.

The fixture deliberately contains an older handoff with multiple obsolete actions, a selected current handoff, a paused Workstream, a typed integer extension and a structured persistent-change value. The historical text remains unchanged. Its PROPOSED profile demonstrates format, not adopted authority. The generic [contract](../../runtime/docs/contracts/CURRENT_STATE_AND_HANDOFF.md) defines the boundaries.

From the framework checkout run:

```text
python scripts/test_current_state.py
```

The tests create and remove only their own temporary fictional directories and exercise the read-only checker. They verify routing, explicit scope, same-type evolution, representation failures and non-authority. They do not operate a real runtime, verify human adoption, test product semantics or repeat live/pilot trials. To try a project migration, prepare its own private profile and decision with the migration seed; never substitute these fictional names for real evidence.
