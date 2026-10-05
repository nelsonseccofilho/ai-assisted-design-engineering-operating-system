# ADR-0011 — Publish the framework as a public, organization-agnostic repository

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `GOVERNANCE`

## Context

The operating system originated through real consulting work, but the resulting method is reusable across multiple Product Design and Design Engineering contexts. The public artifact must represent the reusable research and consulting framework rather than any specific client engagement.

## Evidence

- the framework has been generalized into Operating Model, Project Context, and Handoff layers;
- real project context is isolated in ignored local runtime files;
- public examples are fictional;
- repository-wide privacy scans found no origin-client names, private Figma URLs, file keys, node IDs, or proprietary identifiers;
- the framework now includes explicit public-release and decision-governance checklists.

## Decision

Publish the framework publicly under the repository identity:

`ai-assisted-design-engineering-operating-system`

The repository must remain organization-agnostic and describe itself as personal research and an evolving consulting framework for persistent AI-assisted Design Engineering workflows.

Public visibility does not grant commercial-use rights; licensing remains governed by the repository license files.

## Why

A generic public repository makes the method reusable, reviewable, versionable, and useful for research or noncommercial experimentation without exposing client-specific consulting context.

## Alternatives considered

### Keep the repository private

**Why not selected:**  
It would reduce external reuse, learning, reviewability, and validation of the framework hypothesis.

### Publish the original client-derived material

**Why not selected:**  
It would unnecessarily expose contextual information and reduce portability.

### Use a narrower Figma-specific repository identity

**Why not selected:**  
The framework now covers a broader operating model including Product Design, Design Systems, governance, QA, handoffs, and agentic tooling.

## Impact

### Positive impact
- reusable public framework;
- clearer product/consulting positioning;
- versionable research history;
- easier adoption across different projects.

### Trade-offs / risks
- every public release now requires a privacy scan;
- commercial-use boundaries must remain clearly documented;
- examples must remain fictional or sanitized.

## Validation / QA

Before each public release:

- run `docs/PUBLICATION_CHECKLIST.md`;
- confirm ignored local files are not tracked;
- scan for real client/project names, URLs, IDs, secrets, and proprietary evidence;
- verify decision records and version metadata are consistent.

## Revisit triggers

Revisit if:

- the repository becomes a packaged commercial product;
- the licensing model changes;
- public/private project architecture changes;
- confidential project context needs a different storage model.
