#!/usr/bin/env python3
"""Stage dizgi: render annotations.jsonl into the frozen v16 base (surah page and ayah pages). Script only.

  python3 enrichment/v2/render.py --surah 107 [--annotations PATH] [--out DIR]

Reads work/sNNN/pack/base/{surah.md,S_A.md} and work/sNNN/annotations.jsonl (default). Writes work/sNNN/out/:
  surah.md      the surah page: base paragraphs untouched, each block on its own line after the paragraph that
                contains its `capa` sentence, then the generated source registry
  S_A.md        one page per ayah: blocks whose `ayet` covers the ayah, after the paragraph containing `capa_ayet`,
                or under a closing "## Kaynak katmanları" section when no `capa_ayet` is given
The registry is generated from the corpus metadata of every cited source; agents never write it.
Blocks at one point are ordered by the order of `tur` in schema.json, then by id.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

V2 = Path(__file__).resolve().parent
sys.path.insert(0, str(V2 / "tools"))
import blocks as B  # noqa: E402
import corpus as C  # noqa: E402

TUR_ORDER = {k: i for i, k in enumerate(B.ENUMS["tur"])}
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


def place(paras: list[str], recs: list[dict], key: str) -> tuple[dict[int, list[dict]], list[dict], list[str]]:
    at, tail, errors = {}, [], []
    for r in recs:
        anchor = r.get(key)
        if not anchor:
            tail.append(r)
            continue
        i = find_para(paras, anchor)
        if i is None:
            errors.append(f"{r['id']}: {key} not found in base: {anchor[:80]!r}")
            tail.append(r)
        else:
            at.setdefault(i, []).append(r)
    return at, tail, errors


def sort_blocks(rs: list[dict]) -> list[dict]:
    return sorted(rs, key=lambda r: (TUR_ORDER.get(r.get("tur"), 99), r["id"]))


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


def render_page(base: str, recs: list[dict], key: str, header: str, tail_heading: str | None,
                metas: dict) -> tuple[str, list[str]]:
    paras = paragraphs(base)
    at, tail, errors = place(paras, recs, key)
    out = [header]
    for i, p in enumerate(paras):
        out.append(p)
        for r in sort_blocks(at.get(i, [])):
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
                recs.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{n}: {e}")
    return recs


def render(s: int, ann: Path, out: Path) -> list[str]:
    wd = V2 / "work" / f"s{s:03d}"
    pk = wd / "pack"
    base = json.loads((pk / "base.json").read_text(encoding="utf-8"))
    metas = C.sources_by_id() if hasattr(C, "sources_by_id") else {m["id"]: m for m in C.sources()}
    recs = load(ann)
    out.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    errors = []
    head = (f"<!-- schema:zenginlestirme {B.SCHEMA['version']}; target:S{s}; base:{base['surah']['path']} "
            f"sha256:{base['surah']['sha256']}; rendered:{stamp} -->")
    text, err = render_page((pk / "base" / "surah.md").read_text(encoding="utf-8"), recs, "capa", head, None, metas)
    errors += [f"surah.md: {x}" for x in err]
    (out / "surah.md").write_text(text, encoding="utf-8")
    for ref, info in base["ayat"].items():
        if not info:
            continue
        a = int(ref.split(":")[1])
        mine = [r for r in recs if any(x[1] <= a <= x[2] for x in B.ayah_refs(r["ayet"]))]
        head = (f"<!-- schema:zenginlestirme {B.SCHEMA['version']}; target:{ref}; base:{info['path']} "
                f"sha256:{info['sha256']}; rendered:{stamp} -->")
        text, err = render_page((pk / "base" / f"{s}_{a}.md").read_text(encoding="utf-8"), mine, "capa_ayet", head,
                                AYAH_SECTION, metas)
        errors += [f"{s}_{a}.md: {x}" for x in err if "capa_ayet not found" in x]
        (out / f"{s}_{a}.md").write_text(text, encoding="utf-8")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--annotations", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    wd = V2 / "work" / f"s{a.surah:03d}"
    errors = render(a.surah, a.annotations or wd / "annotations.jsonl", a.out or wd / "out")
    for e in errors:
        print("PLACEMENT", e)
    print(f"rendered S{a.surah} -> {a.out or wd / 'out'}; placement errors: {len(errors)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
