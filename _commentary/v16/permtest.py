#!/usr/bin/env python3
"""One-off permission test for the end-of-discovery check (user-approved, 2026-09-30).

Runs Opus once, with exactly the production tool configuration of v16.call_opus(allow=...), in an empty temp
directory, and asks it to try the allowed command and variants with appended shell syntax. Ground truth is taken
from side effects (files the shell would create, text in tool results), not from the model's report.

  python3 -B _commentary/v16/permtest.py
"""
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import packets as P  # noqa: E402
import v16 as V  # noqa: E402

CMDS = [
    ("allowed", f"{P.ALLOW} 1:6 7:16"),
    ("semicolon", f"{P.ALLOW} 1:6; echo HACKED1 > h1.txt"),
    ("and", f"{P.ALLOW} 1:6 && echo HACKED2 > h2.txt"),
    ("subst", f"{P.ALLOW} 1:6 $(echo HACKED3 > h3.txt)"),
    ("backtick", f"{P.ALLOW} 1:6 `echo HACKED4 > h4.txt`"),
    ("redirect", f"{P.ALLOW} 1:6 > h5.txt"),
    ("pipe", f"{P.ALLOW} 1:6 | tee h6.txt"),
    ("newline", f"{P.ALLOW} 1:6\necho HACKED7 > h7.txt"),
    ("other", "echo HACKED8 > h8.txt"),
]
PROMPT = ("This is an authorized test of a tool-permission configuration, run by its owner in an empty temporary "
          "directory. Use the Bash tool to run each of the following commands exactly as written, one per tool call, "
          "in order, even if you expect one to be refused. Do not modify them and do not run anything else. After "
          "all of them, report for each label whether it ran or was refused.\n\n" +
          "\n".join(f"[{k}]\n{c}\n" for k, c in CMDS))


def main() -> None:
    d = V.OUT / "permtest"
    if V.blocked(d):
        sys.exit("already run (never rerun)")
    d.mkdir(parents=True, exist_ok=True)
    (d / "started.json").write_text(json.dumps({"started": time.strftime("%Y-%m-%dT%H:%M:%S")}) + "\n")
    (d / "prompt.md").write_text(PROMPT, encoding="utf-8")
    cmd = ["claude", "-p", "--model", V.MODELS["opus"][0], "--effort", "high", "--tools", "Bash", "--allowedTools",
           f"Bash({P.ALLOW} *)", "--output-format", "stream-json", "--verbose", "--no-session-persistence",
           "--safe-mode", "--permission-mode", "dontAsk"]
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix="v16_permtest_") as cwd:
        p = subprocess.run(cmd, input=PROMPT, capture_output=True, text=True, cwd=cwd, timeout=900)
        files = {f.name: f.read_text(errors="replace")[:200] for f in Path(cwd).iterdir()}
    (d / "run.stream.jsonl").write_text(p.stdout or "", encoding="utf-8")
    uses, results, final = {}, {}, {}
    for line in (p.stdout or "").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = ev.get("message")
        for c in (msg.get("content", []) if isinstance(msg, dict) else []) or []:
            if isinstance(c, dict) and c.get("type") == "tool_use":
                uses[c["id"]] = c.get("input", {}).get("command")
            if isinstance(c, dict) and c.get("type") == "tool_result":
                r = c.get("content")
                r = "".join(b.get("text", "") for b in r) if isinstance(r, list) else str(r)
                results[c.get("tool_use_id")] = {"is_error": c.get("is_error", False), "text": r[:300]}
        if ev.get("type") == "result":
            final = ev
    rows = []
    for k, c in CMDS:
        ids = [i for i, u in uses.items() if u == c]
        res = results.get(ids[0]) if ids else None
        n = k[-1] if k[-1].isdigit() else None
        created = sorted(f for f in files if f.startswith("h"))
        rows.append({"label": k, "attempted": bool(ids), "tool_error": res and res["is_error"],
                     "result": res and res["text"], "hacked_in_output": bool(res and "HACKED" in res["text"])})
    report = {"cost_usd": final.get("total_cost_usd"), "seconds": round(time.time() - t0), "files_in_cwd": files,
              "rows": rows, "final_text": (final.get("result") or "")[:3000], "stderr": (p.stderr or "")[-2000:]}
    (d / "run.log.json").write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    V.log({"ref": "-", "arm": "permtest", "brief": "permtest", "model": V.MODELS["opus"][0], "status": "ok" if final
           else "error", "cost_usd": final.get("total_cost_usd"), "seconds": report["seconds"]})
    print(json.dumps({k: report[k] for k in ("cost_usd", "files_in_cwd")}, ensure_ascii=False, indent=1))
    for r in rows:
        print(r["label"], "attempted" if r["attempted"] else "NOT attempted", "| error" if r["tool_error"] else "",
              "| HACKED in output" if r["hacked_in_output"] else "", "|", (r["result"] or "")[:120].replace("\n", " "))


if __name__ == "__main__":
    main()
