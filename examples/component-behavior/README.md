# Fictional component behavior specification

**Status:** prepared specification only; every execution and human-acceptance case below is NOT RUN. This is an invented form, not an application, configured runtime, real permission policy or authorization to mutate an artifact.

The [optional seed](../../runtime/docs/templates/COMPONENT_BEHAVIOR.md) supports behavior-focused handoff. All identifiers, rules and content here are invented. The example uses the existing [acceptance boundaries](../../runtime/docs/contracts/REVIEW_AND_ACCEPTANCE.md); no new operational states are introduced.

## Fictional source assumptions

For revision `EXAMPLE-BEHAVIOR-1`, suppose a form edits the title of one fictional draft:

- RULE-EXAMPLE-01: a title contains 1–60 characters after trimming. This is a fixture parameter, not a reusable product requirement.
- RULE-EXAMPLE-02: the modeled service allows a fictional editor to save only within the permitted draft scope. It checks current permission on each request; the client hint is insufficient. Identity binding and enforcement are assumed, not implemented or tested here.
- RULE-EXAMPLE-03: data changes only on a confirmed successful save. A service rejection explicitly marked not committed preserves the prior title. An absent response leaves commit outcome unknown until authorized readback resolves it.
- RULE-EXAMPLE-04: an uncommitted request can be retried after the error is resolved and permission/input are checked again. An operation of unknown outcome must not be blindly resubmitted. No deduplication mechanism is claimed by this document.

These premises establish expected behavior inside this fictional exercise only. In a project, replace them with the actual governing requirements and record gaps rather than treating the example as authority.

## Expected transitions

UI labels such as editing, submitting and outcome-unknown belong to this example, not the framework's task/workstream/report vocabulary. During submission the design retains the input, indicates progress and prevents another conflicting submission; its accessible implementation remains to be checked.

| Case | Event and condition | Expected presentation and recovery | Expected persisted effect | Source / execution |
|---|---|---|---|---|
| B1 — invalid | Submit an empty or over-limit title | Stay in editing; associate an error with the field and move focus to that field. No save request is sent. | No change. | RULE-EXAMPLE-01; NOT RUN |
| B2 — allowed | Submit a valid title with permission indicated | Enter submitting and expose progress through an appropriate status announcement. A client hint alone cannot predict the service decision. | No confirmed change yet. | RULE-EXAMPLE-01/02/03; NOT RUN |
| B3 — denied | The service rejects the save because permission/scope changed while pending | Return to editing with the typed title retained and a clear denial associated with the action. Announce the denial; retain focus if the triggering control remains available, otherwise move to a labeled error summary. Do not claim a save. | No change, because this rejection explicitly reports no commit. | RULE-EXAMPLE-02/03; NOT RUN |
| B4 — retryable failure | The service explicitly reports a transient failure before commit | Show retryable-error, retain input, expose a keyboard-reachable retry action and announce the failure. Retry requires renewed checks. | No change under the explicit no-commit response. | RULE-EXAMPLE-03/04; NOT RUN |
| B5 — safe retry | From retryable-error, activate retry after the condition is resolved | Recheck input/current permission and enter submitting; keep progress perceivable. | Remains unchanged until success. | RULE-EXAMPLE-01/02/04; NOT RUN |
| B6 — success | The modeled service confirms that the permitted save committed | Enter saved, announce success without unexpectedly moving focus, and expose the confirmed title. | Updated title according to the authoritative result; actual durable persistence still needs testing. | RULE-EXAMPLE-02/03; NOT RUN |
| B7 — unknown outcome | A response is lost after submission | Enter outcome-unknown, retain input and explain that confirmation is pending. Provide an authorized status-check path instead of blind resubmission. | Unknown; do not assert rollback or success. | RULE-EXAMPLE-03/04; NOT RUN |
| B8 — reconcile | An authorized readback resolves the pending operation | If the operation is confirmed committed, show saved; if confirmed not committed and retry is safe, show retryable-error. If unresolved, remain outcome-unknown. | Reflect the actual authoritative result, within the actor's permitted scope. | RULE-EXAMPLE-02/03/04; NOT RUN |

The identity of an operation and the service's readback capability must be specified by a real implementation before B8 can run. Missing access or ambiguous results do not authorize a wider read or a guessed conclusion. The proposed focus/announcement behavior also requires an actual implementation and assistive-technology review; a Markdown table proves neither.

## Evidence needed to implement or accept

Before execution, identify the real actor binding, enforcement authority, service contract, object scope, commit/readback semantics, affected consumers and applicable acceptance criteria. Check allowed/denied behavior, unchanged state after explicit rejection, persistence after success, and recovery from both known and unknown outcomes. Verify the chosen keyboard/focus/announcement behavior on the actual interactive target.

This document is a material specification example. Static package QA checks its references and integration, not these eight behaviors. Do not count B1–B8 as passing tests, eight independent participants or evidence of a faster process. A [derived decision brief](../../docs/examples/DECISION_BRIEF.md) shows how to request scoped review without inventing acceptance.
