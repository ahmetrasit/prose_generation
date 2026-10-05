#!/usr/bin/env python3
"""Render one page's records into its frozen v16 base. Script only.

  python3 enrichment/bible/render.py --surah 107 --target surah --annotations PATH --out DIR
  python3 enrichment/bible/render.py --surah 107 --target 107:3 --annotations PATH --out DIR

A target is the surah page (`surah`, base work/sNNN/pack/base/surah.md) or one ayah page (`S:A`, base S_A.md). Writes
DIR/surah.md or DIR/S_A.md: base paragraphs untouched, each block on its own line after the prose paragraph its
`paragraf` number names (numbered as in v16's augment: prose paragraphs from 1, headings and "Kaynaklar:" lines
unnumbered; v16 augment9 additions in an ayah reading are unnumbered and belong to the paragraph before them, so
blocks go after those additions; `capa`, a few exact words of that paragraph or its additions, confirms the number). Validated records always place; the
end section only catches unchecked input. Then the source registry, generated from the corpus metadata of every cited source (agents never write it). Blocks after one
paragraph are ordered by gelenek (islami, tevrat, incil), then by the order of `tur` in schema.json, then by id.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

V2 = Path(__file__).resolve().parent
sys.path.insert(0, str(V2.parents[1]))
from enrichment.bible import blocks as B, corpus as C

TUR_ORDER = {k: i for i, k in enumerate(B.ENUMS["tur"])}
GELENEK_ORDER = {k: i for i, k in enumerate(B.ENUMS["gelenek"])}  # islami, tevrat, incil
AYAH_SECTION = "## Kaynak katmanları"


def paragraphs(text: str) -> list[str]:
    """Split on blank lines, keeping each paragraph byte-exact."""
    return [p for p in re.split(r"\n[ \t]*\n", text.strip("\n")) if p.strip()]


def squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def find_para(paras: list[str], anchor: str) -> int | None:
    if not anchor:
        return None
    a = squash(anchor)
    hits = [i for i, p in enumerate(paras) if a in squash(p)]
    return hits[0] if hits else None


AUGMENT = "<!-- v16:augment "  # v16 augment9's marked additions in an ayah reading (part of the frozen base)
AYAH_AUGMENT = "augment.augment9.opus"  # the v16 production augment dir an ayah base must come from (v16 RUNBOOK)


def is_augment(p: str) -> bool:
    return p.lstrip().startswith(AUGMENT)


def is_prose(p: str) -> bool:
    """A numbered paragraph: not a heading, not a "Kaynaklar:" line, not a v16 augment addition (an addition belongs
    to the paragraph before it and carries that number as para=n, so the numbering is v16's own)."""
    body = p.strip()
    return not body.startswith("#") and not body.startswith("Kaynaklar:") and not is_augment(body)


def addition_text(p: str) -> str:
    """An augment addition without its marker comment line (the comment is metadata, never anchor text)."""
    return p.lstrip().split("\n", 1)[1] if "\n" in p.lstrip() else ""


def marker_mismatches(text: str) -> list[str]:
    """v16 augment markers whose para=n differs from the prose paragraph they follow (empty when all match)."""
    paras, n, bad = paragraphs(text), 0, []
    for p in paras:
        if is_prose(p):
            n += 1
        elif is_augment(p):
            head = p.lstrip().split("\n", 1)[0]  # a paragraph may start with a stray newline (triple blank line)
            m = re.search(r"\bpara=(\d+)", head)
            if not m or int(m.group(1)) != n:
                bad.append(f"{head[:90]} after ¶{n}")
    return bad


def group_end(paras: list[str], i: int) -> int:
    """The last index of paragraph i's group: i plus the v16 augment additions right after it."""
    while i + 1 < len(paras) and is_augment(paras[i + 1]):
        i += 1
    return i


def prose_index(paras: list[str]) -> dict[int, int]:
    """Prose paragraph number (from 1, as in v16 augment) -> index into paras."""
    nums, n = {}, 0
    for i, p in enumerate(paras):
        if is_prose(p):
            n += 1
            nums[n] = i
    return nums


def numbered(base: str) -> str:
    """The base with "[¶n] " before each prose paragraph (what the agent reads; the page itself is never numbered)."""
    paras, n, out = paragraphs(base), 0, []
    for p in paras:
        if is_prose(p):
            n += 1
            p = f"[¶{n}] {p}"
        out.append(p)
    return "\n\n".join(out) + "\n"


def locate(paras: list[str], r: dict) -> tuple[int | None, str]:
    """(index into paras, error) for a record's paragraf + capa."""
    nums = prose_index(paras)
    try:
        n = int(str(r.get("paragraf", "")).lstrip("¶"))
    except ValueError:
        return None, f"paragraf {r.get('paragraf')!r} is not a paragraph number"
    if n not in nums:
        return None, f"paragraf {n} outside 1-{len(nums)}"
    capa = squash(r.get("capa") or "")
    if len(capa.split()) < 3:
        return None, "capa must quote at least three words of the paragraph"
    group = lambda i: squash(" ".join([paras[i]] + [addition_text(p) for p in paras[i + 1:group_end(paras, i) + 1]]))
    if capa not in group(nums[n]):
        other = [m for m, i in nums.items() if capa in group(i)]
        return None, f"capa is not in ¶{n}" + (f" (found in ¶{other[0]})" if other else " (not found in the base)")
    return nums[n], ""


def place(paras: list[str], recs: list[dict]) -> tuple[dict[int, list[dict]], list[dict], list[str]]:
    at, tail, errors = {}, [], []
    for r in recs:
        i, err = locate(paras, r)
        if i is None:
            errors.append(f"{r.get('id')}: {err}")
            tail.append(r)
        else:
            at.setdefault(i, []).append(r)
    return at, tail, errors


def sort_blocks(rs: list[dict]) -> list[dict]:
    return sorted(rs, key=lambda r: (GELENEK_ORDER.get(r.get("gelenek"), 9), TUR_ORDER.get(r.get("tur"), 99), r["id"]))


def registry(recs: list[dict], metas: dict) -> list[str]:
    cited: dict[str, list[str]] = {}
    for r in recs:
        for loc in str(r.get("kaynak", "")).split("|"):
            loc = loc.strip()
            if loc:
                cited.setdefault(loc.split(":")[0], [])
                if loc not in cited[loc.split(":")[0]]:
                    cited[loc.split(":")[0]].append(loc)
    lines = ["## Kaynak kayıtları", ""]
    for sid in sorted(cited):
        if sid == "hafiza":
            lines.append("- **hafiza** — model belleği; kaynakta doğrulanmadı (durum: değerlendirilmedi).")
            continue
        m = metas.get(sid, {})
        who = ", ".join(x for x in (m.get("author"), m.get("title")) if x)
        bits = [who or sid]
        if m.get("edition"):
            bits.append(m["edition"])
        if m.get("access") == "hafiza":
            bits.append("yerel metin yok; bellekten")
        if m.get("relay"):
            bits.append(f"aktarma kaynağı: {m['relay']}")
        if m.get("lineage"):
            bits.append(f"soy: {m['lineage']}")
        lines.append(f"- **{sid}** — " + "; ".join(bits) + ". Atıflar: " + ", ".join(cited[sid]))
    return lines + [""]


def render_page(base: str, recs: list[dict], header: str, tail_heading: str | None,
                metas: dict) -> tuple[str, list[str]]:
    paras = paragraphs(base)
    at, tail, errors = place(paras, recs)
    slot: dict[int, list[dict]] = {}  # blocks go after the paragraph's v16 augment additions, not between them
    for i, rs in at.items():
        slot.setdefault(group_end(paras, i), []).extend(rs)
    out = [header]
    for i, p in enumerate(paras):
        out.append(p)
        for r in sort_blocks(slot.get(i, [])):
            out.append(B.tag_line(r))
    if tail:
        if tail_heading:
            out.append(tail_heading)
        for r in sort_blocks(tail):
            out.append(B.tag_line(r))
    out.append("\n".join(registry(recs, metas)))
    return "\n\n".join(out) + "\n", errors


def load(path: Path) -> list[dict]:
    recs = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                record = json.loads(line)
                if not isinstance(record, dict):
                    raise SystemExit(f'{path}:{n}: expected a JSON object')
                recs.append(record)
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{n}: {e}")
    return recs


def target_page(s: int, target: str) -> tuple[str, str, dict]:
    """(page file name, base text, base.json entry) of a target ("surah" or "S:A")."""
    pk = V2 / "work" / f"s{s:03d}" / "pack"
    base = json.loads((pk / "base.json").read_text(encoding="utf-8"))
    if target == "surah":
        info, name = base["surah"], "surah.md"
    else:
        info = base["ayat"].get(target)
        if not info:
            raise SystemExit(f"no ayah base for {target} (v16 augment9 has not run on it)")
        if f"/{AYAH_AUGMENT}/" not in info["path"]:
            raise SystemExit(f"{target}: the pack's ayah base {info['path']} is not a v16 augment9 reading (the pack "
                             f"predates the switch to augment9): rebuild it with pack.py --surah {s} --force")
        name = target.replace(":", "_") + ".md"
    text = (pk / 'base' / name).read_text(encoding='utf-8')
    if hashlib.sha256(text.encode()).hexdigest() != info['sha256']:
        raise ValueError(f'{target}: frozen base bytes differ from base.json')
    return name, text, info


def render(s: int, target: str, recs: list[dict], out: Path) -> tuple[Path, list[str]]:
    name, base, info = target_page(s, target)
    metas = {m["id"]: m for m in C.sources()}
    head = (f"<!-- schema:zenginlestirme {B.SCHEMA['version']}; target:{'S' + str(s) if target == 'surah' else target}; "
            f"base:{info['path']} sha256:{info['sha256']}; rendered:{date.today().isoformat()} -->")
    text, errors = render_page(base, recs, head, None if target == "surah" else AYAH_SECTION, metas)
    out.mkdir(parents=True, exist_ok=True)
    (out / name).write_text(text, encoding="utf-8")
    return out / name, errors


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--target", default="surah")
    ap.add_argument("--annotations", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    page, errors = render(a.surah, a.target, load(a.annotations), a.out)
    for e in errors:
        print("PLACEMENT", e)
    print(f"rendered S{a.surah} {a.target} -> {page}; placement errors: {len(errors)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
