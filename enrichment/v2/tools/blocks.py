"""Annotation blocks (schema 3.0): load the schema, check records, resolve sources, render tag lines.

Agents write records to annotations.jsonl (one JSON object per line); nothing else writes blocks. One call writes
the records of one page (the surah page or one ayah page). A record is the block's fields plus placement:
  {"id": "S107-HDS-001", "gelenek": "islami", "tur": "hadis", "ayet": "107:6", "islev": "destek", "iliski": "tematik", "durum": "acik",
   "kat": "ek", "derece": "sahih", "derece_veren": "Müslim", "metin": "…", "kaynak": "MUSLIM:2985",
   "paragraf": 4, "capa": "at least three exact words of prose paragraph 4 of that page's base (confirms the number)"}
The block goes right after that paragraph. Prose paragraphs are numbered as in v16's augment (render.numbered).
"""
from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((V2 / "schema.json").read_text(encoding="utf-8"))
ENUMS = SCHEMA["enums"]
FIELDS = SCHEMA["fields"]
REQUIRED = SCHEMA["block"]["required"]
LIMITS = SCHEMA["block"]["word_limits"]
KOD = {k: v["kod"] for k, v in ENUMS["tur"].items()}
PLACEMENT = ("paragraf", "capa")
ORDER = ["id", "gelenek", "tur", "ayet", "islev", "iliski", "durum", "kat", "guc", "klasik_tanik", "tarama", "taranan", "derece",
         "derece_veren", "tarihsellik", "kiraat_turu", "nusha", "tarihleme", "bag", "sozluk", "mutercim", "terim", "kayip", "yon", "kiyas", "taban",
         "hata", "alim", "ravi", "koken", "tekrar", "gerekce", "not", "metin", "kaynak"]
MODERN_DICT = {"VASIT", "MUHIT", "HANSWEHR"}
SHARED_KINDS = {"quran", "modern", "reference"}  # citable from every gelenek
MULTI = {"kayip", "nusha"}  # enum fields that take several pipe-separated values
AYET = re.compile(r"(\d+):(\d+)(?:-(\d+))?")
LOC = re.compile(r"^([A-Z][A-Z0-9-]*)(?::(.+))?$")


def words(text: str) -> int:
    return len(re.findall(r"\S+", text or ""))


class Corpus:
    """Read-only view of enrichment/corpus/corpus.sqlite for source resolution."""

    def __init__(self, index: Path):
        self.con = sqlite3.connect(index)
        self.meta = {r[0]: json.loads(r[1]) for r in self.con.execute("SELECT id, meta FROM src")}

    def resolve(self, loc: str) -> tuple[bool, str, dict]:
        """(ok, message, info). info: kind, access, sahih (hadith)."""
        m = LOC.match(loc)
        if not m:
            return False, f"malformed locator {loc!r}", {}
        sid, rest = m.group(1), m.group(2)
        meta = self.meta.get(sid)
        if not meta:
            return False, f"unknown source {sid!r}", {}
        info = {"kind": meta.get("kind"), "access": meta.get("access"), "id": sid, "gelenek": meta.get("gelenek")}
        if meta.get("access") == "hafiza":
            return True, "pointer (memory)", info
        if rest is None:
            return False, f"{loc}: locator needs a position (e.g. {sid}:107:3)", info
        row = self.con.execute("SELECT extra FROM seg WHERE seg=? OR seg LIKE ? LIMIT 1", (loc, loc + "#%")).fetchone()
        if not row:
            return False, f"{loc}: no such segment", info
        extra = json.loads(row[0] or "{}")
        if "sahih" in extra:
            info["sahih"] = bool(extra["sahih"])
            info["graded_by"] = extra.get("graded_by") or []
        return True, "ok", info


def ayah_refs(ayet: str) -> list[tuple[int, int, int]]:
    out = []
    for part in ayet.split("|"):
        m = AYET.fullmatch(part.strip())
        if not m:
            raise ValueError(part)
        s, a = int(m.group(1)), int(m.group(2))
        out.append((s, a, int(m.group(3) or a)))
    return out


def check_record(r: dict, surah: int, n_ayat: int, corpus: Corpus | None, base_text: str = "") -> list[str]:
    """Every rule of schema.json that can be checked mechanically. Returns error strings."""
    e = []
    rid = r.get("id", "?")
    for k in REQUIRED:
        if not str(r.get(k, "")).strip():
            e.append(f"{rid}: missing {k}")
    for k, v in r.items():
        if k in PLACEMENT:
            continue
        if k not in FIELDS:
            e.append(f"{rid}: unknown field {k}")
            continue
        enum = FIELDS[k].get("enum")
        if enum:
            vals = str(v).split("|") if k in MULTI else [str(v)]
            for x in vals:
                if x not in ENUMS[enum]:
                    e.append(f"{rid}: {k}={x!r} not in {sorted(ENUMS[enum])}")
    tur, gel = r.get("tur"), r.get("gelenek")
    if tur in ENUMS["tur"] and gel in ENUMS["gelenek"] and gel not in ENUMS["tur"][tur]["gelenek"]:
        e.append(f"{rid}: tur {tur} is not used in gelenek {gel}")
    for k, f in FIELDS.items():
        req = f.get("required_for") or {}
        if tur in req.get("tur", []) or r.get("islev") in req.get("islev", []) or gel in req.get("gelenek", []):
            if not str(r.get(k, "")).strip():
                e.append(f"{rid}: {k} is required for {tur}/{r.get('islev')}")
    m = re.fullmatch(r"S(\d{3})-([A-Z]{3})-(\d{3})", rid)
    if not m:
        e.append(f"{rid}: id must be S<sss>-<KOD>-<NNN>")
    else:
        if int(m.group(1)) != surah:
            e.append(f"{rid}: id surah != {surah}")
        if tur in KOD and m.group(2) != KOD[tur]:
            e.append(f"{rid}: id code {m.group(2)} != {KOD[tur]} for tur {tur}")
    try:
        for s, a, b in ayah_refs(r.get("ayet", "")):
            if s != surah or a < 1 or b < a or b > n_ayat:
                e.append(f"{rid}: ayet {s}:{a}-{b} outside S{surah} (1-{n_ayat})")
    except ValueError as x:
        e.append(f"{rid}: malformed ayet {x}")
    limit = LIMITS.get(r.get("kat"), 80)
    if words(r.get("metin", "")) > limit:
        e.append(f"{rid}: metin {words(r.get('metin', ''))} words > {limit} for kat {r.get('kat')}")
    if "\n" in r.get("metin", ""):
        e.append(f"{rid}: metin must be one paragraph")
    # rules
    locs = [x.strip() for x in str(r.get("kaynak", "")).split("|") if x.strip()]
    memory = "hafiza" in locs
    infos = []
    if corpus:
        for loc in locs:
            if loc == "hafiza":
                continue
            ok, msg, info = corpus.resolve(loc)
            if not ok:
                e.append(f"{rid}: kaynak {msg}")
            else:
                infos.append(info)
                memory |= info.get("access") == "hafiza"
                if gel == "islami" and info.get("kind") == "intertext":
                    e.append(f"{rid}: {loc} is a Bible/Jewish/Christian source; it belongs to the separate pass")
                if gel in ("tevrat", "incil") and info.get("kind") not in SHARED_KINDS \
                        and gel not in (info.get("gelenek") or []):
                    e.append(f"{rid}: {loc} is not a source of gelenek {gel}")
                if info["id"] in MODERN_DICT and tur != "anlam_tarihi":
                    e.append(f"{rid}: modern dictionary {info['id']} only inside anlam_tarihi")
    if memory:
        if r.get("durum") != "degerlendirilmedi":
            e.append(f"{rid}: memory source requires durum:degerlendirilmedi")
        if tur in ("hadis", "nuzul"):
            e.append(f"{rid}: memory is not allowed for {tur}")
        if r.get("derece") and r.get("derece") != "degerlendirilmedi":
            e.append(f"{rid}: a grade cannot rest on memory")
    if tur == "hadis":
        if r.get("derece") != "sahih":
            e.append(f"{rid}: hadis accepts only derece:sahih")
        for info in infos:
            if info.get("kind") == "hadith" and info.get("sahih") is False:
                e.append(f"{rid}: {info['id']} report is not sahih under the project rule")
    if tur == "esbab" and r.get("derece") not in (None, "", "degerlendirilmedi") and not r.get("derece_veren"):
        e.append(f"{rid}: derece_veren required when a grade is given")
    if tur == "duzeltme" and base_text and r.get("taban") and r["taban"] not in base_text:
        e.append(f"{rid}: taban not found verbatim in the base")
    if r.get("bag") in ("muhatap", "etki_iddiasi") and not r.get("alim"):
        e.append(f"{rid}: bag {r['bag']} must name the scholar who argues it (alim)")
    if r.get("bag") == "etki_iddiasi" and r.get("tarihleme") == "kuran_sonrasi":
        e.append(f"{rid}: a text dated after the Qur'an cannot carry etki_iddiasi")
    if r.get("islev") == "fazilet" and tur != "hadis":
        e.append(f"{rid}: merit reports are hadith: tur:hadis, sahih only (not {tur})")
    if tur == "yenilik":
        if r.get("kat") != "arastirma":
            e.append(f"{rid}: yenilik blocks are kat:arastirma")
        if r.get("klasik_tanik") in ("acik", "kismi"):
            e.append(f"{rid}: an attested finding goes on its oncul block (klasik_tanik there), not a yenilik block")
    if r.get("islev") == "itiraz" and not r.get("gerekce"):
        e.append(f"{rid}: itiraz needs gerekce (the argument why the reading cannot hold); a preference is tercih")
    return e


def tag_line(r: dict) -> str:
    """Render one record as the canonical one-line block (enum values bare, everything else JSON-quoted)."""
    parts = []
    for k in ORDER + sorted(k for k in r if k not in ORDER and k not in PLACEMENT):
        if k in PLACEMENT or k not in r or r[k] in (None, ""):
            continue
        v = str(r[k])
        bare = FIELDS.get(k, {}).get("enum") and re.fullmatch(r"[a-z_]+", v)
        parts.append(f"{k}:{v}" if bare else f"{k}:{json.dumps(v, ensure_ascii=False)}")
    return "{" + ", ".join(parts) + "}"


def parse_line(line: str) -> dict:
    """Inverse of tag_line (for round-trip checks of rendered pages)."""
    s = line.strip()
    if not (s.startswith("{") and s.endswith("}")):
        raise ValueError("not a block line")
    out, i = {}, 1
    while i < len(s) - 1:
        m = re.compile(r"\s*([a-z_]+):").match(s, i)
        if not m:
            raise ValueError(f"bad key at {i}")
        k, i = m.group(1), m.end()
        if s[i] == '"':
            j, esc = i + 1, False
            while j < len(s):
                if esc:
                    esc = False
                elif s[j] == "\\":
                    esc = True
                elif s[j] == '"':
                    break
                j += 1
            out[k] = json.loads(s[i:j + 1])
            i = j + 1
        else:
            j = s.find(",", i)
            j = len(s) - 1 if j < 0 else j
            out[k] = s[i:j].strip()
            i = j
        if i < len(s) - 1 and s[i] == ",":
            i += 1
    return out
