"""Opt-in, selected-scope state/routing QA. Standard library, Python 3.9+."""
import argparse
import json
import math
import re
from pathlib import Path, PurePosixPath

CONTRACT_ID = "GOV-RUNTIME-STATE-001"
VERSION = "1.0"
BASE_TYPES = {
    "schema_version": ["string"], "runtime_version": ["string"],
    "workstream_id": ["string"], "legacy_workstream_ids": ["array"],
    "status": ["string"], "current_human_operator": ["string"],
    "operator_alias": ["string"], "latest_chat_label": ["string", "null"],
    "artifact": ["object"], "latest_persistent_change": ["string", "object", "null"],
    "latest_session_record": ["string", "null"],
    "last_completed_action": ["string", "null"], "next_action": ["string", "null"],
    "last_validated_at": ["string", "null"],
}
KINDS = {str: "string", dict: "object", list: "array", bool: "boolean",
         int: "integer", float: "number", type(None): "null"}
STATUSES = {"PLANNED", "ACTIVE", "PAUSED", "BLOCKED", "READY_FOR_QA", "FINAL", "ARCHIVED"}
WORKSTREAM = re.compile(r"WS-\d{8}-\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*")


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def type_spec(value):
    return (isinstance(value, list) and bool(value)
            and all(isinstance(v, str) and v in KINDS.values() for v in value)
            and len(value) == len(set(value)))


def matches(value, spec):
    kind = KINDS.get(type(value))
    return type_spec(spec) and (kind in spec or (kind == "integer" and "number" in spec))


def contained(root, ref):
    """Reject non-canonical references and resolved links escaping the runtime."""
    if not nonempty(ref) or "\\" in ref or ":" in ref or ref != ref.strip():
        return None
    p = PurePosixPath(ref)
    if p.is_absolute() or str(p) != ref or any(x in {".", ".."} for x in p.parts):
        return None
    try:
        target = (root / ref).resolve()
        target.relative_to(root)
        return target
    except (OSError, RuntimeError, ValueError):
        return None


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def reject_constant(_):
    raise ValueError("non-finite number")


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("non-finite number")
    return number


def evaluate(runtime, contract_ref):
    root = Path(runtime).resolve()
    errors = []
    checks = 0
    assessed = 0

    def check(ok, code):
        nonlocal checks
        checks += 1
        if not ok:
            errors.append(code)
        return bool(ok)

    def text(ref):
        path = contained(root, ref)
        try:
            if path is not None and path.is_file():
                return path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            pass
        check(False, "REFERENCE_READ")
        return ""

    def load(ref):
        try:
            data = json.loads(text(ref), object_pairs_hook=strict_object,
                              parse_constant=reject_constant, parse_float=finite_float)
            if isinstance(data, dict):
                return data
        except (ValueError, RecursionError):
            pass
        check(False, "JSON_OBJECT")
        return {}

    manifest = load("runtime-manifest.json")
    contract = load(contract_ref)
    check(set(contract) == {"contract_id", "version", "adoption_status", "decision", "workstreams"},
          "CONTRACT_FIELDS")
    check(contract.get("contract_id") == CONTRACT_ID and contract.get("version") == VERSION,
          "CONTRACT_VERSION")
    check(contract.get("adoption_status") in ("PROPOSED", "ACCEPTED"), "ADOPTION_DECLARATION")
    decision = text(contract.get("decision"))
    check(bool(decision.strip()), "DECISION_REFERENCE")
    check(manifest.get("schema_version") == "1.1" and nonempty(manifest.get("runtime_version")),
          "MANIFEST_VERSION")
    check(manifest.get("current_state_contract") == {
        "id": CONTRACT_ID, "version": VERSION, "path": contract_ref}, "MANIFEST_BINDING")
    registry = text(manifest.get("workstream_registry"))
    rows = []
    for line in registry.splitlines():
        if line.strip().startswith("|") and line.strip().endswith("|"):
            rows.append([c.strip().strip("`") for c in line.strip().split("|")[1:-1]])
    identities = manifest.get("operator_identity")
    if not check(isinstance(identities, list), "OPERATOR_REGISTRY"):
        identities = []
    profiles = contract.get("workstreams")
    if not check(isinstance(profiles, dict) and bool(profiles), "WORKSTREAM_PROFILES"):
        profiles = {}
    existing = {p.name for p in (root / "workstreams").glob("WS-*") if p.is_dir()}
    for wid, profile in profiles.items():
        if not check(bool(WORKSTREAM.fullmatch(wid)), "WORKSTREAM_ID"):
            continue
        assessed += 1
        if not check(isinstance(profile, dict) and set(profile) == {
            "extensions", "artifact_fields", "handoff", "required_operator",
            "required_status", "entry_gate"}, "PROFILE_FIELDS"):
            continue
        state_ref = "workstreams/" + wid + "/state.json"
        state = load(state_ref)
        check(set(BASE_TYPES) <= set(state), "REQUIRED_BASE_FIELDS")
        for key, spec in BASE_TYPES.items():
            check(key in state and matches(state[key], spec), "BASE_TYPE")
        check(state.get("schema_version") == manifest.get("schema_version") and
              state.get("runtime_version") == manifest.get("runtime_version"), "STATE_VERSION")
        check(state.get("workstream_id") == wid, "STATE_IDENTITY")
        status = state.get("status")
        check(isinstance(status, str) and status in STATUSES, "STATE_STATUS")
        required_status = profile.get("required_status")
        check(required_status is None or (isinstance(required_status, str) and
              required_status in STATUSES and status == required_status), "STATUS_GATE")
        check(nonempty(profile.get("entry_gate")), "ENTRY_GATE")
        operator = state.get("operator_alias")
        check(nonempty(operator) and operator == profile.get("required_operator"), "OPERATOR_GATE")
        people = [p for p in identities if isinstance(p, dict) and p.get("operator_alias") == operator]
        check(len(people) == 1 and nonempty(state.get("current_human_operator")) and
              people[0].get("human_operator") == state.get("current_human_operator"), "OPERATOR_IDENTITY")
        if len(people) == 1:
            check(bool(text(people[0].get("profile")).strip()), "OPERATOR_REFERENCE")
        aliases = state.get("legacy_workstream_ids")
        check(isinstance(aliases, list) and all(nonempty(a) for a in aliases), "LEGACY_IDENTITIES")
        session = state.get("latest_session_record")
        if session is not None:
            check(bool(text(session).strip()), "SESSION_REFERENCE")
        fields = profile.get("extensions")
        if not check(isinstance(fields, dict) and not set(fields).intersection(BASE_TYPES),
                     "EXTENSION_PROFILE"):
            fields = {}
        check(set(state) - set(BASE_TYPES) == set(fields), "EXACT_EXTENSIONS")
        for key, spec in fields.items():
            check(key in state and matches(state[key], spec), "EXTENSION_TYPE")
        artifact_fields = profile.get("artifact_fields")
        artifact = state.get("artifact")
        valid_artifact = (isinstance(artifact_fields, dict) and
                          artifact_fields.get("system") == ["string"] and
                          isinstance(artifact, dict) and set(artifact) == set(artifact_fields))
        if check(valid_artifact, "ARTIFACT_FIELDS"):
            for key, spec in artifact_fields.items():
                check(matches(artifact[key], spec), "ARTIFACT_TYPE")
        handoff_ref = profile.get("handoff")
        check(handoff_ref in ("workstreams/" + wid + "/HANDOFF.md",
                              "workstreams/" + wid + "/CURRENT_HANDOFF.md"), "HANDOFF_ROUTE")
        handoff = text(handoff_ref)
        selected = [r for r in rows if r and r[0] == wid]
        check(len(selected) == 1 and len(selected[0]) == 10 and
              selected[0][1] == state.get("current_human_operator") and
              selected[0][2] == operator and selected[0][6] == status and
              selected[0][7] == handoff_ref and selected[0][8] == state_ref, "REGISTRY_ALIGNMENT")
        action = state.get("next_action")
        valid_action = (nonempty(action) and action != "NONE" and "\n" not in action and "\r" not in action)
        check(valid_action or (action is None and status in ("FINAL", "ARCHIVED", "PLANNED")), "STATE_ACTION")
        # Count malformed/mixed spellings too; only one canonical line can pass.
        markers = [line for line in handoff.splitlines()
                   if line.lstrip(" *").startswith("NEXT ACTION:")]
        check(len(markers) == 1 and markers[0] in (
            "NEXT ACTION: " + (action if isinstance(action, str) else "NONE"),
            "**NEXT ACTION:** " + (action if isinstance(action, str) else "NONE")), "HANDOFF_ACTION")
    return {
        "contract_id": CONTRACT_ID, "contract_version": VERSION,
        "assessment": "FAIL" if errors else "PASS", "checks": checks,
        "assessed_workstreams": assessed,
        "unassessed_workstreams": len(existing - set(profiles)),
        "authority": "STATIC_VALIDATION_ONLY", "execution_authorized": False,
        "adoption_verified": False, "writes": False,
        "historical_results": "NOT_REWRITTEN", "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--contract", required=True, help="Runtime-relative profile path")
    args = parser.parse_args()
    result = evaluate(args.runtime, args.contract)
    print(json.dumps(result, indent=2))
    return int(result["assessment"] == "FAIL")


if __name__ == "__main__":
    raise SystemExit(main())
