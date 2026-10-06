# SESSION RECORD — TEMPLATE

> Append-only history for one material AI-assisted work session.
>
> Do not copy the full chat transcript.
>
> Persist operationally useful deltas, evidence, mutations, decisions, QA, and handoff outcome.

**Date:** YYYY-MM-DD  
**Started:** <timestamp>  
**Ended:** <timestamp / OPEN>

## 1. Identity

**Human operator:** <person>  
**Session alias:** <stable alias / N/A>  
**Chat label:** <conversation identifier / N/A>  
**Workstream:** <stable workstream ID>

Do not infer the human operator solely from a chat title.

## 2. Starting state

**Handoff loaded:** <path>  
**State loaded:** <path / N/A>  
**Starting checkpoint:** <change/commit / N/A>  
**NEXT ACTION received:** <one action>

## 3. Inspected

- <artifact/source + location>

## 4. Completed

- <material analysis/mutation>

## 5. Persistent artifact changes

- <Figma/file CHANGE ID, code commit, document mutation, etc.>

## 6. Decisions

- <Decision ID / none>

## 7. QA

### Passed
- <...>

### Pending
- <...>

## 8. Divergences / reconciliation

- <runtime snapshot vs live tool state divergence and resolution / none>

## 9. Handoff result

**Handoff updated:** <path / no>  
**Runtime state updated:** <path / no>  
**Registry updated:** <path / no>  
**Git checkpoint:** <commit / pending>

**NEXT ACTION:** <exactly one concrete action>

## Persistence rule

Create a session record when the session materially changes operational state, including one or more of:

- artifact mutation;
- workstream state change;
- significant decision;
- meaningful QA;
- evidence mapping that changes planned work;
- publication/rollout;
- handoff/continuity checkpoint;
- runtime/governance change.

Purely conversational sessions with no operational delta do not require a permanent session record.
