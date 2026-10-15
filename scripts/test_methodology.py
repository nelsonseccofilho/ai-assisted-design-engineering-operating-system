"""Promotion maturity and complete-QA negative regressions. Standard library only."""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from promotion_review import assess

ROOT = Path(__file__).resolve().parents[1]
records = json.loads((ROOT / "examples/promotion-cases.json").read_text(encoding="utf-8"))
cases = 0

def check(condition):
    global cases
    cases += 1
    assert condition

check(not assess(records))
for index in (1, 2):
    broken = copy.deepcopy(records)
    broken[index]["effectiveness_validated"] = True
    check(bool(assess(broken)))
broken = copy.deepcopy(records)
broken[3]["disposition"] = "CLARIFICATION"
check(bool(assess(broken)))
for field in ("evidence", "reviewer", "validation_scope", "limitations"):
    broken = copy.deepcopy(records)
    broken[0].pop(field)
    check(bool(assess(broken)))
broken = copy.deepcopy(records)
broken[0]["verified_at"] = "2026-01-01T12:00:00"
check(bool(assess(broken)))
broken = copy.deepcopy(records)
broken[2]["required_bootstrap_change"] = True
check(bool(assess(broken)))
broken = copy.deepcopy(records)
broken[2]["maturity"] = "VALIDATED_BY_APPROVAL"
check(bool(assess(broken)))
check(bool(assess(records + [records[0]])))
check(bool(assess({})))

# Reproduce a failure only in the final startup gate. Do not change real sources.
# A temporary copy of the validator overrides read() for one late check only;
# its __file__ still points at the real package, so every other gate is real.
source = (ROOT / "scripts/validate_framework.py").read_text(encoding="utf-8")
needle = "check(\"START_NEW_PROJECT\" in read(\"README.md\"), \"README missing new-project example\")"
check(source.count(needle) == 1)
source = source.replace(needle, "check(False, \"injected final-gate regression\")")
with tempfile.TemporaryDirectory(prefix="complete-qa-") as directory:
    harness = Path(directory) / "run.py"
    target = str(ROOT / "scripts/validate_framework.py")
    harness.write_text("import sys\nsys.path.insert(0, " + repr(str(ROOT / "scripts")) +
                       ")\nexec(compile(" + repr(source) + ", " + repr(target) +
                       ", 'exec'), {'__file__': " + repr(target) + "})\n", encoding="utf-8")
    result = subprocess.run([sys.executable, str(harness)], capture_output=True, text=True)
check(result.returncode != 0)
check("FAIL: injected final-gate regression" in result.stdout)
check("PASS:" not in result.stdout)
print(f"PASS: {cases} methodology and final-gate regression checks")
