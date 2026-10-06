"""Dependency-free package QA. Run from any directory with Python 3.9+."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8-sig")

# Local Markdown links.
for source in ROOT.rglob("*.md"):
    text = source.read_text(encoding="utf-8-sig")
    for target in re.findall(r"(?<!!)[[^]]+](([^)]+))", text):
        target = target.split("#", 1)[0].strip("<>")
        if not target or re.match(r"[a-zA-Z]+:", target):
            continue
        check((source.parent / target).exists(),
              f"Broken local link in {source.relative_to(ROOT)}: {target}")

master = read("PROMPT_OPERACIONAL_MASTER.md")
derivative = json.loads(read("prompt-operacional.json"))
version = re.search(r"**Version:** ([0-9.]+)", master).group(1)
check(version == "3.4.0", "Unexpected framework version")
check(derivative["meta"]["version"] == version, "Master/JSON version mismatch")
check(f"**Framework version:** {version}" in read("README.md"), "README version mismatch")

# Mutation ownership contract remains required.
principle = "THE FILE / ARTIFACT THAT OWNS THE MUTATION OWNS THE CHANGE RECORD"
check(principle in master and derivative["change_history"]["principle"] == principle,
      "Missing ownership principle")
rules = derivative["change_history"]["rules"]
expected = {"owner_scoped": True, "read_only_creates_record": False,
            "multi_owner_linked_records": True, "central_fallback_log": False,
            "missing_history_before_final": True, "handoff_replaces_history": False}
for key, value in expected.items():
    check(rules.get(key) == value, f"Incorrect ownership rule: {key}")

# Project Runtime contract.
for path in [
    "WORKSTREAM_REGISTRY_TEMPLATE.md",
    "OPERATOR_DAILY_REPORT_TEMPLATE.md",
    "REPORT_STATE_TEMPLATE.json",
    "docs/OPERATOR_DAILY_REPORTS.md",
    "docs/decisions/ADR-0017-operator-daily-reports.md",
    "SESSION_RECORD_TEMPLATE.md",
    "RUNTIME_STATE_TEMPLATE.json",
    "OPERATOR_PROFILE_TEMPLATE.md",
    "docs/PROJECT_RUNTIME.md",
    "docs/decisions/ADR-0015-project-runtime.md",
    "docs/decisions/ADR-0016-operator-session-workstream-topology.md",
]:
    check((ROOT / path).exists(), f"Missing Project Runtime file: {path}")

runtime = derivative["project_runtime"]
check(runtime["canonical_ref_default"] == "main", "Project Runtime canonical ref must default to main")
check(runtime["workstream_id_pattern"] == "WS-YYYYMMDD-NNN-<slug>", "Wrong Workstream ID pattern")
check("operator_alias" in runtime["identity_fields"] and "session_alias" not in runtime["identity_fields"],
      "Operator alias terminology mismatch")
check(runtime["access_modes"] == ["READ_WRITE", "READ_ONLY", "UNAVAILABLE"],
      "Runtime access modes mismatch")

entry = read("START_CHAT.md")
for token in ["READ_WRITE", "READ_ONLY", "UNAVAILABLE", "Operator alias",
              "WS-YYYYMMDD-NNN-<slug>", "sessions/<OPERATOR_ALIAS>/<YYYY>/<MM>/"]:
    check(token in entry, f"START_CHAT missing {token}")

handoff = read("HANDOFF_TEMPLATE.md")
for token in ["Operator alias", "Latest Chat label", "Latest Session Record",
              "offset-aware timestamp/timezone", "Owner artifact", "History location"]:
    check(token in handoff, f"Handoff missing {token}")

session = read("SESSION_RECORD_TEMPLATE.md")
for token in ["Workstreams touched", "Operator alias", "Chat label", "NEXT ACTION"]:
    check(token in session, f"Session template missing {token}")

state = json.loads(read("RUNTIME_STATE_TEMPLATE.json"))
check("operator_alias" in state and "session_alias" not in state, "Runtime state alias mismatch")
check("workstream_id" in state and "latest_session_record" in state, "Runtime state fields missing")

# ADR index completeness and uniqueness.
index = read("DECISION_LOG.md")
adr_paths = sorted((ROOT / "docs/decisions").glob("ADR-[0-9]*.md"))
ids = []
for path in adr_paths:
    decision_id = path.name[:8]
    ids.append(decision_id)
    check(decision_id in index, f"ADR not indexed: {decision_id}")
check(len(ids) == len(set(ids)), "Duplicate ADR IDs")
for decision_id in ["ADR-0014", "ADR-0015", "ADR-0016", "ADR-0017"]:
    check(decision_id in index, f"Missing decision index entry: {decision_id}")

# Conventional Commits contract.
cc = "https://www.conventionalcommits.org/en/v1.0.0/"
check(cc in read("CONTRIBUTING.md") and cc in entry, "Conventional Commits URL missing")

# Exercise mutation-owner routing contract.
def valid_routing(case):
    mutated = set(case["mutated"])
    records = case["records"]
    owners = [record["owner"] for record in records]
    if set(owners) != mutated or len(owners) != len(mutated):
        return False
    for record in records:
        if record["location"] != record["owner"] + "/history":
            return False
        if not record["namespace"]:
            return False
        if set(record["links"]) != mutated - {record["owner"]}:
            return False
    return True

for case in json.loads(read("examples/ownership-cases.json")):
    check(valid_routing(case) == case["valid"], f"Routing case failed: {case['name']}")

# Public privacy guard.
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix not in {".md", ".json", ".py"}:
        continue
    text = path.read_text(encoding="utf-8-sig")
    check(not re.search(r"https?://(?:www.)?figma.com/(?:design|file)/", text),
          f"Figma artifact URL in {path.relative_to(ROOT)}")

# Operator Daily Report contract.
report_state = json.loads(read("REPORT_STATE_TEMPLATE.json"))
check(report_state["status"] == "NOT_DUE", "Report state must begin NOT_DUE")
check(report_state["first_report_baseline"] == "start_of_current_reporting_day",
      "Wrong first-report baseline")
for token in ["DRAFT never advances", "SENT", "Do not invent blockers"]:
    check(token in master or token in read("docs/OPERATOR_DAILY_REPORTS.md"),
          f"Missing report contract token: {token}")

if errors:
    print("\n".join("FAIL: " + message for message in errors))
    raise SystemExit(1)
print(f"PASS: {checks} package checks, including Project Runtime, Operator Daily Reports and mutation-owner scenarios")
