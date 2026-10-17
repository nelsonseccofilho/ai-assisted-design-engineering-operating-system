# GOV-RUNTIME-STATE-001 — Typed state and explicit current handoff

**Version:** 1.0 (optional, unreleased proposal under framework ADR-0032; its decision record stays in the framework repository).
**Scope:** persisted representation and continuity, not product acceptance or execution authority.

## Required base and declared extensions

Keep all fourteen fields of `workstreams/_template/state.json` and schema 1.1. A populated record must have valid identity, runtime version, registered operator and contained references. Preserve every existing value when investigating a format failure; never normalize a record by dropping unknown fields.

A project may declare an exact extension profile for each selected Workstream. Each added key has an explicit JSON type (or a documented union). Missing, undeclared or incorrectly typed extensions fail. Booleans are not integers. Existing artifact shapes require explicit field/type variants rather than destructive conversion. Structured, textual and null persistent-change forms are supported; validating their outer type does not establish their nested product semantics.

An approved profile allows legitimate same-type value changes. Baseline hashes identify the reviewed input; they do not freeze every future value. Changes to declared fields/types require a reviewed profile revision and appropriate project decision. A profile cannot redefine the mandatory base fields or waive existing governance checks.

## Explicit current routing

Read the normal ordered bootstrap first. Select the Workstream, then reconcile its state and the handoff path explicitly agreed by the manifest-bound profile and the registry. Default `HANDOFF.md` remains supported. Switching to `CURRENT_HANDOFF.md` requires a project migration; filenames, timestamps and the last paragraph never select authority.

The selected handoff has exactly one unindented `NEXT ACTION: <text>` line matching `state.next_action`. The checker also recognizes the existing `**NEXT ACTION:** <text>` spelling and counts both to detect mixed duplicates. For a null action in a terminal or planned state, use `NEXT ACTION: NONE`; literal `NONE` is reserved and cannot be a state action. The registry's ID, operator, status, handoff and state columns must match. Preserve old handoffs and accumulated history byte-for-byte when creating a separate current route.

Record non-empty entry gates, ownership and any required paused status in the profile. A static match does not authorize resumption, execution, navigation to removed sources or cross-owner mutation. Confirm the actual source, scope, permissions and relevant live evidence before action. A missing source is an execution blocker even when context was recovered successfully.

## Proposal, adoption and historical truth

Preparing a profile, passing its checker or merging a proposal is not adoption. The project owner must explicitly approve the version, selected scope, migration and activation. Record that approval in the project's own decision chain, not this framework's ADR history. A populated `adoption_status: ACCEPTED` field is a declaration to inspect, never proof of owner consent.

Before changing current criteria, record original findings with source revisions, criteria versions and exact before-images of records to be edited. Retain the old audit tool or reproducible archived input. Prospective typed acceptance can coexist with historical exact-set failures. Never erase those failures, relabel them as past PASS or use a new mode to silently weaken a mandatory criterion. Report current structural results and historical findings separately.

Source-backed metadata repair must distinguish observed, inferred and unresolved values. Do not invent historical latest-session identities, execution versions or task completion. New metadata may point to the actual repair session; preserve every prior value and document why each edited field changes.

## Optional read-only checker and limits

The package includes `scripts/check_current_state.py` and an unconfigured [migration seed](../templates/CURRENT_STATE_MIGRATION.md). They are optional additions, not mandatory bootstrap or a default replacement for `scripts/validate_runtime.py`. No existing installation adopts them automatically.

From a configured project repository:

```text
python runtime/scripts/check_current_state.py --runtime runtime --contract governance/current-state-contract.json
```

Bind the chosen runtime-relative contract path in the manifest as `current_state_contract: {"id": "GOV-RUNTIME-STATE-001", "version": "1.0", "path": "governance/current-state-contract.json"}`. The manifest/registry and selected files must exist inside that runtime; absolute paths, traversal, backslashes, URL/drive paths and links escaping the runtime are rejected. JSON duplicate keys and non-finite numbers are rejected. Errors report generic codes and counts, never file contents or private values.

The checker assesses only Workstreams explicitly listed in the contract. Its output lists assessed and unassessed counts, always `STATIC_VALIDATION_ONLY`, `execution_authorized: false`, `adoption_verified: false` and `writes: false`. Missing/invalid inputs fail with a nonzero exit. Use `examples/current-state/` in the framework repository to inspect the fictional profile format; examples and framework ADRs are not copied into installed runtimes. A PASS is scoped structural evidence; it is not overall runtime health, approval, security certification, hosted execution or deep payload validation. Existing package, pin, report, source, ownership and safety checks still run under their governing criteria.

## Proportional acceptance and rollback

Before testing, use [GOV-VAL-001](VALIDATION_AND_CLOSURE.md) to state the decision and mandatory evidence. Require affected positive and negative cases for field/type integrity, references, routing and preserved gates; verify exact archives and unchanged unrelated data. Reuse unchanged valid evidence instead of replaying unrelated experiments. Additional live/product tests depend on a concrete affected risk.

Rollback restores the prior contract selection, tooling and affected current records from exact reviewed sources, retaining later unrelated changes and all historical records. No rollback erases decisions, sends reports, changes cursors or promotes pilots. Close the representation/migration stage separately from product acceptance, merge and release.
