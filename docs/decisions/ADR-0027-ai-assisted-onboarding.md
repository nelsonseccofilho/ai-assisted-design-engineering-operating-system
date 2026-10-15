# ADR-0027 — Make AI-assisted setup an explicit onboarding path

**Date:** 2026-10-15
**Status:** PROPOSED
**Scope:** framework onboarding and English repository description

## Context
The repository explains cloning and runtime concepts, but first-time users must assemble environment checks, private configuration and first-session validation themselves. A reusable AI brief can guide those steps using the same inspect, execute, verify and persist principles as the operating framework.

## Decision
Add a provider-neutral copyable setup prompt and a linked procedure. Distinguish guided from tool-assisted capabilities and exploration from private-project initialization. Verify the environment and immutable source before changes, preserve configured work, initialize only generic private seeds, run applicable QA and report observed outcomes. Keep the repository About concise and English.

## Boundaries and alternatives
This is documentation-driven onboarding, not a bundled agent, background service, paid dependency or one-click installer. Manual setup remains available. It introduces no new runtime intent, status enum or mandatory bootstrap step. It does not grant local execution, remote publication, connector permissions or product mutation authority. Existing review, privacy, pin and release gates prevail.

## Validation
Run package/link and synchronization checks and read back changed files. Inspect prompt coverage of missing access, existing installations, failed validation and candidate selection. Add isolated fictional-runtime integration tests for initialization, preservation of existing destinations, configured parity, fresh-process recovery and failure cases. The [scoped validation record](../validation/ONBOARDING_VALIDATION.md) distinguishes those observed checks from independent fresh-machine, provider/OS and cross-chat trials, which remain NOT RUN.

## Supersession
None.
