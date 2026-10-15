"""Mechanical regressions for the retrieval protocol; no AI or human trial is run."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("comparison", HERE / "comparison.py")
comparison = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comparison)


class ComparisonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="retrieval-comparison-qa-")
        cls.root = Path(cls.temp.name)
        cls.lab = cls.root / "laboratory"
        cls.prepared = comparison.prepare(cls.lab, HERE.parents[1])
        cls.records = comparison.load(cls.lab / "run-records.json")
        cls.quality = comparison.load(cls.lab / "quality-review.json")
        cls.frozen = comparison.load(cls.lab / "coordinator.json")

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        for row in comparison.plan()["sessions"]:
            (self.lab / row["id"] / "receipts.jsonl").unlink(missing_ok=True)
        comparison.save(self.lab / "run-records.json", copy.deepcopy(self.records))
        comparison.save(self.lab / "quality-review.json", copy.deepcopy(self.quality))
        comparison.save(self.lab / "coordinator.json", copy.deepcopy(self.frozen))

    def trace(self, sid="SP01", use_index=False, repeat_bootstrap=False, search_before_docs=False):
        row = next(r for r in comparison.plan()["sessions"] if r["id"] == sid)
        room = self.lab / sid
        def read(*args):
            result = subprocess.run([sys.executable, "-X", "utf8",
                str(room / "read_material.py"), *args], capture_output=True,
                text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
        read("manifest")
        read("bootstrap")
        if repeat_bootstrap:
            read("bootstrap")
        for case in row["order"]:
            read("state", case)
            read("list", case)
            if search_before_docs:
                read("search", case, "unmatched-synthetic-search-token")
            if use_index and row["conditions"][case] == "INDEX":
                read("read", case, "INDEX.md")
            for filename in ("01-brief.md", "02-accepted-decision.md",
                             "04-component-source.md", "06-requirement-gaps.md"):
                read("read", case, filename)
            read("complete", case)
        records = copy.deepcopy(self.records)
        records[sid]["run_kind"] = "MECHANICAL_DRY_RUN"
        comparison.save(self.lab / "run-records.json", records)

    def receipts(self, sid):
        path = self.lab / sid / "receipts.jsonl"
        return path, [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def write_receipts(self, path, rows):
        path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

    def test_plan_balances_case_order_and_index_availability(self):
        protocol = comparison.plan()
        self.assertEqual(len(protocol["sessions"]), 8)
        self.assertEqual(protocol["planned_case_observations"], 16)
        self.assertEqual(self.prepared["actual_independent_sessions"], 0)
        for row in protocol["sessions"]:
            room = self.lab / row["id"]
            for case, condition in row["conditions"].items():
                self.assertEqual((room / f"runtime/evidence/pilot-cases/{case}/INDEX.md").exists(),
                                 condition == "INDEX")
            task = (room / "TASK.md").read_text(encoding="utf-8")
            self.assertEqual("consult it before" in task, row["regime"] == "guided")

    def test_unexecuted_plan_has_no_measured_benefit(self):
        result = comparison.summarize(self.lab)
        self.assertEqual(result["efficacy_status"], "NOT_RUN")
        self.assertEqual(result["declared_independent_sessions"], 0)
        self.assertEqual(len(result["observations"]), 16)
        self.assertTrue(all(not r["has_receipts"] and not r["comparison_eligible"]
                            for r in result["observations"]))
        self.assertTrue(all(g["mean_source_bytes"] is None for g in result["groups"]))
        self.assertIsNone(result["financial_savings"])
        self.assertIsNone(result["token_consumption"])

    def test_mechanical_spontaneous_trace_does_not_count_as_trial(self):
        self.trace()
        result = comparison.summarize(self.lab)
        observed = [r for r in result["observations"] if r["session"] == "SP01"]
        self.assertTrue(all(not r["protocol_errors"] for r in observed))
        self.assertTrue(all(not r["index_consulted"] for r in observed))
        self.assertTrue(all(r["source_bytes_inspected"] > 0 for r in observed))
        self.assertEqual(result["mechanical_sessions"], 1)
        self.assertEqual(result["declared_independent_sessions"], 0)
        self.assertEqual(result["efficacy_status"], "NOT_RUN")
        self.assertTrue(all(not r["comparison_eligible"] for r in observed))
        overhead = [r for r in result["session_overhead"] if r["session"] == "SP01"]
        self.assertEqual(len(overhead), 1)
        self.assertEqual(overhead[0]["bootstrap_invocations"], 1)

    def test_guided_trace_requires_index_before_case_documents(self):
        self.trace("GD01")
        result = comparison.summarize(self.lab)
        garden = next(r for r in result["observations"] if r["session"] == "GD01" and r["case"] == "GARDEN")
        self.assertIn("guided index consultation missing or late", garden["protocol_errors"])

    def test_guided_trace_accepts_first_index_and_preserves_source(self):
        self.trace("GD01", use_index=True)
        result = comparison.summarize(self.lab)
        rows = [r for r in result["observations"] if r["session"] == "GD01"]
        self.assertTrue(all(not r["protocol_errors"] and r["source_integrity"] for r in rows))
        self.assertTrue(next(r for r in rows if r["condition"] == "INDEX")["index_consulted"])
        self.assertTrue(all(r["quality"] == "NOT_REVIEWED" and not r["comparison_eligible"] for r in rows))

    def test_missing_bootstrap_blocks_comparison(self):
        self.trace()
        path, rows = self.receipts("SP01")
        self.write_receipts(path, [r for r in rows if r["operation"] != "bootstrap"])
        result = comparison.summarize(self.lab)
        rows = [r for r in result["observations"] if r["session"] == "SP01"]
        self.assertTrue(all("mandatory bootstrap missing before case reads" in r["protocol_errors"] for r in rows))

    def test_negative_bytes_are_rejected(self):
        self.trace()
        path, rows = self.receipts("SP01")
        rows[0]["bytes_inspected"] = -1
        self.write_receipts(path, rows)
        with self.assertRaisesRegex(ValueError, "byte counts"):
            comparison.summarize(self.lab)

    def test_case_order_or_repeated_completion_is_flagged(self):
        self.trace()
        path, rows = self.receipts("SP01")
        duplicate = copy.deepcopy(next(r for r in rows if r["operation"] == "complete"))
        duplicate["at"] = rows[-1]["at"]
        rows.append(duplicate)
        self.write_receipts(path, rows)
        result = comparison.summarize(self.lab)
        garden = next(r for r in result["observations"] if r["session"] == "SP01" and r["case"] == "GARDEN")
        self.assertIn("case order incomplete or interleaved", garden["protocol_errors"])
        self.assertIn("case completion missing or repeated", garden["protocol_errors"])

    def test_prior_exposure_excludes_even_manually_passed_quality(self):
        self.trace()
        records = comparison.load(self.lab / "run-records.json")
        records["SP01"].update(run_kind="INDEPENDENT_SESSION", participant_type="AI",
            independent=True, prior_case_exposure=True, independence_evidence="Synthetic regression only")
        comparison.save(self.lab / "run-records.json", records)
        quality = copy.deepcopy(self.quality)
        for grade in quality["SP01"].values():
            grade.update(reviewer_role="Synthetic test role", evidence_note="Not actual assessment",
                         **{check: True for check in comparison.CHECKS})
        comparison.save(self.lab / "quality-review.json", quality)
        result = comparison.summarize(self.lab)
        rows = [r for r in result["observations"] if r["session"] == "SP01"]
        self.assertTrue(all(r["quality"] == "PASS" and not r["comparison_eligible"] for r in rows))
        self.assertEqual(result["declared_independent_sessions"], 0)

    def test_source_mutation_blocks_acceptance(self):
        self.trace()
        task = self.lab / "SP01/TASK.md"
        original = task.read_bytes()
        try:
            task.write_bytes(original + b"\nSynthetic mutation\n")
            result = comparison.summarize(self.lab)
            rows = [r for r in result["observations"] if r["session"] == "SP01"]
            self.assertTrue(all(not r["source_integrity"] and not r["comparison_eligible"] for r in rows))
        finally:
            task.write_bytes(original)

    def test_existing_destination_is_preserved(self):
        before = (self.lab / "coordinator.json").read_bytes()
        with self.assertRaisesRegex(ValueError, "preserved"):
            comparison.prepare(self.lab, HERE.parents[1])
        self.assertEqual((self.lab / "coordinator.json").read_bytes(), before)

    def test_explicit_review_enables_only_declared_observations(self):
        self.trace()
        records = copy.deepcopy(self.records)
        records["SP01"].update(run_kind="INDEPENDENT_SESSION", participant_type="AI",
            independent=True, prior_case_exposure=False,
            independence_evidence="Synthetic positive-path test; no actual session")
        comparison.save(self.lab / "run-records.json", records)
        quality = copy.deepcopy(self.quality)
        for grade in quality["SP01"].values():
            grade.update(reviewer_role="Synthetic test role", evidence_note="Synthetic review fields",
                         **{check: True for check in comparison.CHECKS})
        comparison.save(self.lab / "quality-review.json", quality)
        result = comparison.summarize(self.lab)
        self.assertEqual(result["eligible_case_observations"], 2)
        self.assertFalse(result["balanced_design_complete"])
        self.assertFalse(result["automatic_savings_or_promotion_claim"])
        for group in result["groups"]:
            selected = [r for r in result["observations"] if r["comparison_eligible"]
                and (r["regime"], r["case"], r["condition"]) ==
                    (group["regime"], group["case"], group["condition"])]
            self.assertEqual(group["eligible_observations"], len(selected))
            if selected:
                self.assertEqual(group["mean_source_bytes"], selected[0]["source_bytes_inspected"])

    def test_repeated_bootstrap_is_not_omitted_or_double_counted(self):
        self.trace(repeat_bootstrap=True)
        result = comparison.summarize(self.lab)
        _, receipts = self.receipts("SP01")
        expected = sum(r["bytes_inspected"] for r in receipts if r["case"] is None)
        overhead = next(r for r in result["session_overhead"] if r["session"] == "SP01")
        self.assertEqual(overhead["source_bytes_inspected"], expected)
        self.assertEqual(overhead["bootstrap_invocations"], 2)
        self.assertEqual(len(result["session_overhead"]), 8)
        observed = [r for r in result["observations"] if r["session"] == "SP01"]
        for row in observed:
            self.assertEqual(row["source_bytes_inspected"],
                sum(r["bytes_inspected"] for r in receipts if r["case"] == row["case"]))

    def test_search_inspection_is_not_index_consultation(self):
        self.trace(search_before_docs=True)
        result = comparison.summarize(self.lab)
        garden = next(r for r in result["observations"] if r["session"] == "SP01" and r["case"] == "GARDEN")
        self.assertFalse(garden["index_consulted"])
        self.assertTrue(garden["index_inspected"])
        self.assertFalse(garden["protocol_errors"])

    def test_guided_search_before_index_is_late_consultation(self):
        self.trace("GD01", use_index=True, search_before_docs=True)
        result = comparison.summarize(self.lab)
        garden = next(r for r in result["observations"] if r["session"] == "GD01" and r["case"] == "GARDEN")
        self.assertTrue(garden["index_consulted"])
        self.assertTrue(garden["index_inspected"])
        self.assertIn("guided index consultation missing or late", garden["protocol_errors"])

    def test_protocol_metadata_matches_implemented_design(self):
        original = comparison.plan()
        for key, changed in (("planned_independent_sessions", 9),
                             ("planned_case_observations", 18),
                             ("required_quality_checks", comparison.CHECKS[:-1]),
                             ("framework_version", "4.0.0")):
            altered = copy.deepcopy(original)
            altered[key] = changed
            with self.subTest(key=key), patch.object(comparison, "load", return_value=altered):
                with self.assertRaisesRegex(ValueError, "metadata differs"):
                    comparison.plan()

    def test_changed_frozen_protocol_is_rejected(self):
        frozen = copy.deepcopy(self.frozen)
        frozen["protocol"]["status"] = "ALTERED"
        comparison.save(self.lab / "coordinator.json", frozen)
        with self.assertRaisesRegex(ValueError, "Frozen"):
            comparison.summarize(self.lab)


if __name__ == "__main__":
    unittest.main(verbosity=2)
