# PROJECT RUNTIME QA — TEMPLATE

**Runtime version:** <version>  
**Framework version / immutable pin:** <version / full commit SHA>  
**Validated at:** <offset-aware timestamp and timezone>  
**Static result:** NOT_RUN  
**Live report pilot:** PENDING  
**Cross-chat pilot:** PENDING

## Static evidence

Record actual checks and their results: bootstrap order and paths; manifest; unique indexed ADRs; links; Workstream IDs and registry/handoff/state consistency; global Session Record pointers; operator/report mappings; schema/template versions; privacy and secret scans; historical aliases explicitly distinguished from current execution.

Do not claim PASS before running checks. Static QA cannot prove command execution or live artifact geometry.

## Pilot evidence

| Gate | Status | Evidence / checkpoint | Remaining action |
|---|---|---|---|
| Report DRAFT → actual send → SENT | PENDING | <none> | <validate coverage cursor and configured languages> |
| New-chat bootstrap → live reconciliation → continuation | PENDING | <none> | <reinspect actual artifact and persist outcome> |

## Publication and continuity

Runtime checkpoints may merge after appropriate static QA. Framework capability promotion/release follows its declared validation gates. Record candidate and stable refs separately; a merged runtime checkpoint is not automatic proof of a pilot.

**NEXT ACTION:** <one concrete action>.
