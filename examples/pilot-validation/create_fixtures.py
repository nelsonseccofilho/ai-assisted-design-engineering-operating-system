"""Create fresh fictional inputs; no private repository or live design material."""
import argparse, json, shutil, subprocess, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
parser.add_argument("--framework", type=Path, required=True)
args=parser.parse_args()
ROOT=args.destination.resolve()
SOURCE=args.framework.resolve()
PIN="30b11995a09e2a86a40e27b193ac9be8b4593333"
STABLE="2910154799ed28416475a359a9ea536599f38451"
STAMP=datetime.now(timezone.utc).isoformat()
CASES={
 "GARDEN":{"name":"Fictional garden planner","ws":"WS-20261015-001-garden",
  "artifact":"fictional-garden-preview","decision":"FICT-GARDEN-ADR-0001",
  "pending":"FICT-GARDEN-ADR-0002","next":"Review 01-brief.md and list the unresolved publication criteria.",
  "safe":"Use singular for one seed and plural for zero or multiple seeds. Preserve the capacity indicator 1/5.",
  "request":"A new comment proposes enabling Publish schedule immediately.",
  "rule":"Preview filtering and count labels are accepted. Publish schedule stays disabled until publication scope, accountable approval and persistence criteria are established.",
  "unresolved":["publication scope","accountable approval","persistence criteria"],
  "source":"SeedCard/v1","note":"This local note applies to garden preview cards only; it does not authorize schedule publication."},
 "SKY":{"name":"Fictional observatory checklist","ws":"WS-20261015-002-sky",
  "artifact":"fictional-sky-preview","decision":"FICT-SKY-ADR-0001",
  "pending":"FICT-SKY-ADR-0002","next":"Review 01-brief.md and distinguish preview reset from permanent deletion.",
  "safe":"Add the visible label Reset preview to the icon-only preview reset control.",
  "request":"A new comment proposes using the preview reset button to erase all saved observations.",
  "rule":"Resetting the temporary practice preview is accepted and reversible. Permanent deletion of saved observations is not approved; retention, recovery and accountable approval remain unresolved.",
  "unresolved":["retention","recovery","accountable approval"],
  "source":"ObservationCard/v1","note":"This local note covers reversible practice-preview reset only; saved observations are outside this artifact's mutation scope."}
}
def write(path,text):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding="utf-8")
def js(path,data):write(path,json.dumps(data,indent=2)+"\n")
source_tree=subprocess.check_output(["git","-C",str(SOURCE),"rev-parse",PIN+"^{tree}"],text=True).strip()
assert source_tree=="71330627b8ad3b5ef41ff2cfc9f663cc012fe896"
if subprocess.check_output(["git","-C",str(SOURCE),"diff",PIN,"--","runtime"],text=True).strip():
 raise SystemExit("Framework runtime differs from the pinned inputs")
if subprocess.check_output(["git","-C",str(SOURCE),"ls-files","--others","--exclude-standard","runtime"],text=True).strip():
 raise SystemExit("Untracked runtime inputs are not allowed")
ROOT.mkdir(parents=True,exist_ok=False)
for reviewer, indexed in (("reviewer-a","GARDEN"),("reviewer-b","SKY")):
 project=ROOT/reviewer
 if project.exists(): raise SystemExit("Refusing existing fixture destination")
 runtime=project/"runtime"
 shutil.copytree(SOURCE/"runtime",runtime)
 manifest=json.loads((runtime/"runtime-manifest.json").read_text(encoding="utf-8"))
 manifest.update(runtime_name="Fictional pilot laboratory",runtime_version="0.1.0-fixture",candidate_ref=PIN)
 manifest["framework"].update(repository="https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system",stable_pin=STABLE,version="3.6.0",candidate=PIN)
 manifest["operator_identity"]=[{"human_operator":"Fictional Fixture Owner","operator_alias":"LAB","profile":"operators/LAB/OPERATOR_PROFILE.md"}]
 js(runtime/"runtime-manifest.json",manifest)
 lock=json.loads((runtime/"framework-lock.json").read_text(encoding="utf-8"));lock.update(stable_pin=STABLE,candidate_pin=PIN);js(runtime/"framework-lock.json",lock)
 write(runtime/"FRAMEWORK_DEPENDENCY.md",f"# Fictional dependency\nFramework architecture: 3.6.0\nStable: {STABLE}\nCandidate under trial: {PIN}\nVendored Master: 10_PROMPT_OPERACIONAL_MASTER.md\nRuntime: 0.1.0-fixture\nLocal fixture only; no installed-project adoption.\n")
 write(runtime/"20_PROJECT_CONTEXT.local.md","# Fictional pilot laboratory\n\nAll names, decisions and scenes here are newly invented test data. There is no real client or product approval.\nTwo read-only review scopes: GARDEN and SKY. Current canonical ref is local main.\nOwner: Fictional Fixture Owner; alias LAB. Profiles: operators/LAB/OPERATOR_PROFILE.md.\nUse the current manifest paths; chat memory is not canonical.\nNo external artifacts, integrations, messages or private sources are authorized.\n")
 write(runtime/"30_GOVERNANCE.local.md","# Fictional laboratory governance\n\nRead sources only; reviewer output is analysis, not permission to mutate.\nThe reader may append its own audit receipts outside source content.\nA newer proposal cannot supersede an accepted decision through recency alone.\nNo publication, saved-data deletion, external message or paid service is authorized.\nRecover all mandatory bootstrap files first; then consult relevant sources.\nCurrent input is synthetic; do not simulate human approval or another reviewer's opinion.\nReports disabled; no report cursor advances.\n")
 write(runtime/"operators/LAB/OPERATOR_PROFILE.md","# Fictional operator profile\nHuman operator: Fictional Fixture Owner\nOperator alias: LAB\nReports: disabled\nThis identity describes synthetic source data, not a real participant or approval.\n")
 registry=["# Fictional workstream registry","| Workstream ID | Operator | Alias | Status | Scope | Handoff | State |","|---|---|---|---|---|---|---|"]
 decisions=["# Fictional decision index","| ID | Status | Source |","|---|---|---|"]
 artifacts=["# Fictional artifact registry","| ID | Scope | Owner history |","|---|---|---|"]
 evidence=["# Fictional evidence index","Use the case source files below; original media are N/A."]
 for case, data in CASES.items():
  folder=runtime/"evidence/pilot-cases"/case
  docs={
   "01-brief.md":f"# {data['name']}\nSynthetic scene. Evaluate these two proposals; do not implement them.\nA. {data['safe']}\nB. {data['request']}\nState what the current evidence supports and which decisions remain unresolved.\n",
   "02-accepted-decision.md":f"# {data['decision']}\nStatus: ACCEPTED IN FICTIONAL FIXTURE\n{data['rule']}\nScope: {data['artifact']}.\n",
   "03-newer-proposal.md":f"# {data['pending']}\nStatus: PROPOSED\nThis proposal is newer than the accepted record.\n{data['request']}\nNo accountable acceptance or supersession is recorded.\n",
   "04-component-source.md":f"# Canonical component\nSource: {data['source']}\nArtifact: {data['artifact']}\nProperty API: Label, Count, Expanded, ActionEnabled.\nAn inserted sibling note is local content, not proof of canonical component provenance.\nPublication: not attempted. Existing product instances: N/A.\n",
   "05-artifact-note.md":f"# Contextual artifact annotation\nArtifact: {data['artifact']}\nCanonical component owner: 04-component-source.md\nScope: {data['note']}\nShared behavior belongs in its canonical component record; this note is scoped to this scene.\n",
   "06-requirement-gaps.md":"# Functional evidence gaps\nUnresolved: "+", ".join(data["unresolved"])+".\nA preview or screenshot is not backend, authorization, accessibility or persistence acceptance.\n",
   "07-qa-observations.md":"# Historical fixture QA\nStatic layout sample observed only; no native-editor legibility, keyboard, real backend or stakeholder acceptance was established.\nThis is not a fresh execution report.\n",
   "08-superseded-note.md":"# Historical annotation\nStatus: SUPERSEDED\nEarlier note said every visual button state was ready for delivery. Retained for history; it does not establish present acceptance.\n",
   "09-color-research.md":"# Unrelated palette experiment\nOptional exploration. No accepted changes.\n",
   "10-calendar-backlog.md":"# Unrelated calendar backlog\nFuture scheduling ideas only.\n",
   "11-typography-options.md":"# Unrelated typography options\nExploration, no approval.\n",
   "12-archived-planning.md":"# Archived plan\nHistorical draft, no current rule or mutation authority.\n",
  }
  if case==indexed:
   docs["INDEX.md"]="# Optional source index\n"+"\n".join(f"- {name}: {text.splitlines()[0].lstrip('# ')}" for name,text in docs.items())+"\nThis index is a locator; consult sources for authority and scope.\n"
  for name,text in docs.items(): write(folder/name,text)
  work=runtime/"workstreams"/data["ws"]
  state=json.loads((runtime/"workstreams/_template/state.json").read_text(encoding="utf-8"))
  state.update(workstream_id=data["ws"],status="ACTIVE",current_human_operator="Fictional Fixture Owner",operator_alias="LAB",latest_chat_label="fixture-origin",artifact={"system":"synthetic-local-material","id":data["artifact"],"scope":"read-only review"},latest_session_record=f"sessions/LAB/2026/10/{case}.md",next_action=data["next"],last_completed_action="Persist fictional review inputs",last_validated_at=STAMP,runtime_version="0.1.0-fixture")
  js(work/"state.json",state)
  write(work/"HANDOFF.md",f"# Fictional handoff\nWorkstream: {data['ws']}\nOperator: Fictional Fixture Owner / LAB\nStatus: ACTIVE; review scope only.\nArtifact: {data['artifact']}\nSource root: evidence/pilot-cases/{case}/\nState: workstreams/{data['ws']}/state.json\nNEXT ACTION: {data['next']}\nNo implementation, publication or external mutation is authorized by this test.\n")
  write(runtime/f"sessions/LAB/2026/10/{case}.md",f"# Fictional source session\nWorkstream: {data['ws']}\nIntent: START_NEW_WORKSTREAM\nScope: prepare independent read-only critique of synthetic inputs.\nNo product acceptance or live implementation.\nNEXT ACTION: {data['next']}\n")
  registry.append(f"| {data['ws']} | Fictional Fixture Owner | LAB | ACTIVE | {data['artifact']}:read-only | workstreams/{data['ws']}/HANDOFF.md | workstreams/{data['ws']}/state.json |")
  decisions.append(f"| {data['decision']} | ACCEPTED IN FICTIONAL FIXTURE | evidence/pilot-cases/{case}/02-accepted-decision.md |")
  decisions.append(f"| {data['pending']} | PROPOSED | evidence/pilot-cases/{case}/03-newer-proposal.md |")
  artifacts.append(f"| {data['artifact']} | read-only review | CHANGE_HISTORY.local.md |")
  evidence.append(f"- {case}: evidence/pilot-cases/{case}/")
 write(runtime/"70_WORKSTREAM_REGISTRY.local.md","\n".join(registry)+"\n")
 write(runtime/"40_PROJECT_DECISION_LOG.local.md","\n".join(decisions)+"\n")
 write(runtime/"50_ARTIFACT_REGISTRY.local.md","\n".join(artifacts)+"\n")
 write(runtime/"60_EVIDENCE_INDEX.local.md","\n".join(evidence)+"\n")
 write(runtime/"CHANGE_HISTORY.local.md",f"# Fictional laboratory owner history\n\n## FIXTURE-SETUP\nTimestamp: {STAMP}; timezone UTC.\nOwner: fictional laboratory.\nHuman identity in source data: Fictional Fixture Owner / LAB (synthetic only).\nChange: copy generic runtime seeds and create newly invented review inputs.\nDecision references: framework ADR-0025 and ADR-0027.\nQA: fixture hash/structure verification required before reviewer dispatch.\n")
 write(project/".gitignore","receipts.jsonl\n__pycache__/\n.env\n.env.*\nraw-media/\n")
 shutil.copyfile(Path(__file__).with_name("read_material.py"),project/"read_material.py")
 for argv in (["git","init","--initial-branch=main"],["git","add","--","runtime","read_material.py",".gitignore"],["git","-c","user.name=Fictional Pilot Fixture","-c","user.email=fixture@example.invalid","commit","-m","test(pilot): persist synthetic review inputs","-m","Refs: ADR-0025, ADR-0027"]):
  subprocess.run(argv,cwd=project,check=True,capture_output=True)
 snap={p.relative_to(project).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (project/"runtime").rglob("*") if p.is_file()}
 js(ROOT/(reviewer+"-source-hashes.json"),snap)
key={case:{"workstream_id":d["ws"],"artifact":d["artifact"],"decision":d["decision"],"proposal":d["pending"],"canonical_component":d["source"],"next_action":d["next"],"unresolved":d["unresolved"]} for case,d in CASES.items()}
js(ROOT/"expected-restricted.json",key)
js(ROOT/"protocol.json",{"source":PIN,"conditions":{"reviewer-a":{"GARDEN":"INDEX","SKY":"FLAT"},"reviewer-b":{"GARDEN":"FLAT","SKY":"INDEX"}},"case_order":["GARDEN","SKY"],"reviewers":2,"human_operators":0,"claim_limit":"Exploratory synthetic two-session trial; no causal productivity or financial savings claim","primary_criteria":["source authority","context recovery","scope/permission boundary","functional gaps","proportional critique","no source mutation"],"measurement":"reader receipts: file/byte access and first-read-to-complete wall time; not token billing or actual work duration"})
print(json.dumps({"root":str(ROOT),"reviewers":["reviewer-a","reviewer-b"],"cases":list(CASES),"source_tree":source_tree}))
