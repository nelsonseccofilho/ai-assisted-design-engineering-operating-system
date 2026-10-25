# Public upstream equalization delta — 2026-10-24

**Status: REVIEW CANDIDATE / DOCUMENTARY ONLY.** No code, methodology catalog state, mandatory bootstrap, package source, release tag, downstream pin or hosted workflow is changed. This assessment contains **no private source text**, product history, people, customer data, source-media locators or restricted repository identifiers.

## Verified source boundary

- Published GitHub Release `v3.9.0` points to immutable SHA `795cedc5737ae023371f5aca477db20a6f2d635b`, with 65 package paths (32 SHARED, 33 CONFIGURED).
- Reviewed public `main=4d002b7d6e0a4aec0d6612ca8990070d534c37eb`, which includes the post-release documentation-only PowerShell execution-context change. **Main after publication ≠ the release source.**
- The [methodology catalog](methodology-catalog.json) still contains 35 topics: 6 EXISTING_CORE, 19 CANDIDATE_PROCEDURE, 7 OPTIONAL_PILOT, 2 CONFIGURABLE, 1 EXCLUDED_PRIVATE. The prior private-document-origin audit found 26 topics, 25 with generic destinations and one intentionally excluded. This is historical **documentary coverage**, not percent-complete implementation, behavior or effectiveness.

## Bounded generic comparison

| Learning area | Public generic coverage | Current disposition | Evidence needed before further promotion |
| --- | --- | --- | --- |
| Durable objective selection across chat turns | `runtime/scripts/runtime_context.py`; `runtime/scripts/op_cycle.py` | ALREADY_PARTLY_COVERED | Independent negative tests for implicit goal switching, paused/blocked objective and return from subordinate investigation |
| Supervised cycle packet | `runtime/scripts/op_cycle.py` | RELEASED_OPTIONAL | Check conceptual invariants only; a project-specific interface is not equivalent automatically and cannot authorize work |
| Bounded source chunks and manifests | `runtime/scripts/context_read_guard.py` | RELEASED_OPTIONAL | Actual host receipt/full reconstruction needed to claim agent received sources |
| Action/claim coherence | `runtime/scripts/check_action_claim.py` | RELEASED_OPTIONAL | Supplied consistency is not action authentication; independent tool-trace and target readback required |
| Typed current state and current handoff | `runtime/docs/contracts/CURRENT_STATE_AND_HANDOFF.md`; `runtime/scripts/check_current_state.py` | GENERIC_OPTIONAL_ADR_PROPOSED | ADR-0032 is not accepted merely because optional files ship; owner activation remains separate |
| Knowledge/archival integrity | Existing evidence/context source rules | GAP_OR_DUPLICATION_REVIEW | Rights and privacy review; demonstrate missing interface with fictional test before new schema |
| Explicit PowerShell execution directory | `docs/POWERSHELL_EXECUTION_CONTEXT.md` | PUBLIC_MAIN_POST_RELEASE | Not part of released tag; version/release/pin decisions separate |
| Current-main vs historical-SHA evidence | Existing source, validation and acceptance contracts | PARTIAL_OVERLAP | Prefer negative regressions over duplicate authority rules; never retroactively label historical QA PASS |

**Never transfer:** populated user/organization state, real transcripts or videos, operator identifiers, private artifact URLs, historical branch/report cursor repairs, product-specific canvas defaults or user-facing local writing conventions. Generic fictional examples may be designed under explicit scope and privacy/rights review; no private files are upstream code inputs.

## Specific gates

1. Compare actual public interfaces with each proposed reusable behavior; record ALREADY_COVERED vs BEHAVIOR_NOT_VERIFIED vs GENUINE_GAP. Existence of a script is not evidence of independent agent compliance.
2. Preserve all seven optional pilots and original ADR statuses. Do not inflate catalog counts with later aliases.
3. Review this **new docs candidate SHA** with official nine-step local QA, complete changed-file/privacy readback, and appropriate GitHub decision. Hosted CI remains NOT_VERIFIED without executed logs.
4. A new public feature merge, new version/release and downstream pin update each need their own source-bound authorization. The v3.9.0-only hosted risk disposition is not a standing waiver.

**Disposition:** DOCUMENTARY_PUBLIC_DELTA_PREPARED; BEHAVIORAL_EQUIVALENCE_NOT_VERIFIED; NO_NEW_RELEASE; NO_NEW_AGENT_TRIAL; LOCAL_QA_ON_THIS_NEW_SHA_NOT_RUN.
