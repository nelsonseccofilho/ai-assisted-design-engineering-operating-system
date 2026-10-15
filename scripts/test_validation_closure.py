"""Negative policy-integration regressions; no AI/human efficacy claim."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from validation_contract import assess_validation_contract

ROOT = Path(__file__).resolve().parents[1]
derivative = json.loads((ROOT / "prompt-operacional.json").read_text(encoding="utf-8"))
master = (ROOT / "PROMPT_OPERACIONAL_MASTER.md").read_text(encoding="utf-8")
contract = (ROOT / "runtime/docs/contracts/VALIDATION_AND_CLOSURE.md").read_text(encoding="utf-8")
seed = (ROOT / "runtime/docs/templates/ACCEPTANCE_CASES.md").read_text(encoding="utf-8")
checks = 0


def check(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError("GOV-VAL-001 regression failed")


def assess(data, **overrides):
    return assess_validation_contract(data, overrides.get("master", master),
                                      overrides.get("contract", contract), overrides.get("seed", seed))


check(not assess(derivative))
broken = copy.deepcopy(derivative)
broken.pop("validation_and_closure")
check(bool(assess(broken)))
for field, value in [("mandatory", False), ("acceptance_before_testing", False),
                     ("required_checks_precede_closure", False),
                     ("cost_waives_mandatory_checks", True), ("agent_may_lower_criteria", True),
                     ("changes_runtime_states", True), ("closure_implies_publication_authority", True),
                     ("evidence_reuse_requires", ["scope"]), ("test_categories", ["OPTIONAL"]),
                     ("assessment_outcomes", ["FINAL"]), ("mandatory", 1)]:
    broken = copy.deepcopy(derivative)
    broken["validation_and_closure"][field] = value
    check(bool(assess(broken)))
broken = copy.deepcopy(derivative)
broken["operational_states"].append("COMPLETED_WITH_CAVEATS")
check(bool(assess(broken)))
check(bool(assess(derivative, master=master.replace("GOV-VAL-001", "removed"))))
check(bool(assess(derivative, contract=contract.replace("Safeguards and exceptions", "removed"))))
check(bool(assess(derivative, seed=seed.replace("GOV-VAL-001", "removed"))))

# A weakened cost safeguard must fail the actual package validator before PASS.
source_path = ROOT / "scripts/validate_framework.py"
source = source_path.read_text(encoding="utf-8")
needle = 'derivative = json.loads(read("prompt-operacional.json"))'
check(source.count(needle) == 1)
source = source.replace(needle, needle + '\nderivative["validation_and_closure"]["cost_waives_mandatory_checks"] = True')
with tempfile.TemporaryDirectory(prefix="gov-val-gate-") as directory:
    harness = Path(directory) / "run.py"
    harness.write_text("import sys\nsys.path.insert(0, " + repr(str(ROOT / "scripts")) +
                       ")\nexec(compile(" + repr(source) + ", " + repr(str(source_path)) +
                       ", 'exec'), {'__file__': " + repr(str(source_path)) + "})\n", encoding="utf-8")
    result = subprocess.run([sys.executable, str(harness)], capture_output=True, text=True)
check(result.returncode != 0)
check("cost_waives_mandatory_checks" in result.stdout)
check("PASS:" not in result.stdout)
print(f"PASS: {checks} GOV-VAL-001 policy-integration regressions")
