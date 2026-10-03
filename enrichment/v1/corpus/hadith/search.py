#!/usr/bin/env python3
"""Search the hadith index.
  search.py 'مراءاة' [--lang ara|eng|tur] [--book bukhari] [--n 10] [--chars 300]
  search.py --get bukhari 6 [--chars 0]
Default is prefix matching per word (e.g. 'مراء' matches مراءاة, يراءون); use --exact for whole words.
Arabic queries are normalized like the index (diacritics stripped, alef/ya/ta marbuta unified).
Quote the opening words of the matn together with book + dataset number; numbering differs across editions.
"""
import argparse, re, sqlite3, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
D = Path(__file__).parent
DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")
def norm(s):
    s = DIAC.sub("", s)
    for a, b in (("أ","ا"),("إ","ا"),("آ","ا"),("ٱ","ا"),("ى","ي"),("ة","ه"),("ؤ","و"),("ئ","ي")): s = s.replace(a, b)
    return s
ap = argparse.ArgumentParser(); ap.add_argument("q", nargs="?"); ap.add_argument("--lang", default="ara")
ap.add_argument("--book"); ap.add_argument("--n", type=int, default=10); ap.add_argument("--chars", type=int, default=300)
ap.add_argument("--exact", action="store_true", help="whole-word match (default: prefix match)")
ap.add_argument("--get", nargs=2, metavar=("BOOK", "NUM")); a = ap.parse_args()
c = sqlite3.connect(D / "hadith.sqlite")
def show(r, ch):
    _, book, num, ref, gr, ara, eng, tur = r
    print(f"== {book} #{int(num) if num==int(num) else num}  ref={ref}  grades={gr}")
    for lab, tx in (("ar", ara), ("en", eng), ("tr", tur)):
        print(f"  {lab}: {tx if ch==0 else tx[:ch]}")
if a.get:
    for r in c.execute("SELECT * FROM h WHERE book=? AND num=?", (a.get[0], float(a.get[1]))): show(r, a.chars if a.chars != 300 else 0)
    sys.exit()
col = {"ara": "ara_n", "eng": "eng", "tur": "tur"}[a.lang]
q = norm(a.q) if a.lang == "ara" else a.q
fq = f"{col} : " + " ".join(f'"{w}"' + ("" if a.exact else "*") for w in q.split())
sql = "SELECT h.* FROM f JOIN h ON h.id=f.rowid WHERE f MATCH ?" + (" AND h.book=?" if a.book else "") + " ORDER BY rank LIMIT ?"
args = [fq] + ([a.book] if a.book else []) + [a.n]
rows = c.execute(sql, args).fetchall()
print(f"{len(rows)} shown (limit {a.n})")
for r in rows: show(r, a.chars)
