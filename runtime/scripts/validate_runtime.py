"""Static structure QA for a canonical Project Runtime tree."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; errors=[]
def check(ok,msg):
    if not ok: errors.append(msg)
def read(p): return (ROOT/p).read_text(encoding="utf-8-sig")
index=json.loads(read("package.index.json")); manifest=json.loads(read("runtime-manifest.json"))
check(index["runtime_root"]=="runtime","Runtime root contract"); check(manifest["runtime_root"]=="runtime","Manifest runtime root")
for item in index["files"]: check((ROOT/item["path"]).is_file(),"Missing canonical runtime path: "+item["path"])
for p in manifest["bootstrap_files"]: check((ROOT/p).is_file(),"Missing bootstrap: "+p)
for p in ROOT.rglob("*.json"):
    try: json.loads(p.read_text(encoding="utf-8-sig"))
    except ValueError as exc: errors.append(f"Invalid JSON: {p.relative_to(ROOT)}: {exc}")
check(manifest["project_decision_index"]["record_template"]=="docs/decisions/PROJECT_ADR_TEMPLATE.md","Project ADR template path")
if errors:
    print("\n".join("FAIL: "+x for x in errors)); raise SystemExit(1)
print(f"PASS: canonical runtime structure ({len(index['files'])} classified paths)")


# Startup intent / compatibility registry.
startup = read("00_START_CHAT.md")
for token in ["CONTINUE_WORKSTREAM","START_NEW_WORKSTREAM","START_NEW_PROJECT"]:
    check(token in startup, "Missing startup intent: " + token)
check((ROOT / "compat/ALIASES.local.md").is_file(), "Missing compatibility alias registry")
