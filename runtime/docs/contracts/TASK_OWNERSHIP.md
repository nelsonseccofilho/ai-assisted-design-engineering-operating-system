# Work-package and artifact task ownership

**Ownership:** SHARED_CONTRACT. **Maturity:** optional adoption contract derived from an operationally adopted policy; complete rollout effectiveness remains unverified. It refines mutation ownership without replacing Workstreams, Sessions, project authority or the current task-state schema.

1. Each executable task has one owning work package and one owning artifact. A work package is a delivery/source boundary, not a product, journey or screen.
2. Multi-artifact work uses separate owner tasks connected by requirement/activity references and explicit dependencies. Reuse existing task IDs; investigate ambiguous ownership before adding executable work.
3. Select one authoritative project task ledger. Mirrors and aggregate indexes refer to its source path and immutable commit; they do not become independent editable status stores.
4. Preserve the source requirement and originating work package separately from the actual execution owner. Reading another owner's context does not grant mutation permission.
5. A transition records the responsible operator, offset-aware timestamp, previous/new state, evidence and applicable QA. Completion also requires the existing acceptance gates and actual owner change record where a mutation occurred. Never invent a reviewer or approval.
6. Inventory complete journeys and relevant scenarios, states, versions and dependencies before concluding coverage. A historical satisfied label, one frame or a FINAL title does not prove end-to-end delivery.
7. A consumer-only adoption records the consumer mutation. A library change has a separate library owner, scope and approval gate. Published library content must be adopted and verified in affected consumers before claiming consumer adoption.
8. Reconcile migration counts, unique IDs, unresolved ownership and mirror provenance before cutover. Retain historical ledgers as clearly archived evidence rather than silently deleting them.

Adoption is explicit and project-local. This package does not create a task directory, prescribe new TODO/BLOCKED/DONE values, migrate populated ledgers or modify private configuration. Use the [task review seed](../templates/TASK_REVIEW.md) only if the existing ledger lacks the necessary fields; prefer extending the owner record over creating a second tracker.

Component maturity order, display column limits and presentation geometry require separate local validation. No private file layout or functional permission is a generic requirement.


Use [evidence reconciliation](EVIDENCE_RECONCILIATION.md) for journey/source mapping and [design change control](DESIGN_CHANGE_CONTROL.md) for API and consumer adoption checks. These procedures do not install a new ledger.
