# Consolidated execution by outcome — operational contract

**Status:** Framework core guidance · ADR-0038  
**Mode:** Default where the operator explicitly authorizes a defined outcome.  
**Authority:** `PROMPT_OPERACIONAL_MASTER.md`, especially sections 21, 21A, 22, 24, 26, 27 and 53.

## Goal

Complete a coherent, evidence-based deliverable without forcing the operator to manually validate routine microchanges. Preserve internal execution traceability, reversible mutations and governed QA. The unit of **human review** is the outcome; the unit of **technical safety** remains the evidence-backed operation.

## One consolidated cycle

| Phase | Required behavior | Evidence |
|---|---|---|
| 1. Inspect | Read current canonical assets, local consumers, governance and prior approvals. Enumerate missing dependencies and affected surfaces. | Current identifiers, source identity, existing API/state matrix |
| 2. Reconcile | Classify `REUSE → COMPOSE → EVOLVE → CREATE`. Use stable keys and semantic equivalence; inspect actual nested component use. Separate historical/remote references from broken links. | Dependency/impact mapping with classification |
| 3. Execute | Group related reversible changes, preserve public IDs/API and consumer overrides, record owner-scoped mutations. Do not introduce unrelated scope. | Changed IDs, diff/commit, rollback strategy |
| 4. Internally validate | Run risk-proportionate structural and visual QA on the entire affected scope, check responsive and accessible behavior where tool evidence permits. Repair identified regressions before external review. | Exact counts, screenshots, property readback, residuals |
| 5. Review once | Deliver one consolidated summary and links, distinguish verified facts from implementation-only expectations, explicitly name final gates. | Outcome decision: completed / caveats / blocked |

### Conditions for proceeding autonomously

- Outcome, mutation owners and do-not-touch boundaries are known.
- The operator has already authorized the work at the appropriate level.
- Relevant canonicals, existing APIs and semantic rules have been inspected.
- There is a feasible post-mutation QA/readback route.
- Reversibility and consumer impact are understood; the source of truth is available.

### Real human decision gates

Seek an external decision when materially necessary: conflicting product semantics; unapproved public parent/API; destructive loss of approved work; global design token impact; unavailable mandatory evidence; significant scope change; security/privacy/legal consequences; release/merge/publication gate. Do not convert these into an automated assumption. An approval of one design artifact is not an approval of code, publication or other artifact owners.

### Anti-patterns

- Asking “may I continue?” after each safe, already-authorized tool call.
- Mistaking Figma variants for functional/keyboard/mobile test evidence.
- Treating remote instances with matching names as broken before checking stable component keys.
- Recreating icons from approximate shapes when the exact source vector is available.
- Multiplying Size × State without proving the underlying anatomy and consumer contract.
- Replacing a semantic icon just because its appearance is similar.
- Marking a task finished with an unknown QA failure or unverified publication.

### Completion evidence (adapt to scope)

1. Master identities and component counts preserved or intentionally documented.
2. Old dependencies eliminated or safely classified as valid imports; no orphan instances.
3. Component public properties and nested overrides preserved.
4. Visual samples are legible with no unexpected overlap or clipping.
5. Responsive examples are tested within the design artifact; runtime claims are separate.
6. Owner history and project decision records exist where required.
7. Any exception and release/consumer impact are explicit.

**Note:** Batch execution can use multiple internal commits and tests. This contract removes avoidable human *microvalidation*, not safety checks.

