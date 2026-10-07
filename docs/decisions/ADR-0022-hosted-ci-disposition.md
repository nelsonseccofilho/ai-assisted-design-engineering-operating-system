# ADR-0022 — Hosted CI non-execution may be explicitly dispositioned

**Date:** 2026-10-06  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK RELEASE GOVERNANCE

## Context

The Project Runtime candidate passed static package QA, privacy/secret scans, real cross-chat continuity, live-artifact reconciliation, structural parity and an actual Daily Report send/confirmation cycle.

The remaining hosted GitHub Actions gate repeatedly produced a workflow run whose only job:

- started and completed within seconds;
- had `runner_id: 0`;
- had an empty runner name;
- exposed zero steps;
- exposed no usable job log;
- therefore supplied no evidence that framework validation code actually ran.

Treating this platform non-execution as a framework-source failure would conflate CI infrastructure availability with product correctness.

## Decision

A hosted CI gate may be explicitly dispositioned as `DISPOSITIONED_INFRASTRUCTURE` when all of the following are true:

1. the hosted job exposes no assigned runner and no executed steps/logs;
2. the workflow definition itself is present and syntactically inspectable;
3. equivalent local/static validation has PASS evidence;
4. required live pilots have PASS evidence;
5. privacy/secret scans pass;
6. the disposition is documented before release;
7. the release notes clearly distinguish "CI did not execute" from "CI passed".

This is not a CI PASS.

It is a governed release decision that the non-executing hosted gate is not blocking the release.

A future hosted run with real executed steps should still be used to restore normal CI evidence.

## Why

Release governance should be evidence-driven. A platform failure before execution cannot validate or invalidate application/framework logic.

## Impact

Framework 3.6.0 may be promoted after the other declared gates pass, while the hosted CI condition remains recorded as an infrastructure disposition rather than a successful CI run.

## Validation / QA

For the current candidate, run `37559276094` reported:

- job name: `package`;
- conclusion: `failure`;
- runner_id: `0`;
- runner_name: empty;
- steps: empty.

Cross-chat continuity, live-artifact reconciliation, structural parity, privacy/secret scans and the real Daily Report cycle have independent PASS evidence.

## Supersession

None.
