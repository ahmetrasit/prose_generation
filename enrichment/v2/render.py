#!/usr/bin/env python3
"""Render one page's records into its frozen v16 base. Script only.

  python3 enrichment/v2/render.py --surah 107 --target surah --annotations PATH --out DIR
  python3 enrichment/v2/render.py --surah 107 --target 107:3 --annotations PATH --out DIR

A target is the surah page (`surah`, base work/sNNN/pack/base/surah.md) or one ayah page (`S:A`, base S_A.md). Writes
DIR/surah.md or DIR/S_A.md: base paragraphs untouched, each block on its own line after the paragraph that contains
its `capa` sentence; blocks without a capa at the end (on an ayah page under "## Kaynak katmanları"); then the source
registry, generated from the corpus metadata of every cited source (agents never write it). Blocks at one point are
ordered by the order of `tur` in schema.json, then by id.
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


def target_page(s: int, target: str) -> tuple[str, str, dict]:
    """(page file name, base text, base.json entry) of a target ("surah" or "S:A")."""
    pk = V2 / "work" / f"s{s:03d}" / "pack"
    base = json.loads((pk / "base.json").read_text(encoding="utf-8"))
    if target == "surah":
        info, name = base["surah"], "surah.md"
    else:
        info = base["ayat"].get(target)
        if not info:
            raise SystemExit(f"no ayah base for {target}")
        name = target.replace(":", "_") + ".md"
    return name, (pk / "base" / name).read_text(encoding="utf-8"), info


def render(s: int, target: str, recs: list[dict], out: Path) -> tuple[Path, list[str]]:
    name, base, info = target_page(s, target)
    metas = {m["id"]: m for m in C.sources()}
    head = (f"<!-- schema:zenginlestirme {B.SCHEMA['version']}; target:{'S' + str(s) if target == 'surah' else target}; "
            f"base:{info['path']} sha256:{info['sha256']}; rendered:{date.today().isoformat()} -->")
    text, errors = render_page(base, recs, "capa", head, None if target == "surah" else AYAH_SECTION, metas)
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
