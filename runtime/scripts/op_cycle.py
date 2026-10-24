"""Optional read-only cycle focus packet; never executes or authorizes an action.

Requires a project-reviewed GOV-CTX-001 profile and an explicitly selected
Workstream. Its current state, operator and NEXT ACTION are source-backed.
An objective is never inferred from a NEXT ACTION or historical note.
"""
import argparse
import json
import sys
from pathlib import Path

from runtime_context import ContextError, packet as context_packet

PHASES = ("INICIAR", "STATUS", "CONTINUAR", "VALIDAR", "FINALIZAR")
GUIDANCE = {
    "INICIAR": "RECOVER_OBJECTIVE_AND_CONFIRM_SCOPE_BEFORE_AUTHORIZED_WORK",
    "STATUS": "REPORT_CURRENT_SOURCE_BACKED_STATE_AND_UNVERIFIED_GATES",
    "CONTINUAR": "IDENTIFY_NEXT_SAME_SCOPE_UNIT_SUBJECT_TO_EXISTING_AUTHORITY",
    "VALIDAR": "PREPARE_EVIDENCE_FOR_HUMAN_REVIEW_NOT_ACCEPTANCE",
    "FINALIZAR": "ASSESS_MANDATORY_GATES_AND_SEEK_SEPARATE_ACCEPTANCE",
}


def cycle_packet(runtime, workstream, activity, phase="STATUS"):
    if not isinstance(phase, str) or phase.strip().upper() not in PHASES:
        raise ContextError("UNKNOWN_CYCLE_PHASE")
    if not isinstance(workstream, str) or not workstream.strip():
        raise ContextError("EXPLICIT_WORKSTREAM_REQUIRED")
    if not isinstance(activity, str) or not activity.strip():
        raise ContextError("EXPLICIT_ACTIVITY_REQUIRED")
    selected = phase.strip().upper()
    report = context_packet(runtime, "context", activity=activity,
                            workstream=workstream, access="READ_ONLY")
    if (report.get("workstream") != workstream or
            report.get("execution_authorized") is not False or
            report.get("writes") is not False):
        raise ContextError("CYCLE_CONTEXT_NOT_READ_ONLY")
    sources = report.get("sources", [])
    state_sources = [s for s in sources if s.get("role") == "current-state"]
    handoff_sources = [s for s in sources if s.get("role") == "explicit-current-handoff"]
    if len(state_sources) != 1 or len(handoff_sources) != 1:
        raise ContextError("CYCLE_CURRENT_SOURCES_UNAVAILABLE")
    state_source = state_sources[0]
    handoff = handoff_sources[0]
    try:
        state = json.loads(state_source["content"])
    except (KeyError, ValueError, TypeError):
        raise ContextError("CYCLE_CURRENT_STATE_UNREADABLE") from None
    action = state.get("next_action")
    if (state.get("workstream_id") != workstream or
            not isinstance(action, str) or not action.strip() or
            not isinstance(state.get("operator_alias"), str) or
            not isinstance(state.get("status"), str)):
        raise ContextError("CYCLE_CURRENT_STATE_INCOMPLETE")
    # GOV-CTX-001 already confirmed the registry/state/handoff action agreement.
    # This packet adds NO parallel task or objective store.
    return {
        "kind": "READ_ONLY_CYCLE_FOCUS_PACKET",
        "phase": selected,
        "operation": GUIDANCE[selected],
        "workstream": workstream,
        "operator": state["operator_alias"],
        "workstream_status": state["status"],
        "next_action": action,
        "objective": None,
        "objective_status": "REQUIRES_SOURCE_RECONSTRUCTION",
        "objective_source_candidates": [state_source["path"], handoff["path"]],
        "latest_session_ref_unread": state.get("latest_session_record"),
        "source_revisions": [
            {"path": s["path"], "sha256": s["sha256"], "role": s["role"]}
            for s in sources
        ],
        "loaded_modules": report["loaded_modules"],
        "entry_gates": report["entry_gates"],
        "constraints": [
            "Explicit selected Workstream only; never select first ACTIVE",
            "NEXT ACTION is not evidence of independently recovered objective",
            "Confirm evidence, task ownership and permission before each action",
            "FAIL, SKIPPED, NOT RUN and INDETERMINATE are not PASS",
            "Human review, merge and project acceptance are separate gates",
            "No background execution, alternate ledger or implicit scope switch",
        ],
        "source_read_by_agent_verified": False,
        "execution_authorized": False,
        "merge_authorized": False,
        "acceptance_verified": False,
        "adoption_verified": False,
        "writes": False,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--workstream", required=True)
    parser.add_argument("--activity", required=True)
    parser.add_argument("--phase", default="STATUS")
    args = parser.parse_args(argv)
    try:
        result = cycle_packet(args.runtime, args.workstream, args.activity,
                              args.phase)
    except (ContextError, OSError, ValueError, TypeError, KeyError) as error:
        code = str(error) if isinstance(error, ContextError) else "INVALID_CONFIGURATION"
        print(json.dumps({"assessment": "FAIL", "code": code,
                          "execution_authorized": False, "writes": False}))
        return 1
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
