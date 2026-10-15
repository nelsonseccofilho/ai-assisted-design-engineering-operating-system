"""Execute the predeclared fictional acceptance cases in fresh temporary databases."""
import hashlib
from contextlib import closing
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from local_mvp import Actor, Denied, InjectedFailure, Invalid, act, initialize, read_card

HERE = Path(__file__).resolve().parent
PLAN = json.loads((HERE / "acceptance.json").read_text(encoding="utf-8"))
EDITOR = Actor("fixture-editor", "EDITOR", "ALPHA")
REVIEWER = Actor("fixture-reviewer", "REVIEWER", "ALPHA")
READER = Actor("fixture-reader", "READER", "ALPHA")


class FunctionalCases(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fictional-functional-")
        self.db = Path(self.temp.name) / "fictional.sqlite"
        initialize(self.db)

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self):
        with closing(sqlite3.connect(self.db)) as connection:
            return {name: connection.execute("SELECT * FROM " + name + " ORDER BY 1").fetchall()
                    for name in ("cards", "approvals", "events")}

    def unchanged_after(self, error, function, *args, **kwargs):
        before = self.snapshot()
        with self.assertRaises(error):
            function(*args, **kwargs)
        self.assertEqual(before, self.snapshot())

    def approve(self):
        act(self.db, REVIEWER, "approve", "CARD-A")

    def test_F01_allowed_rename(self):
        result = act(self.db, EDITOR, "rename", "CARD-A", "New fictional title")
        self.assertEqual((result["title"], result["revision"]), ("New fictional title", 2))
        self.assertEqual(len(self.snapshot()["events"]), 1)

    def test_F02_reader_denial(self):
        self.unchanged_after(Denied, act, self.db, READER, "rename", "CARD-A", "Forbidden")

    def test_F03_scope_isolation(self):
        self.unchanged_after(Denied, read_card, self.db, READER, "CARD-B")
        self.unchanged_after(Denied, act, self.db, EDITOR, "rename", "CARD-B", "Forbidden")

    def test_F04_missing_approval(self):
        self.unchanged_after(Denied, act, self.db, EDITOR, "publish", "CARD-A")

    def test_F05_reviewed_publication(self):
        self.approve()
        self.assertEqual(act(self.db, EDITOR, "publish", "CARD-A")["status"], "PUBLISHED")
        self.assertEqual(len(self.snapshot()["events"]), 2)

    def test_F06_editor_cannot_approve(self):
        self.unchanged_after(Denied, act, self.db, EDITOR, "approve", "CARD-A")

    def test_F07_stale_approval(self):
        self.approve()
        result = act(self.db, EDITOR, "rename", "CARD-A", "New revision")
        self.assertFalse(result["current_approval"])
        self.unchanged_after(Denied, act, self.db, EDITOR, "publish", "CARD-A")

    def test_F08_invalid_input(self):
        for title in ("  ", "x" * 81):
            with self.subTest(length=len(title)):
                self.unchanged_after(Invalid, act, self.db, EDITOR, "rename", "CARD-A", title)

    def test_F09_atomic_rollback_and_recovery(self):
        self.approve()
        self.unchanged_after(InjectedFailure, act, self.db, EDITOR, "publish", "CARD-A", inject_failure=True)
        self.assertEqual(act(self.db, EDITOR, "publish", "CARD-A")["status"], "PUBLISHED")
        self.assertEqual(len(self.snapshot()["events"]), 2)

    def test_F10_fresh_process_persistence(self):
        act(self.db, EDITOR, "rename", "CARD-A", "Persisted fictional title")
        self.approve()
        act(self.db, EDITOR, "publish", "CARD-A")
        result = subprocess.run([sys.executable, "-X", "utf8", str(HERE / "local_mvp.py"),
            "--db", str(self.db), "show", "CARD-A", "--actor", READER.alias,
            "--role", READER.role, "--scope", READER.scope], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        value = json.loads(result.stdout)
        self.assertEqual((value["title"], value["revision"], value["status"]),
                         ("Persisted fictional title", 2, "PUBLISHED"))
        self.assertTrue(value["current_approval"])

    def test_F11_invalid_actor(self):
        self.unchanged_after(Denied, act, self.db, Actor("fixture", "UNKNOWN", "ALPHA"), "publish", "CARD-A")
        self.unchanged_after(Invalid, act, self.db, Actor("", "EDITOR", "ALPHA"), "publish", "CARD-A")

    def test_F12_existing_destination(self):
        original = self.db.read_bytes()
        with self.assertRaises(FileExistsError):
            initialize(self.db)
        self.assertEqual(self.db.read_bytes(), original)

    def test_F13_unknown_action(self):
        self.unchanged_after(Invalid, act, self.db, EDITOR, "unknown", "CARD-A")

    def test_F14_published_state(self):
        self.approve()
        act(self.db, EDITOR, "publish", "CARD-A")
        self.unchanged_after(Invalid, act, self.db, EDITOR, "rename", "CARD-A", "Forbidden")

    def test_F15_unrelated_record_preserved(self):
        actor = Actor("fixture-beta-reader", "READER", "BETA")
        original = read_card(self.db, actor, "CARD-B")
        self.approve()
        act(self.db, EDITOR, "publish", "CARD-A")
        self.assertEqual(original, read_card(self.db, actor, "CARD-B"))


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.outcomes = {}

    def addSuccess(self, test):
        super().addSuccess(test)
        self.outcomes[test._testMethodName.split("_")[1]] = "PASS"

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.outcomes[test._testMethodName.split("_")[1]] = "FAIL"

    def addError(self, test, err):
        super().addError(test, err)
        self.outcomes[test._testMethodName.split("_")[1]] = "ERROR"


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FunctionalCases)
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult).run(suite)
    complete = set(result.outcomes) == set(PLAN["required_cases"])
    passed = result.wasSuccessful() and complete and result.testsRun == len(PLAN["required_cases"])
    report = {"protocol_id": PLAN["protocol_id"], "execution_kind": "SYNTHETIC_LOCAL_FUNCTIONAL",
        "test_count": result.testsRun, "required_cases_complete": complete,
        "cases": result.outcomes, "pass": passed,
        "source_normalization": "UTF-8 LF",
        "source_sha256": {name: hashlib.sha256((HERE / name).read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")).hexdigest()
                          for name in ("acceptance.json", "local_mvp.py", "test_local_mvp.py")},
        "humans": 0, "actor_context": "TRUSTED_FICTIONAL_INPUT",
        "production_authentication_validated": False, "human_acceptance": False,
        "private_product_validated": False, "external_publication": False,
        "native_editor_validated": False, "delivery_efficiency_demonstrated": False,
        "general_pilot_promotion": False}
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if passed else 1)
