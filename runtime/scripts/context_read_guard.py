"""Bounded, attributable source delivery for GOV-CTX-001 (read-only).

This opt-in generic helper reuses runtime_context.packet() for routing and selection.
Its manifest lists all selected original sources WITHOUT claiming they were read
by an agent. Each part is small enough for normal tool output; independent host
traces must prove receipt and full reconstruction before any claimed reading PASS.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from runtime_context import ContextError, packet

PART_CHARS = 2400


def digest(body):
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def describe(source, index):
    body = source["content"]
    return {
        "source_index": index,
        "path": source["path"],
        "role": source["role"],
        "selectors": source["selectors"],
        "raw_source_sha256": source["sha256"],
        "selected_content_sha256": digest(body),
        "selected_chars": len(body),
        "part_chars_limit": PART_CHARS,
        "part_count": max(1, (len(body) + PART_CHARS - 1) // PART_CHARS),
    }


def bounded_packet(report, source_index=None, part_index=None):
    """Create a manifest or exactly one part of one canonical selected source."""
    originals = report["sources"]
    base = {k: v for k, v in report.items() if k != "sources"}
    if source_index is None:
        if part_index is not None:
            raise ContextError("SOURCE_INDEX_REQUIRED")
        return {
            **base,
            "kind": "READ_ONLY_CONTEXT_SOURCE_MANIFEST",
            "source_count": len(originals),
            "sources": [describe(source, i) for i, source in enumerate(originals)],
            "reading_verified": False,
            "external_actions_observed": False,
        }
    if type(source_index) is not int or not 0 <= source_index < len(originals):
        raise ContextError("SOURCE_INDEX_OUT_OF_RANGE")
    if type(part_index) is not int:
        raise ContextError("PART_INDEX_REQUIRED")
    source = originals[source_index]
    meta = describe(source, source_index)
    if not 0 <= part_index < meta["part_count"]:
        raise ContextError("PART_INDEX_OUT_OF_RANGE")
    start = part_index * PART_CHARS
    end = min(start + PART_CHARS, len(source["content"]))
    part = source["content"][start:end]
    return {
        "kind": "READ_ONLY_CONTEXT_SOURCE_PART",
        "phase": report["phase"],
        "activity": report["activity"],
        "workstream": report["workstream"],
        "authority": "READING_PACKET_ONLY",
        "execution_authorized": False,
        "writes": False,
        "reading_verified": False,
        "source_count": len(originals),
        **meta,
        "part_index": part_index,
        "part_start_char": start,
        "part_end_char": end,
        "part_chars": len(part),
        "part_sha256": digest(part),
        "part": part,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--runtime", type=Path, required=True)
    p.add_argument("--phase", choices=("bootstrap", "context"), required=True)
    p.add_argument("--activity")
    p.add_argument("--workstream")
    p.add_argument("--source-index", type=int)
    p.add_argument("--part-index", type=int)
    args = p.parse_args()
    try:
        if args.phase == "bootstrap" and (args.activity or args.workstream):
            raise ContextError("BOOTSTRAP_SCOPE_UNEXPECTED")
        report = packet(args.runtime, args.phase, activity=args.activity,
                        workstream=args.workstream, access="READ_ONLY")
        result = bounded_packet(report, args.source_index, args.part_index)
    except (ContextError, OSError, TypeError, KeyError, ValueError) as exc:
        code = str(exc) if isinstance(exc, ContextError) else "INVALID_CONFIGURATION"
        print(json.dumps({"assessment": "FAIL", "code": code,
                          "execution_authorized": False, "writes": False}))
        raise SystemExit(1)
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
