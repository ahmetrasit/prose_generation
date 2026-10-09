"""Parse frozen v16 surah sections for Bible discovery."""
import re
SECTION = re.compile(r"(?m)^## (.+)$")
KAYNAK = re.compile(r"(?m)^Kaynaklar:\s*(.*)$")
MEMBER = re.compile(r"\s*(\d+:\d+)\s+(.+?)\s+([ء-ي](?:\s+[ء-ي]){2,3})\s+(B\d+(?:\s*,\s*B\d+)*)\s*(?:\((in phrase)\))?\s*")
# a word cited under another root's branch: "103:2 word ء ن س (in ع ص ر B008)" (S103 images, 2026-10)
MEMBER_IN = re.compile(r"\s*(\d+:\d+)\s+(.+?)\s+([ء-ي](?:\s+[ء-ي]){2,3})\s+\(in\s+([ء-ي](?:\s+[ء-ي]){2,3})\s+(B\d+(?:\s*,\s*B\d+)*)\)\s*")

def sections(text: str) -> list[dict]:
    """The `## ` sections of images.md in order: title, span, prose, the surah ayat named in Kaynaklar, the roots."""
    heads = list(SECTION.finditer(text))
    out = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[h.end():end]
        km = KAYNAK.search(body)
        members = []
        if km:
            for item in km.group(1).split(";"):
                m = MEMBER.fullmatch(item)
                if m:
                    members.append({"ayah": m.group(1), "word": m.group(2), "root": " ".join(m.group(3).split()),
                                    "branch": ", ".join(re.findall(r"B\d+", m.group(4)))}
                                   | ({"note": "in phrase"} if m.group(5) else {}))
                    continue
                m = MEMBER_IN.fullmatch(item)
                if not m:
                    raise ValueError(f"section {i + 1}: unparsed Kaynaklar item: {item!r}")
                # the word's own root, cited through a branch of another root: both roots are members
                members.append({"ayah": m.group(1), "word": m.group(2), "root": " ".join(m.group(3).split()),
                                "branch": "", "note": f"cited under {' '.join(m.group(4).split())} {m.group(5)}"})
                members.append({"ayah": m.group(1), "word": m.group(2), "root": " ".join(m.group(4).split()),
                                "branch": ", ".join(re.findall(r"B\d+", m.group(5)))})
        elif not h.group(1).strip().lower().startswith("buluşma"):
            raise ValueError(f"section {i + 1}: missing Kaynaklar line")
        prose = KAYNAK.sub("", body).strip()
        out.append({"k": i + 1, "title": h.group(1).strip(), "start": h.start(), "end": end, "prose": prose,
                    "members": members, "ayat": sorted({x["ayah"] for x in members}, key=lambda r: tuple(map(int, r.split(":")))),
                    "roots": sorted({x["root"] for x in members}), "meetings": h.group(1).strip().lower().startswith("buluşma")})
    return out
