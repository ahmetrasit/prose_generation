#!/usr/bin/env python3
"""Ask a diagnostic follow-up inside a finished v16 call's own session (user, 2026-09-30).

  python3 -B _commentary/v16/resume.py out/1_6/<run dir> "question" [--go]

The call's started.json gives its session id, working directory, model and effort (calls from 2026-09-30 on keep
their session). The follow-up resumes that session with no tools, so the model answers from what it read and wrote.
Answers are diagnostics: they go to <run dir>/followups/ and the ledger (arm "followup"), never into a reading.
Without --go it only prints the estimate. Gate $5, as for every call. Claude Code deletes old sessions
(cleanupPeriodDays, default 30); after that a resume fails with an error.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import v16 as V  # noqa: E402

ANSWER_TOKENS = 15_000  # assumed answer length, thinking included


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run", type=Path)
    ap.add_argument("question")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    d = a.run if a.run.is_absolute() else V.HERE / a.run
    if not (d / "started.json").exists() or not (d / "run.log.json").exists():
        raise SystemExit(f"{d}: no finished call here")
    started = json.loads((d / "started.json").read_text(encoding="utf-8"))
    log = json.loads((d / "run.log.json").read_text(encoding="utf-8"))
    if log.get("is_error") or log.get("partial") or log.get("safety_stop"):
        raise SystemExit(f"{d}: the call did not end cleanly; no follow-up on it")
    sid, cwd = started.get("session_id"), started.get("session_cwd")
    if not sid or not cwd:
        raise SystemExit(f"{d}: no session recorded (calls before 2026-09-30 ran without session persistence)")
    model = next((k for k, v in V.MODELS.items() if v[0] == started.get("model")), None)
    if model is None:
        raise SystemExit(f"{d}: unknown model {started.get('model')}")
    _, w, o = V.MODELS[model]
    # The session is re-read from cache, or re-cached if the 1 h cache has expired: price it as a full cache write.
    context = (d / "prompt.md").read_text(encoding="utf-8") + (log.get("result") or "")
    est = V.est_tokens(context + a.question) * w + ANSWER_TOKENS * o
    print(f"{d.relative_to(V.HERE)}: follow-up in session {sid}; est ${est:.2f}")
    if not a.go:
        return
    ref = re.sub(r"^s0*(\d+)$", r"S\1", d.parent.name).replace("_", ":")
    if est >= V.GATE_USD:
        V.log({"ref": ref, "arm": "followup", "brief": d.name, "status": "gated", "estimate_usd": round(est, 2)})
        raise SystemExit(f"gated at ${est:.2f}")
    Path(cwd).mkdir(parents=True, exist_ok=True)  # the CLI finds the session by its cwd
    cmd = ["claude", "-p", "--resume", sid, "--model", V.MODELS[model][0], "--effort", started.get("effort", "high"),
           "--tools", "", "--output-format", "stream-json", "--verbose", "--safe-mode",
           "--permission-mode", "dontAsk", "--system-prompt", V.SYSTEM]
    env = {**os.environ, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "128000"}
    t0 = time.time()
    p = subprocess.run(cmd, input=a.question, capture_output=True, text=True, cwd=cwd, env=env)
    texts, final = [], {}
    for line in (p.stdout or "").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant" and isinstance(ev.get("message"), dict):
            texts += [c.get("text", "") for c in ev["message"].get("content", []) if c.get("type") == "text"]
        elif ev.get("type") == "result":
            final = ev
    answer = "".join(texts) or final.get("result") or ""
    fd = d / "followups"
    fd.mkdir(exist_ok=True)
    n = 1
    while True:  # never overwrite an earlier follow-up
        try:
            with (fd / f"{n:02d}.md").open("x", encoding="utf-8") as f:
                f.write(f"## Question\n\n{a.question}\n\n## Answer\n\n{answer}\n")
            break
        except FileExistsError:
            n += 1
    (fd / f"{n:02d}.stream.jsonl").write_text(p.stdout or "", encoding="utf-8")
    usage = final.get("usage", {}) or {}
    row = {"ref": ref, "arm": "followup", "brief": d.name, "followup": n,
           "model": V.MODELS[model][0], "session_id": sid, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2), "cost_usd": final.get("total_cost_usd"),
           "status": "ok" if answer and p.returncode == 0 and final and not final.get("is_error") else "error",
           "output_tokens": usage.get("output_tokens"), "returncode": p.returncode,
           "stderr_tail": (p.stderr or "")[-500:] if p.returncode else ""}
    V.log(row)
    print(f"{fd.relative_to(V.HERE)}/{n:02d}.md: {row['status']} ${row['cost_usd']}")
    if row["status"] != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
