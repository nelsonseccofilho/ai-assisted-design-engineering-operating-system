"""Read-only source reader with separate, explicit measurement receipts."""
import argparse,hashlib,json,subprocess,time
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
RUNTIME=ROOT/"runtime"
LOG=ROOT/"receipts.jsonl"
p=argparse.ArgumentParser()
p.add_argument("operation",choices=["manifest","bootstrap","state","list","read","search","complete"])
p.add_argument("case",nargs="?",choices=["GARDEN","SKY"])
p.add_argument("value",nargs="?")
a=p.parse_args()
start=time.perf_counter()
paths=[];parts=[];inspected=0
def read(path):
 global inspected
 text=path.read_text(encoding="utf-8");paths.append(path.relative_to(ROOT).as_posix());inspected+=len(text.encode())
 return text
if a.operation=="manifest":
 text=subprocess.check_output(["git","-C",str(ROOT),"show","main:runtime/runtime-manifest.json"],text=True,encoding="utf-8")
 if json.loads(text)!=json.loads((RUNTIME/"runtime-manifest.json").read_text(encoding="utf-8")):
  raise SystemExit("Canonical manifest differs from the working copy")
 parts=[text];paths=["runtime/runtime-manifest.json"];inspected=len(text.encode())
elif a.operation=="bootstrap":
 manifest=json.loads((RUNTIME/"runtime-manifest.json").read_text(encoding="utf-8"))
 for name in manifest["bootstrap_files"]:parts.append("FILE: "+name+"\n"+read(RUNTIME/name))
elif a.case:
 folder=RUNTIME/"evidence/pilot-cases"/a.case
 if a.operation=="state":
  work=next((RUNTIME/"workstreams").glob("*-"+a.case.lower()))
  for path in [work/"HANDOFF.md",work/"state.json",RUNTIME/f"sessions/LAB/2026/10/{a.case}.md",RUNTIME/"operators/LAB/OPERATOR_PROFILE.md"]:parts.append("FILE: "+path.relative_to(RUNTIME).as_posix()+"\n"+read(path))
 elif a.operation=="list":parts=["\n".join(sorted(x.name for x in folder.glob("*.md")))]
 elif a.operation=="read":
  path=(folder/(a.value or "")).resolve()
  if path.parent!=folder.resolve() or path.suffix!=".md":raise SystemExit("Source path outside selected case")
  parts=[read(path)]
 elif a.operation=="search":
  if not a.value:raise SystemExit("Search term required")
  for path in sorted(folder.glob("*.md")):
   text=read(path);matches=[line[:240] for line in text.splitlines() if a.value.casefold() in line.casefold()]
   if matches:parts.append(path.name+":\n"+"\n".join(matches[:4]))
 elif a.operation=="complete":parts=["Review completion marker recorded; no source changed."]
else:raise SystemExit("Case required")
output="\n\n".join(parts)
receipt={"at":datetime.now(timezone.utc).isoformat(),"operation":a.operation,"case":a.case,"paths":paths,"bytes_inspected":inspected,"bytes_returned":len(output.encode()),"reader_seconds":round(time.perf_counter()-start,6)}
with LOG.open("a",encoding="utf-8") as stream:stream.write(json.dumps(receipt)+"\n")
print(output)
