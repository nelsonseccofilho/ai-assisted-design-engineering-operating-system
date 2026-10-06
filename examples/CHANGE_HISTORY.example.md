# Change History — fictional examples

All identities, locations and IDs below are generic examples, not project exports.

| Activity | Actual mutations | Evidence-only dependencies | Required records |
|---|---|---|---|
| Inspect library | none | library | none |
| Adopt published token locally | consumer | library | EXAMPLE-CONSUMER:adoption |
| Evolve shared component using consumer screenshots | library | consumer | EXAMPLE-LIBRARY:component |
| Evolve library and update consumer | library, consumer | none | EXAMPLE-LIBRARY:rollout ↔ EXAMPLE-CONSUMER:rollout |
| Consumer lacks history | consumer | library | establish <consumer-history> and namespace; never use <library-history> as fallback |

## Linked records

At <library-history>, EXAMPLE-LIBRARY:rollout records the actual shared component mutation, library QA and publication note. It cites activity EXAMPLE-ACTIVITY:rollout and links EXAMPLE-CONSUMER:rollout at <consumer-history>.

At <consumer-history>, EXAMPLE-CONSUMER:rollout records actual local adoption, consumer QA and consumer impact. It cites the same activity and links EXAMPLE-LIBRARY:rollout. Both may reference EXAMPLE-DECISION:rollout at <private-project-decisions>; shared rationale does not merge mutation histories.

## Append-only ownership correction

A consumer-only mutation was incorrectly logged as EXAMPLE-LIBRARY:old at <library-history>. Preserve its payload and ID. Add EXAMPLE-CONSUMER:corrected at <consumer-history> as the canonical copy, with original provenance and correction rationale. Append an archived/pointer annotation at the original history pointing to the new canonical copy; append the reciprocal original pointer in the canonical record. No destructive deletion or rewrite is performed.

## Executable scenarios

[scripts/validate_framework.py](../scripts/validate_framework.py) checks generic fixtures in [ownership-cases.json](ownership-cases.json), including rejection of false dependency records, fallback routing, unlinked multi-owner records and missing history.
