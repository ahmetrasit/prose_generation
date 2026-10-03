#!/usr/bin/env python3
"""Write enrichment/v2/SCHEMA.md from schema.json (the JSON is the source of truth; never edit SCHEMA.md by hand)."""
import json
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
S = json.loads((V2 / "schema.json").read_text(encoding="utf-8"))

PREFACE = f"""# Annotation schema {S['version']} (generated from schema.json — do not edit)

Every block is one line in the rendered page and one JSON object in annotations.jsonl:

```
{{id:"S107-HDS-001", tur:hadis, ayet:"107:6", islev:destek, iliski:tematik, durum:acik, kat:ek, derece:sahih, derece_veren:"Müslim", metin:"…", kaynak:"MUSLIM:2985"}}
```

- Keys and values are ASCII-folded Turkish. The reader shows labels in Turkish, English or German from schema.json.
- Required in every block: {', '.join(S['block']['required'])}. Further fields are required by type (see below).
- `id` = S<surah, 3 digits>-<kod of the type>-<NNN>. `ayet` = this page's ayah or range ("107:1-3"; several with |).
- `kaynak` = corpus locators, pipe-separated, exactly as `tools/corpus.py` prints them, or `hafiza` (model memory).
- `metin` = one paragraph in the page language; at most {S['block']['word_limits']['temel']} words (temel, ek) or
  {S['block']['word_limits']['arastirma']} (arastirma).
- Placement (records only, not rendered): `capa` = an exact sentence of the base of the page the record belongs to
  (the surah page or one ayah page; one call writes one page's records); without it the block goes to the end.
"""


def cell(x: str) -> str:
    return str(x).replace("|", "\\|")


def table(name: str) -> list[str]:
    e = S["enums"][name]
    has_kod = any("kod" in v for v in e.values())
    head = "| value | " + ("kod | " if has_kod else "") + "tr | en | definition |"
    rows = [head, "|" + "---|" * (head.count("|") - 1)]
    for k, v in e.items():
        rows.append(f"| `{k}` | " + (f"{v.get('kod', '')} | " if has_kod else "")
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


if __name__ == "__main__":
    main()
