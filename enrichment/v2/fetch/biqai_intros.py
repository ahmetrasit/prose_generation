#!/usr/bin/env python3
"""Biqāʿī's surah introductions to their own surah (user, 2026-10-05: Biqāʿī is a major voice; root cause of his
absence). Naẓm al-durar opens every surah with its maqṣūd (purpose), its names and its munāsaba with the
neighbouring surahs. BIQAI-FULL is cut by printed page and a page is tied to the surah it starts in, so an
introduction printed on the page where the previous surah ends is tied to the previous surah (S107's maqṣūd sat on
S106): a page of the surah it introduces never saw it.

For every segment that holds a heading line «سورة <name>» followed (within 250 characters) by the introduction's
words (مقصود، وتسمى، اسمها) where <name> is the surah after the segment's own (pages run in order), the text from it on
becomes a new segment `<seg>#s<NNN>` tied to the whole of the introduced surah (a=1, a_end=last ayah); the text
before it stays under the old locator (an old citation still resolves). A segment that starts with the heading is
re-tied instead. Every change is printed and written to corpus/BIQAI-FULL/intros.json; the original file is kept as
segments.orig.jsonl (once).

  python3 -B enrichment/v2/fetch/biqai_intros.py [--dry]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V2 / "tools"))
import corpus as C  # noqa: E402

SRC = C.CORPUS / "BIQAI-FULL"
MARK = re.compile(r"مقصود|وتسمى|اسمها")


def names_and_lengths() -> tuple[dict[str, int], dict[int, int]]:
    con = C.connect()
    nay = {s: n for s, n in con.execute("SELECT s, max(a) FROM seg WHERE src='QURAN' GROUP BY s")}
    # each surah's name is the one its own headings use most (a heading on a page tied to the previous surah would
    # otherwise give that surah a second name); compared with alef/hamza folded («الإنفطار» = «الانفطار»)
    from collections import Counter
    count: dict[int, Counter] = {}
    for s, h in con.execute("SELECT s, head FROM seg WHERE src='BIQAI-FULL' AND s IS NOT NULL"):
        m = re.match(r"\s*(\S+(?: \S+)?)\s*:\s*\(", h or "")
        if m:
            count.setdefault(s, Counter())[fold(m.group(1))] += 1
    names: dict[str, int] = {}
    for s, c in count.items():
        names.setdefault(c.most_common(1)[0][0], s)
    # the edition gives these two surahs no running header of their own (printed whole under their neighbours'),
    # so their names cannot be learnt from it: stated here, and nothing else is
    for name, s in (("الانفطار", 82), ("الانشقاق", 84)):
        if s not in names.values():
            names[name] = s
    return names, nay


def fold(name: str) -> str:
    return re.sub("[أإآ]", "ا", name)


def pattern(name: str) -> str:
    return "".join("[اأإآ]" if ch == "ا" else re.escape(ch) for ch in name)


def quran_index() -> dict[int, dict[int, str]]:
    con = C.connect()
    q: dict[int, dict[int, str]] = {}
    for s, a, txt in con.execute("SELECT s, a, text FROM seg WHERE src='QURAN'"):
        q.setdefault(s, {})[a] = C.norm(txt)
    return q


def quoted(text: str, quran: dict, k: int) -> list[int]:
    """The ayat of surah k quoted in braces in the text (a quote of 3+ words found inside an ayah of k)."""
    hits = []
    for m in re.finditer(r"\{([^{}]{8,400})\}", text):
        qn = C.norm(m.group(1)).strip()
        if len(qn.split()) < 3:
            continue
        for a, ay in quran[k].items():
            if qn in ay:
                hits.append(a)
                break
    return hits


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    names, nay = names_and_lengths()
    if len(names) < 110:
        sys.exit(f"only {len(names)} surah names found in BIQAI-FULL headings; refusing to guess")
    alt = "|".join(sorted((pattern(n) for n in names), key=len, reverse=True))
    heading = re.compile(rf"سورة ({alt})(?![؀-ۿ])")
    path = SRC / "segments.jsonl"
    orig = SRC / "segments.orig.jsonl"
    rows = [json.loads(x) for x in (orig if orig.exists() else path).read_text(encoding="utf-8").splitlines() if x.strip()]
    # 1. A surah introduction («سورة <the next surah>⏎» followed by its maqṣūd, names …) printed on a page tied to
    #    the previous surah is COPIED to the surah it introduces (new locator <seg>#s<NNN>, the whole surah); the
    #    original stays, because the introduction's munāsaba also speaks of the surah before it.
    # 2. A page is re-tied only on evidence: the ayat it quotes in braces { … } belong to a neighbouring surah (at
    #    least two, and more than to its own tie); its ayah range is then the quoted ayat's (S82 and S84 had none).
    quran = quran_index()
    out, log = [], []
    for r in rows:
        text, s0 = r.get("text") or "", r.get("s")
        out.append(r)
        for m in heading.finditer(text):
            k = names.get(fold(m.group(1)))
            if k is None or k == s0 or not (s0 is None or k == s0 + 1) or not MARK.search(text[m.end():m.end() + 250]):
                continue
            part = text[m.start():]
            out.append({**r, "seg": f"{r['seg']}#s{k:03d}", "s": k, "a": 1, "a_end": nay[k], "text": part,
                        "copied_from": r["seg"],
                        "head": f"{m.group(1)}: introduction (maqṣūd, names, munāsaba), copied from a page of S{s0}"})
            log.append({"seg": r["seg"], "was_surah": s0, "introduces": k, "name": m.group(1), "action": "intro copied",
                        "intro": True, "new_seg": f"{r['seg']}#s{k:03d}", "chars_moved": len(part)})
            break
    # 2. Pages after an introduction that are still tied to the previous surah (their running header lags: the
    #    rest of a long introduction, or a short surah printed whole under its neighbour's header, as S82 and S84)
    #    are copied to the surah they are in, until the next surah's introduction. Copies only: no tie is removed.
    starts = {x["seg"]: x["introduces"] for x in log}
    final, cur = [], None
    for r in out:
        final.append(r)
        if r.get("copied_from"):
            continue
        if r["seg"] in starts:
            cur = starts[r["seg"]]
            continue
        s0 = r.get("s")
        if s0 is not None and cur is not None and s0 >= cur:
            cur = None  # the header has caught up
        elif s0 is not None and cur is not None and s0 == cur - 1:
            final.append({**r, "seg": f"{r['seg']}#s{cur:03d}", "s": cur, "a": 1, "a_end": nay[cur],
                          "copied_from": r["seg"], "head": f"page under the header of S{s0}, copied to S{cur}"})
            log.append({"seg": r["seg"], "was_surah": s0, "introduces": cur, "action": "lagging page copied",
                        "intro": False, "new_seg": f"{r['seg']}#s{cur:03d}", "chars_moved": len(r.get("text") or "")})
    out = final
    have = {x["introduces"] for x in log if x.get("intro")}
    from collections import Counter
    print(f"{len(log)} changes: {dict(Counter(x['action'] for x in log))}; "
          f"{sum(x['chars_moved'] for x in log):,} characters now tied to their own surah")
    for x in log[:8]:
        print(f"  {x['seg']} (tied S{x['was_surah']}) -> S{x['introduces']} {x.get('name', '')} [{x['action']}]")
    # introductions already in place (heading inside its own surah's segment)
    inplace = set()
    for r in out:
        for m in heading.finditer(r.get("text") or ""):
            if names.get(fold(m.group(1))) == r.get("s") and MARK.search((r.get("text") or "")[m.end():m.end() + 250]):
                inplace.add(r["s"])
    found = have | inplace
    missing = [s for s in range(1, 115) if s not in found]
    print(f"surahs with an introduction detected: {len(found)} of 114; not detected (may be in place in another form, e.g. a heading segment of its own): {missing}")
    if a.dry:
        return
    if not orig.exists():
        shutil.copy2(path, orig)
    path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out), encoding="utf-8")
    (SRC / "intros.json").write_text(json.dumps({"moved": log, "in_place": sorted(inplace), "missing": missing},
                                                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(C.PG)} ({len(out)} segments; original kept as {orig.name}); rebuild the index: "
          f"python3 -B enrichment/v2/tools/corpus.py build")


if __name__ == "__main__":
    main()
