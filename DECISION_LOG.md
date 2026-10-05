# DECISION LOG

This file is the index of significant decisions made about the **AI-Assisted Design Engineering Operating System** itself.

Project/client-specific decisions should be documented in the corresponding private project context or decision log and must not be committed to a public repository when they contain confidential information.

---

## Decision status

Use one of:

- `PROPOSED`
- `ACCEPTED`
- `REJECTED`
- `SUPERSEDED`
- `DEPRECATED`

A decision marked `ACCEPTED` remains part of the operating model until it is explicitly superseded.

Never silently rewrite history.

---

## Index

| ID | Date | Status | Decision |
|---|---|---|---|
| ADR-0001 | 2026-10-05 | ACCEPTED | Separate the operating model from project context and current handoff |
| ADR-0002 | 2026-10-05 | ACCEPTED | Treat project/client context as local/private runtime data |
| ADR-0003 | 2026-10-05 | ACCEPTED | Use AI-Assisted Design Engineering as the practice name |
| ADR-0004 | 2026-10-05 | ACCEPTED | Collect project context progressively, just in time |
| ADR-0005 | 2026-10-05 | ACCEPTED | Current inspectable tool state outranks stale conversational snapshots |
| ADR-0006 | 2026-10-05 | ACCEPTED | Require parity before UX evolution during reconstruction |
| ADR-0007 | 2026-10-05 | ACCEPTED | Use bounded autonomy based on risk and reversibility |
| ADR-0008 | 2026-10-05 | ACCEPTED | Keep the public repository free of client-specific context |
| ADR-0009 | 2026-10-05 | ACCEPTED | Adopt noncommercial public licensing with commercial rights reserved |
| ADR-0010 | 2026-10-05 | ACCEPTED | Require explicit documentation for every significant decision |
| ADR-0011 | 2026-10-05 | ACCEPTED | Publish the framework as a public, organization-agnostic repository |

---

## Rule

A significant decision is not considered complete until it is documented.

Documentation may live in:

- this repository's `docs/decisions/` directory for framework-level decisions;
- a private project decision log for client/project decisions;
- a project handoff only for temporary operational state, with links to the permanent decision record where applicable.

The Handoff is not a replacement for the Decision Log.
