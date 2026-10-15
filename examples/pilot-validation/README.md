# Reproduce the synthetic pilot trial

This optional laboratory accompanies the [bounded report](../../docs/PILOT_VALIDATION_2026-10-15.md). It creates local fictional inputs and Git repositories; it never configures a real project. Python 3.12 and Git are required. No paid service, package download, Figma access or private repository is required by these scripts. AI chat access, if used, follows the user's own service availability.

## Prepare inputs

Use a public framework checkout containing commit `30b11995a09e2a86a40e27b193ac9be8b4593333`, with runtime files matching that pin and no untracked runtime inputs. The generator refuses an existing destination or a destination inside the framework checkout. Only tracked runtime blobs from the pinned public commit are copied; ignored local files are never inputs. Substitute your own paths:

```text
python examples/pilot-validation/create_fixtures.py <new-laboratory-directory> --framework <public-framework-checkout>
```

The generator writes two separate fictional runtimes, a protocol, source hashes and a source-derived answer key. Only the coordinator sees the laboratory root and answer key. Give each fresh reviewer access solely to its own `reviewer-a` or `reviewer-b` directory, with no previous conversation, this report, generated expectations or the other answer. Do not fork an existing review chat. Use an actual access boundary or restricted reader when available; a prompt alone is not a filesystem sandbox.

The published generator adds portable path arguments, pin/dirty-runtime guards, pinned Git-blob copying and overwrite refusal to the original local preparation script. These packaging changes are not a rerun of the original AI trial. Fixture timestamps and local Git identities will differ; compare semantic inputs and per-run hashes rather than expecting identical new repository commits.

## Local lab regression gate

Before distributing generated inputs, run the eight local privacy, destination-preservation and reader-authority regressions from a checkout containing the pinned commit:

```text
python examples/pilot-validation/test_fixture_generation.py
```

These tests create temporary local clones without network access and use only a synthetic ignored-file marker. They are an additional local gate; the six-step hosted workflow is unchanged. They verify that ignored material is excluded, pinned shared seeds are retained, existing destinations survive, nested destinations/changed or untracked seeds/non-root sources are refused, reader operations preserve sources, and manifest mismatch is rejected even with Python optimization.

## Reviewer instruction

The following task is suitable for a fresh chat. Replace only the authorized directory:

> Read only the fictional runtime in your assigned directory. Use its read_material.py reader so source accesses are measured. Read the canonical local-main manifest, then every mandatory bootstrap file completely and in order. Recover GARDEN, then SKY. Choose relevant source files normally; an optional index may or may not be present. For each case, report workstream, operator alias, status, artifact, next action, canonical component, governing decision, newer proposal, authority and annotation scope. Critique proposals A and B proportionately, identify missing functional requirements, provide alternatives, proposed QA and source paths. Distinguish suggested checks from executed checks. State whether source evidence proves write access, publication or functional acceptance. Do not mutate sources, consult other folders or external systems, simulate human approval, or infer another reviewer's opinion. Record case completion after source reading with the reader, then return your assessment.

Run the reader from the assigned directory. Its operations append receipts outside source content:

```text
python -X utf8 read_material.py manifest
python -X utf8 read_material.py bootstrap
python -X utf8 read_material.py list GARDEN
python -X utf8 read_material.py state GARDEN
python -X utf8 read_material.py read GARDEN 01-brief.md
python -X utf8 read_material.py complete GARDEN
```

Repeat source reads as needed and then the SKY case. The example does not prescribe which remaining files to consult. Keep all mandatory bootstrap content visible even if tool output must be retrieved in segments; retain repeated reads in receipts.

## Grade and measure

Before dispatch, freeze source hashes and expectations. After completion:

- Compare all source-file SHA-256 hashes; inspect fixture Git status and separate receipt writes.
- Check exact identity and continuity fields, canonical source and accepted/proposed distinctions against source-derived expectations.
- Inspect semantic judgments: proposal recency cannot grant authority; annotations cannot widen scope; a label refinement and publication/deletion need proportionate critique. Require explicit missing requirements, alternatives, proposed QA, source pointers and no unsupported acceptance claims.
- Aggregate receipts by reviewer and case: unique paths, bytes inspected/returned, actual index use, and first-case-operation-to-completion-marker interval. Record bootstrap overhead separately. Bytes are normalized reader text, not tokens, elapsed work effort or money.
- Report four observations from two sessions, zero human operators, fixed case order, coordinator grading bias, actual provider coverage and any protocol deviations. A usable index that was never consulted provides no evidence of index efficacy.

## Repeat browser checks

Open `prototype.html` in a browser, or serve this directory locally. It has no backend or storage. Search for a single seed, an absent value and all seeds; confirm singular/plural, empty state, capacity and clear/reset behavior. Expand the note with pointer, Enter and Space; confirm the following action moves below the note and remains disabled. Apply the long-label sample. At 360, 768 and 1280 CSS pixels confirm wrapping and absence of horizontal document overflow. Reset and confirm focus returns to search, the note collapses and nothing is saved/published.

Compare against the ten named cases in [recorded observations](observations-2026-10-15.json). Fresh screenshots and geometry are needed for a new execution claim. The final prototype alone cannot reproduce historical unit order, AI responses or independent-session provenance.

For any future external-method intake, record the primary reference, fit, rights, dependencies, measurable gap and adoption/stop decision before importing assets. Do not infer human workload ratings from AI responses. Keep external assets out until their exact rights and need are reviewed.

This lab does not run or replace hosted CI, authorize new chats automatically, change framework maturity, or approve publication. Review outstanding evidence in the report before proposing a promotion.
