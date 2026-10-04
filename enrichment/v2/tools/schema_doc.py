#!/usr/bin/env python3
"""Write enrichment/v2/SCHEMA.md from schema.json (the JSON is the source of truth; never edit SCHEMA.md by hand)."""
import json
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
S = json.loads((V2 / "schema.json").read_text(encoding="utf-8"))

PREFACE = f"""# Annotation schema {S['version']} (generated from schema.json — do not edit)

Every block is one line in the rendered page and one JSON object in annotations.jsonl:

```
{{id:"S107-HDS-001", gelenek:islami, tur:hadis, ayet:"107:6", islev:destek, iliski:tematik, durum:acik, kat:ek, derece:sahih, derece_veren:"Müslim", metin:"…", kaynak:"MUSLIM:2985"}}
{{id:"S107-MTF-001", gelenek:incil, tur:motif, ayet:"107:6", islev:karsit, iliski:tematik, durum:acik, kat:ek, nusha:yunanca_ahit, tarihleme:kuran_oncesi, bag:benzerlik, metin:"…", kaynak:"SBLGNT:Matt.6.5"}}
```

- Two passes write blocks to the same frozen base and never read each other's records: the Islamic-literature pass
  (gelenek islami, stamped by the script) and the Bible pass (gelenek tevrat or incil, per block). A merged page
  shows, after each base paragraph, its islami blocks, then its tevrat blocks, then its incil blocks.

- Keys and values are ASCII-folded Turkish. The reader shows labels in Turkish, English or German from schema.json.
- Required in every block: {', '.join(S['block']['required'])}. Further fields are required by type (see below).
- `id` = S<surah, 3 digits>-<kod of the type>-<NNN>. `ayet` = this page's ayah or range ("107:1-3"; several with |).
- `kaynak` = corpus locators, pipe-separated, exactly as `tools/corpus.py` prints them, or `hafiza` (model memory).
- `metin` = one paragraph in the page language; at most {S['block']['word_limits']['temel']} words (temel, ek) or
  {S['block']['word_limits']['arastirma']} (arastirma).
- Placement (records only, not rendered), both required: `paragraf` = the number of a prose paragraph of the base of
  the page the record belongs to (numbered from 1 as in v16's augment; headings and "Kaynaklar:" lines unnumbered;
  the pack's numbered/ files show the numbers; v16 augment8 additions in an ayah base, `<!-- v16:augment … para=n -->`,
  are unnumbered and belong to ¶n), and `capa` = at least three exact words of that paragraph or of its additions, which
  confirm the number. The block is rendered right after that paragraph (after its additions); there are no
  end-of-page blocks, and a record whose number and words do not match is dropped. Both passes number the same base, so they merge by
  paragraph.
"""


def cell(x: str) -> str:
    return str(x).replace("|", "\\|")


def table(name: str) -> list[str]:
    e = S["enums"][name]
    has_kod = any("kod" in v for v in e.values())
    has_gel = any("gelenek" in v for v in e.values())
    head = "| value | " + ("kod | " if has_kod else "") + ("gelenek | " if has_gel else "") + "tr | en | definition |"
    rows = [head, "|" + "---|" * (head.count("|") - 1)]
    for k, v in e.items():
        rows.append(f"| `{k}` | " + (f"{v.get('kod', '')} | " if has_kod else "")
                    + (f"{', '.join(v.get('gelenek', []))} | " if has_gel else "")
                    + f"{v['label']['tr']} | {v['label']['en']} | {cell(v['def'])} |")
    return rows


def main() -> None:
    out = [PREFACE, "## Fields", "", "| field | tr | en | required for | definition |", "|---|---|---|---|---|"]
    for k, f in S["fields"].items():
        req = "all" if k in S["block"]["required"] else ", ".join(
            f"{a}: {'|'.join(b)}" for a, b in (f.get("required_for") or {}).items())
        enum = f" Values: `{f['enum']}` table." if f.get("enum") else ""
        out.append(f"| `{k}` | {f['label']['tr']} | {f['label']['en']} | {cell(req)} | {cell(f['def'])}{enum} |")
    for name in S["enums"]:
        out += ["", f"## `{name}`", ""] + table(name)
    out += ["", "## Rules", ""] + [f"- **{r['id']}**: {r['def']}" for r in S["rules"]]
    (V2 / "SCHEMA.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote", V2 / "SCHEMA.md")
    card()


def card() -> None:
    """SCHEMA_CARD.md: the compact form agents read (values and requirements, no labels in other languages)."""
    req_by: dict[str, list[str]] = {}
    for k, f in S["fields"].items():
        for axis, vals in (f.get("required_for") or {}).items():
            for v in vals:
                req_by.setdefault(f"{axis}:{v}", []).append(k)
    out = [f"# Schema {S['version']} card for the Islamic-literature pass (generated from schema.json; the full "
           "reference, with the Bible pass, is SCHEMA.md)", "",
           "Record = one JSON object per line in annotations.jsonl. Required in every record: "
           + ", ".join(k for k in S["block"]["required"] if k != "gelenek") + ", paragraf, capa "
           "(gelenek is added by the script).",
           f"- id S<sss>-<KOD>-<NNN>; ayet \"107:3\" or \"107:1-3\" (several with |); kaynak = corpus locators, "
           f"pipe-separated, or hafiza; metin one paragraph, at most {S['block']['word_limits']['temel']} words "
           f"(temel, ek) or {S['block']['word_limits']['arastirma']} (arastirma).",
           "- paragraf = the [¶n] number of the page's prose paragraph; capa = at least three exact words of it (or of "
           "its v16 additions, the unnumbered `<!-- v16:augment … para=n -->` blocks under it in an ayah base).", "",
           "## tur (KOD; traditions; extra required fields)"]
    bible_only = {"gelenek", "bag", "tarihleme", "nusha"}
    for k, v in S["enums"]["tur"].items():
        if "islami" not in v.get("gelenek", []):
            continue
        extra = sorted(set(req_by.get(f"tur:{k}", [])))
        out.append(f"- {k} ({v['kod']}; {','.join(v.get('gelenek', []))})" + (f" + {', '.join(extra)}" if extra else "")
                   + f": {v['def']}")
    out += ["", "## Values"]
    for name, e in S["enums"].items():
        if name == "tur" or name in bible_only:
            continue
        out.append(f"- {name}: " + "; ".join(f"{k} = {v['def']}" for k, v in e.items()))
    extra_islev = {k: v for k, v in req_by.items() if k.startswith("islev:")}
    if extra_islev:
        out += ["", "## Also required"] + [f"- {k}: {', '.join(sorted(set(v)))}" for k, v in extra_islev.items()]
    out += ["", "## Optional fields"] + [f"- {k}: {f['def']}" for k, f in S["fields"].items()
                                          if k not in S["block"]["required"] and not f.get("required_for")
                                          and k not in bible_only]
    out += ["", "## Rules"] + [f"- {r['id']}: {r['def']}" for r in S["rules"] if r["id"] != "paralel_bagimlilik_degil"]
    (V2 / "SCHEMA_CARD.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote", V2 / "SCHEMA_CARD.md")


if __name__ == "__main__":
    main()
