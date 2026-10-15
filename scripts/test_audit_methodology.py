"""Negative coverage checks. Fixtures are fictional and contain no private sources."""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from audit_methodology import assess_catalog, assess_source_coverage

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "docs/methodology-catalog.json").read_text(encoding="utf-8"))
paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file()}
checks = 0
def check(ok):
    global checks
    checks += 1
    assert ok

check(not assess_catalog(catalog, paths))
for field, value in [("id", ""), ("targets", ["missing.md"]), ("targets", ["../outside.md"]),
                     ("claim", "ALL_LIVE_PILOTS_PASSED"), ("release_status", "RELEASED"),
                     ("validation_scope", ""), ("maturity", "PROJECT_ONLY"),
                     ("title", "https://example.invalid/private-source")]:
    broken = copy.deepcopy(catalog)
    broken["entries"][0][field] = value
    check(bool(assess_catalog(broken, paths)))
broken = copy.deepcopy(catalog)
broken["entries"].append(copy.deepcopy(broken["entries"][0]))
check(bool(assess_catalog(broken, paths)))
broken = copy.deepcopy(catalog)
broken["entries"][0]["source_path"] = "fictional-private-record"
check(bool(assess_catalog(broken, paths)))
pins = {"private": "a" * 40, "candidate": "b" * 40, "stable": "c" * 40}
inventory = {"pins": pins, "private": [{"path": "fictional/source.md", "sha": "d" * 40}]}
ledger = {"pins": pins, "files": [{"path": "fictional/source.md", "blob_sha": "d" * 40,
          "disposition": "METHOD_EVIDENCE", "method_ids": ["METH-004"],
          "review_level": "CONTENT_SCREEN_AND_CONTEXTUAL_FAMILY_REVIEW", "exclusion_reason": ""}]}
check(not assess_source_coverage(inventory, ledger, catalog))
for field, value in [("blob_sha", "e" * 40), ("method_ids", ["METH-999"]),
                     ("disposition", "EXCLUDED_PRIVATE"), ("review_level", "ALL_ORIGINAL_MEDIA_REPLAYED")]:
    broken = copy.deepcopy(ledger)
    broken["files"][0][field] = value
    check(bool(assess_source_coverage(inventory, broken, catalog)))
broken = copy.deepcopy(ledger)
broken["files"] = []
check(bool(assess_source_coverage(inventory, broken, catalog)))
broken = copy.deepcopy(ledger)
broken["files"].append(copy.deepcopy(broken["files"][0]))
check(bool(assess_source_coverage(inventory, broken, catalog)))
broken = copy.deepcopy(ledger)
broken["pins"] = {"private": "e" * 40}
check(bool(assess_source_coverage(inventory, broken, catalog)))
# Regression: a final runtime startup failure must not be printed after PASS.
source_path = ROOT / "runtime/scripts/validate_runtime.py"
source = source_path.read_text(encoding="utf-8")
needle = 'check((ROOT / "compat/ALIASES.local.md").is_file(), "Missing compatibility alias registry")'
check(source.count(needle) == 1)
source = source.replace(needle, 'check(False, "injected runtime final gate")')
with tempfile.TemporaryDirectory(prefix="runtime-final-gate-") as directory:
    harness = Path(directory) / "run.py"
    harness.write_text("exec(compile(" + repr(source) + ", " + repr(str(source_path)) +
                       ", 'exec'), {'__file__': " + repr(str(source_path)) + "})", encoding="utf-8")
    result = subprocess.run([sys.executable, str(harness)], capture_output=True, text=True)
check(result.returncode != 0)
check("FAIL: injected runtime final gate" in result.stdout)
check("PASS:" not in result.stdout)

print(f"PASS: {checks} methodology catalog and restricted coverage checks")
