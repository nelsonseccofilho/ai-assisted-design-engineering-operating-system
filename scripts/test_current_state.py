"""Fictional behavior regressions for the opt-in current-state contract."""
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "runtime/scripts/check_current_state.py"
module_spec = importlib.util.spec_from_file_location("current_state_checker", SCRIPT)
checker = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(checker)
WID = "WS-20300101-001-fictional-review"
WORK = "workstreams/" + WID + "/"
STATE = WORK + "state.json"
HANDOFF = WORK + "CURRENT_HANDOFF.md"
PROFILE = "governance/current-state-contract.json"
FIXTURE = json.loads((ROOT / "examples/current-state/fixture.json").read_text(encoding="utf-8"))


def write(root, ref, value):
    path = root / ref
    path.parent.mkdir(parents=True, exist_ok=True)
    content = value if isinstance(value, str) else json.dumps(value, indent=2) + "\n"
    path.write_text(content, encoding="utf-8", newline="\n")


def digest(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class CurrentStateTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fictional-current-state-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = copy.deepcopy(FIXTURE["files"])
        for ref, value in self.files.items():
            write(self.root, ref, value)

    def run_cli(self, contract=PROFILE):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT),
                                 "--runtime", str(self.root), "--contract", contract],
                                capture_output=True, encoding="utf-8")
        self.assertNotIn("Traceback", result.stderr)
        return result.returncode, json.loads(result.stdout)

    def assess(self):
        return checker.evaluate(self.root, PROFILE)

    def test_cli_read_only_scoped_and_never_authorizes(self):
        before = digest(self.root)
        code, result = self.run_cli()
        self.assertEqual(code, 0, result)
        self.assertEqual(result["assessment"], "PASS")
        self.assertEqual(result["assessed_workstreams"], 1)
        self.assertEqual(result["unassessed_workstreams"], 0)
        self.assertEqual(result["authority"], "STATIC_VALIDATION_ONLY")
        for flag in ("writes", "execution_authorized", "adoption_verified"):
            self.assertIs(result[flag], False)
        self.assertEqual(digest(self.root), before)
        # Even a declaration cannot prove actual owner acceptance.
        self.files[PROFILE]["adoption_status"] = "ACCEPTED"
        write(self.root, PROFILE, self.files[PROFILE])
        self.assertFalse(self.assess()["adoption_verified"])
        self.assertFalse(self.assess()["execution_authorized"])

    def test_declared_values_evolve_and_history_does_not_select_action(self):
        historical = (self.root / (WORK + "HANDOFF.md")).read_bytes()
        state = self.files[STATE]
        state["review_round"] = 2
        state["review_note"] = "New fictional same-type value."
        state["latest_persistent_change"] = "Fictional textual reference."
        write(self.root, STATE, state)
        self.assertEqual(self.assess()["assessment"], "PASS")
        self.assertEqual((self.root / (WORK + "HANDOFF.md")).read_bytes(), historical)
        write(self.root, WORK + "HANDOFF.md", historical.decode() + "NEXT ACTION: Later obsolete note.\n")
        state["latest_persistent_change"] = None
        write(self.root, STATE, state)
        self.assertEqual(self.assess()["assessment"], "PASS")

    def test_missing_extra_type_identity_and_gate_failures(self):
        baseline = copy.deepcopy(self.files[STATE])
        cases = [
            ("missing base", lambda s: s.pop("runtime_version"), "REQUIRED_BASE_FIELDS"),
            ("missing extension", lambda s: s.pop("review_round"), "EXACT_EXTENSIONS"),
            ("unknown extension", lambda s: s.update(unreviewed=True), "EXACT_EXTENSIONS"),
            ("boolean integer", lambda s: s.update(review_round=True), "EXTENSION_TYPE"),
            ("wrong extension", lambda s: s.update(review_note=[]), "EXTENSION_TYPE"),
            ("wrong base", lambda s: s.update(legacy_workstream_ids=False), "BASE_TYPE"),
            ("bad alias", lambda s: s.update(legacy_workstream_ids=[False]), "LEGACY_IDENTITIES"),
            ("wrong identity", lambda s: s.update(workstream_id="fictional-wrong"), "STATE_IDENTITY"),
            ("wrong schema", lambda s: s.update(schema_version="0"), "STATE_VERSION"),
            ("wrong version", lambda s: s.update(runtime_version="9"), "STATE_VERSION"),
            ("unknown operator", lambda s: s.update(operator_alias="OTHER"), "OPERATOR_GATE"),
            ("wrong person", lambda s: s.update(current_human_operator="Another Fictional Person"), "OPERATOR_IDENTITY"),
            ("pause removed", lambda s: s.update(status="ACTIVE"), "STATUS_GATE"),
            ("invalid status", lambda s: s.update(status=[]), "STATE_STATUS"),
            ("missing action", lambda s: s.update(next_action=None), "STATE_ACTION"),
            ("action changed", lambda s: s.update(next_action="Changed fictional action."), "HANDOFF_ACTION"),
            ("artifact loss", lambda s: s["artifact"].pop("id"), "ARTIFACT_FIELDS"),
            ("missing session", lambda s: s.update(latest_session_record="missing.md"), "SESSION_REFERENCE"),
            ("escape session", lambda s: s.update(latest_session_record="../outside.md"), "SESSION_REFERENCE"),
        ]
        for label, mutate, expected in cases:
            with self.subTest(label=label):
                state = copy.deepcopy(baseline)
                mutate(state)
                write(self.root, STATE, state)
                result = self.assess()
                self.assertIn(expected, result["errors"])
                self.assertEqual(result["assessment"], "FAIL")
        write(self.root, STATE, baseline)

    def test_routes_registry_markers_and_manifest_must_agree(self):
        mutations = [
            (HANDOFF, lambda f: f + "**NEXT ACTION:** Duplicate.\n", "HANDOFF_ACTION"),
            (HANDOFF, lambda f: f.replace("NEXT ACTION:", " NEXT ACTION:"), "HANDOFF_ACTION"),
            ("registry.md", lambda f: f.replace("CURRENT_HANDOFF.md", "HANDOFF.md"), "REGISTRY_ALIGNMENT"),
            ("registry.md", lambda f: f + f.splitlines()[-1] + "\n", "REGISTRY_ALIGNMENT"),
            ("runtime-manifest.json", lambda f: {**f, "current_state_contract": None}, "MANIFEST_BINDING"),
            ("runtime-manifest.json", lambda f: {**f, "operator_identity": {}}, "OPERATOR_REGISTRY"),
        ]
        for ref, mutate, expected in mutations:
            with self.subTest(ref=ref, expected=expected):
                write(self.root, ref, mutate(copy.deepcopy(self.files[ref])))
                self.assertIn(expected, self.assess()["errors"])
                write(self.root, ref, self.files[ref])
        (self.root / HANDOFF).unlink()
        code, result = self.run_cli()
        self.assertEqual(code, 1)
        self.assertIn("HANDOFF_ACTION", result["errors"])

    def test_profiles_reject_unreviewed_contract_changes(self):
        for label in ("version", "unknown", "base overlap", "bad type", "entry gate", "orphan", "route"):
            with self.subTest(label=label):
                config = copy.deepcopy(self.files[PROFILE])
                profile = config["workstreams"][WID]
                if label == "version": config["version"] = "2.0"
                if label == "unknown": config["ignore_errors"] = True
                if label == "base overlap": profile["extensions"]["status"] = ["string"]
                if label == "bad type": profile["extensions"]["review_round"] = ["anything"]
                if label == "entry gate": profile["entry_gate"] = ""
                if label == "orphan": config["workstreams"]["WS-20300101-002-absent"] = copy.deepcopy(profile)
                if label == "route": profile["handoff"] = WORK + "HANDOFF.md"
                write(self.root, PROFILE, config)
                self.assertEqual(self.assess()["assessment"], "FAIL")
        write(self.root, PROFILE, self.files[PROFILE])

    def test_malformed_json_and_unsafe_paths_fail_without_disclosure(self):
        for content in ("{", "[]", '{"private-marker": NaN}', '{"private-marker": 1e999}',
                        '{"private-marker": 1, "private-marker": 2}'):
            write(self.root, STATE, content)
            code, result = self.run_cli()
            self.assertEqual(code, 1)
            self.assertNotIn("private-marker", json.dumps(result))
            self.assertIn("JSON_OBJECT", result["errors"])
        for ref in ("../outside.json", "C:/outside.json", "/outside.json", "\\\\host\\file", "https://example.invalid/file"):
            code, result = self.run_cli(ref)
            self.assertEqual(code, 1)
            self.assertIn("REFERENCE_READ", result["errors"])
            self.assertNotIn(ref, json.dumps(result))
        self.assertIsNone(checker.contained(self.root, "a/../runtime-manifest.json"))
        self.assertIsNone(checker.contained(self.root, "a//file.json"))

    def test_variants_legacy_route_terminal_action_and_scope(self):
        state = self.files[STATE]
        config = self.files[PROFILE]
        profile = config["workstreams"][WID]
        state["artifact"] = {"system": "fictional-local", "reference": None}
        profile["artifact_fields"] = {"system": ["string"], "reference": ["string", "null"]}
        profile["extensions"]["review_round"] = ["number"]
        state["review_round"] = 1.5
        profile["handoff"] = WORK + "HANDOFF.md"
        write(self.root, WORK + "HANDOFF.md", "**NEXT ACTION:** " + state["next_action"] + "\n")
        registry = self.files["registry.md"].replace("CURRENT_HANDOFF.md", "HANDOFF.md")
        write(self.root, "registry.md", registry)
        write(self.root, STATE, state)
        write(self.root, PROFILE, config)
        self.assertEqual(self.assess()["assessment"], "PASS")
        state["status"] = "FINAL"
        state["next_action"] = None
        profile["required_status"] = None
        write(self.root, STATE, state)
        write(self.root, PROFILE, config)
        write(self.root, "registry.md", registry.replace("| PAUSED |", "| FINAL |"))
        write(self.root, WORK + "HANDOFF.md", "NEXT ACTION: NONE\n")
        # Explicitly unassessed content cannot be reported as runtime-wide health.
        write(self.root, "workstreams/WS-20300101-002-unassessed/state.json", "invalid")
        result = self.assess()
        self.assertEqual(result["assessment"], "PASS")
        self.assertEqual(result["unassessed_workstreams"], 1)
        self.assertFalse(result["execution_authorized"])
        state["next_action"] = "NONE"
        write(self.root, STATE, state)
        self.assertIn("STATE_ACTION", self.assess()["errors"])

    def test_base_contract_and_containment_of_resolved_links(self):
        template = json.loads((ROOT / "runtime/workstreams/_template/state.json").read_text())
        self.assertEqual(set(checker.BASE_TYPES), set(template))
        self.assertEqual(len(template), 14)
        with tempfile.TemporaryDirectory(prefix="fictional-outside-runtime-") as outside:
            external = Path(outside) / "session.md"
            external.write_text("Fictional outside-runtime content.\n", encoding="utf-8")
            link = self.root / "linked-session.md"
            try:
                link.symlink_to(external)
            except OSError:
                self.skipTest("Host does not permit creating symlinks; path guard reviewed in source")
            self.assertIsNone(checker.contained(self.root, "linked-session.md"))
            state = self.files[STATE]
            state["latest_session_record"] = "linked-session.md"
            write(self.root, STATE, state)
            self.assertIn("SESSION_REFERENCE", self.assess()["errors"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
