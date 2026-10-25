"""Static integration guards for GOV-VAL-001; no runtime acceptance engine."""

POLICY_ID = "GOV-VAL-001"
CONTRACT = "runtime/docs/contracts/VALIDATION_AND_CLOSURE.md"
CATEGORIES = ["MANDATORY", "CONDITIONAL", "OPTIONAL", "REDUNDANT"]
OUTCOMES = ["COMPLETED", "COMPLETED_WITH_CAVEATS", "BLOCKED"]
VALIDITY = ["scope", "source_revision_or_content", "environment", "dependencies", "no_material_invalidation"]


def assess_validation_contract(derivative, master, contract, seed):
    errors = []
    policy = derivative.get("validation_and_closure")
    if not isinstance(policy, dict):
        return ["Missing GOV-VAL-001 policy"]
    expected = {"id": POLICY_ID, "decision": "ADR-0029", "contract": CONTRACT,
                "mandatory": True, "acceptance_before_testing": True,
                "required_checks_precede_closure": True,
                "cost_waives_mandatory_checks": False,
                "agent_may_lower_criteria": False,
                "changes_runtime_states": False,
                "closure_implies_publication_authority": False,
                "test_categories": CATEGORIES, "assessment_outcomes": OUTCOMES,
                "evidence_reuse_requires": VALIDITY}
    for key, value in expected.items():
        if type(policy.get(key)) is not type(value) or policy.get(key) != value:
            errors.append("GOV-VAL-001 incompatible policy: " + key)
    if POLICY_ID not in master or CONTRACT not in master:
        errors.append("Master does not expose GOV-VAL-001")
    states = derivative.get("operational_states", [])
    if any(value in states for value in OUTCOMES[:2]):
        errors.append("Closure outcomes must not extend runtime states")
    for token in [POLICY_ID, "Acceptance before testing", "Test categories and evidence reuse",
                  "Evidence-based closure", "Safeguards and exceptions",
                  "AI responsibility and continuous improvement"]:
        if token not in contract:
            errors.append("Missing GOV-VAL-001 contract section: " + token)
    # Mandatory documented policy, not a runtime agent.
    marker = "## 3A. Parent-deliverable gate: prevent circular tests and PRs"
    end = "## 4. Evidence-based closure"

    if (
        contract.count(marker) != 1
        or contract.count(end) != 1
        or contract.index(marker) >= contract.index(end)
    ):
        errors.append(
            "Missing or misplaced GOV-VAL-001 parent-deliverable gate"
        )
    else:
        gate = contract.split(marker, 1)[1].split(end, 1)[0]
        requirements = {
            "parent objective": "accountable parent objective",
            "progress": "accepted parent outcomes separately from intermediate milestones",
            "mandatory": "Perform every applicable MANDATORY check",
            "conditional": "triggered CONDITIONAL check",
            "reuse": "Reuse still-valid exact-source/environment evidence",
            "material change": "only for a bounded, owned material change",
            "authority": "separate human integration authority",
            "closure": "required owner acceptance and independent target readback",
            "loop trigger": "two consecutive discretionary iterations",
            "loop response": "Stop speculative test/PR preparation",
            "security": "do not retry by another tool",
            "no duplicate ledger": "do not create a parallel anti-loop register",
        }
        for name, required_text in requirements.items():
            if required_text not in gate:
                errors.append(
                    "Missing GOV-VAL-001 parent-deliverable safeguard: " + name
                )
    if POLICY_ID not in seed:
        errors.append("Acceptance seed does not reference GOV-VAL-001")
    return errors
