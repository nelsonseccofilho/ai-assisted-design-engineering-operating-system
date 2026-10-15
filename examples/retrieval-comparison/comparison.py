"""Prepare and measure a fictional retrieval trial; standard library and local Git only."""
import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import statistics
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
FIXTURES = HERE.parent / "pilot-validation"
CHECKS = ["continuity_correct", "authority_correct", "annotation_scope_correct",
          "requirements_correct", "no_unsupported_acceptance"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def command(args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, stderr=subprocess.PIPE,
                                   text=True, encoding="utf-8")


def plan():
    value = load(HERE / "protocol.json")
    implemented = {"schema_version": "1.1", "protocol_id": "retrieval-comparison-v1.1",
        "status": "PREPARED_NOT_RUN", "framework_version": "3.6.0",
        "baseline_commit": "8e72681bde72a7aeadbc9959f9f59b52f9959118",
        "seed_commit": "30b11995a09e2a86a40e27b193ac9be8b4593333", "target": "METH-021",
        "planned_independent_sessions": 8, "planned_case_observations": 16,
        "required_quality_checks": CHECKS}
    if any(value.get(key) != expected for key, expected in implemented.items()):
        raise ValueError("Protocol metadata differs from the implemented design")
    rows = value["sessions"]
    if len(rows) != 8 or len({r["id"] for r in rows}) != 8:
        raise ValueError("Protocol must contain eight unique sessions")
    for regime, prefix in (("spontaneous", "SP"), ("guided", "GD")):
        selected = [r for r in rows if r["regime"] == regime]
        if {r["id"] for r in selected} != {prefix + f"{i:02d}" for i in range(1, 5)}:
            raise ValueError("Invalid session identifiers")
        positions = Counter()
        for row in selected:
            if sorted(row["order"]) != ["GARDEN", "SKY"] or set(row["conditions"]) != {"GARDEN", "SKY"}:
                raise ValueError("Invalid case assignment")
            if sorted(row["conditions"].values()) != ["FLAT", "INDEX"]:
                raise ValueError("Each session needs both index conditions")
            for position, case in enumerate(row["order"]):
                positions[(position, case, row["conditions"][case])] += 1
        if len(positions) != 8 or any(n != 1 for n in positions.values()):
            raise ValueError("Case, position and availability must be counterbalanced")
    return value


def kit_hashes():
    return {p.relative_to(HERE.parent).as_posix(): digest(p.read_bytes()) for p in
            [HERE / "comparison.py", HERE / "protocol.json",
             FIXTURES / "create_fixtures.py", FIXTURES / "read_material.py"]}


def source_hashes(room):
    paths = [p for p in (room / "runtime").rglob("*") if p.is_file()]
    paths += [room / name for name in ("TASK.md", "read_material.py", ".gitignore")]
    return {p.relative_to(room).as_posix(): digest(p.read_bytes()) for p in paths}


def task(row):
    extra = ""
    if row["regime"] == "guided":
        extra = ("If INDEX.md exists for the selected case, consult it before reading "
                 "case documents. If absent, choose source documents normally.\n")
    return ("# Fictional retrieval task\n\n"
            "Read only your assigned directory through read_material.py. "
            "Read the canonical local-main manifest and every mandatory bootstrap file "
            "completely, in order, before any case. The task is read-only; reader receipts "
            "are the only allowed generated file.\n\n"
            "Case order: " + " then ".join(row["order"]) + ".\n"
            "Choose relevant sources normally. " + extra +
            "For each case recover workstream, operator alias, status, artifact, next action, "
            "canonical component and governing/proposed decisions. Assess authority, annotation "
            "scope, missing requirements and proposals A/B proportionately. Provide alternatives, "
            "proposed QA and source paths. Distinguish proposed from executed checks. "
            "Do not claim proven write access, publication or functional acceptance without evidence.\n"
            "Record complete for each case after its source reading, before the next case, "
            "then return both assessments in your chat. Do not write answers into this directory, "
            "read another directory, use external systems or simulate human approval.\n\n"
            "Use: python -X utf8 read_material.py <operation> [case] [filename]. "
            "Operations: manifest, bootstrap, state, list, read, search, complete. "
            "Recover truncated output fully and retain repeated accesses in receipts.\n\n"
            "Change record: prepared fictional comparison instructions; no real acceptance. "
            "Refs: ADR-0025, ADR-0027.\n")


def prepare(destination, framework):
    destination, framework = destination.resolve(), framework.resolve()
    if destination.exists():
        raise ValueError("Existing laboratory destination is preserved")
    if destination.is_relative_to(framework):
        raise ValueError("Destination must be outside the framework checkout")
    protocol = plan()
    # The existing generator verifies the public pin, dirty runtime and tracked inputs.
    # Build its sanitized templates outside both the real checkout and final destination.
    with tempfile.TemporaryDirectory(prefix="retrieval-templates-") as temporary:
        templates = Path(temporary) / "seeds"
        command([sys.executable, "-X", "utf8", str(FIXTURES / "create_fixtures.py"),
                 str(templates), "--framework", str(framework)])
        destination.mkdir(parents=True)
        frozen = {"protocol": protocol, "kit_sha256": kit_hashes(), "sources": {},
                  "bootstrap_files": load(templates / "reviewer-a/runtime/runtime-manifest.json")["bootstrap_files"],
                  "expected": load(templates / "expected-restricted.json")}
        records, grading = {}, {}
        for row in protocol["sessions"]:
            room = destination / row["id"]
            template = templates / ("reviewer-a" if row["conditions"]["GARDEN"] == "INDEX" else "reviewer-b")
            room.mkdir()
            # Only tracked files of newly generated synthetic templates are selected.
            for name in command(["git", "ls-files", "-z"], template).split("\0"):
                if not name:
                    continue
                target = room / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(template / name, target)
            (room / "TASK.md").write_text(task(row), encoding="utf-8")
            for args in (["git", "init", "--initial-branch=main"],
                         ["git", "add", "--", "runtime", "read_material.py", ".gitignore", "TASK.md"],
                         ["git", "-c", "user.name=Fictional Comparison Fixture",
                          "-c", "user.email=fixture@example.invalid", "commit",
                          "-m", "test(pilot): prepare fictional comparison sources",
                          "-m", "Refs: ADR-0025, ADR-0027"]):
                command(args, room)
            frozen["sources"][row["id"]] = source_hashes(room)
            records[row["id"]] = {"run_kind": "NOT_RUN", "participant_type": None,
                "independent": None, "prior_case_exposure": None,
                "independence_evidence": None, "provider": None, "model": None}
            grading[row["id"]] = {case: {"reviewer_role": None, "evidence_note": None,
                **{check: None for check in CHECKS}} for case in row["order"]}
        save(destination / "coordinator.json", frozen)
        save(destination / "run-records.json", records)
        save(destination / "quality-review.json", grading)
    return {"status": "PREPARED_NOT_RUN", "planned_sessions": 8,
            "planned_case_observations": 16, "actual_independent_sessions": 0}


def summarize(root):
    frozen = load(root / "coordinator.json")
    if frozen["protocol"] != plan() or frozen["kit_sha256"] != kit_hashes():
        raise ValueError("Frozen protocol or measurement tooling changed")
    records, reviews = load(root / "run-records.json"), load(root / "quality-review.json")
    output, session_counts, overhead = [], Counter(), []
    operations = {"manifest", "bootstrap", "state", "list", "read", "search", "complete"}
    for row in frozen["protocol"]["sessions"]:
        sid, room = row["id"], root / row["id"]
        record, errors = records[sid], []
        intact = source_hashes(room) == frozen["sources"][sid]
        if not intact or command(["git", "status", "--porcelain"], room).strip():
            errors.append("source mutation or unexpected file")
        receipt_file = room / "receipts.jsonl"
        receipts = [json.loads(line) for line in receipt_file.read_text(encoding="utf-8").splitlines()] if receipt_file.exists() else []
        allowed_paths = set(frozen["sources"][sid])
        previous_time = None
        for r in receipts:
            if r["operation"] not in operations or r["case"] not in [None, "GARDEN", "SKY"]:
                raise ValueError("Invalid receipt operation/case")
            if any(type(r[k]) is not int or r[k] < 0 for k in ("bytes_inspected", "bytes_returned")):
                raise ValueError("Invalid receipt byte counts")
            timestamp = datetime.fromisoformat(r["at"])
            if timestamp.tzinfo is None or (previous_time and timestamp < previous_time):
                raise ValueError("Receipt timestamps must be zoned and ordered")
            previous_time = timestamp
            if any(p not in allowed_paths for p in r["paths"]):
                errors.append("receipt references an unprepared source")
            if r["case"] is not None:
                for p in r["paths"]:
                    if "/pilot-cases/" in p and f"/pilot-cases/{r['case']}/" not in p:
                        errors.append("cross-case source access")
            if r["operation"] in {"manifest", "bootstrap"} and r["case"] is not None:
                errors.append("common source incorrectly attributed to a case")
            if r["operation"] not in {"manifest", "bootstrap"} and r["case"] is None:
                errors.append("case operation missing its case")
            if r["operation"] == "bootstrap" and r["paths"] != ["runtime/" + p for p in frozen["bootstrap_files"]]:
                errors.append("incomplete or reordered bootstrap")
        common = [r for r in receipts if r["case"] is None]
        case_receipts = [r for r in receipts if r["case"] is not None]
        overhead.append({"session": sid, "reader_operations": len(common),
            "source_bytes_inspected": sum(r["bytes_inspected"] for r in common),
            "bytes_returned": sum(r["bytes_returned"] for r in common),
            "bootstrap_invocations": sum(r["operation"] == "bootstrap" for r in common)})
        if receipts:
            first_case = next((i for i, r in enumerate(receipts) if r["case"] is not None), len(receipts))
            if receipts[0]["operation"] != "manifest" or not any(r["operation"] == "bootstrap" for r in receipts[:first_case]):
                errors.append("mandatory bootstrap missing before case reads")
            sequence = []
            for r in case_receipts:
                if not sequence or sequence[-1] != r["case"]:
                    sequence.append(r["case"])
            if sequence != row["order"]:
                errors.append("case order incomplete or interleaved")
            for case in row["order"]:
                part = [r for r in case_receipts if r["case"] == case]
                if not part or part[-1]["operation"] != "complete" or sum(r["operation"] == "complete" for r in part) != 1:
                    errors.append("case completion missing or repeated")
        independent = (record["run_kind"] == "INDEPENDENT_SESSION" and
            record["participant_type"] in {"AI", "HUMAN"} and record["independent"] is True and
            record["prior_case_exposure"] is False and
            isinstance(record["independence_evidence"], str) and bool(record["independence_evidence"].strip()))
        kind = record["run_kind"]
        if kind not in {"NOT_RUN", "MECHANICAL_DRY_RUN", "INDEPENDENT_SESSION"}:
            raise ValueError("Invalid run kind")
        session_counts["declared_independent_with_receipts"] += int(independent and bool(receipts))
        session_counts["mechanical_with_receipts"] += int(kind == "MECHANICAL_DRY_RUN" and bool(receipts))
        for case in row["order"]:
            part = [r for r in case_receipts if r["case"] == case]
            paths = {p for r in part for p in r["paths"]}
            index = f"runtime/evidence/pilot-cases/{case}/INDEX.md"
            index_inspected = index in paths
            index_used = any(r["operation"] == "read" and r["paths"] == [index] for r in part)
            case_errors = list(errors)
            document_reads = [r for r in part if any(f"/pilot-cases/{case}/" in p for p in r["paths"])]
            first_is_index = bool(document_reads) and document_reads[0]["operation"] == "read" and document_reads[0]["paths"] == [index]
            if row["regime"] == "guided" and row["conditions"][case] == "INDEX" and part and not first_is_index:
                case_errors.append("guided index consultation missing or late")
            grade = reviews[sid][case]
            if any(grade[k] is not None and type(grade[k]) is not bool for k in CHECKS):
                raise ValueError("Quality review fields must be true, false or null")
            reviewed = bool(grade["reviewer_role"] and grade["evidence_note"]) and all(grade[k] is not None for k in CHECKS)
            quality = "PASS" if reviewed and all(grade[k] for k in CHECKS) else "FAIL" if reviewed else "NOT_REVIEWED"
            eligible = bool(part) and independent and not case_errors and quality == "PASS"
            interval = ((datetime.fromisoformat(part[-1]["at"]) - datetime.fromisoformat(part[0]["at"])).total_seconds() if part else None)
            output.append({"session": sid, "regime": row["regime"], "case": case,
                "condition": row["conditions"][case], "run_kind": kind,
                "has_receipts": bool(part), "source_integrity": intact,
                "protocol_errors": sorted(set(case_errors)), "quality": quality,
                "comparison_eligible": eligible, "index_consulted": index_used,
                "index_inspected": index_inspected,
                "unique_paths": len(paths), "reader_operations": len(part),
                "source_bytes_inspected": sum(r["bytes_inspected"] for r in part),
                "bytes_returned": sum(r["bytes_returned"] for r in part),
                "case_interval_seconds": interval})
    groups = []
    for regime in ("spontaneous", "guided"):
        for case in ("GARDEN", "SKY"):
            for condition in ("INDEX", "FLAT"):
                selected = [r for r in output if r["regime"] == regime and r["case"] == case and r["condition"] == condition and r["comparison_eligible"]]
                groups.append({"regime": regime, "case": case, "condition": condition,
                    "eligible_observations": len(selected),
                    "mean_source_bytes": statistics.mean(r["source_bytes_inspected"] for r in selected) if selected else None,
                    "index_consultations": sum(r["index_consulted"] for r in selected)})
    return {"protocol_id": frozen["protocol"]["protocol_id"],
        "efficacy_status": "EXPLORATORY_ONLY" if session_counts["declared_independent_with_receipts"] else "NOT_RUN",
        "declared_independent_sessions": session_counts["declared_independent_with_receipts"],
        "mechanical_sessions": session_counts["mechanical_with_receipts"],
        "quality_note": "Manual source-based review is required. Self-reported independence and receipts are not tamper-proof proof.",
        "balanced_design_complete": all(r["comparison_eligible"] for r in output),
        "eligible_case_observations": sum(r["comparison_eligible"] for r in output),
        "automatic_savings_or_promotion_claim": False, "token_consumption": None, "financial_savings": None,
        "observations": output, "session_overhead": overhead, "groups": groups}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    create = sub.add_parser("prepare")
    create.add_argument("destination", type=Path)
    create.add_argument("--framework", type=Path, required=True)
    measure = sub.add_parser("summarize")
    measure.add_argument("laboratory", type=Path)
    args = parser.parse_args()
    try:
        result = prepare(args.destination, args.framework) if args.operation == "prepare" else summarize(args.laboratory.resolve())
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Cannot complete comparison operation: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
