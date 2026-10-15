# GOV-VAL-001 — Risk-Proportionate Validation & Evidence-Based Closure

**Ownership:** SHARED_CONTRACT. **Classification:** mandatory operational contract.
**Applicability:** authorized human operators and AI agents across analysis, development, UX/UI, design tools, engineering, QA, audits, documentation and delivery.
**Decision:** ADR-0029. Policy adoption does not establish measured efficiency or promote any pilot.

## 1. Principle

Validation supplies sufficient evidence for a safe decision. It does not eliminate every possible uncertainty indefinitely. Match rigor to risk, execution cost, reversibility and expected impact. Resource limits may require a safe pause or a separately authorized smaller deliverable; they do not justify unsupported success claims.

## 2. Acceptance before testing

Before testing, identify the deliverable and decision, acceptance criteria, required authority, concrete risks and the evidence already available. Each test must answer a relevant question. Identify mandatory checks from the applicable governance, product requirements and safety obligations; the agent cannot downgrade them unilaterally. Newly discovered risks may add required checks.

Preserve initial criteria and results. A material criterion change requires a recorded reason and the appropriate decision owner; never lower criteria retrospectively to convert a failed or missing result into acceptance.

## 3. Test categories and evidence reuse

| Category | Conduct |
|---|---|
| MANDATORY | Execute, or reuse demonstrably valid evidence when permitted by the governing gate. All applicable safety and acceptance obligations remain binding. |
| CONDITIONAL | Execute when its recorded risk, dependency or evidence trigger is present; it then becomes required for that scope. |
| OPTIONAL | Record useful follow-up without blocking a deliverable whose mandatory criteria are satisfied. |
| REDUNDANT | Do not execute; cite the still-valid evidence or explain the absence of a decision-relevant question. |

Reuse approved evidence only when its source revision or relevant content, scope, environment, dependencies and assumptions still support the same claim, with no material invalidation or credible failure signal. Reference its existing record and explain validity proportionately. Do not relabel historical execution as a new run.

After a material change, reassess affected evidence and run affected checks plus every verification explicitly required for the current candidate. Reuse never overrides a gate requiring a fresh full-package, live, visual, security or other verification. A source-only check does not replace behavioral evidence; local PASS does not establish hosted PASS.

Consider human effort, time, compute, mutation risk and the decision value of additional information. Before an extra test, state the risk, hypothesis or missing evidence, possible outcomes, how each could change the decision, and why its cost is proportionate. A brief note in the existing record is sufficient; no separate approval form is introduced. If there is no objective justification, recommend closure and continue with the next authorized activity.

## 4. Evidence-based closure

Close the selected deliverable when all applicable mandatory criteria and essential evidence are satisfied, no untreated blocking risk remains, relevant caveats are documented and additional checks have no proportionate decision value. A triggered conditional failure remains blocking until treated. Unknown material risks cannot be hidden as caveats.

Use these assessment outcomes within the existing owner record:

| Outcome | Meaning |
|---|---|
| COMPLETED / CONCLUÍDO | Acceptance criteria met; no blocking issue. |
| COMPLETED_WITH_CAVEATS / CONCLUÍDO COM RESSALVAS | Essential mandatory criteria met; only documented non-blocking limitations remain. |
| BLOCKED / BLOQUEADO | A material failure, missing required authority or uncertainty prevents safe completion of this scope. |

These are assessment outcomes, not new runtime states or a separate status store. Preserve the current project's state vocabulary and transition authority. A blocked dependent activity does not stop independent authorized work.

Name the completed scope: analysis, document, static design, prototype, application behavior or entire delivery. Completion of one unit does not complete later units, grant mutation/publication/merge authority or advance report cursors. Design acceptance cannot close a task whose criteria still require functional tests.

## 5. Safeguards and exceptions

This contract cannot waive mandatory security, privacy, data protection, integrity, compliance, accessibility obligations where applicable, loss-prevention checks or other binding acceptance gates. High potential impact may require costly validation. Cost alone never waives a mandatory check.

Existing authorized exception procedures retain their own authority, scope, expiry and residual-risk requirements. An infrastructure disposition is not an executed test or PASS. This contract creates no new waiver authority and does not automatically extend a previous exception to another candidate.

## 6. AI responsibility and continuous improvement

Before requesting more validation, ask: which decision depends on it, what evidence is missing, could the outcomes change that decision, is the cost proportionate, and have closure criteria already been met? Use a short rationale in the existing acceptance/change record when relevant, not repetitive process narration.

Resolved incidents should produce reusable learning. They do not automatically authorize another test campaign or a new obligation; a regression or further test needs a concrete recurrence risk or governing requirement. Reopen closed work only for material new evidence, invalidation, contradiction or changed scope.

Use the existing [acceptance cases seed](../templates/ACCEPTANCE_CASES.md) and [review contract](REVIEW_AND_ACCEPTANCE.md). Validate what is necessary, document what matters, and advance when evidence is sufficient.
