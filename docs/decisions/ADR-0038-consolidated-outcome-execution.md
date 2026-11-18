# ADR-0038 — Consolidated, outcome-based execution

**Date:** 2026-11-18  
**Status:** ACCEPTED — framework integration subject to PR review and merge  
**Scope:** Generic operating method; no automatic adopter activation or release

## Context

The operating contract already permits autonomous tool execution, proportionate QA and bounded human accountability. However, its emphasis on small patches can be misread as requiring a separate user-facing review after every microchange. In a well-evidenced, explicitly authorized component or design-system task, serial microapprovals slow delivery without necessarily improving safety. The missing distinction is between an **internal technical checkpoint** and an **external decision gate**.

## Decision

Prefer **one outcome-oriented work cycle** when the operator has approved the goal, scope, risk boundaries and observable acceptance criteria:

`inspect full scope → reconcile evidence and dependencies → plan a coherent batch → execute reversible changes → internal risk-based QA and repair → provide one consolidated result for review`.

1. **Do not repeatedly ask for approval of implementation microsteps** that are already covered by outcome-level authorization.
2. **Preserve internal checkpoints.** The agent may use multiple tool calls, commits, QA reads and reversible patches; "one cycle" never means one unvalidated mutation.
3. **Honor authority gates.** Ask only when a consequential product-semantic choice, unapproved new public component contract, destructive change, publication/merge or other required gate lacks authorization. If one branch is blocked, finish safe independent work and report the blocker.
4. **Use a bounded inventory.** Classify each finding as reuse, composition, evolution, justified creation or backlog. Never multiply variants or create a parent simply because another library offers one.
5. **QA by risk and evidence.** Verify affected masters and dependent instances, IDs, properties, semantics, tokens, responsive states and visible presentation as applicable. Evidence reuse must remain within its validity envelope; governed checks are not waived.
6. **Report once per outcome** with mutations, exact verified counts, residual risks, scope exclusions and the final human decision still required. Progress communication is allowed when work is extended; it is not a microapproval request.
7. **Keep ownership and privacy.** Records belong to mutated artifact owners. External references, private project identifiers, production links and current client data do not enter the generic core.

## Non-goals

- No relaxation of GOV-VAL-001, action-time admission, source-of-truth order, ADR-0014 ownership or publication gates.
- No automatic merge, release, adopter pin update or claim of browser/assistive-technology QA from Figma-only inspection.
- No requirement to execute an entire complex task in one irreversible write.

## Acceptance and validation

- A task with clear authorization completes as a coherent delivery without unnecessary human confirmation between safe mutations.
- New, ambiguous or irreversible choices still activate the existing human decision gate.
- A missing dependency is reconciled by stable source identity and semantic mapping, not name-only substitution.
- Postflight records distinguish **completed**, **completed with caveats** and **blocked** as scoped outcomes, without inventing acceptance or publication evidence.
- Generic master, exact runtime mirror, decision index and documentation remain synchronized in the candidate branch; QA and PR review precede adoption.

## References

- [Operating Master](../../PROMPT_OPERACIONAL_MASTER.md), sections 2, 11–13, 19–27 and 53.
- [Consolidated execution contract](../CONSOLIDATED_EXECUTION.md).
- [ADR-0007](../../DECISION_LOG.md), bounded autonomy.
- [ADR-0014](ADR-0014-mutation-owned-change-records.md), mutation-owned records.
- [ADR-0029](ADR-0029-risk-proportionate-validation.md), GOV-VAL-001.

