# Choose the next design method

**Use:** optional, after the current manifest's mandatory startup. This guide selects a scoped deliverable; it introduces no startup intent, task state, fixed pipeline or new approval checkpoint.

Recover the current goal, owner, accepted decisions, relevant evidence and existing deliverable before asking for more input. Reuse adequate work. A screen, persona, model output or newer proposal is not authority to invent missing requirements. Label assumptions and resolve only the gaps that affect the next safe action.

## Route by the deliverable needed now

| Situation | Deliverable to produce | Existing guidance and smallest useful next action |
|---|---|---|
| The problem or requested outcome is unclear | A scoped question with sources, known constraints and unresolved assumptions | Use [evidence reconciliation](../runtime/docs/contracts/EVIDENCE_RECONCILIATION.md). Recover intent and competing explanations; ask the smallest blocking question. Do not manufacture research or restart discovery when current approved evidence is sufficient. |
| A component or flow has interacting states | A behavior specification linking states, events, conditions, effects and recovery | Use the [component behavior seed](../runtime/docs/templates/COMPONENT_BEHAVIOR.md) and [fictional example](../examples/component-behavior/README.md). Separate UI presentation, persisted data and actual permission enforcement. |
| An existing interface needs review | Evidence-backed findings limited to the actual task, rendering and affected states | Apply [review and acceptance](../runtime/docs/contracts/REVIEW_AND_ACCEPTANCE.md), [foundation QA](../runtime/docs/contracts/DESIGN_FOUNDATION_QA.md) and [content QA](../runtime/docs/contracts/CANVAS_AND_CONTENT_QA.md) as relevant. Capture the concrete problem before proposing a change; a screenshot cannot establish runtime or accessibility behavior. |
| Work is ready for handoff or a decision | A source-linked specification or concise decision brief | Reuse the current handoff and owner records; fill only relevant behavior/specification gaps. Use the [decision-brief example](examples/DECISION_BRIEF.md) when a human decision is actually needed. Distinguish contextual recovery, implementation completeness and acceptance. |
| A shared component is changing or needs adoption | A bounded migration/adoption plan with source and consumer evidence | Use [design change control](../runtime/docs/contracts/DESIGN_CHANGE_CONTROL.md) and the [migration seed](../runtime/docs/templates/COMPONENT_MIGRATION.md). Verify publication separately from consumer synchronization and preserve properties/overrides. A local change grants no cross-file authority. |

If two situations apply, choose the first deliverable that removes a real dependency and name what follows. If none applies, state the mismatch instead of forcing a route. A role or method is a way to organize work, not a requirement to create another agent, install a plugin or use a particular provider.

## Keep the route proportionate

State the chosen deliverable and why it is needed. Reuse the existing owner record to capture acceptance, relevant checks and evidence validity under [GOV-VAL-001](../runtime/docs/contracts/VALIDATION_AND_CLOSURE.md). Skip unrelated methods; preserve applicable security, privacy, integrity and acceptance gates. Limited effort, a short summary or a self-check cannot satisfy a missing mandatory criterion.

When a local question is blocked, continue independent authorized work. Change routes only when new evidence, scope or a dependency makes the current route unsuitable. No fixed document count, stage sequence, research quota, chat-per-phase rule or mandatory repetition follows from this guide.

The [adaptation rationale](EXTERNAL_METHOD_ADAPTATION.md) identifies reviewed sources, what was retained and what was deliberately changed. This original guide is an optional documentation candidate; it does not claim measured productivity, independent usability acceptance or pilot promotion.
