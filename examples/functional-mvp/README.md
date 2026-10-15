# Fictional local functional MVP

**Target:** METH-020, bounded local functional evidence. **Protocol:** fictional-local-functional-v1.
**Policy:** [GOV-VAL-001](../../runtime/docs/contracts/VALIDATION_AND_CLOSURE.md).

This executable SQLite fixture tests draft editing, revision-specific fictional review, a local publication state, scope isolation and atomic rollback/recovery. It contains two invented cards and three invented actor roles. It accesses no private runtime, native editor, external service or paid API.

## Acceptance fixed before execution

The [acceptance cases](acceptance.json) define fifteen mandatory scenarios before execution: allowed/denied actions, cross-scope isolation, missing and stale approvals, rejected inputs/roles/actions, rollback after writes, recovery, fresh-process persistence, preservation of an existing database and unrelated records. Full fixture state is compared before and after denied/failed mutations. Schema/code/plan hashes are retained with results.

Required closure: all fifteen cases actually pass, no unexplained source drift or partial writes, and the evidence limits remain explicit. These functional checks do not require another retrieval trial or human/provider test. They do not establish sequencing or delivery efficiency.

## Run

Use Python 3.12 with its standard-library sqlite3; no packages or network are needed:

```text
python examples/functional-mvp/test_local_mvp.py
```

The suite creates and cleans its own temporary fictional databases. It never selects an existing project database. It exercises the actual local implementation; the persistence scenario opens a separate Python process through the CLI.

For an optional manual exploration, select an explicitly new disposable database file outside project data. Existing files are refused by init. Example commands use a placeholder path that you must replace:

```text
python examples/functional-mvp/local_mvp.py --db <new-fictional-db> init
python examples/functional-mvp/local_mvp.py --db <fictional-db> approve CARD-A --actor fixture-reviewer --role REVIEWER --scope ALPHA
python examples/functional-mvp/local_mvp.py --db <fictional-db> publish CARD-A --actor fixture-editor --role EDITOR --scope ALPHA
python examples/functional-mvp/local_mvp.py --db <fictional-db> show CARD-A --actor fixture-reader --role READER --scope ALPHA
```

The operator deliberately selects a fictional actor context. This is **not an authentication mechanism**: an actual application must authenticate identities and derive trusted roles/scopes independently. Direct SQLite tampering, concurrent writers, production recovery, encryption, backup strategy, human approval and real product permission matrices are outside this fixture. Local PUBLISHED is only a database value; it sends and publishes nothing externally. Fault injection is available to the test harness, not as a CLI operation.

Model approval uses a fictional reviewer; it never represents approval from a real person. Separate real deployment, authorization and acceptance gates remain binding. Passing the suite supplies bounded implementation evidence, not global acceptance of METH-020 or any other pilot.


## Recorded execution

The [bounded report](../../docs/LOCAL_FUNCTIONAL_MVP_2026-10-15.md) records fifteen passing functional cases and the earlier blocked setup attempt. [Numeric observations](observations-2026-10-15.json) retain both attempts and source hashes. A writable temporary directory is required; infrastructure setup failure is not a functional PASS.
