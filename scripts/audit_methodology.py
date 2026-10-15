"""Read-only generic catalog and optional restricted source-coverage QA."""
import argparse
import json
import re
from pathlib import Path

DISPOSITIONS = {"EXISTING_CORE", "CANDIDATE_PROCEDURE", "OPTIONAL_PILOT", "CONFIGURABLE", "EXCLUDED_PRIVATE"}
MATURITY = {"EXISTING_CORE", "OPERATIONALLY_ADOPTED", "NARROWLY_VERIFIED", "PILOT_PENDING", "PROJECT_ONLY"}
FIELDS = {"id", "title", "disposition", "maturity", "targets", "validation_scope", "claim", "release_status", "origin"}

def assess_catalog(catalog, framework):
    errors = []
    if not isinstance(catalog, dict) or catalog.get("schema_version") != "1.0":
        return ["Unsupported methodology catalog"]
    entries = catalog.get("entries")
    if not isinstance(entries, list) or not entries:
        return ["Catalog needs entries"]
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("Catalog entry must be an object")
            continue
        identity = entry.get("id")
        if not isinstance(identity, str) or not re.fullmatch(r"METH-[0-9]{3}", identity) or identity in seen:
            errors.append("Missing or duplicate methodology ID")
        if isinstance(identity, str):
            seen.add(identity)
        if set(entry) != FIELDS:
            errors.append("Unexpected public catalog fields")
        for field in ("title", "validation_scope"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append("Missing " + field)
        if entry.get("origin") not in {"EXISTING_PUBLIC_CORE", "PRIVATE_DOCUMENT_REVIEW", "USER_REQUEST"}:
            errors.append("Missing methodology origin")
        disposition, maturity = entry.get("disposition"), entry.get("maturity")
        if disposition not in DISPOSITIONS or maturity not in MATURITY:
            errors.append("Unsupported disposition or maturity")
        if (disposition == "EXISTING_CORE") != (maturity == "EXISTING_CORE"):
            errors.append("Existing-core classification mismatch")
        if (disposition == "EXCLUDED_PRIVATE") != (maturity == "PROJECT_ONLY"):
            errors.append("Private exclusion classification mismatch")
        if entry.get("claim") != "BOUNDED_DOCUMENTARY_COVERAGE" or entry.get("release_status") != "UNRELEASED_REVIEW":
            errors.append("Unsupported validation/release claim")
        targets = entry.get("targets")
        if not isinstance(targets, list) or not targets:
            errors.append("Missing public target")
            continue
        for target in targets:
            if not isinstance(target, str) or target.startswith(("/", "\\\\")) or ".." in target.split("/") or ":" in target:
                errors.append("Unsafe public target")
            elif target not in framework:
                errors.append("Missing public target: " + target)
        # Catalog is deliberately source-free; private provenance belongs in the local ledger.
        text = json.dumps(entry, ensure_ascii=False)
        if re.search(r"https?://|figma\\.com|[?&]node-id=|(?:[A-Z][A-Z0-9_]{1,15})-(?:ADR|CHANGE)-[0-9]+", text, re.I):
            errors.append("Source locator/identifier is not allowed in public catalog")
    return errors

def assess_source_coverage(inventory, ledger, catalog):
    errors = []
    try:
        sources = inventory["private"]
        records = ledger["files"]
        expected = {item["path"]: item["sha"] for item in sources}
        known = {item["id"] for item in catalog["entries"]}
    except (KeyError, TypeError):
        return ["Malformed restricted coverage inputs"]
    if len(expected) != len(sources):
        errors.append("Duplicate inventory path")
    if inventory.get("pins") != ledger.get("pins"):
        errors.append("Source snapshot pins differ")
    mapped = {}
    for row in records:
        path = row.get("path")
        if path in mapped:
            errors.append("Duplicate source disposition")
        mapped[path] = row
        if path not in expected or row.get("blob_sha") != expected.get(path):
            errors.append("Source identity mismatch")
        if row.get("disposition") not in {"SHARED_CORE", "METHOD_EVIDENCE", "CONFIGURED_INSTANCE", "PRIVATE_HISTORY", "EXCLUDED_PRIVATE"}:
            errors.append("Missing source disposition")
        methods = row.get("method_ids", [])
        if not isinstance(methods, list) or any(m not in known for m in methods):
            errors.append("Unknown methodology mapping")
        if not methods and not row.get("exclusion_reason"):
            errors.append("Source has neither mapping nor exclusion")
        if row.get("disposition") in {"EXCLUDED_PRIVATE", "CONFIGURED_INSTANCE", "PRIVATE_HISTORY"} and not row.get("exclusion_reason"):
            errors.append("Private/configured/history disposition needs a reason")
        if row.get("review_level") != "CONTENT_SCREEN_AND_CONTEXTUAL_FAMILY_REVIEW":
            errors.append("Unsupported review claim")
    if set(mapped) != set(expected):
        errors.append("Incomplete or extra source coverage")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--framework", type=Path, required=True)
    parser.add_argument("--private-inventory", type=Path)
    parser.add_argument("--private-ledger", type=Path)
    args = parser.parse_args()
    root = args.framework.resolve()
    catalog = json.loads((root / "docs/methodology-catalog.json").read_text(encoding="utf-8"))
    paths = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    errors = assess_catalog(catalog, paths)
    source_count = None
    if bool(args.private_inventory) != bool(args.private_ledger):
        errors.append("Provide both restricted inputs")
    elif args.private_inventory:
        inventory = json.loads(args.private_inventory.read_text(encoding="utf-8"))
        ledger = json.loads(args.private_ledger.read_text(encoding="utf-8"))
        errors.extend(assess_source_coverage(inventory, ledger, catalog))
        source_count = len(ledger.get("files", []))
    print(json.dumps({"errors": errors, "methodologies": len(catalog.get("entries", [])),
                      "source_files": source_count, "writes": False}, indent=2))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
