# Exploratory pilot validation — 2026-10-15

**Disposition:** bounded evidence for review; no global pilot promotion, release or project adoption.
**Architecture:** 3.6.0. **Input commit:** `30b11995a09e2a86a40e27b193ac9be8b4593333`.
**Governance:** ADR-0025 evidence limits and ADR-0027 onboarding; their proposal statuses remain unchanged.

Two fresh AI chats assessed newly invented materials, and a separate local browser prototype passed ten checks. These observations support specific recovery, critique and interface behaviors. They do not establish general productivity, financial savings, native editor effectiveness or human acceptance.

## Protocol and grading

The conditions and source-derived expectations were persisted before reviewer dispatch. Each reviewer received only its assigned fictional runtime and a read-only task, without this conversation, the answer key or the other reviewer's output. Both independently read the canonical local-main manifest and all eight mandatory bootstrap files before the two cases. Index availability was counterbalanced; case order remained GARDEN then SKY.

- Reviewer A: GARDEN with an optional index; SKY without one.
- Reviewer B: GARDEN without an index; SKY with one.
- Two independent AI sessions, zero human operators. Four case observations are not four independent participants. Provider configuration was the default; cross-provider independence was not established.
- The coordinator checked identity/continuity fields and source-path existence against the pretrial key, and manually inspected authority, annotation scope, proportional critique and missing requirements. The coordinator also prepared the fixtures; this was not a blinded independent grading panel.
- Reviewers proposed QA cases; those suggestions are not executed functional tests. Browser checks described below were executed separately.

See the [reproduction protocol](../examples/pilot-validation/README.md) and [sanitized observations](../examples/pilot-validation/observations-2026-10-15.json). Raw chat outputs, machine paths and operational ledgers are not part of the public package.

## Recovery and critique observations

All four case assessments recovered the workstream, operator alias, status, artifact, next action, canonical component and accepted/proposed decision distinction. All four kept local annotations scoped to their fictional artifact, identified functional gaps, supplied at least four alternatives and seven proposed QA cases, and did not claim proven write access, publication or functional acceptance.

GARDEN contrasted a limited singular/plural label correction (preserving capacity `1/5`) with prematurely enabling publication. SKY contrasted a visible preview-reset label with permanent deletion of saved observations. Both reviewers distinguished the low-impact content refinement from actions requiring accountable approval and additional requirements. A newer proposal and a superseded visual-ready note did not override accepted source authority.

SHA-256 comparison found **87/87 fixture source files unchanged per reviewer**; both fixture Git worktrees remained clean. Receipt files were separate from source content. These are synthetic read-only recovery observations, not acceptance of a live product or proof of write permissions.

## Retrieval measurement

| Reviewer | Case | Optional index available / consulted | Unique paths | Source bytes inspected | Case interval, seconds |
|---|---|---|---:|---:|---:|
| A | GARDEN | Yes / No | 12 | 3,593 | 23.03 |
| A | SKY | No / No | 12 | 3,649 | 20.68 |
| B | GARDEN | No / No | 12 | 3,593 | 23.77 |
| B | SKY | Yes / No | 12 | 3,649 | 19.55 |

Each case used eleven reader operations: listing, state retrieval, eight source-document reads and a completion marker. Intervals run from the first case operation (which can be listing) to the marker, excluding subsequent answer composition. Bytes are UTF-8 text inspected by the reader, with newline normalization; returned bytes include headings/listing output. They are neither model tokens nor billing records.

Neither reviewer consulted `INDEX.md`; source bytes were identical for the same case across conditions. **No index read-volume advantage, causal time improvement or financial saving was demonstrated.** Fixed case order, small sample and unobserved differences in generation/tool latency prevent causal timing claims.

Both sessions invoked the complete eight-file bootstrap three times while recovering from encoding/output visibility issues: 125,799 normalized source bytes inspected per session (41,933 per invocation), separately from case reads. Repetition was retained in the measurement rather than omitted as overhead; it does not mean the bootstrap was skipped.

## Local prototype observations

The fictional Garden prototype used no backend, storage, external integration or publication. Three material units were built in order: filtering/counts; scoped annotation and dependent reflow; reversible reset and long-label stress. U1 and U2 passed their checks before the following unit began. U3 results were saved after browser execution; its completion log was consolidated later and was not backdated. Work intervals include other experimental activity and are not productivity measurements.

Ten executed checks passed:

1. One match uses singular and preserves capacity.
2. Zero matches uses plural and shows the empty state.
3. Multiple matches and filter reset restore the three cards.
4. Annotation expansion increases its container and moves the disabled publication action below it.
5. A 97-character unbroken label wraps without document overflow.
6. Local reset restores cards, query and collapsed note, focuses search, and leaves publication disabled.
7. Expanded annotation and long label fit at 360 CSS pixels.
8. Enter and Space toggle the note.
9. Expanded content fits at 768 CSS pixels.
10. Expanded content fits at 1280 CSS pixels.

DOM geometry and fresh browser screenshots were inspected. An initial mobile capture was stale relative to the expanded DOM; a fresh capture confirmed the expanded state. The [portable final prototype](../examples/pilot-validation/prototype.html) is a synthetic fixture. Geometry and keyboard results do not establish screen-reader coverage, backend authorization, persistence, native canvas behavior or real publication acceptance.

## External-method intake

A real primary reference was reviewed to exercise METH-031: the official [NASA Task Load Index page](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/). It describes a subjective human workload instrument and usage permission, with instructions needed for correct use. That permission does not establish a repository-compatible software license for every related asset.

**Decision: DEFER adoption for this trial.** There were no human respondents and no justified measurement gap requiring this instrument. AI answers cannot supply valid human workload ratings. No forms, code, questionnaire, media or other NASA assets were incorporated. The stop decision exercises one intake review; it does not validate the instrument's benefit, its integration or a general external-method performance claim.

## Pilot disposition and next evidence

| Topic | Supported by this trial | Still unvalidated |
|---|---|---|
| METH-018 — deliverable-first iteration | Three material units with sequential QA are feasible in this fixture | Comparative efficiency, repeated real delivery outcomes |
| METH-019 — review depth and pair critique | Two actual independent AI reviews; proportional critique in 4/4 observations | Human pair review, cross-provider replication, measured UX benefit |
| METH-020 — reversible MVP sequencing | Local reset, blocked publication and ten browser checks | Real permissions/persistence/release acceptance; sequencing advantage |
| METH-021 — shared knowledge and retrieval | 4/4 context recoveries with full bootstrap | Index benefit, human multi-operator continuity, token/cost savings |
| METH-023 — annotation and handoff | 4/4 textual annotation-scope recoveries | Native visual/functional assessment and post-library-sync adoption |
| METH-024 — containment and reflow | Browser wrapping, dependent reflow and three viewport widths | Native editor occupancy, canvas rollout and downstream instances |
| METH-031 — external-method intake | One primary-reference review with a justified stop decision | Method adoption, integration, licensing of any future assets and efficacy |

The catalog classifications remain `OPTIONAL_PILOT`; existing maturity values remain unchanged (including the earlier, separately attributed narrow evidence for METH-023). ADRs remain proposed. A later promotion requires a separately scoped review of the missing evidence, accountable acceptance and compatibility checks. This report creates no new waiver or permission to mutate a private runtime or design file.

## Follow-through review of the portable lab

Review found that the first portable generator copied the working runtime directory, including any Git-ignored local files. The revised generator copies only tracked runtime blobs from the fixed public commit, refuses destinations inside the framework checkout, and preserves the dirty/untracked-input and overwrite gates. The reader now decodes canonical Git output explicitly as UTF-8 and uses an explicit manifest comparison that remains active with Python optimization.

Eight local regression scenarios passed. The ignored-file regression also failed against the original PR implementation, demonstrating that it detects the corrected behavior. These tests use synthetic markers and temporary local clones without network access. They validate the laboratory tooling, not the efficacy of the seven pilots; the historical independent-chat observations and their limits are unchanged.

## Publication validation boundary

This is an additive evidence package. All six repository Python workflow steps passed locally under Python 3.12: 570 package checks, runtime-sync regressions, 17 methodology regressions, 34-topic catalog audit with zero errors, 23 audit regressions and seven onboarding tests. Three suites initially encountered sandbox temporary-directory permission errors; their authorized rerun passed without source changes. Privacy scanning and protected architecture/pin comparisons passed. The portable generator was also exercised with fresh fictional inputs. Changed-file readback is required again on the resulting PR commit. Local Windows checks do not reproduce the hosted Ubuntu runner or hosted setup actions. No hosted CI pass is inferred, and no release or merge is authorized by this report.
