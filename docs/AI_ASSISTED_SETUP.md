# AI-assisted setup and first-use procedure

**Status:** unreleased onboarding proposal under [ADR-0027](decisions/ADR-0027-ai-assisted-onboarding.md).
**Purpose:** make the existing framework understandable and configurable with help from an AI assistant. This is a supported onboarding path alongside manual setup, not a new runtime intent, autonomous installer or verified compatibility claim for every AI product/OS.

Start with the [copyable setup prompt](../INSTALL_WITH_AI.md). AI-assisted setup is part of the process because environment inspection, progressive configuration and evidence-based verification are already operating principles. The assistant adapts guidance to available tools; the canonical repository instructions remain the source.

## 1. Choose the setup mode

| Mode | Assistant behavior | Ready means |
|---|---|---|
| Guided | No local execution; explain a small step and inspect user-supplied results | Required results were reviewed, with user-executed steps attributed |
| Tool-assisted | Inspect and perform authorized local operations within actual access | Required operations returned success and files/results were read back |
| Exploration | Obtain/read public framework without project configuration | Public entrypoints accessible; no claim of operational project readiness |
| Private project initialization | Configure a distinct runtime from generic seeds | Configuration, structure and first-session checks pass for the selected scope |

Guided/tool-assisted describe capabilities; exploration/private initialization describe the user's goal. Do not infer capabilities from the assistant's name, an old connection or another resource. ChatGPT, Gemini and other assistants can receive the same brief; no specific local execution or browsing feature is assumed.

## 2. Inspect before changing the computer

Confirm OS, target folder, existing installation and intended mode. Inspect existing files before writes. Reuse Git and a compatible Python interpreter; Python 3.9+ is the framework's documented minimum for its standard-library validators. Keep the exact interpreter invocation consistent; on some machines it is python3 or py rather than python.

If prerequisites are missing, consult the official vendor instructions for that OS before recommending a command or installer. Explain the change and obey applicable approval rules. Do not run an opaque downloaded command, bypass security protections or add unrelated dependencies.

No application server, database, model installation, paid API, GPU, recording software, WhisperX, Figma access or multi-agent setup is required for framework exploration. Connectors are optional capabilities configured separately for the work actually requested.

## 3. Obtain and identify the public framework

Use a new or inspected destination. The README's Git clone path is sufficient for a new public checkout; GitHub's source download is an alternative for reading. A source archive without Git history still needs a verified immutable upstream commit before serving as a pinned runtime dependency.

Read README, START_CHAT, runtime README, manifest and package index at the same source commit. Record the declared framework version separately from that commit. Consult changelog and repository status to distinguish released behavior, unreleased changes and draft candidates. Do not treat a PR branch as stable or invent a release tag. Inspect an existing checkout's origin, current commit and local changes before updating it; never reset or discard work as part of setup.

If baseline validation fails, record the failure. A documented candidate containing fixes can be proposed explicitly; do not silently switch branches or claim that the stable checkout passed.

## 4. Initialize a private project only when requested

Keep the public checkout intact. Create a separate empty project destination with the same runtime/ relative layout, copying only generic seeds from the selected framework commit. Do not copy a populated project, public Git history, credentials or the public root ignore rules wholesale.

Configure progressively:
- project context and accountable operator;
- project governance and decision namespace;
- artifact ownership and evidence locations where needed;
- runtime-manifest.json project/framework fields;
- framework-lock.json stable/candidate pins and FRAMEWORK_DEPENDENCY.md, with verified provenance;
- the first Workstream's handoff, state and registry entry under the existing identity rules.

For stable setup, use the independently verified stable commit in the manifest/dependency/lock. For explicitly chosen candidate evaluation, record candidate_pin separately and preserve the independently verified stable baseline; do not label a candidate released. Unknown project facts stay unresolved rather than fabricated.

Preserve shared source content and configured extension fields. Keep optional report policy configurable; do not invent reporting languages or destinations. Use a private ignore policy appropriate to project tracking that excludes credentials, environment secrets, unapproved media and raw exports while allowing the intended operational records. Review staged paths before any authorized commit.

Local initialization does not require a remote push. If the user requests a remote, verify private visibility before uploading project data. Do not broaden access, create credentials or publish a repository merely to test setup.

## 5. Run the applicable checks

From the public framework checkout, run:

```text
python scripts/validate_framework.py
python scripts/test_runtime_sync.py
python scripts/test_methodology.py
python scripts/audit_methodology.py --framework .
python scripts/test_audit_methodology.py
python scripts/test_onboarding.py
python scripts/runtime_sync.py --framework .
```

These commands apply to the candidate containing this guide. For another immutable source, inspect which checks it actually supplies; missing checks are NOT RUN, not fabricated successes. Run commands separately and preserve errors.

For an initialized project, run its runtime/scripts/validate_runtime.py and, from the framework checkout, run:

```text
python scripts/runtime_sync.py --framework "<framework-checkout>" --runtime "<private-project-root>"
```

The project root contains runtime/. Verify the framework checkout's immutable commit against the selected lock pin independently. Read-only synchronization reports configured-file differences for review; it does not overwrite them.

The onboarding regression creates and removes only fictional fixtures in a temporary directory, checks configured-runtime parity and a fresh-process readback, and refuses an existing fixture destination. Its default pins are synthetic test inputs, not upstream provenance. For a real checkout trial, independently verify the stable commit, then use `python scripts/test_onboarding.py --stable-pin <full-verified-stable-commit>`; the candidate is read from the actual local Git HEAD. This is an integration test, not a general-purpose installer or an independent assistant/chat trial.

Static validators check package structure and parity. They do not establish correct project facts, installed connector permissions, security acceptance or successful user onboarding. Inspect remaining placeholders and null fields according to the selected mode; generic seeds are intentionally unconfigured. Verify pin agreement, bootstrap order, owner locations and no accidental public/private mixing. Record PASS/FAIL/NOT RUN for each applicable gate.

## 6. Verify first use and continuity

Use the existing START_NEW_PROJECT intent for a new project; then follow runtime/00_START_CHAT.md and the manifest's eight-file bootstrap. No new setup intent or permanent bootstrap file is introduced.

Confirm actual runtime access, operator identity, scope and initial Workstream. Recover its handoff/state and one concrete next action. Check that the action identifies an available source/target and that essential configuration is resolved; coherent text recovery alone cannot establish execution readiness. For a stronger continuity claim, open a separate session and recover the same state from the persisted runtime without reexplaining project history. If that trial was not performed, leave it NOT RUN. No Figma, production or library mutation is needed to test onboarding.

## Acceptance record

Record privately, proportionally to the setup:
- selected goal, capability mode, OS and destination;
- immutable source/version and stable versus candidate provenance;
- files created/configured, with preserved existing work;
- actual check results, user-executed steps and unresolved fields;
- runtime access and first-workstream recovery evidence;
- optional integrations, deliberately deferred tests and one next-session prompt.

Do not persist credentials, full terminal histories or personal machine details in the public repository. A completed setup report is not evidence that this onboarding procedure has passed independent trials.

## Validation scope for this proposal

Repository link, privacy and package checks validate this documentation change. The scoped Windows checkout/configuration trial, fresh-process readback and one independent Codex conversation recovery trial are recorded in [the onboarding validation record](validation/ONBOARDING_VALIDATION.md). Clean-machine trials on Windows/macOS/Linux and independent ChatGPT/Gemini guided sessions remain NOT RUN. Keep release and pilot gates explicit; do not advertise one-click installation or universal compatibility.

## Repository About

The repository description is English and describes the operating framework without claiming unattended installation. Direct metadata changes are separate from branch/release publication and must be read back after saving.
