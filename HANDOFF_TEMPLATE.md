# WORKSTREAM HANDOFF / LOCAL CURRENT HANDOFF — TEMPLATE

> Local minimal mode: copy to `HANDOFF_CURRENT.local.md`.
>
> Persistent Project Runtime mode: use one current `HANDOFF.md` per Workstream.
>
> A handoff stores current state; Session Records store material chat history.

**Snapshot:** <offset-aware timestamp + timezone>
**Workstream ID:** <WS-ID / N/A in local minimal mode>
**Current Human operator:** <person / N/A>
**Operator alias:** <stable alias / N/A>
**Latest Chat label:** <label / UNRESOLVED / N/A>  
**Operational status:** `NOT STARTED | IN PROGRESS | READY FOR QA | BLOCKED | READY TO PUBLISH | FINAL | REOPENED | SUPERSEDED`

---

## 1. CURRENT OBJECTIVE

<what is being delivered now>

---

## 2. ACTIVE SCOPE

**Work Package / initiative:**  
<value or N/A>

**Journey / flow:**  
<value>

**Work file:**  
<name + URL>

**Reference / source:**  
<URL / node / document / N/A>

**Rebuild / consumer / target:**  
<URL / node / N/A>

**Local Components:**  
<URL / node / N/A>

---

## 3. REQUEST / REQUIREMENT

### Original request

<concise summary>

### Evidence used

- <source + location + date when useful>
- <source + location + date when useful>

### Source status

- `CANONICAL`: <...>
- `HISTORICAL EVIDENCE`: <...>
- `SUPERSEDED`: <...>

---

## 4. DECISIONS

- <decision>
- <decision>

Classify when useful:

- business rule;
- stakeholder request;
- approved behavior;
- UX;
- UI;
- Design System;
- tool limitation;
- preference;
- hypothesis.

---

## 5. COMPLETED

- <completed mutation / analysis>
- <completed mutation / analysis>

---

## 6. PENDING

- <pending item>
- <pending item>

---

## 7. DECISION / CHANGE HISTORY

| Owner artifact | History location | Namespace-qualified record ID / status | Actual mutation | Linked owner records / decision IDs |
|---|---|---|---|---|
| <owner> | <persistent location> | <namespace:record-id> | <mutation> | <links or N/A> |

**Read-only dependencies / evidence:** <references; no change record unless mutated>  
**Missing owner history / finalization blockers:** <setup still required or none>

For AI-assisted mutations, include offset-aware timestamp/timezone plus Human operator, Operator alias, Chat label and Workstream ID in owner-scoped records when session provenance is relevant.

Handoff/workstream/chat memory is a snapshot and does not replace persistent owner Change History. Correct historical ownership append-only; retain original archived/pointer evidence.

---

## 8. QA STATUS

**Status:** `<state>`

### Passed

- <...>

### Still required

- <...>

---

## 9. KNOWN PROBLEMS / RISKS

- <problem + impact>

---

## 10. OPEN ASSUMPTIONS

- `ASSUMPTION`: <...>

---

## 11. DO NOT TOUCH

- <out-of-scope area>
- <approved behavior that must be preserved>

---

## 12. PUBLICATION / CONSUMER IMPACT

**Publication pending:** yes/no/N/A  
**Consumer impact:** <...>  
**Consumers requiring follow-up:** <...>

---

## 13. PROJECT RUNTIME CONTINUITY

**Runtime access:** `READ_WRITE | READ_ONLY | UNAVAILABLE | N/A`  
**Machine-readable state:** <path / N/A>  
**Latest Session Record:** <global sessions/... path / N/A>  
**Last Git checkpoint:** <commit / N/A>

---

## 14. LAST COMPLETED ACTION

<exact last completed step>

---

## 15. NECESSARY LINKS

- <label>: <URL/location>
- <label>: <URL/location>

---

## 16. NEXT ACTION

**NEXT ACTION:** <one concrete operational action for the next session>



## DECISION RECORDS

List persistent decision IDs relevant to this handoff.

- `ADR-XXXX` — <decision>
- `<PROJECT-DECISION-ID>` — <decision>

Do not use the handoff as the only permanent record for significant decisions.

---

