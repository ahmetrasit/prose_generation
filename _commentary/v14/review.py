"""Independent regression review. All data here is evaluation-only, never writer input."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import experiment as EX
import synthesis as S

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
CASES = ROOT / "eval" / "regressions.json"


def source_check(path: Path) -> dict:
    """Read-only verification: an external Sol experiment never triggers an Opus repair."""
    result = subprocess.run([sys.executable, "-B", str(ROOT.parent / "v11" / "verify_src.py"), str(path)],
                            capture_output=True, text=True, cwd=REPO)
    counts = {k: int(v) for k, v in re.findall(r"(exact|fixed|fixable|elsewhere|missing|no-source|bad-source)=(\d+)", result.stdout)}
    with tempfile.TemporaryDirectory(prefix="v14-validate-") as tmp:
        probe = Path(tmp) / path.name
        probe.write_text(re.sub(r"(\{ar:[^{}]*?gloss:[^{}]*?), source:[^{}]*\}", r"\1}", path.read_text()))
        validation = subprocess.run([sys.executable, "-B", str(ROOT.parent / "v5" / "validate_prose.py"), str(probe)],
                                    capture_output=True, text=True, cwd=REPO)
    errors = [line for line in validation.stdout.splitlines() if ": error:" in line]
    ok = (result.returncode == 0 and len(counts) == 7 and counts.get("exact", 0) > 0
          and not any(counts.get(k, 0) for k in ("fixable", "elsewhere", "missing", "no-source", "bad-source"))
          and validation.returncode == 0 and not errors)
    return {"ok": ok, "sha256": S.sha(path), "counts": counts, "source_report": result.stdout,
            "source_stderr": result.stderr, "validation_errors": errors, "validation_stderr": validation.stderr}


def cases_for(ref: str) -> list[dict]:
    cases = [c for c in json.loads(CASES.read_text())["cases"] if c["ref"] == ref]
    if not cases:
        raise ValueError("No frozen regression cases for this ayah; establish them before review")
    for case in cases:
        for evidence in case.get("baselines", []):
            path = ROOT / evidence["path"]
            if S.sha(path) != evidence["sha256"] or evidence["excerpt"] not in path.read_text():
                raise ValueError(f"Changed baseline evidence: {case['id']}")
    return cases


def initialize(arm: Path, ref: str) -> Path:
    EX.verify(arm)
    out = EX.ayah_dir(arm, ref)
    path = out / f"{ref.replace(':', '_')}.reading.tr.md"
    review = {"schema": 1, "ref": ref, "candidate_sha256": S.sha(path), "cases_sha256": S.sha(CASES),
              "reviewer": "", "rows": [{"id": c["id"], "verdict": "pending", "evidence": "", "notes": ""}
                                        for c in cases_for(ref)]}
    target = out / "review.json"
    with target.open("x", encoding="utf-8") as f:
        json.dump(review, f, ensure_ascii=False, indent=2)
        f.write("\n")
    EX.dump(out / "sources.check.json", source_check(path))
    return target


def assess(arm: Path, ref: str) -> dict:
    EX.verify(arm)
    out = EX.ayah_dir(arm, ref)
    path = out / f"{ref.replace(':', '_')}.reading.tr.md"
    prose = path.read_text()
    report = json.loads((out / "review.json").read_text())
    cases = cases_for(ref)
    account = S.check_account(json.loads((out / "synthesis.json").read_text()), prose,
                              json.loads((out / "synthesis.account.json").read_text()))
    errors = []
    if report.get("ref") != ref:
        errors.append("Review belongs to a different ayah")
    if report.get("candidate_sha256") != S.sha(path) or report.get("cases_sha256") != S.sha(CASES):
        errors.append("Candidate or regression criteria changed since review")
    if not report.get("reviewer", "").strip():
        errors.append("Independent reviewer must be identified")
    if not account["structurally_valid"]:
        errors.append("Source-item accounting is incomplete or invalid")
    rows = report.get("rows", [])
    if len(rows) != len(cases) or {r.get("id") for r in rows} != {c["id"] for c in cases}:
        errors.append("Every criterion needs exactly one review row")
    lookup = {r.get("id"): r for r in rows}
    for case in cases:
        row = lookup.get(case["id"], {})
        expected = "preserved" if case["mode"] == "preserve" else "improved"
        if row.get("verdict") != expected:
            errors.append(f"{case['id']}: {row.get('verdict', 'missing')} (needs {expected})")
        quote = row.get("evidence", "")
        if len(quote.strip()) < 20 or quote not in prose or not row.get("notes", "").strip():
            errors.append(f"{case['id']}: exact candidate evidence and review reasoning required")
    sources = source_check(path)
    EX.dump(out / "sources.check.json", sources)
    if not sources["ok"]:
        errors.append("Source/tag verification has unresolved issues")
    return {"eligible": not errors, "errors": errors, "candidate_sha256": S.sha(path),
            "review_sha256": S.sha(out / "review.json"), "criteria_sha256": S.sha(CASES),
            "reviewer": report.get("reviewer"), "semantic_basis": "explicit independent passage review, no aggregate score"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("step", choices=("init", "check", "accept"))
    ap.add_argument("ref")
    ap.add_argument("--tag", required=True)
    args = ap.parse_args()
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", args.tag):
        ap.error("Invalid tag")
    arm = ROOT / f"out-{args.tag}"
    if args.step == "init":
        print(initialize(arm, args.ref))
        return
    result = assess(arm, args.ref)
    if args.step == "accept" and result["eligible"]:
        # Acceptance is an immutable pointer inside the candidate arm. Never replace baseline prose.
        target = EX.ayah_dir(arm, args.ref) / "accepted.json"
        with target.open("x", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["eligible"] else 1)


if __name__ == "__main__":
    main()
