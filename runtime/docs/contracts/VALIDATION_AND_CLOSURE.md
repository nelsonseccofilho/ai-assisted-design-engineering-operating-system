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

## 3A. Parent-deliverable gate: prevent circular tests and PRs

**Trace before acting.** Before starting a discretionary test, analysis cycle, preparation artifact or PR, identify the accountable parent objective, its observable final acceptance, the current milestone and the specific decision or real blocker the action will resolve. Use the existing owner record to show previous to current verified progress, evidence already available and the smallest authorized material deliverable. Report accepted parent outcomes separately from intermediate milestones; a PR, test count, branch, checklist, comment or elapsed iteration is not progress by itself. Report INDETERMINATE when no grounded denominator exists.

**Test admission.** Perform every applicable MANDATORY check and triggered CONDITIONAL check; this rule grants no waiver. Admit an additional discretionary test only if it addresses a new material risk, invalidated evidence or decision-relevant unanswered question, and state how its possible outcomes change the next decision. Reuse still-valid exact-source/environment evidence. A local/static rerun cannot substitute for a missing independent host, permission boundary or behavioral trace; keep that gate BLOCKED, NOT_RUN or INDETERMINATE as supported.

**Purpose-bound verification.** A temporary/fresh chat validates only observed agent behavior in that host and test; it does not establish invisible access restrictions, isolation or future conduct. For a localized governance or validator change, run directly affected checks, a negative regression case and exact-source readback. Full-package, live, symlink and other security checks remain due at the applicable acceptance, merge or release gate, not automatically for every preparatory iteration. A failed Windows symlink preflight is an environment capability limitation, not a candidate defect; record the full-suite outcome as FAIL/BLOCKED and unrun checks as NOT_RUN, while preserving earlier localized PASS without promotion to full PASS. Do not start unrelated machine-configuration projects, repeatedly rerun identical probes, or create preparatory PRs as a substitute for delivery. Never waive an applicable mandatory gate: use a permitted capable environment, an existing owner-approved exception when allowed, or pause the dependent merge/release with its exact blocker.

**PR admission.** Open a PR only for a bounded, owned material change or evidence artifact explicitly required to be versioned by an existing mandatory gate. Cite its parent outcome, changed canonical owner, acceptance criteria, scope, required QA and separate human integration authority. Group related, already-authorized changes into one coherent candidate when safe; do not combine incompatible owners or bypass distinct approvals. An accepted disposition change in its canonical record can be material. Do not open a PR merely to repeat a diagnosis, copy a receipt, rename a milestone or manufacture progress. Count closure only after required owner acceptance and independent target readback, never when the PR is opened.

**Stop-and-redirect.** After two consecutive discretionary iterations without a verified milestone closure or removal of a real dependency, flag LOOP_RISK only as an assessment in the existing owner record, not a new runtime state. Stop speculative test/PR preparation and choose the next independently authorized deliverable within the same parent objective; otherwise identify the exact missing human decision/external capability and pause the blocked unit. A mandatory safety, privacy, integrity or acceptance check remains binding regardless of loop risk.

**Security denial and authority.** If a platform or tool denies an operation for security, do not retry by another tool, identity, interface or route to evade that denial. Record the observed denial without inventing its cause; use a permitted review/maintainer workflow. Neither this rule nor a generic instruction to continue grants new write, merge, agent, access-policy, release or cross-owner authority. Keep the brief justification in existing Workstream/decision/acceptance history; do not create a parallel anti-loop register.

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
