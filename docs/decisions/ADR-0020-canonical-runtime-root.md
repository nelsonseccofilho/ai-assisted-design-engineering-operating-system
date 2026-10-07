# ADR-0020 — Canonical runtime root and structural parity

**Date:** 2026-10-06  
**Status:** ACCEPTED  
**Scope:** FRAMEWORK  
**Supersedes:** ADR-0019 where it required a `runtime-template/` prefix.

## Context

The first package model stored generic deployable files under `runtime-template/` and private instance files at repository root. It was machine-valid but visually confusing and required prefix stripping.

## Decision

Use `runtime/` as the canonical Project Runtime root in both the generic framework and every adopting instance.

`framework runtime/<path> ↔ project runtime/<path>`

No prefix stripping or filename translation is required.

Repository-root differences are allowed when they express repository role rather than runtime structure.

Add `runtime/package.index.json`, a lightweight `runtime/evidence/` surface, a project-owned ADR template under `runtime/docs/decisions/`, and `runtime/compat/` for explicit temporary historical pointers.

Framework ADR history remains framework-owned and must not be copied into project decision history.

## Validation / QA

Require structural parity, package-index coverage, configured schema compatibility, shared-content parity/baseline exceptions, privacy scans and deterministic bootstrap from `runtime/00_START_CHAT.md`.

Live report and hosted CI gates remain independent.
