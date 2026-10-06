# Framework and runtime promotion

The generic framework is the canonical master of reusable behavior. A populated project runtime is an instance and a place to test that behavior against real work.

## Ownership of evolution

1. Capture the issue, evidence and operational result in the project runtime.
2. Decide whether it is a reusable rule, configurable project policy or project-only value.
3. Generalize reusable rules/templates/schemas/QA in a framework feature branch and PR, with a unique indexed framework ADR when the decision is significant.
4. Scan public candidate contents for confidential identifiers and secrets; preserve project evidence privately.
5. Record explicit static and live validation gates. Keep the candidate Draft until required pilots have actual evidence.
6. Merge the approved framework change, establish its immutable stable pin and version.
7. Update runtime dependency metadata, vendored Master and companion references in a runtime PR; verify parity and rerun QA.

Do not let generic method evolve only in private governance indefinitely. A runtime may carry documented overrides while its upstream candidate is being tested; every reusable override needs an upstream disposition.

## Parity matrix

| Capability learned in runtime operation | Generic source | Runtime instance |
|---|---|---|
| Deterministic bootstrap | Manifest bootstrap_files and mapping below | Concrete ordered files |
| Project governance and scope | GOVERNANCE_TEMPLATE.md | Configured private governance |
| Artifact ownership and locators | ARTIFACT_REGISTRY_TEMPLATE.md | Real owner locations |
| Primary evidence indexing | EVIDENCE_INDEX_TEMPLATE.md | Approved private source links |
| Operator identity | OPERATOR_PROFILE_TEMPLATE.md | Registered people and aliases |
| Global Session Records | SESSION_RECORD_TEMPLATE.md | Material per-chat records |
| Continuing Workstreams | WORKSTREAM_REGISTRY_TEMPLATE.md, HANDOFF_TEMPLATE.md, RUNTIME_STATE_TEMPLATE.json | Assignments and current state |
| Daily reporting | Report templates and docs/OPERATOR_DAILY_REPORTS.md | Configured commands/languages/requirement and reports |
| Runtime configuration | RUNTIME_MANIFEST_TEMPLATE.json | runtime-manifest.json |
| QA and live gates | RUNTIME_QA_TEMPLATE.md | Actual validation evidence |
| Framework dependency | FRAMEWORK_DEPENDENCY_TEMPLATE.md | Stable pin and verified vendor |
| Out-of-scope findings | BACKLOG_TEMPLATE.md | Project backlog |
| Privacy boundary | SECURITY.md | Private access and approved data |

## Recommended private runtime assembly

Create these files in a separate private runtime. Public templates are generic sources, not populated runtime state.

| Private destination | Generic source |
|---|---|
| 00_START_CHAT.md | START_CHAT.md, configured to the manifest's numeric order |
| 10_PROMPT_OPERACIONAL_MASTER.md | PROMPT_OPERACIONAL_MASTER.md at the stable pin |
| 20_PROJECT_CONTEXT.local.md | PROJECT_CONTEXT_TEMPLATE.md |
| 30_GOVERNANCE.local.md | GOVERNANCE_TEMPLATE.md |
| 40_PROJECT_DECISION_LOG.local.md | Project decision index using docs/decisions/ADR_TEMPLATE.md |
| 50_ARTIFACT_REGISTRY.local.md | ARTIFACT_REGISTRY_TEMPLATE.md |
| 60_EVIDENCE_INDEX.local.md | EVIDENCE_INDEX_TEMPLATE.md |
| 70_WORKSTREAM_REGISTRY.local.md | WORKSTREAM_REGISTRY_TEMPLATE.md |
| runtime-manifest.json | RUNTIME_MANIFEST_TEMPLATE.json |
| FRAMEWORK_DEPENDENCY.md | FRAMEWORK_DEPENDENCY_TEMPLATE.md |
| PACKAGE_QA.md | RUNTIME_QA_TEMPLATE.md |
| BACKLOG.local.md | BACKLOG_TEMPLATE.md |
| operators/<OPERATOR_ALIAS>.md | OPERATOR_PROFILE_TEMPLATE.md |
| sessions/_template/SESSION_RECORD.md | SESSION_RECORD_TEMPLATE.md |
| workstreams/_template/HANDOFF.md | HANDOFF_TEMPLATE.md |
| workstreams/_template/state.json | RUNTIME_STATE_TEMPLATE.json |
| reports/daily/_template/DAILY_REPORT.md | OPERATOR_DAILY_REPORT_TEMPLATE.md |
| reports/daily/_template/state.json | REPORT_STATE_TEMPLATE.json |

Declare filename translations in the runtime manifest/startup; never depend on implicit lexical discovery. Numeric prefixes are recommended for multi-file bootstrap, while the manifest defines the authoritative order. Generic minimal local mode remains supported.

Keep populated folders out of the public framework. Different repository shapes are expected: the master contains reusable sources, the runtime contains configured instances and real history. Missing generic sources are product gaps; extra private data is not a gap.

## Configuration and schemas

Configure report requirement, timezone, languages and operator command mappings explicitly in the runtime manifest; profiles and per-operator state must agree. Languages must not be empty for live reporting. Commands resolve people through registered aliases, never solely from chat titles.

RUNTIME_STATE_TEMPLATE schema 1.1 adds runtime_version to the generic core. Older 1.0 records can be upgraded by adding the independently governed runtime version; preserve unknown project extension fields. REPORT_STATE_TEMPLATE schema 1.1 defines coverage/delivery/waiver fields. Runtime-specific policy descriptions may extend that core without becoming generic requirements.

## Scope of pilots

Static checks verify repository contracts. A live report pilot requires a persisted DRAFT, actual external sending and SENT confirmation with a correct coverage cursor. A cross-chat pilot requires canonical bootstrap, actual artifact reconciliation and a persisted continuation. A new chat or a repository-only audit alone does not prove either pilot.

## Canonical runtime package (ADR-0019)

The authoritative deployable layout is now `runtime-template/`. Strip that prefix to obtain the identical instance filename. `runtime-template.index.json` is the exhaustive allowlist and classifies each path as shared or configured. Root template names remain compatibility mirrors; edit the canonical source and regenerate its mirror in the same change. QA rejects different contents. Existing root framework entrypoints remain supported.

Shared files are immutable installed content recorded by SHA-256 in the private `framework-lock.json`. A documented stable-baseline exception may retain an older immutable Master while a candidate is being piloted. Keep its stable commit/source/hash separate from candidate source/hash. Do not claim the candidate was released or adopted wholesale.

Configured files are seeds with the same filenames; updates require reviewed migrations and must preserve private values. Populated operators, sessions, reports, workstreams, decisions and evidence are private history, never package inputs. A file's suffix alone is not a privacy boundary. An upstream change must be implemented from generalized requirements in the public branch, never by merging private history.

Run `python scripts/validate_framework.py` and `python scripts/runtime_sync.py --framework .` for public package QA. For an instance, independently fetch the candidate commit named in its lock, then run `python scripts/runtime_sync.py --framework <candidate-checkout> --runtime <instance-checkout> --denylist <private-json-array>`. This command is read-only: errors block consolidation and review items form the update plan. It never overwrites configured files or publishes anything. Verify the checkout SHA separately against the lock and verify any stable exception against its own immutable source.

The private `upstream-disposition.json` records reusable findings with evidence and PROJECT_ONLY, UPSTREAM_PENDING or PROMOTED. PROMOTED means implemented in the linked candidate, not released; release gates remain explicit. New reusable changes must update this registry. The checker reports recorded pending items; it cannot infer semantic reuse from arbitrary prose.

Compatibility migrations retain old path pointers for historical records. Do not rewrite closed sessions or reports. In an existing instance, migrate current references from an artifact-specific registry filename to `50_ARTIFACT_REGISTRY.local.md` and preserve the old name as an alias.
