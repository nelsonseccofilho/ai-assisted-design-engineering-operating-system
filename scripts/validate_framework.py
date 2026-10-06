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
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0].strip("<>")
        if not target or re.match(r"[a-zA-Z]+:", target):
            continue
        check((source.parent / target).exists(),
              f"Broken local link in {source.relative_to(ROOT)}: {target}")

master = read("PROMPT_OPERACIONAL_MASTER.md")
derivative = json.loads(read("prompt-operacional.json"))
version = re.search(r"\*\*Version:\*\* ([0-9.]+)", master).group(1)
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
    check(not re.search(r"https?://(?:www\.)?figma\.com/(?:design|file)/", text),
          f"Figma artifact URL in {path.relative_to(ROOT)}")

# Operator Daily Report contract.
report_state = json.loads(read("REPORT_STATE_TEMPLATE.json"))
check(report_state["status"] == "NOT_DUE", "Report state must begin NOT_DUE")
check(report_state["first_report_baseline"] == "start_of_current_reporting_day",
      "Wrong first-report baseline")
for token in ["DRAFT never advances", "SENT", "Do not invent blockers"]:
    check(token in master or token in read("docs/OPERATOR_DAILY_REPORTS.md"),
          f"Missing report contract token: {token}")


# Parse all JSON files and validate report template integration.
for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8-sig"))
        check(True, str(path))
    except ValueError as exc:
        check(False, f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")
check(report_state["schema_version"] == "1.1", "Report schema mismatch")
check(report_state["required"] is False, "Generic reports must remain configurable")
for field in ["last_sent_at", "reporting_date", "waiver"]:
    check(field in report_state, f"Missing report field: {field}")
for key, target in {"operator_daily_report_template": "OPERATOR_DAILY_REPORT_TEMPLATE.md",
                    "report_state_template": "REPORT_STATE_TEMPLATE.json"}.items():
    check(derivative["runtime_files"].get(key) == target, f"Report template mapping: {key}")
check("interval_end" in derivative["operator_daily_reports"]["cursor_rule"],
      "Cursor must freeze report coverage")
check(derivative["operator_daily_reports"]["waiver_advances_cursor"] is False,
      "Waiver cannot advance cursor")
check("Git checkpoint or PR merge alone" in read("SESSION_RECORD_TEMPLATE.md"),
      "Missing session closure discipline")
for target in ["operators/", "sessions/", "workstreams/", "reports/", "*.local.md"]:
    check(target in read(".gitignore"), f"Unprotected runtime path: {target}")


# Preserve stable-main governance checks alongside new runtime checks.
check(derivative["meta"]["canonical_source"] == "PROMPT_OPERACIONAL_MASTER.md", "Canonical source")
check("append-only" in rules["historical_correction"], "Destructive correction contract")
check(derivative["startup_order"] == [
    "master", "project_context_or_onboarding", "handoff",
    "owner_registry_and_governance_records", "current_state_inspection",
    "reconcile", "next_action"], "Wrong bootstrap order")
startup = master.split("# 36. STARTUP PROTOCOL", 1)[1].split("# 37.", 1)[0]
tokens = ["load this Master", "load `PROJECT_CONTEXT.local.md`",
          "load `HANDOFF_CURRENT.local.md`", "resolve the artifact registry",
          "inspect current tool state", "execute `NEXT ACTION`"]
positions = [startup.find(token) for token in tokens]
check(all(p >= 0 for p in positions) and positions == sorted(positions),
      "Master bootstrap/load order changed")
minimal = entry.split("## If only local minimal mode exists", 1)[1].split("---", 1)[0]
check(entry.index("## Always load") < entry.index("## If only local minimal mode exists") and
      minimal.index("PROJECT_CONTEXT.local.md") < minimal.index("HANDOFF_CURRENT.local.md"),
      "Startup load order")
check("resolve target mutation owners" in entry and "Change History records" in entry,
      "Startup omits owner records")
context = read("PROJECT_CONTEXT_TEMPLATE.md")
for field in ["Artifact identity", "Governance location", "Change History location",
              "Change namespace", "Decision log location", "Evidence archive"]:
    check(field in context, f"Context registry missing {field}")
for field in ["Namespace-qualified record ID", "Read-only dependencies", "Missing owner history"]:
    check(field in handoff, f"Handoff missing {field}")
check("does not replace persistent owner Change History" in handoff, "Handoff replaces history")
adr = read("docs/decisions/ADR-0014-mutation-owned-change-records.md")
for section in ["Context", "Evidence", "Decision", "Why", "Impact",
                "Alternatives considered", "Validation / QA", "Supersession"]:
    check(f"## {section}" in adr, f"ADR-0014 missing {section}")
check("Decision: ADR-0014" in read("CONTRIBUTING.md"), "Commit traceability")
check("ADR-0014" in read("CHANGELOG.md") and "3.3.0" in read("CHANGELOG.md"),
      "Governance/release history")


# Framework/runtime template parity from ADR-0018.
manifest = json.loads(read("RUNTIME_MANIFEST_TEMPLATE.json"))
check(manifest["schema_version"] == "1.0", "Manifest schema version")
check(manifest["canonical_runtime_ref"] == "main", "Manifest canonical ref")
check(manifest["runtime_repository"] is None and manifest["operator_identity"] == [],
      "Manifest contains instance identity")
check(manifest["framework"]["stable_pin"] is None and manifest["framework"]["candidate"] is None,
      "Generic manifest has a private/candidate pin")
check(manifest["runtime_access_modes"] == runtime["access_modes"], "Manifest access mode drift")
check(manifest["workstream_id_pattern"] == runtime["workstream_id_pattern"], "Manifest ID drift")
check(manifest["session_record_pattern"] == runtime["session_record_pattern"], "Manifest session path drift")
expected_bootstrap = [
    "00_START_CHAT.md", "10_PROMPT_OPERACIONAL_MASTER.md", "20_PROJECT_CONTEXT.local.md",
    "30_GOVERNANCE.local.md", "40_PROJECT_DECISION_LOG.local.md", "50_ARTIFACT_REGISTRY.local.md",
    "60_EVIDENCE_INDEX.local.md", "70_WORKSTREAM_REGISTRY.local.md"]
check(manifest["bootstrap_files"] == expected_bootstrap, "Deterministic bootstrap drift")
mapping = manifest["template_sources"]
assembly = read("docs/FRAMEWORK_RUNTIME_SYNC.md")
for destination, source in mapping.items():
    check((ROOT / source).is_file(), f"Missing runtime source: {source}")
    check(destination in assembly and source in assembly, f"Unmapped assembly source: {source}")
check(manifest["project_decision_index"]["destination"] == expected_bootstrap[4],
      "Project decision index bootstrap")
check((ROOT / manifest["project_decision_index"]["record_template"]).is_file(),
      "Missing project decision template")
for field in ["governance_template", "artifact_registry_template", "evidence_index_template",
              "backlog_template", "runtime_qa_template", "framework_dependency_template",
              "runtime_manifest_template"]:
    target = derivative["runtime_files"][field]
    check((ROOT / target).is_file(), f"Missing generic template mapping: {field}")
config = manifest["daily_operator_reports"]
check(config["required"] is False and config["languages"] == [] and config["timezone"] is None,
      "Generic report policy must remain configurable")
check(config["statuses"] == derivative["operator_daily_reports"]["statuses"],
      "Manifest report states drift")
check(config["first_report_baseline"] == report_state["first_report_baseline"],
      "Manifest report baseline drift")
check(manifest["validation_gates"] == {"live_report_cycle": "PENDING", "cross_chat_pilot": "PENDING"},
      "Generic template must not assert live validation")
check(state["schema_version"] == "1.1" and state["runtime_version"] is None,
      "Runtime state schema/version drift")
check("ADR-0018" in index and "ADR-0018" in read("CHANGELOG.md"),
      "Promotion ADR not indexed/changelogged")
check(derivative["framework_runtime_promotion"]["promote_reusable_findings"] is True,
      "Reusable findings cannot stay private-only")
check(manifest["conventional_commits"]["version"] == derivative["git_contract"]["conventional_commits"],
      "Manifest commit contract")
for field in ["timestamp_with_offset", "timezone", "human_operator", "operator_alias",
              "chat_label", "workstream_id"]:
    check(field in manifest["mutation_attribution"] and
          field in derivative["change_history"]["record_fields"], f"Mutation provenance drift: {field}")
check((ROOT / "SECURITY.md").is_file(), "Missing public security boundary")

from runtime_sync import assess, snapshot
package_errors, _ = assess(snapshot(ROOT))
for message in package_errors:
    check(False, message)
check(not package_errors, "Canonical package parity")

if errors:
    print("\n".join("FAIL: " + message for message in errors))
    raise SystemExit(1)
print(f"PASS: {checks} package checks, including Project Runtime, Operator Daily Reports and mutation-owner scenarios")
