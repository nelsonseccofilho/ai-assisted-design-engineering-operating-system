"""Read-only framework/runtime parity and update planning. Python 3.9+."""
import argparse
import hashlib
import json
import re
from pathlib import Path

def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()

def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_text(encoding="utf-8-sig")
            for p in root.rglob("*") if p.is_file()
            and ".git" not in p.relative_to(root).parts
            and "__pycache__" not in p.relative_to(root).parts}

def assess(framework, runtime=None, deny=()):
    errors, review = [], []
    contract = json.loads(framework["runtime-template.index.json"])
    paths = {item["path"] for item in contract["files"]}
    prefix = contract["template_root"] + "/"
    for item in contract["files"]:
        source = prefix + item["path"]
        if source not in framework:
            errors.append("Missing canonical source: " + source)
            continue
        alias = item.get("compatibility_alias")
        if alias and framework.get(alias) != framework[source]:
            errors.append("Compatibility alias drift: " + alias)
        if item["mode"] not in ("shared", "configured"):
            errors.append("Unknown file class: " + item["path"])
    for path, text in framework.items():
        if path.startswith(prefix) and path[len(prefix):] not in paths:
            errors.append("Unclassified template file: " + path)
        if path.split("/")[0] in contract["private_roots"] or path.endswith(".local.md") and not path.startswith(prefix):
            errors.append("Private instance path in framework: " + path)
        if re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{24,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)", text):
            errors.append("Secret pattern: " + path)
        if any(value.lower() in text.lower() for value in deny if value):
            errors.append("Private denylist match: " + path)
    if runtime is None:
        return errors, review
    lock = json.loads(runtime["framework-lock.json"])
    if not re.fullmatch(r"[0-9a-f]{40}", lock.get("candidate_pin", "")):
        errors.append("Candidate must use immutable full commit")
    if lock.get("schema_version") != "1.0":
        errors.append("Lock schema")
    if set(lock["files"]) != paths:
        errors.append("Lock inventory differs from canonical inventory")
    for item in contract["files"]:
        path = item["path"]
        if path not in runtime:
            errors.append("Missing runtime path: " + path)
            continue
        entry = lock["files"].get(path, {})
        if entry.get("mode") != item["mode"]:
            errors.append("File class drift: " + path)
        if entry.get("source_hash") != digest(framework.get(prefix + path, "")):
            errors.append("Candidate source drift: " + path)
        if item["mode"] == "shared":
            if digest(runtime[path]) != entry.get("installed_hash"):
                errors.append("Shared file modified: " + path)
            if entry.get("installed_hash") != entry.get("source_hash"):
                exception = entry.get("baseline_exception", {})
                if not re.fullmatch(r"[0-9a-f]{40}", exception.get("pin", "")) or not exception.get("reason") or not exception.get("source"):
                    errors.append("Undocumented shared baseline: " + path)
                else:
                    review.append("Stable baseline retained pending promotion: " + path)
        elif runtime[path] != framework.get(prefix + path):
            review.append("Preserve configured file; review changes manually: " + path)
    manifest = json.loads(runtime["runtime-manifest.json"])
    seed = json.loads(framework[prefix + "runtime-manifest.json"])
    for field in ("canonical_runtime_ref", "bootstrap_files", "workstream_id_pattern", "session_record_pattern", "runtime_access_modes"):
        if manifest.get(field) != seed.get(field):
            errors.append("Manifest contract drift: " + field)
    for path in ("workstreams/_template/state.json", "reports/daily/_template/state.json"):
        configured = json.loads(runtime[path])
        generic = json.loads(framework[prefix + path])
        if not set(generic).issubset(configured) or configured.get("schema_version") != generic["schema_version"]:
            errors.append("Schema drift: " + path)
    registry = json.loads(runtime["upstream-disposition.json"])
    for entry in registry["entries"]:
        if entry["status"] not in contract["upstream_statuses"] or not entry.get("evidence"):
            errors.append("Invalid upstream disposition")
        if entry["status"] == "PROMOTED" and not entry.get("candidate"):
            errors.append("Promotion missing candidate")
        if entry["status"] == "UPSTREAM_PENDING":
            review.append("Upstream pending: " + entry["id"])
    return errors, review

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--framework", type=Path, required=True)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--denylist", type=Path, help="Private JSON array; never commit this list publicly")
    args = parser.parse_args()
    deny = json.loads(args.denylist.read_text(encoding="utf-8-sig")) if args.denylist else []
    errors, review = assess(snapshot(args.framework), snapshot(args.runtime) if args.runtime else None, deny)
    print(json.dumps({"errors": errors, "review": review, "writes": False}, indent=2))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
