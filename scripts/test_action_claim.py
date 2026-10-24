"""Unit tests for action-claim consistency; no live tools are called."""
import copy
import json
import unittest

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime/scripts"))
from check_action_claim import assess, unique_json_object


BASE = {
    "operation_id": "fixture-op-001",
    "target": "fixture://sandbox/non-production",
    "attempted": True,
    "tool_result": "SUCCEEDED",
    "tool_response_ref": "tool-call-1",
    "readback_result": "MATCH",
    "readback_ref": "independent-read-2",
    "reported": "VERIFIED",
}


class ActionClaimTests(unittest.TestCase):
    def check(self, updates, expected_assessment="PASS", expected=None, reason=None):
        record = copy.deepcopy(BASE)
        record.update(updates)
        result = assess(record)
        self.assertEqual(result["assessment"], expected_assessment, result)
        self.assertFalse(result["observed_execution_verified"])
        self.assertFalse(result["mutation_authorized"])
        if expected:
            self.assertEqual(result["expected_report"], expected)
        if reason:
            self.assertEqual(result["reason"], reason)

    def test_consistent_outcomes(self):
        self.check({
            "attempted": False,
            "tool_result": "NOT_CALLED",
            "tool_response_ref": None,
            "readback_result": "NOT_RUN",
            "readback_ref": None,
            "reported": "NOT_ATTEMPTED",
        }, expected="NOT_ATTEMPTED")
        self.check({
            "tool_result": "FAILED",
            "readback_result": "NOT_RUN",
            "readback_ref": None,
            "reported": "ATTEMPT_FAILED",
        }, expected="ATTEMPT_FAILED")
        self.check({
            "readback_result": "NOT_RUN",
            "readback_ref": None,
            "reported": "TOOL_SUCCESS_UNVERIFIED",
        }, expected="TOOL_SUCCESS_UNVERIFIED")
        self.check({
            "readback_result": "PARTIAL",
            "reported": "PARTIALLY_VERIFIED",
        }, expected="PARTIALLY_VERIFIED")
        self.check({}, expected="VERIFIED")
        self.check({
            "readback_result": "MISMATCH",
            "reported": "INDETERMINATE",
        }, expected="INDETERMINATE")
        self.check({
            "tool_result": "FAILED",
            "readback_result": "MATCH",
            "reported": "INDETERMINATE",
        }, expected="INDETERMINATE")

    def test_prevent_false_success_and_false_denial(self):
        self.check({
            "readback_result": "NOT_RUN",
            "readback_ref": None,
            "reported": "VERIFIED",
        }, "FAIL", expected="TOOL_SUCCESS_UNVERIFIED", reason="CLAIM_CONTRADICTS_SUPPLIED_EVIDENCE")
        self.check({
            "reported": "NOT_ATTEMPTED",
        }, "FAIL", expected="VERIFIED", reason="CLAIM_CONTRADICTS_SUPPLIED_EVIDENCE")
        self.check({
            "readback_result": "PARTIAL",
            "reported": "VERIFIED",
        }, "FAIL", expected="PARTIALLY_VERIFIED", reason="CLAIM_CONTRADICTS_SUPPLIED_EVIDENCE")

    def test_require_distinct_target_and_evidence(self):
        self.check({"tool_response_ref": None}, "FAIL", reason="TOOL_RESPONSE_REFERENCE_REQUIRED")
        self.check({"readback_ref": None}, "FAIL", reason="READBACK_REFERENCE_MISMATCH")
        self.check({"readback_ref": "tool-call-1"}, "FAIL", reason="READBACK_MUST_BE_SEPARATE_OBSERVATION")
        self.check({"target": " "}, "FAIL", reason="INVALID_ID_OR_TARGET")
        self.check({"operation_id": ""}, "FAIL", reason="INVALID_ID_OR_TARGET")

    def test_reject_contradictory_attempts(self):
        self.check({"attempted": False}, "FAIL", reason="CONTRADICTORY_NOT_ATTEMPTED")
        self.check({"tool_result": "NOT_CALLED"}, "FAIL", reason="CONTRADICTORY_ATTEMPTED")
        self.check({"attempted": "false"}, "FAIL", reason="INVALID_ATTEMPTED")

    def test_unknown_is_not_verified(self):
        self.check({
            "tool_result": "UNKNOWN",
            "tool_response_ref": None,
            "reported": "INDETERMINATE",
        }, expected="INDETERMINATE")
        self.check({
            "tool_result": "UNKNOWN",
            "reported": "INDETERMINATE",
        }, "FAIL", reason="UNKNOWN_TOOL_RESULT_CANNOT_HAVE_CONFIRMED_RESPONSE")

    def test_malformed_types_fail_per_record(self):
        for field, reason in (
            ("tool_result", "INVALID_OUTCOME"),
            ("readback_result", "INVALID_OUTCOME"),
            ("reported", "INVALID_REPORTED_CLAIM"),
        ):
            for value in ([], {}, [1], None):
                with self.subTest(field=field, value=value):
                    self.check({field: value}, "FAIL", reason=reason)


    def test_cli_rejects_false_denial_and_duplicate_operations(self):
        import subprocess
        import sys
        from pathlib import Path

        checker = ROOT / "runtime/scripts/check_action_claim.py"
        valid = copy.deepcopy(BASE)
        process = subprocess.run(
            [sys.executable, "-B", str(checker), "--input", "-"],
            input=json.dumps(valid), text=True, capture_output=True, check=False
        )
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["assessment"], "PASS")
        self.assertEqual(json.loads(process.stdout)["real_tool_execution"], "NOT_OBSERVED")

        denied = copy.deepcopy(BASE)
        denied["reported"] = "NOT_ATTEMPTED"
        process = subprocess.run(
            [sys.executable, "-B", str(checker), "--input", "-"],
            input=json.dumps(denied), text=True, capture_output=True, check=False
        )
        self.assertEqual(process.returncode, 1)
        self.assertEqual(
            json.loads(process.stdout)["results"][0]["reason"],
            "CLAIM_CONTRADICTS_SUPPLIED_EVIDENCE"
        )

        process = subprocess.run(
            [sys.executable, "-B", str(checker), "--input", "-"],
            input=json.dumps([valid, valid]), text=True, capture_output=True, check=False
        )
        self.assertEqual(process.returncode, 1)
        self.assertEqual(json.loads(process.stdout)["reason"], "INVALID_INPUT")

    def test_cli_rejects_malformed_and_unsafe_evidence(self):
        import subprocess
        import sys
        from pathlib import Path

        checker = ROOT / "runtime/scripts/check_action_claim.py"
        cases = (
            '{"operation_id":"a","operation_id":"b"}',
            "[]",
            "not-json",
            json.dumps({**BASE, "reported": []}),
            json.dumps({**BASE, "readback_ref": BASE["tool_response_ref"]}),
        )
        for payload in cases:
            with self.subTest(payload=payload[:70]):
                process = subprocess.run(
                    [sys.executable, "-B", str(checker), "--input", "-"],
                    input=payload, text=True, capture_output=True, check=False
                )
                self.assertEqual(process.returncode, 1, process.stderr)
                self.assertEqual(json.loads(process.stdout)["assessment"], "FAIL")

    def test_cli_emits_ascii_safe_json_for_unicode_ids(self):
        import subprocess
        import sys
        from pathlib import Path

        record = copy.deepcopy(BASE)
        record["operation_id"] = "ação-verificada-☑"
        checker = ROOT / "runtime/scripts/check_action_claim.py"
        process = subprocess.run(
            [sys.executable, "-B", str(checker), "--input", "-"],
            input=json.dumps(record, ensure_ascii=True),
            text=True, capture_output=True, check=False
        )
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertTrue(process.stdout.isascii())
        self.assertEqual(
            json.loads(process.stdout)["results"][0]["operation_id"],
            record["operation_id"]
        )

    def test_strict_json_duplicate_keys(self):
        with self.assertRaisesRegex(ValueError, "DUPLICATE_JSON_KEY"):
            json.loads('{"attempted":true,"attempted":false}', object_pairs_hook=unique_json_object)


if __name__ == "__main__":
    unittest.main(verbosity=2)
