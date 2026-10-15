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
broken["runtime/operators/person.md"] = "private"
assert any("Unclassified" in x for x in assess(broken)[0])
broken = dict(framework)
broken["runtime/sessions/person/record.md"] = "private"
assert any("Unclassified canonical runtime file" in x for x in assess(broken)[0])
assert assess(framework, deny=["Canonical runtime package"])[0]

# A released runtime may have a stable immutable pin and no active candidate.
released = dict(framework)
lock = json.loads(released["runtime/framework-lock.json"])
lock["stable_pin"] = "f" * 40
lock["candidate_pin"] = None
released["runtime/framework-lock.json"] = json.dumps(lock, indent=2) + "\n"
assert not any("Candidate pin" in x or "Stable pin" in x for x in assess(framework, released)[0])

# When a candidate exists it must still be an immutable full commit.
candidate = dict(released)
lock = json.loads(candidate["runtime/framework-lock.json"])
lock["candidate_pin"] = "not-a-sha"
candidate["runtime/framework-lock.json"] = json.dumps(lock, indent=2) + "\n"
assert any("Candidate pin" in x for x in assess(framework, candidate)[0])

# Documentation pointers retain their entrypoint without requiring byte parity.
for pointer in ("docs/CHANGE_RECORD_OWNERSHIP.md", "docs/DOCUMENTATION_OWNERSHIP.md"):
    broken = dict(framework)
    broken[pointer] = "[wrong](missing.md)"
    assert any("Documentation pointer drift" in x for x in assess(broken)[0])
    broken.pop(pointer)
    assert any("Missing documentation pointer" in x for x in assess(broken)[0])
broken = dict(framework)
broken.pop("REPORT_STATE_TEMPLATE.json")
assert any("Missing compatibility alias" in x for x in assess(broken)[0])

print("PASS: public synchronization regression scenarios for canonical runtime root")
