# ADR-0019 — Canonical runtime package and controlled synchronization

Status: Superseded by ADR-0020 for runtime-root naming; synchronization principles remain historical context.

## Context

Root framework template names and instance filenames differed, making omissions and independent template edits hard to detect.

## Decision

Use runtime-template/ as the canonical deployable tree, an exhaustive classified inventory, exact compatibility mirrors and a read-only parity/update planner. Instances retain private configuration and history. Lock shared content to immutable source commits and hashes; explicitly record stable exceptions while candidates are tested.

## Validation / QA

Check inventory, aliases, shared hashes, manifest/schema parity and privacy before publishing. Exercise negative drift cases. A static pass does not validate live report sending or cross-chat reconciliation.

## Consequences

Configured files require review. Synchronization is never a bidirectional repository mirror. Upstream changes are generalized in clean public commits. Runtime version and framework version remain independent.


## Supersession

ADR-0020 replaces the `runtime-template/` prefix with identical `runtime/` roots in framework and instance.
