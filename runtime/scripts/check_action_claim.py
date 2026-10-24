"""Generic optional coherence check for supplied tool-action evidence; never verifies authenticity.

This checker reads a JSON object or an array from --input PATH (use "-" for stdin).
It never accesses targets, mutates state, grants permission or changes formal task status.
A PASS means a *self-reported* action claim is logically consistent with the supplied
references, not that an action really happened. Independent target readback is still
required under governing policy.
"""
import argparse
import json
import sys
from pathlib import Path

TOOL_RESULTS = {"NOT_CALLED", "FAILED", "SUCCEEDED", "UNKNOWN"}
READBACK_RESULTS = {"NOT_RUN", "MATCH", "PARTIAL", "MISMATCH", "INDETERMINATE"}
CLAIMS = {
    "NOT_ATTEMPTED",
    "ATTEMPT_FAILED",
    "TOOL_SUCCESS_UNVERIFIED",
    "PARTIALLY_VERIFIED",
    "VERIFIED",
    "INDETERMINATE",
}
FIELDS = {
    "operation_id", "target", "attempted", "tool_result",
    "tool_response_ref", "readback_result", "readback_ref", "reported",
}


def unique_json_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("DUPLICATE_JSON_KEY")
        obj[key] = value
    return obj


def evidence_ref(value):
    return isinstance(value, str) and bool(value.strip()) and value == value.strip()


def assess(record):
    """Check declared evidence coherence; does not check any external tool or artifact."""
    def result(assessment, reason, expected=None, operation_id=None):
        return {
            "assessment": assessment,
            "reason": reason,
            "operation_id": operation_id,
            "expected_report": expected,
            "observed_execution_verified": False,
            "mutation_authorized": False,
        }

    if not isinstance(record, dict) or set(record) != FIELDS:
        return result("FAIL", "INVALID_FIELDS")
    op = record["operation_id"]
    if not evidence_ref(op) or not evidence_ref(record["target"]):
        return result("FAIL", "INVALID_ID_OR_TARGET")
    if type(record["attempted"]) is not bool:
        return result("FAIL", "INVALID_ATTEMPTED", operation_id=op)
    if (not isinstance(record["tool_result"], str)
            or not isinstance(record["readback_result"], str)
            or record["tool_result"] not in TOOL_RESULTS
            or record["readback_result"] not in READBACK_RESULTS):
        return result("FAIL", "INVALID_OUTCOME", operation_id=op)
    if not isinstance(record["reported"], str) or record["reported"] not in CLAIMS:
        return result("FAIL", "INVALID_REPORTED_CLAIM", operation_id=op)
    tool_ref = record["tool_response_ref"]
    read_ref = record["readback_ref"]
    if tool_ref is not None and not evidence_ref(tool_ref):
        return result("FAIL", "INVALID_TOOL_REF", operation_id=op)
    if read_ref is not None and not evidence_ref(read_ref):
        return result("FAIL", "INVALID_READBACK_REF", operation_id=op)
    tool = record["tool_result"]
    read = record["readback_result"]
    if not record["attempted"]:
        if tool != "NOT_CALLED" or read != "NOT_RUN" or tool_ref is not None or read_ref is not None:
            return result("FAIL", "CONTRADICTORY_NOT_ATTEMPTED", operation_id=op)
        expected = "NOT_ATTEMPTED"
    else:
        if tool == "NOT_CALLED":
            return result("FAIL", "CONTRADICTORY_ATTEMPTED", operation_id=op)
        if tool in {"FAILED", "SUCCEEDED"} and tool_ref is None:
            return result("FAIL", "TOOL_RESPONSE_REFERENCE_REQUIRED", operation_id=op)
        if tool == "UNKNOWN" and tool_ref is not None:
            return result("FAIL", "UNKNOWN_TOOL_RESULT_CANNOT_HAVE_CONFIRMED_RESPONSE", operation_id=op)
        if (read == "NOT_RUN") != (read_ref is None):
            return result("FAIL", "READBACK_REFERENCE_MISMATCH", operation_id=op)
        if read_ref is not None and read_ref == tool_ref:
            return result("FAIL", "READBACK_MUST_BE_SEPARATE_OBSERVATION", operation_id=op)
        if tool == "SUCCEEDED":
            expected = {
                "NOT_RUN": "TOOL_SUCCESS_UNVERIFIED",
                "MATCH": "VERIFIED",
                "PARTIAL": "PARTIALLY_VERIFIED",
                "MISMATCH": "INDETERMINATE",
                "INDETERMINATE": "INDETERMINATE",
            }[read]
        elif tool == "FAILED" and read == "NOT_RUN":
            expected = "ATTEMPT_FAILED"
        else:
            expected = "INDETERMINATE"
    if record["reported"] != expected:
        return result("FAIL", "CLAIM_CONTRADICTS_SUPPLIED_EVIDENCE", expected, op)
    return result("PASS", "INTERNAL_CONSISTENCY_ONLY_NOT_ATTESTATION", expected, op)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, help="JSON object/array evidence file; - for stdin")
    args = p.parse_args()
    try:
        if args.input == "-":
            raw = sys.stdin.read()
        else:
            raw = Path(args.input).read_text(encoding="utf-8-sig")
        source = json.loads(raw, object_pairs_hook=unique_json_object)
        records = source if isinstance(source, list) else [source]
        if not records:
            raise ValueError("EMPTY_EVIDENCE")
        assessed = [assess(v) for v in records]
        ids = [x["operation_id"] for x in assessed]
        if None in ids or len(set(ids)) != len(ids):
            raise ValueError("MISSING_OR_DUPLICATE_OPERATION_ID")
        ok = all(x["assessment"] == "PASS" for x in assessed)
        output = {
            "assessment": "PASS" if ok else "FAIL",
            "scope": "SUPPLIED_EVIDENCE_CONSISTENCY_ONLY",
            "real_tool_execution": "NOT_OBSERVED",
            "results": assessed,
            "mutation_authorized": False,
        }
    except (OSError, ValueError, UnicodeError, TypeError) as exc:
        output = {
            "assessment": "FAIL",
            "reason": "INVALID_INPUT",
            "error_kind": type(exc).__name__,
            "real_tool_execution": "NOT_OBSERVED",
            "mutation_authorized": False,
        }
    print(json.dumps(output, ensure_ascii=True, indent=2))
    raise SystemExit(0 if output["assessment"] == "PASS" else 1)


if __name__ == "__main__":
    main()
