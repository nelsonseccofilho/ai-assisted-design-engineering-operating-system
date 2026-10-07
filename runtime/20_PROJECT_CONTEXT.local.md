# PROJECT CONTEXT — LOCAL TEMPLATE

> Copy this file to `PROJECT_CONTEXT.local.md`.
>
> In local minimal mode, copy this file to `PROJECT_CONTEXT.local.md` and keep it private. In a governed private Project Runtime, project-specific context may be intentionally versioned there.

**Context status:** `DRAFT | ACTIVE | ARCHIVED`  
**Last updated:** YYYY-MM-DD

---

## 1. PROJECT IDENTITY

**Organization / client:**  
<optional>

**Product / project:**  
<required>

**Primary stakeholder / decision-maker:**  
<required>

**Other relevant stakeholders:**  
<optional>

**Work Package / initiative:**  
<optional>

**Journey / flow:**  
<required>

---

## 2. PROJECT RUNTIME

**Persistent Project Runtime enabled:**  
<yes / no>

**Project Runtime repository / location:**  
<private repository URL / local path / N/A>

**Canonical stable ref:**  
<main / governed ref / N/A>

**Workstream registry:**  
<path / N/A>

**Session record root:**  
<path / N/A>

**Runtime access expectation:**  
<READ_WRITE / READ_ONLY / varies / N/A>

A Project Runtime is canonical for operational continuity, not for current live artifact state.

### Operator identity convention

**Human operator model:**  
<how people are identified>

**Operator alias convention:**  
<stable aliases / N/A>

**Chat label convention:**  
<individual conversation labels / N/A>

Keep Human operator, Operator alias, Chat label and Workstream ID separate.

---

## 3. DESIGN ENVIRONMENT

**Design System / UI Kit name:**  
<name or N/A>

**Design System / UI Kit URL:**  
<private/internal URL or N/A>

**Primary work file name:**  
<required before direct execution>

**Primary work file URL:**  
<required before direct execution>

**Approved reference / source of truth:**  
<URL / node / document / N/A>

**Local Components location:**  
<URL / node / N/A>

---

## 4. GOVERNANCE AND HISTORY

### Artifact registry

Keep one row per relevant artifact. Resolve locations before significant-change finalization. Read-only dependencies need no mutation record. Add rows just in time.

| Artifact identity / role | Governance location or baseline | Change History location | Change namespace | Decision log location | Evidence archive |
|---|---|---|---|---|---|
| <stable owner / consumer> | <location or Master + context> | <owner-local history or owner-scoped companion; unresolved until established> | <unique owner namespace> | <persistent rationale location> | <location or none> |
| <stable owner / shared library> | <location or baseline> | <its own history> | <distinct namespace> | <location> | <location or none> |

Project-level locations below are compatibility summaries. They do not override owner routing or permit a central fallback log.

**Governance location:**  
<URL / page / document / none>

**Project decision index / history summary location:**  
<URL / page / document / none>

**Evidence archive location:**  
<URL / folder / page / none>

---

## 5. EVIDENCE SOURCES

List the sources that may carry requirements or decisions:

- <source>
- <source>

Examples: recordings, transcripts, tickets, specs, research, implementation notes.

---

## 6. TECHNICAL / PRODUCT CONSTRAINTS

- <constraint>
- <constraint>

---

## 7. OPERATING NOTES

- <project-specific convention>
- <project-specific convention>

Do not place generic framework rules here; those belong in the Master.

---

## 8. PRIVACY

This file may contain confidential project information.

Do not commit it to a public repository.


---

## Decision governance

**Decision log location:**  
<private/local path, repository path, or supported project location>

Significant project decisions must be documented persistently and referenced from handoffs.

## Runtime configuration

**Runtime manifest:** <path / N/A>  
**Governance file:** <path / N/A>  
**Framework dependency / immutable pin:** <path / commit / N/A>  
**Daily reports required:** <true / false>  
**Report timezone:** <IANA timezone / N/A>  
**Report languages:** <codes / N/A>  
**Operator command mappings:** <manifest section / N/A>

Use the manifest as configuration authority and keep profiles/state aligned. See [framework/runtime assembly](https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/blob/feat/project-runtime-continuity/docs/FRAMEWORK_RUNTIME_SYNC.md).
