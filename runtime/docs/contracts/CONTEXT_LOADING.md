# GOV-CTX-001 — Explicit contextual reading

Version: 1.0. Ownership: SHARED_CONTRACT. Optional project adoption; framework ADR-0033.

## Authority and compatibility

The Master remains the canonical public operating contract. Existing eight-file bootstrap, schema1.1, state fields/enums, paths, root compatibility mirrors and installed pins remain supported. The unconfigured profile does not activate itself. A project explicitly adopts a reviewed reading plan, modules, applicability and rollback in its own decision chain. Bind `context_loading` with `id`, `version`, runtime-relative `profile` and `adoption_decision` in its manifest. A declared decision or packet PASS is not verified consent.

Maintain the manifest's00–70 order. A configured plan may emit an index instead of accumulated decision/workstream history or project policy bodies, only when every normative section omitted has an explicit contextual route and applicable mandatory modules are selected before dependent work. The generic Master remains fully loaded in the first implementation; reducing its obligations requires a separate reviewed change. No target byte budget can justify losing a rule.

## One source, explicit applicability

Keep rule text in its existing canonical source. The profile holds paths/selectors and activity/workstream routing, not duplicated policy/status. `*` emits an entire source; exact Markdown headings emit their original section including descendants; `@headings` and `@tables` are discovery indexes, never replacements for governing bodies. An unknown, missing or ambiguous selector fails. New indexed normative sections without a module route fail. Preserve modal force, sequence, scope, actors, exceptions, source hierarchy, QA and authorization.

Before a dependent action, load bootstrap and the appropriate context packet, plus relevant original decisions/evidence. Select work by explicit intent and bounded objective, not solely by file, operator, ACTIVE status, filename, newest timestamp or last paragraph. If ambiguous, recover available evidence and resolve the smallest missing scope question; independent authorized reading may continue. Read-only startup creates no Workstream, Session, mutation history or dummy permission test.

## Current work and historical truth

The selected registry row, state and explicitly registered current handoff must agree. Preserve accumulated history separately; an old action inside history cannot select execution. New metadata repair does not impersonate a product session. A new checkpoint that invalidates the action requires an attributable current update, not automatic last-paragraph selection. Keep product task ledgers, operator ownership, reporting state, live-artifact precedence and owner histories independent.

Bind each concrete inspection to returned source hashes. A later material change invalidates affected reading/evidence; reread affected sources. Source hashes report observed revisions, not an indefinite freeze of legitimate state values. Runtime READ_WRITE availability never creates authorization. A READ_ONLY or UNAVAILABLE packet supplies no execution permission. Tool reads, writes and outcome verification remain target-specific under existing governance.

## Reader and acceptance

From the repository root, use `python -B runtime/scripts/runtime_context.py --runtime runtime bootstrap`, then the same prefix with `context --activity <configured-activity> --workstream <explicit-id>` where applicable. From inside the runtime folder, use `python -B scripts/runtime_context.py --runtime .` instead. CLI JSON is UTF-8 even when the host console uses a legacy encoding. Output is read-only JSON with original selected content, source hashes, route gates, bytes and `execution_authorized:false`, `adoption_verified:false`, `writes:false`. It does not enforce an AI's subsequent conduct, verify approval, test live tools, send reports or certify product readiness. Byte counts measure emitted content separately from source bytes read; no token/cost/productivity claim follows.

Require existing package/sync checks and affected positive/negative/fresh-process regressions for missing routes, unknown modules, wrong order, path escape, duplicate JSON, stale/ambiguous headings, unclassified normative sections and state/registry/action inconsistency. Preserve exact historical inputs/results. Fresh-process fixtures are distinct from independent fresh-chat behavior and actual operator trials. Evaluate both authority recovery and tool-action traces before claiming behavioral effectiveness. Record NOT RUN separately.

Rollback only adopted plan/manifest/selected current records to reviewed sources, preserving later unrelated work and all history. Legacy full bootstrap remains the safe fallback when profile adoption or integrity is unresolved; fallback does not authorize mutation.

## Optional bounded source delivery (generic candidate; no automatic adoption)

For large selected sources, the opt-in `scripts/context_read_guard.py` emits a
manifest of **every** `runtime_context.packet()` selected source followed by
exactly one requested part at a time. This is an output transport helper, not
a new authority or context selector. It inherits the existing adoption, module,
workstream route, integrity and read-only checks of GOV-CTX-001.

From the repository root, after a project has adopted a contextual profile:

```sh
python -B runtime/scripts/context_read_guard.py --runtime runtime --phase bootstrap
python -B runtime/scripts/context_read_guard.py --runtime runtime --phase bootstrap --source-index 1 --part-index 0
python -B runtime/scripts/context_read_guard.py --runtime runtime --phase context --activity analysis --workstream WS-YYYYMMDD-NNN-example
```

Inspect the manifest before requesting parts. Source indices are zero-based,
each part is at most 2400 **Python characters**, and `part_count` may be greater
than one. `raw_source_sha256` hashes the original source bytes as selected by
the existing reader; `selected_content_sha256` hashes the UTF-8 representation
of the selected text; each `part_sha256` hashes exactly the returned part.
Reconstruct each source in ascending part-index order, compare length and hash,
and never infer a complete read from a partial response. Character count is not
a token budget or guaranteed byte bound.

Both manifest and parts explicitly report `reading_verified: false`.
Generation of a source, its manifest, its parts, or passing these regressions
does **not** prove an AI agent received, reconstructed or used them. Only an
independent host trace and a faithful review may support that behavioral claim.
The CLI does not write state, capture private transcripts, perform background
work, grant tool/merge authority or update reporting cursors. Errors fail closed
without publishing another source part. Legacy full-context reading remains
supported; opting in to transport does not activate a candidate project.

The new helper and fictional regressions are **proposed for review only** until
the exact public candidate SHA passes required package checks, privacy/rights
review and a separately approved integration. This addition does not modify
the immutable v3.8.0 release, project pins or the decision statuses of optional
pilots or ADR-0025/ADR-0032.

### One-file Markdown transport (opt-in; generated, not a new contract)

To avoid copying many fragmented outputs into a new session, the **same** `context_read_guard.py` can combine the configured eight-file bootstrap and the selected activity/workstream context in one local, temporary Markdown file. Source text remains owned by the original files; the bundle is not checked into Git and is not an additional authority.

From the repository root, after confirming the adopted profile and the actual Workstream:

```sh
python -B runtime/scripts/context_read_guard.py --runtime runtime --phase bundle --activity analysis-and-design --workstream WS-YYYYMMDD-NNN-example --bundle-output /absolute/path/outside-repository/context-YYYYMMDD.md
```

The output path must be an **absolute, new `.md` path outside the canonical runtime/repository**, in an existing directory. The tool will not overwrite an existing file. It resolves the normal `bootstrap` and `context` packets, retains their original order and selected text, labels each source with its role/selectors and raw/selected SHA-256, then prints only a small receipt containing the generated file SHA. Invalid profile, missing required module, unsafe path or stale Workstream route fails closed.

**Read the generated file in the new chat before dependent actions.** The file does not load itself into ChatGPT; attach/open it explicitly or use an authorized host integration. It may contain project-private evidence and must never be published to the generic framework. Generation and matching hashes do **not** prove the model received or read it, establish live source freshness, grant mutation permission or waive ordinary postflight QA. The existing per-part mode remains available when a combined file is unavailable or too large for reliable delivery.

## Optional explicit cycle-focus preparation (generic candidate)

The opt-in `scripts/op_cycle.py` prepares an **informational, read-only**
packet for five semantic phases: `INICIAR`, `STATUS`, `CONTINUAR`,
`VALIDAR` and `FINALIZAR`. It reuses the GOV-CTX-001 context reader
rather than installing a command catalog, a second Workstream ledger, a new
agent, or automatic background execution. The user must already know which
Workstream is in scope and which activity is configured in a project-adopted
context profile.

```sh
python -B runtime/scripts/op_cycle.py --runtime runtime --workstream WS-YYYYMMDD-NNN-example --activity analysis --phase STATUS
```

The helper requires exact current registry/state/handoff agreement as checked
by `runtime_context.packet()`. It surfaces source revisions, responsible
operator, current status, NEXT ACTION, and candidate sources for reconstructing
the work objective. **An action line is not a verified work objective**.
Therefore `objective=null`, `objective_status=REQUIRES_SOURCE_RECONSTRUCTION`,
and `source_read_by_agent_verified=false` remain explicit, including when
the packet passes. A Session reference may be reported as **unread**; it
is not presented as evidence consumed by the tool. Human/agent review must
read the authoritative source and resolve the objective within its owners
before any dependent action.

Every phase retains `execution_authorized=false`,
`merge_authorized=false`, `acceptance_verified=false`,
`adoption_verified=false` and `writes=false`. The names are suggestions
for presenting a request, **not** built-in chatbot commands, implicit
permissions, Figma/product actions, task state transitions, acceptance,
or actual execution. Invalid phase, missing selection, stale NEXT ACTION,
absent adoption and ambiguous source routing fail closed. No new
project-specific `OP_COMMAND_CATALOG.json` or operator record is copied.

The new CLI and four fictional regression methods are a **candidate** until
the exact Git SHA has passed the existing official Python package workflow,
appropriate privacy/rights review and separate human merge acceptance.
These fixtures do not establish independent multi-chat objective continuity,
human compliance or productivity. They neither change the historical v3.8.0
release nor activate anything in a project or promote optional pilots.
