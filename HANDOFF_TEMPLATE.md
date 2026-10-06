# WORKSTREAM HANDOFF — TEMPLATE

> Use one current `HANDOFF.md` per persistent workstream when a project runtime supports multiple workstreams.
>
> For a simple/local-only setup this template may still be copied to `HANDOFF_CURRENT.local.md`.
>
> A handoff stores current workstream state. Append-only session history belongs in session records, not here.

**Snapshot:** YYYY-MM-DDTHH:MM:SSZ  
**Operational status:** `NOT STARTED | IN PROGRESS | READY FOR QA | BLOCKED | READY TO PUBLISH | FINAL | REOPENED | SUPERSEDED`

---

## 1. IDENTITY

**Workstream ID:** <stable ID>  
**Human operator:** <person>  
**Session alias:** <stable project-defined alias / N/A>  
**Latest chat label:** <conversation label / N/A>  
**Latest session record:** <path / N/A>

---

## 2. CURRENT OBJECTIVE

<what is being delivered now>

---

## 3. ACTIVE SCOPE

**Work Package / initiative:** <value or N/A>  
**Journey / flow:** <value>  
**Work file / artifact:** <name + URL>  
**Reference / source:** <URL / node / document / N/A>  
**Rebuild / consumer / target:** <URL / node / N/A>  
**Local Components:** <URL / node / N/A>

---

## 4. REQUEST / REQUIREMENT

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

## 5. DECISIONS

- <decision>

Persistent significant decisions must live in the project/framework decision system; this handoff only references them.

---

## 6. LAST COMPLETED

<exact latest completed checkpoint>

---

## 7. COMPLETED

- <completed mutation / analysis>

---

## 8. PENDING

- <pending item>

---

## 9. DECISION / CHANGE HISTORY

- `<record-id>` — <description/status>

---

## 10. QA STATUS

**Status:** `<state>`

### Passed
- <...>

### Still required
- <...>

---

## 11. KNOWN PROBLEMS / RISKS

- <problem + impact>

---

## 12. OPEN ASSUMPTIONS

- `ASSUMPTION`: <...>

---

## 13. DO NOT TOUCH

- <out-of-scope area>

---

## 14. PUBLICATION / CONSUMER IMPACT

**Publication pending:** yes/no/N/A  
**Consumer impact:** <...>  
**Consumers requiring follow-up:** <...>

---

## 15. PERSISTENT RUNTIME STATE

**Runtime repository:** <private repo / N/A>  
**State file:** <path / N/A>  
**Active-workstream registry:** <path / N/A>  
**Last Git checkpoint:** <commit / N/A>

---

## 16. NECESSARY LINKS

- <label>: <URL/location>

---

## 17. DECISION RECORDS

- `ADR-XXXX` — <framework decision>
- `<PROJECT-DECISION-ID>` — <project decision>

---

## 18. NEXT ACTION

**NEXT ACTION:** <exactly one concrete operational action for the next session>
