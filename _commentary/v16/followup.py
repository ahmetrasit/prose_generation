#!/usr/bin/env python3
"""Reconstructed follow-up to a finished v16 run (the calls ran without session persistence, so they cannot be
resumed). One new Opus call gets the run's exact prompt, then its own full response, then the follow-up questions.
Its answer is a post-hoc account by the same model on the same evidence, not a replay of the original reasoning.

  python3 -B _commentary/v16/followup.py --run-dir out/1_6/DM.r8 --topic pulley [--go]
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import v16 as V  # noqa: E402

QUESTIONS = {
    "pulley": """You wrote the reading and ledger above from the supplied evidence. The map's chain 9 (the well rig: the
pulley قامة of this ayah's ق و م hung from the نعامة crossbeam of 1:7's ن ع م, the brimming well of 1:2, water as
what keeps a traveller's affair standing in 1:4) did not enter your prose. Your ledger says:
{ledger_line}

Answer in plain English, briefly, as the editor's notes (not reader prose):
1. Why did the pulley image stay out? Name what in the evidence, the map or the brief led you there.
2. What instruction, in the writing brief or in the surah map, would have led you to use the pulley image in the
   prose where it contributes, without forcing it where it does not? Give the exact wording you would want.""",
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--topic", choices=tuple(QUESTIONS), required=True)
    ap.add_argument("--go", action="store_true", help="make the call (default: build and estimate)")
    a = ap.parse_args()
    src = V.HERE / a.run_dir
    prompt = (src / "prompt.md").read_text(encoding="utf-8")
    response = json.loads((src / "run.log.json").read_text(encoding="utf-8"))["result"].strip()
    ledger = (src / "ledger.md").read_text(encoding="utf-8")
    line = next((l for l in ledger.splitlines() if "chain 9" in l or "pulley" in l.lower()), "(no ledger line)")
    text = (prompt + "\n\n===== YOUR EARLIER RESPONSE (reading, then ledger) =====\n" + response +
            "\n\n===== FOLLOW-UP =====\n" + QUESTIONS[a.topic].format(ledger_line=line))
    d = src.parent / f"{src.name}.followup-{a.topic}"
    est = V.estimate(text, "ayah")
    print(f"{d.relative_to(V.HERE)}: {len(text):,} chars, est ${est:.2f}")
    if not a.go:
        return
    if V.blocked(d) or est >= V.GATE_USD:
        sys.exit("blocked: started before, or estimate at/over the gate")
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = V.call_opus(text, d)
    result = (obj.get("result") or "").strip()
    if result:
        (d / "answer.md").write_text(result + "\n", encoding="utf-8")
    ref = src.parent.name.replace("_", ":")
    V.log({"ref": ref, "arm": f"{src.name}.followup-{a.topic}", "brief": "followup", "model": V.MODELS["opus"][0],
           "seconds": round(time.time() - t0), "estimate_usd": round(est, 2), **V.usage_row(obj, text),
           "source_prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()})
    print(f"done: ${obj.get('total_cost_usd')} {len(result.split())}w")


if __name__ == "__main__":
    main()
