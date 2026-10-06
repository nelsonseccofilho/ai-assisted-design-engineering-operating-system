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

# Package references: Markdown targets are resolved relative to their source.
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
check(derivative["meta"]["version"] == version, "Master/JSON version mismatch")
check(f"**Framework version:** {version}" in read("README.md"), "README version mismatch")
check(derivative["meta"]["canonical_source"] == "PROMPT_OPERACIONAL_MASTER.md",
      "Wrong canonical source")
principle = "THE FILE / ARTIFACT THAT OWNS THE MUTATION OWNS THE CHANGE RECORD"
check(principle in master and derivative["change_history"]["principle"] == principle,
      "Missing ownership principle")
rules = derivative["change_history"]["rules"]
expected = {"owner_scoped": True, "read_only_creates_record": False,
            "multi_owner_linked_records": True, "central_fallback_log": False,
            "missing_history_before_final": True, "handoff_replaces_history": False}
for key, value in expected.items():
    check(rules.get(key) == value, f"Incorrect ownership rule: {key}")
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
entry = read("START_CHAT.md")
check(entry.index("PROMPT_OPERACIONAL_MASTER.md") <
      entry.index("PROJECT_CONTEXT.local.md") <
      entry.index("HANDOFF_CURRENT.local.md"), "Startup template load order mismatch")
check("resolve target owners" in entry and "persistent decision/change records" in entry,
      "Startup entry omits owner records")
context = read("PROJECT_CONTEXT_TEMPLATE.md")
for field in ["Artifact identity", "Governance location", "Change History location",
              "Change namespace", "Decision log location", "Evidence archive"]:
    check(field in context, f"Context registry missing {field}")
handoff = read("HANDOFF_TEMPLATE.md")
for field in ["Owner artifact", "History location", "Namespace-qualified record ID",
              "Read-only dependencies", "Missing owner history"]:
    check(field in handoff, f"Handoff missing {field}")
check("does not replace persistent owner Change History" in handoff,
      "Handoff substitutes for history")

index = read("DECISION_LOG.md")
for path in sorted((ROOT / "docs/decisions").glob("ADR-[0-9]*.md")):
    decision_id = path.name[:8]
    check(decision_id in index, f"ADR not indexed: {decision_id}")
adr = read("docs/decisions/ADR-0014-mutation-owned-change-records.md")
for section in ["Context", "Evidence", "Decision", "Why", "Impact",
                "Alternatives considered", "Validation / QA", "Supersession"]:
    check(f"## {section}" in adr, f"ADR-0014 missing {section}")
check("Decision: ADR-0014" in read("CONTRIBUTING.md"), "Missing commit traceability")
check("ADR-0014" in read("CHANGELOG.md"), "Missing framework change history")
check("3.3.0" in read("CHANGELOG.md"), "Historical release missing")

# Exercise a runtime routing contract with independent expected outcomes.
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

# Guard against accidental public identifiers; generic placeholders remain valid.
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix not in {".md", ".json", ".py"}:
        continue
    text = path.read_text(encoding="utf-8-sig")
    check(not re.search(r"https?://(?:www\.)?figma\.com/(?:design|file)/", text),
          f"Figma artifact URL in {path.relative_to(ROOT)}")

if errors:
    print("\n".join("FAIL: " + message for message in errors))
    raise SystemExit(1)
print(f"PASS: {checks} package checks, including 10 ownership routing scenarios")
