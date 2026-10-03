#!/usr/bin/env python3
"""Build hadith.sqlite (FTS5) from the ara/eng/tur edition files in this folder."""
import json, re, sqlite3
from pathlib import Path
D = Path(__file__).parent
BOOKS = "bukhari muslim abudawud tirmidhi nasai ibnmajah malik".split()
DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")

def norm(s):  # strip tashkil/tatweel, unify alef/ya/ta marbuta/hamza carriers
    s = DIAC.sub("", s)
    for a, b in (("أ","ا"),("إ","ا"),("آ","ا"),("ٱ","ا"),("ى","ي"),("ة","ه"),("ؤ","و"),("ئ","ي")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s)

db = D / "hadith.sqlite"
db.unlink(missing_ok=True)
c = sqlite3.connect(db)
c.execute("CREATE TABLE h(id INTEGER PRIMARY KEY, book TEXT, num REAL, ref TEXT, grades TEXT, ara TEXT, eng TEXT, tur TEXT)")
c.execute("CREATE VIRTUAL TABLE f USING fts5(ara_n, eng, tur, content='', tokenize='unicode61 remove_diacritics 2')")
for b in BOOKS:
    ed = {l: {x["hadithnumber"]: x for x in json.load(open(D / f"{l}-{b}.json"))["hadiths"]} for l in ("ara", "eng", "tur")}
    for n, a in ed["ara"].items():
        e, t = ed["eng"].get(n, {}), ed["tur"].get(n, {})
        cur = c.execute("INSERT INTO h(book,num,ref,grades,ara,eng,tur) VALUES(?,?,?,?,?,?,?)",
            (b, n, json.dumps(a.get("reference"), ensure_ascii=False), json.dumps(a.get("grades"), ensure_ascii=False),
             a["text"], e.get("text", ""), t.get("text", "")))
        c.execute("INSERT INTO f(rowid,ara_n,eng,tur) VALUES(?,?,?,?)", (cur.lastrowid, norm(a["text"]), e.get("text", ""), t.get("text", "")))
c.commit()
print(c.execute("SELECT book,count(*) FROM h GROUP BY book").fetchall())
