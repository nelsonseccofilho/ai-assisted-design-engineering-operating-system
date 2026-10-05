# ADR-0012 — Adopt Conventional Commits for repository history

**Date:** 2026-10-05  
**Status:** `ACCEPTED`  
**Scope:** `GOVERNANCE`

## Context

The repository is intended to preserve a structured, machine-readable and human-readable history of the framework.

Unstructured commit messages reduce:

- traceability;
- automated changelog potential;
- semantic versioning support;
- contributor clarity;
- release automation potential.

## Evidence

The Conventional Commits 1.0.0 specification defines a lightweight convention for adding explicit human- and machine-readable meaning to commit messages.

Canonical reference:

https://www.conventionalcommits.org/en/v1.0.0/

## Decision

All repository commits authored as part of this framework must follow **Conventional Commits 1.0.0**.

Required structure:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

Preferred types:

- `feat`
- `fix`
- `docs`
- `refactor`
- `test`
- `build`
- `ci`
- `chore`
- `perf`
- `style`
- `revert`

Recommended repository scopes include:

- `master`
- `governance`
- `decisions`
- `templates`
- `examples`
- `licensing`
- `release`
- `docs`

Breaking changes must be expressed using either:

```text
feat(scope)!: description
```

or a `BREAKING CHANGE:` footer.

Each commit should represent one coherent logical change whenever practical.

## Why

Structured commit history improves:

- readability;
- auditability;
- automated changelog generation;
- semantic release compatibility;
- contribution quality;
- long-term maintainability.

## Impact

Every future commit must be checked against Conventional Commits before being written.

Commit wording becomes part of repository governance.

## Historical note

The repository's GitHub-generated initial commit predates this decision and is preserved as historical evidence.

The history must not be rewritten destructively merely to normalize that pre-policy commit unless an explicit migration decision is made later.

## Validation / QA

Before creating a commit, verify:

1. a valid type exists;
2. optional scope is meaningful;
3. description clearly states the change;
4. breaking changes are explicitly marked;
5. the commit contains one coherent logical change where practical.

## Revisit triggers

Revisit if:

- the project adopts automated semantic-release tooling;
- commitlint or equivalent CI enforcement is introduced;
- repository contribution strategy changes;
- squash-only PR workflows are adopted.
