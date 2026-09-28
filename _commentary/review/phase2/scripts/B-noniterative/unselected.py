"""The 'unselected index' of design B (verification step 4e): what the readings contain that the integrated commentary
does not, as a short list handed to the fixed challenge turn (and kept in the record: nothing lost silently).

Ingredients compared: cited refs (focus excluded), Arabic quotations (normalised, >= 2 words), 'root Bnnn' anchors.
Each unselected item carries its sentence from the reading, so the integrator sees the payoff argument, not a bare id.

Demonstration (no model runs): stand-in 'readings' and 'commentary' taken from earlier outputs of the same ayah.
"""
import re, os, sys
import load

C = load.PG + "/_commentary"
REF = re.compile(r"(?<![\d.:/])(\d{1,3}):(\d{1,3})(?::\d{1,3})?(?![\d])")
TAG = re.compile(r"\{\{?ar:\s*([^,|}]+)")
ANC = re.compile(r"([ء-ي] [ء-ي] [ء-ي](?: [ء-ي])?) (B\d{3})")


def sentences(t):
    return re.split(r"(?<=[.!?])\s+|\n+", t)


def ingredients(t, focus):
    fs, fa = map(int, focus.split(":"))
    refs = {f"{m.group(1)}:{m.group(2)}" for m in REF.finditer(t)
            if 1 <= int(m.group(1)) <= 114 and (int(m.group(1)), int(m.group(2))) != (fs, fa)}
    tags = {load.norm(x).strip() for x in TAG.findall(t) if len(load.norm(x).split()) >= 2}
    anc = {f"{r} {b}" for r, b in ANC.findall(t)}
    return refs, tags, anc


def index(readings, commentary, focus):
    ct = open(commentary, encoding="utf-8").read()
    cr, ctg, ca = ingredients(ct, focus)
    ctn = load.norm(ct)
    out = []
    for label, p in readings.items():
        t = open(p, encoding="utf-8").read()
        r, tg, a = ingredients(t, focus)
        sents = sentences(t)
        for x in sorted(r - cr):
            s = next((s for s in sents if x in s), "")
            out.append((label, "ref", x, s.strip()[:220]))
        for x in sorted(tg):
            if x not in ctn:
                s = next((s for s in sents if x in load.norm(s)), "")
                out.append((label, "quote", x, s.strip()[:220]))
        for x in sorted(a - ca):
            s = next((s for s in sents if x in s), "")
            out.append((label, "anchor", x, s.strip()[:220]))
    return out


DEMO = {
    "18:86": ({"R_mem~cold": f"{C}/v9/lines/work/18_86/synth/w10-opus-cold/18_86.reading.tr.md",
               "R_lex~dict": f"{C}/v9/lines/work/18_86/synth/w10-opus-dict/18_86.reading.tr.md"},
              f"{C}/v11/out/s018/18_86/18_86.reading.tr.md"),
    "4:34": ({"R_mem~cold": f"{C}/v9/lines/work/4_34/synth/w10-opus-cold/4_34.reading.tr.md",
              "R_lex~dict": f"{C}/v9/lines/work/4_34/synth/w10-opus-dict/4_34.reading.tr.md"},
             f"{C}/v15/out-nocap/s004/4_34/commentary.tr.md"),
    "1:6": ({"R_mem~cold": f"{C}/v9/lines/work/1_6/synth/w10-opus-cold/1_6.reading.tr.md",
             "R_lex~dict": f"{C}/v9/lines/work/1_6/synth/w10-opus-dict/1_6.reading.tr.md"},
            f"{C}/v15/out/s001/1_6/commentary.tr.md"),
}

if __name__ == "__main__":
    lines = []
    for focus, (rd, cm) in DEMO.items():
        idx = index(rd, cm, focus)
        chars = sum(len(x[3]) + len(x[2]) + 12 for x in idx)
        kinds = {}
        for x in idx:
            kinds[x[1]] = kinds.get(x[1], 0) + 1
        rchars = sum(len(open(p, encoding="utf-8").read()) for p in rd.values())
        lines.append(f"## {focus}: readings {rchars} chars (integrator input ~{int(rchars / 2.0)} tokens); "
                     f"unselected items vs stand-in commentary: {len(idx)} {kinds}; index ~{chars} chars")
        for x in idx[:8]:
            lines.append(f"   [{x[0]} {x[1]}] {x[2]} :: {x[3][:140]}")
    txt = "\n".join(lines)
    open(os.path.join(load.OUT, "unselected_demo.txt"), "w").write(txt + "\n")
    print(txt)
