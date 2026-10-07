# Change record ownership

The normative contract is [Master section 27](../PROMPT_OPERACIONAL_MASTER.md#27-change-history), justified by [ADR-0014](decisions/ADR-0014-mutation-owned-change-records.md).

## Workflow

1. Load Master, Project Context and Handoff in existing order.
2. Resolve artifact registry rows; distinguish planned mutation targets from read-only evidence dependencies.
3. Load owner governance and relevant persistent decisions/history; inspect current state and reconcile the handoff.
4. Establish missing owner-scoped history and namespace before significant-change finalization. Use the Master/context baseline when separate governance is absent.
5. Mutate within scope, validate, and record only actual mutations in their owners.
6. Link every owner record for a multi-artifact activity; cite evidence-only dependencies without creating false mutation records.
7. Verify persistent records before FINAL; update handoff with owner/location/qualified IDs and any unresolved setup.
8. When Git is used, link relevant implementing commits and significant Decision IDs. Follow Conventional Commits.

## Record template

- OWNER / HISTORY LOCATION / NAMESPACE-QUALIFIED RECORD ID:
- WHEN (offset-aware timestamp) / TIMEZONE / STATUS / SCOPE:
- HUMAN OPERATOR / OPERATOR ALIAS / CHAT LABEL / WORKSTREAM ID (AI-assisted mutations):
- WHY / EVIDENCE:
- ACTUAL MUTATION:
- EVIDENCE-ONLY DEPENDENCIES:
- DECISION / PERSISTENT DECISION REFERENCES:
- LINKED OWNER RECORDS / ACTIVITY REFERENCE:
- QA:
- PUBLICATION NOTE / CONSUMER IMPACT:
- IMPLEMENTING COMMIT (if Git is used):
- SUPERSESSION / OWNERSHIP CORRECTION (if applicable):

Records may be in a file's governance page, artifact-local document, or an explicitly attached durable owner-scoped companion. A registry/index may link all histories; it must not act as a central fallback mutation log.

## Historical correction

Add a canonical copy to the correct owner's history with its own qualified ID and the original's provenance. Append correction metadata to the original history identifying the retained original as archived/pointer evidence and pointing to the canonical copy. Append the reciprocal pointer in the new owner record. Preserve original payload, IDs and rationale; do not silently rewrite or delete evidence.

## Separation of responsibilities

| Persistent source | Responsibility |
|---|---|
| Owner Change History | Actual mutation and QA at that owner |
| Decision Log / ADR | Significant choice and rationale |
| Git / Conventional Commit | Repository implementation; significant commit references Decision ID |
| Changelog / release | Framework release summary; not external consumer history |
| Handoff / workstream / chat memory | Current continuity snapshot with persistent record links |
| Artifact registry | Resolve owner locations/namespaces; not a fallback log |

Read-only inspection creates no mutation record in the inspected artifact. It may still yield a significant decision requiring a persistent rationale record. See [fictional scenarios](../examples/CHANGE_HISTORY.example.md).
