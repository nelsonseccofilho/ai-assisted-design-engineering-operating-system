"""Validate generic promotion review evidence; no project data or task mutations."""
from datetime import datetime

MATURITY = {"EXISTING_CORE", "NARROWLY_VERIFIED", "OPERATIONALLY_ADOPTED",
            "PILOT_PENDING", "PROJECT_ONLY"}

def assess(records):
    errors = []
    if not isinstance(records, list):
        return ["Reviews must be a list"]
    seen = set()
    for item in records:
        if not isinstance(item, dict):
            errors.append("Review must be an object")
            continue
        identity = item.get("id")
        if not isinstance(identity, str) or not identity.strip() or identity in seen:
            errors.append("Missing or duplicate review ID")
        if isinstance(identity, str):
            seen.add(identity)
        maturity = item.get("maturity")
        if maturity not in MATURITY:
            errors.append("Unknown maturity")
        for field in ("claim", "scope", "limitations"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append("Missing " + field)
        if item.get("disposition") not in {"REFERENCE_CORE", "CLARIFICATION", "OPTIONAL_PILOT", "EXCLUDE"}:
            errors.append("Unknown public disposition")
        if maturity == "PROJECT_ONLY" and item.get("disposition") != "EXCLUDE":
            errors.append("Project-only material must be excluded")
        if maturity in {"OPERATIONALLY_ADOPTED", "PILOT_PENDING"}:
            if item.get("effectiveness_validated") is not False:
                errors.append("Policy adoption or pending pilot is not effectiveness validation")
            if item.get("disposition") not in {"OPTIONAL_PILOT", "CLARIFICATION"}:
                errors.append("Incomplete method must remain optional or bounded clarification")
        if maturity == "NARROWLY_VERIFIED" or item.get("effectiveness_validated") is True:
            if not item.get("evidence") or not item.get("reviewer") or not item.get("validation_scope"):
                errors.append("Verification requires evidence, reviewer and validation scope")
            try:
                timestamp = datetime.fromisoformat(item.get("verified_at", ""))
                if timestamp.utcoffset() is None:
                    raise ValueError()
            except (ValueError, TypeError):
                errors.append("Verification requires an offset-aware timestamp")
        if item.get("required_bootstrap_change") is not False:
            errors.append("Additive review must preserve mandatory bootstrap")
    return errors
