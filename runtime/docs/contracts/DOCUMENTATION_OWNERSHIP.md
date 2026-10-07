# Documentation ownership boundary

This contract defines where durable documentation belongs when a generic operating framework is used by one or more private project runtimes.

## Classification

Every durable record must be classified as exactly one of:

### FRAMEWORK_OWNED

Canonical owner: the public/generic framework repository.

Examples:
- generic operating rules;
- framework ADRs;
- reusable templates and schemas;
- framework scripts and QA;
- framework CI/release notes;
- generic examples and documentation.

Project runtimes may reference these records but must not become the canonical owner of the framework history.

### PROJECT_OWNED

Canonical owner: the private project runtime.

Examples:
- client/project context;
- stakeholder requirements;
- operator configuration;
- private artifact URLs/IDs;
- transcripts and proprietary evidence;
- business rules;
- project Decisions;
- populated Workstreams, Sessions, Reports and Backlog;
- project QA.

These records must not be copied into a public framework when they contain private or project-specific information.

### SHARED_CONTRACT

Canonical upstream owner: the public framework.

The same contract is vendored/pinned into adopting runtimes and should remain content-equivalent unless a governed baseline exception is explicitly declared.

Examples include the Operating Master, shared runtime READMEs, shared runtime contracts and shared synchronization scripts.

Rule:

`PUBLIC upstream → released/pinned version → PRIVATE consumer`

Do not edit shared-contract copies independently in private runtimes.

### CROSS_REPO_REFERENCE

A durable reference that links two canonical owners without duplicating ownership.

Examples:
- a private project Decision adopting a public framework ADR;
- a private dependency file recording the released framework version and pin;
- an upstream-disposition record linking a private finding to its public promotion;
- a public release note stating that a capability was validated in a private adopter without copying confidential details.

A cross-repo reference must identify the canonical owner and link/reference it rather than duplicating the full owner history.

## Promotion flow

```text
private finding
→ classify reusable vs project-only
→ PROJECT_ONLY or UPSTREAM_PENDING
→ public ADR / docs / template / code
→ public release
→ private pin update
→ PROMOTED reference
```

## Historical overlap

Do not delete or silently rewrite accepted historical records that predate this boundary.

When an older project ADR contains framework architecture that was later promoted upstream:

1. preserve the historical project ADR;
2. append an ownership note identifying the canonical public ADR/contract;
3. classify the project record as adoption/history or cross-repo reference;
4. do not duplicate future framework evolution inside the private ADR.

## Completion rule

A documentation change is not complete until:

- its ownership class is known;
- the canonical owner contains the durable record;
- any required shared copy is synchronized;
- cross-repository references point to the canonical owner;
- private information remains private.
