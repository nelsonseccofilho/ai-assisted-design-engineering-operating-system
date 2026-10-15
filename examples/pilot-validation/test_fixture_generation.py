"""Local regression checks for the optional fictional pilot lab (no network)."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAMEWORK = HERE.parents[1]
GENERATOR = HERE / "create_fixtures.py"
PIN = "30b11995a09e2a86a40e27b193ac9be8b4593333"


def run(argv, cwd=None):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8")


def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class PilotLabTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="fictional-pilot-qa-")
        cls.root = Path(cls.temp.name)
        cls.source = cls.root / "public-framework"
        clone = run(["git", "-c", "core.autocrlf=false", "clone", "--no-hardlinks",
                     "--no-checkout", str(FRAMEWORK), str(cls.source)])
        if clone.returncode:
            raise RuntimeError(clone.stderr)
        checkout = run(["git", "-c", "core.autocrlf=false", "-C", str(cls.source),
                        "checkout", "--detach", PIN])
        if checkout.returncode:
            raise RuntimeError(checkout.stderr)
        # Synthetic ignored input models the privacy boundary without real data.
        with (cls.source / ".git/info/exclude").open("a", encoding="utf-8") as stream:
            stream.write("\n/runtime/ignored-fixture.txt\n")
        (cls.source / "runtime/ignored-fixture.txt").write_text(
            "SYNTHETIC-EXCLUDED-MARKER", encoding="utf-8")
        cls.good = cls.root / "good-lab"
        generated = run([sys.executable, "-X", "utf8", str(GENERATOR),
                         str(cls.good), "--framework", str(cls.source)])
        if generated.returncode:
            raise RuntimeError(generated.stderr)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def generate(self, destination, source=None):
        return run([sys.executable, "-X", "utf8", str(GENERATOR), str(destination),
                    "--framework", str(source or self.source)])

    def test_ignored_material_excluded_and_pinned_seed_preserved(self):
        before = hashes(self.source / "runtime")
        pinned = subprocess.check_output(
            ["git", "-C", str(self.source), "show",
             PIN + ":runtime/10_PROMPT_OPERACIONAL_MASTER.md"])
        for reviewer in ("reviewer-a", "reviewer-b"):
            project = self.good / reviewer
            self.assertFalse((project / "runtime/ignored-fixture.txt").exists())
            self.assertEqual((project / "runtime/10_PROMPT_OPERACIONAL_MASTER.md").read_bytes(),
                             pinned)
            self.assertEqual(run(["git", "status", "--porcelain"], project).stdout, "")
        self.assertEqual(hashes(self.source / "runtime"), before)

    def test_existing_destination_is_preserved(self):
        destination = self.root / "existing"
        destination.mkdir()
        sentinel = destination / "sentinel.txt"
        sentinel.write_text("preserve", encoding="utf-8")
        self.assertNotEqual(self.generate(destination).returncode, 0)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")
        self.assertEqual(list(destination.iterdir()), [sentinel])

    def test_destination_inside_framework_is_refused(self):
        destination = self.source / "nested-lab"
        before = hashes(self.source / "runtime")
        result = self.generate(destination)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("outside the framework", result.stderr)
        self.assertFalse(destination.exists())
        self.assertEqual(hashes(self.source / "runtime"), before)

    def test_changed_seed_refused_before_output(self):
        seed = self.source / "runtime/10_PROMPT_OPERACIONAL_MASTER.md"
        original = seed.read_bytes()
        destination = self.root / "dirty-lab"
        try:
            seed.write_bytes(original + b"\nSynthetic local change\n")
            result = self.generate(destination)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("differs from the pinned", result.stderr)
            self.assertFalse(destination.exists())
        finally:
            seed.write_bytes(original)

    def test_untracked_seed_refused_before_output(self):
        seed = self.source / "runtime/not-ignored-fixture.txt"
        destination = self.root / "untracked-lab"
        try:
            seed.write_text("synthetic", encoding="utf-8")
            result = self.generate(destination)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Untracked runtime", result.stderr)
            self.assertFalse(destination.exists())
        finally:
            seed.unlink()

    def test_reader_receipts_and_source_preservation(self):
        project = self.good / "reviewer-a"
        before = hashes(project / "runtime")
        reader = project / "read_material.py"
        for args in (["manifest"], ["bootstrap"], ["state", "GARDEN"],
                     ["list", "GARDEN"], ["read", "GARDEN", "01-brief.md"],
                     ["complete", "GARDEN"]):
            result = run([sys.executable, "-X", "utf8", str(reader)] + args)
            self.assertEqual(result.returncode, 0, result.stderr)
        rejected = run([sys.executable, "-X", "utf8", str(reader), "read",
                        "GARDEN", "../SKY/01-brief.md"])
        self.assertNotEqual(rejected.returncode, 0)
        receipts = [json.loads(line) for line in
                    (project / "receipts.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual([r["operation"] for r in receipts],
                         ["manifest", "bootstrap", "state", "list", "read", "complete"])
        self.assertEqual(len(receipts[1]["paths"]), 8)
        self.assertEqual(hashes(project / "runtime"), before)
        self.assertEqual(run(["git", "status", "--porcelain"], project).stdout, "")

    def test_manifest_mismatch_rejected_with_optimization(self):
        project = self.good / "reviewer-b"
        manifest = project / "runtime/runtime-manifest.json"
        original = manifest.read_bytes()
        try:
            data = json.loads(original)
            data["runtime_name"] = "Synthetic changed manifest"
            manifest.write_text(json.dumps(data), encoding="utf-8")
            result = run([sys.executable, "-X", "utf8", "-O",
                          str(project / "read_material.py"), "manifest"])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Canonical manifest differs", result.stderr)
        finally:
            manifest.write_bytes(original)

    def test_framework_subdirectory_is_refused(self):
        destination = self.root / "non-root-lab"
        result = self.generate(destination, self.source / "runtime")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("repository root", result.stderr)
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
