# Fictional local functional MVP — 2026-10-15

**Target:** METH-020, bounded synthetic implementation evidence. **Architecture:** 3.6.0.
**Protocol:** fictional-local-functional-v1. **Closure:** COMPLETED_WITH_CAVEATS for this local fixture only, under GOV-VAL-001; this label is not a runtime-state transition or pilot promotion.

## Question and acceptance

Can an executable local fixture enforce its modeled role/scope/revision rules, persist data across a fresh process and recover atomically from an injected failure, using only invented data? The [acceptance plan](../examples/functional-mvp/acceptance.json) defined fifteen mandatory cases before testing. It excluded production authentication, real product permissions, human approval, native-editor behavior, external publication and delivery-efficiency claims.

The [laboratory](../examples/functional-mvp/README.md) uses Python 3.12 and SQLite from the standard library. It models two fictional cards and trusted fictional actor contexts. A reviewer role can approve a draft revision; an editor can publish its local database state only with that current approval. A later edit makes the old approval inapplicable. Local publication sends nothing externally.

## Observed execution

All fifteen required cases passed in the successful Windows/Python 3.12 local execution:

- allowed editor mutation persisted a new revision and event;
- reader, scope, missing/stale approval and actor/action/state denials left persisted state unchanged;
- invalid input produced no partial write or event;
- an injected failure after writes rolled back both card state and event; a subsequent operation succeeded;
- a separate Python process read the saved title, revision, approval and local publication state;
- initialization refused an existing database, and an unrelated scope's record remained unchanged.

See [sanitized observations](../examples/functional-mvp/observations-2026-10-15.json) for all fifteen case outcomes and normalized source hashes. This is one synthetic implementation with fifteen scenarios, not fifteen participants, independent studies or human acceptances. No causal timing or financial metric was measured.

## Failed preparation retained

The first executed attempt reported fifteen setup errors because the restricted environment denied creation of temporary SQLite files. No functional assertion was reached. That result is retained as BLOCKED_SETUP, not discarded or counted as a functional PASS.

Before the successful attempt, execution received access to local temporary files and the test snapshot helper was changed to close SQLite connections explicitly for reliable cleanup. The application code and predeclared acceptance criteria did not change. Both attempts' source hashes and outcomes are retained; raw machine paths and command logs remain restricted. A pre-execution permission-review timeout started no process and supplied no test evidence.

## Limits and disposition

Actor contexts are trusted fixture inputs. The CLI deliberately permits choosing those contexts; it is not authentication and cannot protect a database from its local owner. Production identity binding, tamper resistance, concurrent writers, durable production backup/recovery, encryption, actual user approval, private-product behavior and native UI remain untested. The recovery result concerns a single local SQLite transaction, not general disaster recovery.

The functional acceptance cases are satisfied within that declared boundary. METH-020 remains OPTIONAL_PILOT / PILOT_PENDING; this report narrows an evidence gap without accepting the entire pilot. METH-018 delivery-efficiency comparison, human handoff/critique and native annotation/reflow remain separate pending packages. No existing ADR status, runtime pin/schema, bootstrap, release or private adoption changes.

## Verification and next action

The final candidate still requires the six existing local workflow Python steps, privacy/protected-file review and readback. Their observed results belong in the PR record for the resulting commit. The unchanged GOV-VAL-001 regressions and previous retrieval experiments are reusable within their existing scope; this fixture does not justify rerunning those studies.

The next decision is whether a matched delivery-efficiency protocol has sufficient value and resources. Define matched inputs, quality criteria, effort measurement, independent execution and stop rules before any comparison. Passing functional scenarios alone does not establish faster delivery. Hosted CI remains separately suspended, with no hosted PASS or new exception implied.
