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



def generated_bundle(bootstrap, context):
    """Combine the selected originals into one generated Markdown transport."""
    if bootstrap["phase"] != "bootstrap" or context["phase"] != "context":
        raise ContextError("BUNDLE_PHASE_MISMATCH")
    if bootstrap["authority"] != "READING_PACKET_ONLY" or context["authority"] != "READING_PACKET_ONLY":
        raise ContextError("BUNDLE_AUTHORITY_MISMATCH")
    chunks = [
        "# GENERATED CONTEXT — NOT A SOURCE OF AUTHORITY\n\n",
        "This temporary file collects canonical runtime excerpts. "
        "It is not an adopted contract, an authorization or proof that an agent "
        "received or read the sources. Read the full selected material below, "
        "verify freshness and inspect the target before taking action.\n\n",
        f"Activity: {context['activity']}  \n",
        f"Workstream: {context['workstream'] or 'NONE'}  \n",
        "source_read_by_agent_verified: false  \n",
        "execution_authorized: false  \n\n",
    ]
    for heading, report in (("BOOTSTRAP — manifest order", bootstrap),
                            ("CONTEXT — selected modules and current state", context)):
        chunks.append(f"## {heading}\n\n")
        for index, source in enumerate(report["sources"]):
            body = source["content"]
            meta = {
                "path": source["path"], "role": source["role"],
                "selectors": source["selectors"],
                "raw_source_sha256": source["sha256"],
                "selected_content_sha256": digest(body),
                "selected_chars": len(body),
            }
            chunks.extend((
                f"### Source {index + 1}: {source['path']}\n\n",
                "~~~json\n", json.dumps(meta, ensure_ascii=False, sort_keys=True),
                "\n~~~\n\n", f"<!-- BEGIN SOURCE {index + 1} -->\n",
                body,
                f"\n<!-- END SOURCE {index + 1} -->\n\n",
            ))
    return "".join(chunks)


def write_bundle(runtime, activity, workstream, output):
    """Write a new local transport copy, never the canonical runtime."""
    root = Path(runtime).resolve()
    target = Path(output)
    if not target.is_absolute() or target.suffix.lower() != ".md":
        raise ContextError("BUNDLE_ABSOLUTE_MD_PATH_REQUIRED")
    target = target.resolve()
    protected = (root.parent if root.name == "runtime" and
                 (root.parent / ".git").exists() else root)
    if target.is_relative_to(protected):
        raise ContextError("BUNDLE_MUST_BE_OUTSIDE_RUNTIME_REPOSITORY")
    if not target.parent.is_dir():
        raise ContextError("BUNDLE_OUTPUT_DIRECTORY_MISSING")
    if target.exists():
        raise ContextError("BUNDLE_OUTPUT_EXISTS")
    bootstrap = packet(root, "bootstrap", access="READ_ONLY")
    context = packet(root, "context", activity=activity, workstream=workstream,
                     access="READ_ONLY")
    body = generated_bundle(bootstrap, context)
    try:
        with target.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(body)
    except OSError as exc:
        raise ContextError("BUNDLE_WRITE_FAILED") from exc
    return {
        "kind": "GENERATED_CONTEXT_BUNDLE_RECEIPT",
        "bundle_path": str(target),
        "bundle_sha256": digest(body),
        "bundle_chars": len(body),
        "bootstrap_sources": len(bootstrap["sources"]),
        "context_sources": len(context["sources"]),
        "activity": activity, "workstream": workstream,
        "source_read_by_agent_verified": False,
        "execution_authorized": False,
        "source_mutation": False,
        "local_bundle_written": True,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--runtime", type=Path, required=True)
    p.add_argument("--phase", choices=("bootstrap", "context", "bundle"), required=True)
    p.add_argument("--activity")
    p.add_argument("--workstream")
    p.add_argument("--source-index", type=int)
    p.add_argument("--part-index", type=int)
    p.add_argument("--bundle-output", type=Path)
    args = p.parse_args()
    try:
        if args.phase == "bundle":
            if args.bundle_output is None or not args.activity or args.source_index is not None or args.part_index is not None:
                raise ContextError("BUNDLE_ARGUMENTS")
            result = write_bundle(args.runtime, args.activity, args.workstream,
                                  args.bundle_output)
        else:
            if args.bundle_output is not None:
                raise ContextError("BUNDLE_PHASE_REQUIRED")
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
