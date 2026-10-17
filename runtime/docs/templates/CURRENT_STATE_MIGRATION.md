# Current-state migration — unconfigured review seed

Use [GOV-RUNTIME-STATE-001](../contracts/CURRENT_STATE_AND_HANDOFF.md). This seed does not adopt or activate a contract. Populate it privately in the existing owner record; do not create a competing source of truth.

## Scope and acceptance before testing

- Decision to make, accountable owner, selected Workstreams and source revision: UNRESOLVED.
- Old criteria/tool revision and original findings: UNRESOLVED.
- Mandatory acceptance: all base fields; exact declared extension keys/types; preserved artifact variants; valid identity/version/operator/session references; state/registry/current-handoff agreement; existing package/pin/report/safety obligations retained.
- Conditional tests and risk/question answered: UNRESOLVED.
- Unchanged evidence reused, scope/environment/dependency validity: UNRESOLVED.
- Optional improvements (non-blocking): UNRESOLVED.

## Inventory and proposal

For every extra key, record observed type(s), supporting source, intended meaning, disposition and owner. Keep populated values private. Mark unknown meaning UNRESOLVED; an observed type does not validate nested semantics. Do not silently remove fields or convert legitimate variants.

Propose a versioned profile with `contract_id`, `version`, `adoption_status: PROPOSED`, `decision`, and a `workstreams` map. Per selected Workstream declare `extensions`, `artifact_fields`, `handoff`, `required_operator`, nullable `required_status` and non-empty `entry_gate`. Types are non-empty arrays drawn from `string`, `object`, `array`, `boolean`, `integer`, `number`, `null`; integer values also satisfy JSON number, booleans do not.

Use the public fictional example only as a format reference. Profile keys and artifact shapes come from project evidence, not arbitrary copying. Store baseline hashes in the review record as provenance, separate from evolving live values.

## Before-images and migration

| Affected current record | Exact before-image/hash | Proposed changed fields | Source for each new value | Owner |
|---|---|---|---|---|
| UNRESOLVED | UNRESOLVED | UNRESOLVED | UNRESOLVED | UNRESOLVED |

Preserve all old values, historical handoffs and unrelated files. Create a separate current handoff only when the owner selects that route; align manifest binding and registry explicitly. Do not activate the binding merely to test a proposal: run the checker against a disposable copy. Leave installed default validation unchanged until adoption is approved. Source-backed repair is distinct from changing product status or permission.

## Evidence and accountable activation

- Candidate revision/tree, local commands, environment and actual results: UNRESOLVED.
- Current representation result versus historical audit result: UNRESOLVED (never rewrite old FAIL as past PASS).
- Preserved mandatory gates and negative cases: UNRESOLVED.
- Readback and privacy/scope review: UNRESOLVED.
- Exact owner approval of contract version/scope and activation, decision reference and receipt: PENDING.
- Product entry gates and separate remaining approvals: UNRESOLVED.

Proposal merge alone does not supply the acceptance above. Only after explicit approval, record the project adoption decision, set the configured declaration to ACCEPTED, activate the reviewed binding/routing/tool integration and retain the acceptance receipt. Static output cannot verify that decision's authenticity or authorize action.

## Closure and rollback

Stage assessed: UNRESOLVED. Outcome: UNRESOLVED (`COMPLETED`, `COMPLETED_WITH_CAVEATS` or `BLOCKED` under GOV-VAL-001; not new runtime statuses).

Essential evidence, material limitations, known blockers and reason further tests would/would not change the decision: UNRESOLVED.

Rollback source and affected paths, handling of later edits, owner and trigger: UNRESOLVED. Keep reports, task state, decisions and history intact. Merge/publication/live acceptance remain separate gates.
