"""Negative regression cases for controlled synchronization."""
import copy
import json
from pathlib import Path
from runtime_sync import assess, snapshot
root = Path(__file__).resolve().parents[1]
framework = snapshot(root)
assert not assess(framework)[0]
broken = dict(framework)
broken["REPORT_STATE_TEMPLATE.json"] += " "
assert any("alias drift" in x for x in assess(broken)[0])
broken = dict(framework)
broken["runtime-template/operators/person.md"] = "private"
assert any("Unclassified" in x for x in assess(broken)[0])
broken = dict(framework)
broken["sessions/person/record.md"] = "private"
assert any("Private instance" in x for x in assess(broken)[0])
assert assess(framework, deny=["Canonical runtime package"])[0]
print("PASS: 5 public synchronization regression scenarios")
