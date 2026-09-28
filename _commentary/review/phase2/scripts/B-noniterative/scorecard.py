"""Frozen mechanical scorecard (the script half of the evaluation; the other half is the user's blind read).

Per commentary file:
  form      words, paragraphs, mean/max words per paragraph, headings, disclaimer rate per 1,000 words
            ('anlamına gelmez', 'demek değildir', 'söylemez', 'iddia etmez', 'kesin değildir'), 'değil,' count
  sourcing  Arabic tags, share with a source attribute (src: / source:)
  reach     distinct refs, same-surah, other-surah (focus excluded)
  pooled    recall of refs against the POOL = union of refs of every file scored for that ayah (TREC-style
            pooling: no single earlier run is the gold; new arms enlarge the pool)
  watch     evaluation-only ingredient probes for the watch cases (never shown to any model)
Usage: python3 scorecard.py  (runs the built-in demonstration sets: 1:6 four configurations, 4:34, 18:86, 18:96, 29:38)
"""
import re, os, sys, collections
C = "/Volumes/OZTURK/_projects/prose_generation/_commentary"
OUT = os.path.dirname(os.path.abspath(__file__))
REF = re.compile(r"(?<![\d.:/])(\d{1,3}):(\d{1,3})(?::\d{1,3})?(?![\d])")
DISC = re.compile(r"anlamına gelmez|demek değildir|söylemez|iddia etmez|kesin değildir|anlamına gelmiyor|söylemiyor",
                  re.I)
TAG = re.compile(r"\{\{?ar:[^}]*\}\}?")

WATCH = {
    "29:38": [("eye film named", r"göz\w*[^.]{0,80}(perde|zar|ağ|örtü|hastalı)|(perde|zar|örtü)[^.]{0,80}göz"),
              ("spider-house tie (29:41 or örümcek)", r"29:41|örümcek"),
              ("kohl", r"sürme|kohl|كحل")],
    "18:86": [("ḥamaʾ creation passages", r"15:26|15:28|15:33"),
              ("observer / looking at the clay", r"(gör|bak|seyr|tanık)\w*[^.]{0,120}(balçık|çamur)|(balçık|çamur)[^.]{0,120}(gör|bak|tanık)")],
    "18:96": [("animating nafakha passages", r"15:29|38:72|32:9|21:91|66:12|3:49|5:110"),
              ("animating/life named", r"can (ver|üfle)|dirilt|hayat ver|ruh üfle|canlandır")],
}


def refs(text, focus):
    fs, fa = map(int, focus.split(":"))
    out = set()
    for m in REF.finditer(text):
        s, a = int(m.group(1)), int(m.group(2))
        if 1 <= s <= 114 and 1 <= a <= 286 and (s, a) != (fs, fa):
            out.add((s, a))
    return out


def score(path, focus):
    t = open(path, encoding="utf-8", errors="replace").read()
    words = t.split()
    paras = [p for p in re.split(r"\n\s*\n", t) if p.strip() and not p.strip().startswith("#")]
    pw = [len(p.split()) for p in paras] or [0]
    tags = TAG.findall(t)
    src = sum(1 for x in tags if "src:" in x or "source:" in x)
    r = refs(t, focus)
    fs = int(focus.split(":")[0])
    w = {}
    for name, rx in WATCH.get(focus, []):
        w[name] = bool(re.search(rx, t, re.I))
    return dict(words=len(words), paras=len(paras), mean_pw=round(sum(pw) / len(pw)), max_pw=max(pw),
                headings=len(re.findall(r"^#", t, re.M)), disc_per_k=round(1000 * len(DISC.findall(t)) / max(len(words), 1), 1),
                degil=t.count("değil,"), tags=len(tags), sourced=f"{src}/{len(tags)}", refs=r,
                same=len({x for x in r if x[0] == fs}), other=len({x for x in r if x[0] != fs}), watch=w)


SETS = {
    "1:6": {"v5 middle (Luna)": f"{C}/v5/middle/s001-fresh-20260910/s001/1_6/1_6.prose.middle.tr.md",
            "cold (memory)": f"{C}/v9/lines/work/1_6/synth/w10-opus-cold/1_6.reading.tr.md",
            "dict": f"{C}/v9/lines/work/1_6/synth/w10-opus-dict/1_6.reading.tr.md",
            "v11": f"{C}/v11/out/s001/1_6/1_6.reading.tr.md",
            "v15": f"{C}/v15/out/s001/1_6/commentary.tr.md"},
    "4:34": {"cold": f"{C}/v9/lines/work/4_34/synth/w10-opus-cold/4_34.reading.tr.md",
             "cold2": f"{C}/v9/lines/work/4_34/synth/w10-opus-cold2/4_34.reading.tr.md",
             "dict": f"{C}/v9/lines/work/4_34/synth/w10-opus-dict/4_34.reading.tr.md",
             "v11-script": f"{C}/v9/lines/work/4_34/synth/v11-script/4_34.reading.tr.md",
             "v15 nocap": f"{C}/v15/out-nocap/s004/4_34/commentary.tr.md"},
    "18:86": {"cold": f"{C}/v9/lines/work/18_86/synth/w10-opus-cold/18_86.reading.tr.md",
              "dict": f"{C}/v9/lines/work/18_86/synth/w10-opus-dict/18_86.reading.tr.md",
              "package": f"{C}/v9/lines/work/18_86/synth/w10-opus/18_86.reading.tr.md",
              "v11": f"{C}/v11/out/s018/18_86/18_86.reading.tr.md",
              "v5 editorial": f"{C}/v5/editorial/s018-regular-20260912/s018/18_86/18_86.prose.editorial.tr.md"},
    "18:96": {"cold": f"{C}/v9/lines/work/18_96/synth/w10-opus-cold/18_96.reading.tr.md",
              "package": f"{C}/v9/lines/work/18_96/synth/w10-opus/18_96.reading.tr.md",
              "v13": f"{C}/v13/out/s018/18_96/18_96.reading.tr.md",
              "v13 v2": f"{C}/v13/out-v2/s018/18_96/18_96.reading.tr.md",
              "v5 editorial": f"{C}/v5/editorial/s018-regular-20260912/s018/18_96/18_96.prose.editorial.tr.md"},
    "29:38": {"v9 pilot (Opus, package)": f"{C}/v9/pilot/29_38/29_38.reading.tr.md",
              "v9 pilot v2": f"{C}/v9/pilot/29_38-v2/29_38.reading.tr.md",
              "v9 opus-findings": f"{C}/v9/pilot/29_38-opus-findings/29_38.reading.tr.md",
              "v9 sol": f"{C}/v9/pilot/29_38-gpt-6-sol/29_38.reading.tr.md",
              "v9 luna": f"{C}/v9/pilot/29_38-gpt-6-luna/29_38.reading.tr.md"},
}

if __name__ == "__main__":
    lines = []
    for focus, runs in SETS.items():
        sc = {k: score(p, focus) for k, p in runs.items() if os.path.exists(p)}
        pool = set().union(*(v["refs"] for v in sc.values()))
        lines.append(f"\n## {focus}  (pool of refs over {len(sc)} runs: {len(pool)})")
        lines.append("run | words | paras | mean/max w/para | disc/1k | 'değil,' | tags sourced | refs same/other | pooled recall | watch")
        for k, v in sc.items():
            wt = "; ".join(f"{n}:{'Y' if ok else 'n'}" for n, ok in v["watch"].items())
            lines.append(f"{k} | {v['words']} | {v['paras']} | {v['mean_pw']}/{v['max_pw']} | {v['disc_per_k']} | {v['degil']} | "
                         f"{v['sourced']} | {v['same']}/{v['other']} | {len(v['refs']) / max(len(pool), 1):.2f} | {wt}")
    txt = "\n".join(lines)
    open(os.path.join(OUT, "scorecard_demo.txt"), "w").write(txt + "\n")
    print(txt)
