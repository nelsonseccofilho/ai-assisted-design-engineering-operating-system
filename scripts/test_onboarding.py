"""Isolated onboarding integration checks; not an installer or cross-chat AI trial."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = [
    "00_START_CHAT.md", "10_PROMPT_OPERACIONAL_MASTER.md",
    "20_PROJECT_CONTEXT.local.md", "30_GOVERNANCE.local.md",
    "40_PROJECT_DECISION_LOG.local.md", "50_ARTIFACT_REGISTRY.local.md",
    "60_EVIDENCE_INDEX.local.md", "70_WORKSTREAM_REGISTRY.local.md",
]
WS = "WS-20261015-001-onboarding-smoke"
OPERATOR = "Fictional Operator"
ALIAS = "EXAMPLE"
BRIEF = "evidence/fictional-brief.md"
NEXT = "Review evidence/fictional-brief.md without editing external artifacts."
STAMP = "2026-10-15T12:00:00+00:00"
PUBLIC = "https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system"
# Synthetic immutable-shaped test inputs unless --stable-pin is explicitly supplied.
STABLE, CANDIDATE = "a" * 40, "b" * 40


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def digest_tree(root):
    return {
        p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts
    }


def initialize_fixture(project):
    """Only test fixtures, only an absent destination; never merge into existing work."""
    if project.exists():
        raise FileExistsError("Fixture destination already exists")
    project.mkdir(parents=True)
    shutil.copytree(ROOT / "runtime", project / "runtime")
    runtime = project / "runtime"
    manifest = load(runtime / "runtime-manifest.json")
    manifest.update(runtime_name="Fictional onboarding fixture", runtime_version="0.0.0",
                    candidate_ref=CANDIDATE)
    manifest["framework"].update(repository=PUBLIC, version="3.6.0",
                                 stable_pin=STABLE, candidate=CANDIDATE)
    manifest["operator_identity"] = [{
        "human_operator": OPERATOR, "operator_alias": ALIAS,
        "profile": "operators/EXAMPLE/OPERATOR_PROFILE.md",
    }]
    write_json(runtime / "runtime-manifest.json", manifest)
    lock = load(runtime / "framework-lock.json")
    lock.update(stable_pin=STABLE, candidate_pin=CANDIDATE)
    write_json(runtime / "framework-lock.json", lock)
    (runtime / "FRAMEWORK_DEPENDENCY.md").write_text(
        "# Fictional fixture dependency\n\n"
        f"Repository: {PUBLIC}\nStable pin: {STABLE}\nCandidate pin: {CANDIDATE}\n"
        "Framework version: 3.6.0\nRuntime version: 0.0.0\n"
        "Vendored Master: 10_PROMPT_OPERACIONAL_MASTER.md\n"
        "Candidate evaluation only; not a stable adoption or release.\n", encoding="utf-8")
    (runtime / "20_PROJECT_CONTEXT.local.md").write_text(
        "# Fictional onboarding project\n\n"
        f"Decision-maker: {OPERATOR}\nGoal: local setup and readback only.\n"
        "Runtime: local runtime/; canonical ref: main. No remote configured.\n"
        "No external artifacts, connectors, media or real project information.\n"
        "Product requirements and later project facts: UNRESOLVED.\n", encoding="utf-8")
    with (runtime / "30_GOVERNANCE.local.md").open("a", encoding="utf-8") as stream:
        stream.write("\n## Fictional fixture scope\n"
                     "Local setup/readback only. Reports remain optional and disabled.\n"
                     "No product, design, external artifact, remote or release mutation.\n")
    (runtime / BRIEF).write_text(
        "# Fictional local brief\n\n"
        "Synthetic input for this onboarding fixture only.\n"
        "Task: review this brief and report unresolved requirements.\n"
        "Scope: read-only local analysis; no product or external artifact mutation.\n"
        "No real client, stakeholder, recording, transcript or product data.\n", encoding="utf-8")
    profile = runtime / "operators/EXAMPLE/OPERATOR_PROFILE.md"
    profile.parent.mkdir()
    profile.write_text(
        f"# Fictional operator\n\nHuman operator: {OPERATOR}\n"
        f"Operator alias: {ALIAS}\nChat label convention: onboarding-smoke\n"
        "Report commands: N/A; daily reports disabled in manifest.\n", encoding="utf-8")
    work = runtime / "workstreams" / WS
    work.mkdir()
    state = load(runtime / "workstreams/_template/state.json")
    session = "sessions/EXAMPLE/2026/10/2026-10-15_onboarding-smoke.md"
    state.update(workstream_id=WS, status="ACTIVE", current_human_operator=OPERATOR,
                 operator_alias=ALIAS, latest_chat_label="onboarding-smoke",
                 artifact={"system": "local-files", "id": "fictional-runtime", "scope": "setup/readback"},
                 latest_persistent_change="FICT-CHANGE-0001",
                 latest_session_record=session, last_completed_action="Initialize fictional runtime",
                 next_action=NEXT, last_validated_at=STAMP, runtime_version="0.0.0")
    write_json(work / "state.json", state)
    (work / "HANDOFF.md").write_text(
        f"# Fictional onboarding handoff\n\nWorkstream ID: {WS}\n"
        f"Human operator: {OPERATOR}\nOperator alias: {ALIAS}\n"
        "Chat label: onboarding-smoke\nOperational status: IN PROGRESS\n"
        "Runtime access: READ_WRITE (authorized fixture creation and readback observed)\n"
        "Scope: local setup/readback. External artifacts: N/A.\n"
        f"State: workstreams/{WS}/state.json\nSession: {session}\n"
        "Owner history: CHANGE_HISTORY.local.md#fict-change-0001\n"
        "QA: structure and continuity checks pending until test completion.\n"
        "Live report cycle and independent cross-chat AI trial: NOT RUN.\n"
        f"NEXT ACTION: {NEXT}\n", encoding="utf-8")
    (runtime / "70_WORKSTREAM_REGISTRY.local.md").write_text(
        "# Fictional Workstream registry\n\n"
        "| Workstream ID | Human operator | Operator alias | Chat label | Scope | Mutation scope | Status | Handoff | State | Last validated |\n"
        "|---|---|---|---|---|---|---|---|---|---|\n"
        f"| {WS} | {OPERATOR} | {ALIAS} | onboarding-smoke | local setup | fictional runtime | ACTIVE | "
        f"workstreams/{WS}/HANDOFF.md | workstreams/{WS}/state.json | {STAMP} |\n", encoding="utf-8")
    record = runtime / session
    record.parent.mkdir(parents=True)
    record.write_text(
        f"# Fictional setup session\n\nTimestamp: {STAMP}\nTimezone: UTC\n"
        f"Human operator: {OPERATOR}\nOperator alias: {ALIAS}\n"
        f"Chat label: onboarding-smoke\nWorkstream: {WS}\n"
        "Intent: START_NEW_PROJECT. Authorized only to initialize this fictional fixture.\n"
        "Action: seed copy, local configuration and readback.\n"
        "Owner history: CHANGE_HISTORY.local.md#fict-change-0001\n"
        f"NEXT ACTION: {NEXT}\n", encoding="utf-8")
    (runtime / "CHANGE_HISTORY.local.md").write_text(
        "# Fictional runtime owner history\n\n## FICT-CHANGE-0001\n"
        f"Timestamp: {STAMP}\nTimezone: UTC\nHuman operator: {OPERATOR}\n"
        f"Operator alias: {ALIAS}\nChat label: onboarding-smoke\nWorkstream: {WS}\n"
        "Mutation: generic seed initialization and fictional configuration in this runtime only.\n"
        "Owner: fictional-runtime. Rationale: ADR-0027 in selected framework dependency.\n"
        "QA: checks pending until test completion; no external owner changed.\n", encoding="utf-8")
    # Project tracking policy: no public history or public root ignore rules are copied.
    (project / ".gitignore").write_text(
        ".env\n.env.*\n!.env.example\ncredentials/\nraw-media/\nraw-exports/\n__pycache__/\n",
        encoding="utf-8")
    return runtime


def recover(runtime):
    """Read only persisted runtime state in a fresh process."""
    manifest = load(runtime / "runtime-manifest.json")
    if manifest["bootstrap_files"] != BOOTSTRAP:
        raise ValueError("Bootstrap contract changed")
    bootstrap = [(runtime / path).read_text(encoding="utf-8") for path in BOOTSTRAP]
    lock = load(runtime / "framework-lock.json")
    for key, manifest_key in (("stable_pin", "stable_pin"), ("candidate_pin", "candidate")):
        if not re.fullmatch(r"[0-9a-f]{40}", lock[key] or ""):
            raise ValueError("Missing immutable pin")
        if lock[key] != manifest["framework"][manifest_key]:
            raise ValueError("Manifest/lock pin mismatch")
        if lock[key] not in (runtime / "FRAMEWORK_DEPENDENCY.md").read_text(encoding="utf-8"):
            raise ValueError("Dependency pin mismatch")
    registry = bootstrap[-1]
    if WS not in registry or "ACTIVE" not in registry:
        raise ValueError("Active Workstream missing from registry")
    state = load(runtime / f"workstreams/{WS}/state.json")
    handoff = (runtime / f"workstreams/{WS}/HANDOFF.md").read_text(encoding="utf-8")
    identity = manifest["operator_identity"][0]
    profile = (runtime / identity["profile"]).read_text(encoding="utf-8")
    session = (runtime / state["latest_session_record"]).read_text(encoding="utf-8")
    for value in (state["workstream_id"], state["current_human_operator"], state["operator_alias"]):
        if value not in registry or value not in handoff or value not in session:
            raise ValueError("Identity mismatch")
    if identity["human_operator"] != state["current_human_operator"] or identity["operator_alias"] != state["operator_alias"]:
        raise ValueError("Operator identity mismatch")
    if state["operator_alias"] not in profile or state["current_human_operator"] not in profile:
        raise ValueError("Operator profile mismatch")
    if f"NEXT ACTION: {state['next_action']}" not in handoff:
        raise ValueError("Next action mismatch")
    return {"workstream_id": state["workstream_id"], "status": state["status"],
            "human_operator": state["current_human_operator"], "alias": state["operator_alias"],
            "next_action": state["next_action"], "bootstrap_count": len(bootstrap)}


def action_source_available(runtime):
    """Source availability is separate from context recovery and full readiness."""
    return (runtime / BRIEF).is_file()


class OnboardingTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fictional-onboarding-")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "fictional-project"
        self.runtime = initialize_fixture(self.project)

    def test_configured_runtime_and_fresh_process_readback(self):
        from runtime_sync import assess, snapshot
        self.assertEqual(STABLE, load(self.runtime / "framework-lock.json")["stable_pin"])
        manifest = load(self.runtime / "runtime-manifest.json")
        self.assertFalse(manifest["daily_operator_reports"]["required"])
        self.assertEqual({"live_report_cycle": "PENDING", "cross_chat_pilot": "PENDING"},
                         manifest["validation_gates"])
        self.assertFalse((self.project / ".git").exists())
        self.assertNotEqual((ROOT / ".gitignore").read_bytes(),
                            (self.project / ".gitignore").read_bytes())
        before = digest_tree(self.runtime)
        errors, review = assess(snapshot(ROOT), snapshot(self.project))
        self.assertEqual([], errors)
        self.assertTrue(any("Preserve configured file" in line for line in review))
        validator = subprocess.run([sys.executable, str(self.runtime / "scripts/validate_runtime.py")],
                                   capture_output=True, text=True)
        self.assertEqual(0, validator.returncode, validator.stdout + validator.stderr)
        self.assertIn("PASS:", validator.stdout)
        child = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                                "--recover", str(self.runtime)], capture_output=True, text=True)
        self.assertEqual(0, child.returncode, child.stderr)
        result = json.loads(child.stdout)
        self.assertEqual(NEXT, result["next_action"])
        self.assertTrue(action_source_available(self.runtime))
        self.assertEqual(8, result["bootstrap_count"])
        self.assertEqual(WS, result["workstream_id"])
        self.assertEqual(OPERATOR, result["human_operator"])
        self.assertEqual(ALIAS, result["alias"])
        self.assertEqual("ACTIVE", result["status"])
        self.assertEqual(before, digest_tree(self.runtime), "Validation/recovery must be read-only")

    def test_missing_action_source_does_not_imply_lost_context(self):
        (self.runtime / BRIEF).unlink()
        self.assertEqual(NEXT, recover(self.runtime)["next_action"])
        self.assertFalse(action_source_available(self.runtime))

    def test_existing_destination_is_preserved(self):
        before = digest_tree(self.project)
        with self.assertRaises(FileExistsError):
            initialize_fixture(self.project)
        self.assertEqual(before, digest_tree(self.project))

    def test_missing_handoff_blocks_recovery(self):
        (self.runtime / f"workstreams/{WS}/HANDOFF.md").unlink()
        with self.assertRaises(FileNotFoundError):
            recover(self.runtime)

    def test_pin_mismatch_blocks_recovery(self):
        lock_path = self.runtime / "framework-lock.json"
        lock = load(lock_path)
        lock["candidate_pin"] = "c" * 40
        write_json(lock_path, lock)
        with self.assertRaisesRegex(ValueError, "pin mismatch"):
            recover(self.runtime)

    def test_changed_bootstrap_blocks_recovery(self):
        path = self.runtime / "runtime-manifest.json"
        manifest = load(path)
        manifest["bootstrap_files"].reverse()
        write_json(path, manifest)
        with self.assertRaisesRegex(ValueError, "Bootstrap"):
            recover(self.runtime)

    def test_inconsistent_next_action_blocks_recovery(self):
        path = self.runtime / f"workstreams/{WS}/state.json"
        state = load(path)
        state["next_action"] = "An inconsistent action"
        write_json(path, state)
        with self.assertRaisesRegex(ValueError, "Next action"):
            recover(self.runtime)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recover", type=Path)
    parser.add_argument("--stable-pin", help="Optional independently verified local Git commit; uses real HEAD as candidate")
    args = parser.parse_args()
    if args.recover:
        print(json.dumps(recover(args.recover)))
    else:
        if args.stable_pin:
            STABLE = subprocess.check_output(
                ["git", "-C", str(ROOT), "rev-parse", "--verify", args.stable_pin + "^{commit}"],
                text=True).strip()
            CANDIDATE = subprocess.check_output(
                ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
            if not all(re.fullmatch(r"[0-9a-f]{40}", pin) for pin in (STABLE, CANDIDATE)):
                raise SystemExit("Could not verify immutable Git inputs")
            print("Pin mode: verified local Git objects; stable/candidate kept separate", flush=True)
        else:
            print("Pin mode: synthetic test fixtures; no upstream provenance claim", flush=True)
        unittest.main(argv=[sys.argv[0]], verbosity=2)
