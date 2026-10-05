# ADR-0013 — Link significant commits to decision records

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `GOVERNANCE`

## Context

The repository now uses both persistent decision records and Conventional Commits.

A decision record explains **why** a significant choice was made.

A commit explains **what changed** in the repository.

Without an explicit link between them, future readers may need to infer which repository change implemented which decision.

## Evidence

The framework already requires:

- persistent ADRs for significant decisions;
- Conventional Commits for repository history;
- changelog entries for notable changes;
- stable Decision IDs.

The missing link is direct traceability between the commit that implements a significant decision and the corresponding decision record.

## Decision

Any commit that **implements, changes, supersedes, or operationalizes a significant decision** must reference the corresponding Decision ID in the commit body or footer.

Preferred form:

```text
docs(governance): link significant commits to ADRs

Decision: ADR-0013
```

Multiple decisions may be referenced when genuinely necessary:

```text
Decision: ADR-0012
Decision: ADR-0013
```

Routine commits that do not implement or change a significant decision do **not** require an ADR reference.

Examples that normally do not require one:

- typo corrections;
- formatting-only changes;
- non-semantic documentation cleanup;
- mechanical maintenance with no governance/product consequence.

A commit message does not replace the ADR.

The ADR remains the authoritative record of rationale.

## Why

This creates an explicit traceability chain:

```text
problem / evidence
        ↓
decision record (ADR)
        ↓
implementation commit
        ↓
changelog / release
```

The chain makes the framework easier to:

- audit;
- understand;
- reverse;
- evolve;
- automate;
- review across human and AI sessions.

## Alternatives considered

### Require an ADR reference in every commit

**Why not selected:**  
This would create unnecessary ceremony for trivial changes and dilute the meaning of decision references.

### Keep ADRs and commits separate

**Why not selected:**  
It preserves both histories but forces future readers to infer their relationship.

### Put all rationale in commit messages

**Why not selected:**  
Commit messages are implementation history, not a durable substitute for structured decision records.

## Impact

### Positive impact

- direct commit-to-decision traceability;
- clearer audit trail;
- easier release reconstruction;
- stronger human/AI continuity;
- better foundation for future automation.

### Trade-offs / risks

- contributors must determine whether a change is decision-significant;
- significant commits require one extra metadata line.

### Workflow impact

Before committing a significant change:

1. confirm the decision record exists;
2. confirm its stable Decision ID;
3. use a valid Conventional Commit header;
4. include `Decision: <ID>` in the body or footer.

## Validation / QA

A significant repository change is correctly traceable when:

- its ADR exists;
- the ADR is indexed in `DECISION_LOG.md`;
- its implementing commit references the ADR ID;
- the changelog/release references the decision when relevant.

## Revisit triggers

Revisit if:

- commitlint or another validator is introduced;
- semantic-release automation is introduced;
- GitHub Actions begin validating Decision IDs;
- a pull-request workflow becomes the primary integration model.
