"""Read-only framework/runtime parity and update planning. Python 3.9+."""
import argparse, json, re
from pathlib import Path

def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_text(encoding="utf-8-sig")
            for p in root.rglob("*") if p.is_file()
            and ".git" not in p.relative_to(root).parts and "__pycache__" not in p.relative_to(root).parts}

def assess(framework, runtime=None, deny=()):
    errors, review = [], []
    index_path="runtime/package.index.json"
    if index_path not in framework:
        return ["Missing canonical package index: "+index_path], review
    contract=json.loads(framework[index_path]); prefix=contract["runtime_root"].rstrip("/")+"/"
    paths={x["path"] for x in contract["files"]}
    for item in contract["files"]:
        source=prefix+item["path"]
        if source not in framework: errors.append("Missing canonical runtime source: "+source); continue
        alias=item.get("compatibility_alias")
        if alias and alias in framework and framework[alias] != framework[source]:
            errors.append("Compatibility alias drift: "+alias)
    for path,text in framework.items():
        if path.startswith(prefix):
            rel=path[len(prefix):]
            if rel!="package.index.json" and rel not in paths:
                errors.append("Unclassified canonical runtime file: "+rel)
        if re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{24,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)",text):
            errors.append("Secret pattern: "+path)
        if any(v.lower() in text.lower() for v in deny if v): errors.append("Private denylist match: "+path)
    if runtime is None: return errors,review
    lock=json.loads(runtime.get(prefix+"framework-lock.json","{}"))
    if lock.get("schema_version")!="2.0": errors.append("Unsupported lock schema")
    if lock.get("package_index")!=index_path: errors.append("Lock package index drift")
    stable_pin=lock.get("stable_pin")
    candidate_pin=lock.get("candidate_pin")
    if stable_pin is not None and not re.fullmatch(r"[0-9a-f]{40}",stable_pin):
        errors.append("Stable pin must be null or an immutable full commit")
    if candidate_pin is not None and not re.fullmatch(r"[0-9a-f]{40}",candidate_pin):
        errors.append("Candidate pin must be null or an immutable full commit")
    baselines=lock.get("shared_baselines",{})
    for item in contract["files"]:
        rel=item["path"]; path=prefix+rel
        if path not in runtime: errors.append("Missing runtime path: "+path); continue
        generic=framework.get(path,""); installed=runtime[path]
        if item["mode"]=="shared" and installed!=generic:
            ex=baselines.get(rel,{})
            if not re.fullmatch(r"[0-9a-f]{40}",ex.get("pin","") or "") or not ex.get("source") or not ex.get("reason"):
                errors.append("Undocumented shared baseline: "+rel)
            else: review.append("Stable baseline retained pending promotion: "+rel)
        elif item["mode"]=="configured" and installed!=generic:
            review.append("Preserve configured file; review changes manually: "+rel)
    manifest=json.loads(runtime[prefix+"runtime-manifest.json"]); seed=json.loads(framework[prefix+"runtime-manifest.json"])
    for field in ("runtime_root","canonical_runtime_ref","bootstrap_files","workstream_id_pattern","session_record_pattern","runtime_access_modes"):
        if manifest.get(field)!=seed.get(field): errors.append("Manifest contract drift: "+field)
    return errors,review

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--framework",type=Path,required=True); p.add_argument("--runtime",type=Path); p.add_argument("--denylist",type=Path)
    a=p.parse_args(); deny=json.loads(a.denylist.read_text(encoding="utf-8-sig")) if a.denylist else []
    errors,review=assess(snapshot(a.framework),snapshot(a.runtime) if a.runtime else None,deny)
    print(json.dumps({"errors":errors,"review":review,"writes":False},indent=2)); raise SystemExit(bool(errors))
if __name__=="__main__": main()
