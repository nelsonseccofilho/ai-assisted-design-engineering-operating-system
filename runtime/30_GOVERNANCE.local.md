# PROJECT GOVERNANCE — TEMPLATE

**Status:** DRAFT  
**Project:** <project>  
**Decision-maker:** <person or role>  
**Runtime access expectation:** READ_WRITE

This file configures project rules. Generic method rules belong in the pinned framework Master.

## Authority and scope

Requirements and significant product approvals remain attributable to primary evidence and the project decision-maker. Distinguish WHAT (required behavior) from HOW (design/implementation response). Declare the approved scope; record out-of-scope findings in BACKLOG.local.md.

Current inspected artifacts outrank stale snapshots. The runtime governs operational continuity. Never use chat memory as its substitute.

## Artifact ownership and concurrency

Declare artifact identities, owner-scoped history locations and namespaces in ARTIFACT_REGISTRY.local.md. The owner of each actual mutation owns its Change record. Read-only dependencies do not receive mutation records.

Use WORKSTREAM_REGISTRY.local.md before mutation. Two ACTIVE Workstreams must not own overlapping scopes. Resolve ownership before continuing.

## Identity, continuity and decisions

Separate Human operator, stable Operator alias, Chat label and operator-independent Workstream ID. Use WS-YYYYMMDD-NNN-<slug>. Material Session Records live in sessions/<OPERATOR_ALIAS>/<YYYY>/<MM>/ and may reference multiple Workstreams.

Maintain handoff/state continuously. Context-limit warnings trigger a safe atomic stop, QA, synchronization and a governed checkpoint ending with one NEXT ACTION. Close sessions only at actual end, context limit or explicit handoff. Preserve history through append-only corrections.

Significant decisions require unique indexed project ADRs. Governed commits follow Conventional Commits 1.0.0 and significant commits reference the implementing Decision ID.

AI-assisted mutation records require offset-aware timestamp, timezone, Human operator, Operator alias, Chat label and Workstream ID. Record unresolved identity explicitly and resolve before finalization or document an explicit exception.

## Access and completion

READ_WRITE permits governed persistence. READ_ONLY permits inspection/reconciliation but blocks significant mutation depending on runtime writes unless a human authorizes a documented degraded exception. UNAVAILABLE requires reconnection before project mutation.

FINAL requires evidence-appropriate QA and persistent owner records. Reports are a separate communication gate.

## Daily Operator Reports

**Required:** false (configure per project)  
**Timezone:** <IANA timezone>  
**Languages:** <language codes>  
**Generate command:** <operator_alias_lower>_report  
**Confirm actual sending:** <operator_alias_lower>_report_sent

Use the report contract in the pinned Master and docs/OPERATOR_DAILY_REPORTS.md. DRAFT never advances the cursor. SENT advances to the frozen interval_end, with delivery time separate. WAIVED requires human/date/time/reason and never advances coverage. When required, each operator with material activity must end the day with SENT or explicit WAIVED.

## Privacy

Store populated runtime files in a separate governed private repository. Never copy confidential values, authentication material or unapproved raw evidence into the public framework.
