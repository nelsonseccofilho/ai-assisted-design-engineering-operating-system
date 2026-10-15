# Retrieval comparison laboratory

**Protocol:** retrieval-comparison-v1.1. **Status:** PREPARED / NOT RUN. Target: optional pilot METH-021. Architecture: 3.6.0.
This kit prepares fictional reviewer inputs and measures reader receipts. It has run no new human or independent AI session and demonstrates no index benefit. See the [next-cycle plan](../../docs/PILOT_VALIDATION_NEXT_CYCLE.md) and [earlier bounded trial](../../docs/PILOT_VALIDATION_2026-10-15.md).

## Question and design

The earlier trial had no actual index consultation. This protocol separates optional-index availability under normal source choice from compliance with an explicit index-first instruction:

| Regime | Instruction | Question supported |
|---|---|---|
| Spontaneous | Choose relevant sources normally | Is an available index consulted; what reading is observed? |
| Guided | Consult the selected case's index first if it exists | Does the guided retrieval procedure work, and what reading does it entail? |

Within each regime, four planned fresh sessions balance GARDEN/SKY case order and INDEX/FLAT availability. Each session gets two cases, one per availability condition. There are eight planned independent sessions and sixteen planned case observations, not sixteen participants. The [machine-readable assignments](protocol.json) are checked for balance before preparation.

This is a small exploratory design, without a power calculation or causal productivity claim. No new chats, paid services or participants are created by the kit. Session execution, participants and provider access require a separate authorized scope. The original cases are public: exclude participants already exposed to their answers or materials; do not reuse this conversation or the previous reviewers.

## Prepare locally

Use Python 3.12, Git and a public framework checkout containing the seed commit `30b11995a09e2a86a40e27b193ac9be8b4593333`. No Python packages or network calls are required by the kit.

```text
python examples/retrieval-comparison/comparison.py prepare <new-laboratory-directory> --framework <public-framework-checkout>
python examples/retrieval-comparison/comparison.py summarize <laboratory-directory>
python examples/retrieval-comparison/test_comparison.py
```

Choose a new destination outside the framework checkout. Existing destinations are preserved. The kit reuses the [hardened fictional generator](../pilot-validation/create_fixtures.py), selecting pinned public runtime blobs and refusing dirty/untracked runtime inputs. Only tracked files of its freshly generated synthetic templates are copied into reviewer rooms. Ignored local framework files are not inputs.

Preparation creates SP01–SP04 and GD01–GD04, each a local Git repository with a fictional runtime, TASK.md and the metered reader. There are no remotes or automatic chat dispatches. All mandatory bootstrap files are retained. Coordinator-only files remain at the laboratory root:

- `coordinator.json`: frozen protocol/tool hashes, source-file hashes, bootstrap paths and source-derived expectations.
- `run-records.json`: initially NOT_RUN, with unknown participant type, independence, prior exposure and provider/model.
- `quality-review.json`: initially null review decisions, role and evidence notes.

Keep this root, the answer key, the other rooms, reports and protocol conditions away from fresh reviewers. Give each only its assigned room and TASK.md. The folder layout and prompt do not provide an OS sandbox; enforce an actual access boundary where available. The source-derived key does not constitute a real product decision or human approval.

## Before independent execution

Freeze the protocol commit, generated source hashes, assignment list, participant eligibility, provider/model availability and all changes before dispatch. Record unverified provider/model information as unknown. Use fresh sessions without parent history; do not create new chats from this kit automatically.

Assign eligible participants before seeing results. Preserve failed and incomplete attempts. Do not replace unfavorable observations or add sessions after inspection to seek a benefit. If resources cannot support the planned eight sessions, mark the study incomplete or revise a new protocol version before execution, retaining the earlier plan. Do not treat incomplete data as a completed balanced comparison.

Every session must read the canonical local-main manifest and all eight bootstrap files completely, in order, before either case. The same bootstrap remains in INDEX and FLAT conditions. Receipt repetition for output recovery stays in the record.

After mandatory bootstrap, follow TASK.md in the assigned case order. The reader operations are the same as the [earlier lab](../pilot-validation/README.md): manifest, bootstrap, state, list, read, search and complete. A case's completion marker follows its source reads, before the next case and before final answer composition. Case intervals exclude answer composition and are not full work duration.

## Record execution and review

The coordinator updates a session's run record only from actual evidence:

- `run_kind`: NOT_RUN, MECHANICAL_DRY_RUN or INDEPENDENT_SESSION.
- `participant_type`: AI or HUMAN when known.
- `independent`: true only after verifying fresh-session provenance.
- `prior_case_exposure`: false only after screening; unknown/true cannot enter comparison.
- `independence_evidence`: a short provenance note; keep original identifiers and logs restricted.
- `provider` and `model`: actual observed values or null; never invent cross-provider coverage.

The participant's answer is assessed against the coordinator key and authoritative case files. The reviewer records their role, a source-based evidence note and five explicit true/false checks per case: correct continuity, correct accepted/proposed authority, correct annotation scope, unresolved requirements and absence of unsupported acceptance claims. Null means unreviewed. Identity and source fields alone do not establish a good critique.

The quality review is manual. Do not substitute a mechanical trace, a self-reported PASS, or the participant's agreement for review. A coordinator may grade, but disclose that role and lack of blinded independent grading. Record false results and disagreements rather than hiding them.

## What the summary measures

`summarize` reads existing material and receipts; it does not modify them. It reports:

- normalized UTF-8 source bytes inspected, returned bytes, unique source paths and reader operations;
- index source inspection (including a search scan), explicit full-index retrieval and guided index-first compliance;
- first-case-operation-to-completion intervals;
- manifest/bootstrap overhead once per session, separately from case totals, including every repeated invocation;
- source integrity, protocol errors and manual-quality status;
- eligible counts and mean source bytes per regime, case and availability.

Search counts every file inspected, not just matching snippets. `index_inspected` records any such access. `index_consulted` counts only an explicit full INDEX.md retrieval through the read operation: a search scan alone, even with a matching snippet, does not satisfy consultation. Neither field proves understanding. Guided compliance requires that explicit index retrieval be the first case-document access; a search before it is late consultation. Listings/output headings affect returned bytes. Counters cover instrumented source payloads, not every filesystem/metadata access or setup/grading operation. These are reader measurements, not token usage, billing, cognitive effort or end-to-end delivery duration. Token consumption and financial savings remain null.

Eligibility requires receipts, verified declared independence, no prior exposure, source preservation, complete ordered bootstrap/cases, guided-procedure compliance when applicable and explicit manual-quality PASS. Unknown fields and incomplete sessions remain visible but excluded. Mechanical dry runs never enter eligible groups, even if they successfully exercise the tools.

Receipts and locally stored hashes detect ordinary drift against the frozen record, not malicious alteration of all records or unlogged access. The tool cannot authenticate a person, prove provider identity, enforce read-only permissions or verify an independence assertion by itself.

## Protocol review revision

Version 1.1 fixes a measurement false positive in the original prepared v1: a search could inspect INDEX.md without returning it, yet count as consultation. The two metrics are now separate; guided order is checked at operation level. Protocol sample counts, required quality checks and baseline/version fields are also checked against the implemented design.

The original v1 is retained in Git history at `cac55e1eefd9d251f7845b3f8b72a4339ea31a2c`. No independent v1 trial was run. Frozen v1 preparation directories must be regenerated with v1.1 before dispatch; do not relabel or rewrite prior logs. The review changes the measurement specification, not framework version 3.6.0 or pilot maturity.

## Acceptance and stop rules

Before calling the comparison complete, require eight eligible independent sessions, sixteen reviewed case observations and balanced assignments within each regime. A correctness/authority/scope failure is a recorded primary failure; investigate it before considering a benefit. Missing records, contamination, changed tools or source mutation block acceptance. This is not a global pilot promotion gate by itself.

Compare only like-for-like case/regime groups and preserve quality and overhead alongside source volume. If an available index is not used, report uptake and availability observations; do not infer index efficacy. Guided success supports the instructed procedure, not spontaneous adoption. Overlapping timing, repetition, case learning and default-provider limits must remain explicit. Lower bytes cannot establish financial savings or overall productivity.

The summary exposes eligible observation counts and whether all sixteen planned observations are eligible; a partial run cannot satisfy that completion flag. The tests use synthetic assertions to exercise both exclusion and positive aggregation paths; they provide no participant evidence. The summary never issues an automatic savings claim or maturity promotion. Candidate acceptance, any catalog/ADR change, merge, release and private adoption are separate gates. Existing project design files and private runtimes are outside this experiment.
