#!/usr/bin/env python3
"""Bible-owned source cache and index. No writes to the other enrichment pathway."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import sys
import unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
PG = HERE.parents[1]
sys.path.insert(0,str(PG))
from enrichment.bible import intertext
CORPUS = HERE / 'corpus'
INDEX = CORPUS / 'corpus.sqlite'
INDEX_INTERTEXT = INDEX
INTERTEXT = True
EXCLUDED_KINDS = set()
CALL_LIMIT = 9000
OUT_BYTES = 24000
_used = 0
_unshown = []
PREVIEW = False

_AR_DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")
_AR_MAP = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي"})
_TR_MAP = str.maketrans({"ı": "i", "İ": "i", "I": "i"})

def norm(text: str) -> str:
    """Remove Hebrew pointing and Greek accents as well as Arabic/Turkish search variants."""
    text = unicodedata.normalize("NFKC", text or "")
    text = _AR_DIAC.sub("", text).translate(_AR_MAP).translate(_TR_MAP).lower()
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)
                   or "؀" <= c <= "ۿ")
    return re.sub(r"\s+", " ", text)



def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()



def sources() -> list[dict]:
    out = []
    # one level, plus grouped pointer records (ACADEMIC/<ID>/source.json); never anything under raw/
    paths = list(CORPUS.glob("*/source.json")) + [p for p in CORPUS.glob("*/*/source.json") if "raw" not in p.parts]
    for p in sorted(paths):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8")))
        except json.JSONDecodeError as e:
            print(f"bad source.json {p}: {e}", file=sys.stderr)
    return out



def flat(v) -> str:
    """Segment fields are usually strings; some sources give notes as lists or objects."""
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return " ".join(flat(x) for x in v)
    if isinstance(v, dict):
        return " ".join(flat(x) for x in v.values())
    return "" if v is None else str(v)



def running_calls() -> list[str]:
    """Enrichment calls started without a run.log.json (and not confirmed dead): they read this index."""
    work = HERE / "work"
    pattern = "s*/ehlikitap*" if INTERTEXT else "s*/zengin*"  # include alternate modes
    dirs = sorted(work.glob(pattern)) + ([] if INTERTEXT else sorted(work.glob("s*/okuma.*/*")))  # reading calls
    return [str(d.relative_to(work)) for d in dirs
            if (d / "started.json").exists() and not (d / "run.log.json").exists() and not (d / "dead.json").exists()]



def build() -> None:
    if running_calls():
        raise SystemExit(f"enrichment calls are running {running_calls()}: rebuilding the index would change what "
                         "their validator sees; wait for them")
    index = INDEX_INTERTEXT if INTERTEXT else INDEX
    tmp = index.with_suffix(".sqlite.tmp")
    tmp.unlink(missing_ok=True)
    con = sqlite3.connect(tmp)
    con.executescript("""
        CREATE TABLE src(id TEXT PRIMARY KEY, kind TEXT, access TEXT, meta TEXT);
        CREATE TABLE seg(id INTEGER PRIMARY KEY, seg TEXT UNIQUE, src TEXT, s INT, a INT, a_end INT,
                         head TEXT, text TEXT, extra TEXT);
        CREATE INDEX seg_ayah ON seg(s, a, a_end);
        CREATE INDEX seg_src ON seg(src);
        CREATE VIRTUAL TABLE f USING fts5(body, content='', tokenize='unicode61 remove_diacritics 2');
    """)
    total, source_hashes, metadata_hashes = 0, {}, {}
    for meta in sources():
        kind = meta.get("kind")
        if INTERTEXT:  # the Bible pass index: the intertext sources plus what every pass may cite (Quran, modern, reference)
            if kind not in {"intertext", "quran", "modern", "reference"}:
                continue
        elif kind in EXCLUDED_KINDS:  # the Islamic index never holds intertext
            continue
        con.execute("INSERT INTO src VALUES(?,?,?,?)", (meta["id"], meta.get("kind"), meta.get("access"),
                                                         json.dumps(meta, ensure_ascii=False)))
        metadata_hashes[meta['id']] = sha256(CORPUS / meta['id'] / 'source.json')
        path = CORPUS / meta["id"] / "segments.jsonl"
        if not path.exists():
            if meta.get("access") != "hafiza":  # memory pointers have no text by design
                print(f"WARNING: {meta['id']}: no segments.jsonl; not indexed", file=sys.stderr)
            continue
        n = 0
        if INTERTEXT:
            source_hashes[meta['id']] = sha256(path)
        with path.open(encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                if INTERTEXT and meta['id'] == 'WLC' and (r.get('text_reading') != 'ketiv' or 'variant_notes' not in r):
                    con.close()
                    raise ValueError('WLC still uses the old mixed-variant extraction; reimport bible_text.py wlc first')
                if kind == 'intertext':
                    r.update(intertext.metadata(meta['id'], r))
                extra = {k: v for k, v in r.items() if k not in ("seg", "s", "a", "a_end", "head", "text")}
                try:
                    cur = con.execute("INSERT INTO seg(seg,src,s,a,a_end,head,text,extra) VALUES(?,?,?,?,?,?,?,?)",
                                      (r["seg"], meta["id"], r.get("s"), r.get("a"), r.get("a_end") or r.get("a"),
                                       r.get("head"), r.get("text", ""), json.dumps(extra, ensure_ascii=False)))
                except sqlite3.IntegrityError:
                    con.close()
                    raise ValueError(f"duplicate locator {r['seg']} in {meta['id']}")
                body = " ".join(flat(r.get(k)) for k in ("head", "text", "en", "tr", "notes") if r.get(k))
                con.execute("INSERT INTO f(rowid, body) VALUES(?,?)", (cur.lastrowid, norm(body)))
                n += 1
        total += n
        print(f"{meta['id']:22} {n:>8}", flush=True)
    con.commit()
    con.close()
    tmp.replace(index)
    if INTERTEXT:
        manifest = {'format': 'intertext-2', 'source_hashes': source_hashes,
                    'metadata_hashes': metadata_hashes, 'index_sha256': sha256(index)}
        index.with_suffix('.manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f"indexed {total} segments -> {index}")



def connect() -> sqlite3.Connection:
    index = INDEX_INTERTEXT if INTERTEXT else INDEX
    if not index.exists():
        sys.exit(f"no index: run `corpus.py {'--intertext ' if INTERTEXT else ''}build` first")
    return sqlite3.connect(f"file:{index}?mode=ro", uri=True)



def show(row, chars: int, start: int = 0) -> None:
    global _used
    seg, src, s, a, a_end, head, text, extra = row
    extra = json.loads(extra or "{}")
    flags = []
    if "sahih" in extra:
        flags.append(f"sahih={extra['sahih']} by={'|'.join(extra.get('graded_by') or []) or '-'}")
    if extra.get("page"):
        flags.append(f"page={extra['page']}")
    head_line = f"== {seg}" + (f"  [{head}]" if head else "") + ("  " + " ".join(flags) if flags else "")
    room = CALL_LIMIT - _used if CALL_LIMIT else None
    if CALL_LIMIT and _bytes_out() > OUT_BYTES - 3_000:  # leave room for the closing note
        room = 0
    if room is not None and room <= 0:  # listed once, compactly, by close_call()
        _unshown.append(f"{seg}({len(text):,})")
        return
    body = text[start:]
    n = len(body) if not chars else min(chars, len(body))
    if room is not None:
        n = min(n, room)
    shown = body[:n]
    span = f"  [characters {start + 1:,}–{start + n:,} of {len(text):,}]" if (start or n < len(body)) else ""
    print(head_line + span)
    if n < len(body):
        tail = (f" … [preview: `corpus.py get {seg}` for the text]" if PREVIEW else
                f" … [cut: `corpus.py get {seg} --from {start + n}` for the rest]")
    else:
        tail = ""
    print(shown + tail)
    _used += n
    for k in ("en", "tr", "notes"):
        if extra.get(k):
            v = flat(extra[k])
            v = v if not chars else v[:chars]
            print(f"  {k}: {v}")
            _used += len(v)
    if extra.get('gelenek') is not None:
        print('  witness metadata: ' + json.dumps({k: extra[k] for k in
              ('gelenek', 'nusha', 'versification', 'text_reading', 'text_language', 'language',
               'translation_aid', 'background_only') if k in extra},
              ensure_ascii=False))
    if extra.get('variant_notes'):
        print('  variants (separate from the verse): ' + json.dumps(
            [{k: n[k] for k in ('after_word', 'type', 'readings')} for n in extra['variant_notes']], ensure_ascii=False))



class _Counter:
    """stdout that counts the bytes written, so a call can stop before the harness's spill limit."""
    def __init__(self, inner):
        self.inner, self.n = inner, 0

    def write(self, s):
        self.n += len(s.encode("utf-8"))
        return self.inner.write(s)

    def flush(self):
        return self.inner.flush()



def _bytes_out() -> int:
    return getattr(sys.stdout, "n", 0)



def close_call() -> None:
    """The segments past the call's limit, listed once: each locator when few, else per source (count, characters)."""
    if not _unshown:
        return
    if len(_unshown) <= 12:
        listing = " ".join(_unshown)
    else:
        by: dict[str, list[int]] = {}
        for x in _unshown:
            loc, n = x.rsplit("(", 1)
            by.setdefault(loc.split(":")[0], []).append(int(n.rstrip(")").replace(",", "")))
        listing = "; ".join(f"{src} {len(v)} segments {sum(v):,} chars" for src, v in by.items())
    print(f"NOTE: {len(_unshown)} segments not shown (the {CALL_LIMIT:,}-character limit of one call): {listing}. "
          f"Get them in another call; use get with the indicated locator and offset")



def cmd_get(locs: list[str], chars: int, start: int = 0) -> None:
    con = connect()
    for loc in locs:
        # the segment and its sub-segments (loc#2 …) by two index lookups; `OR … LIKE` would scan the whole table
        rows = (con.execute("SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE seg=?", (loc,)).fetchall()
                + con.execute("SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE seg>=? AND seg<? ORDER BY id",
                              (loc + "#", loc + "$")).fetchall())
        if not rows:
            print(f"== {loc}: NOT FOUND")
        for r in rows:
            show(r, chars, start)



def kinds_filter(kinds: str | None) -> tuple[str, list]:
    if not kinds:
        return "", []
    ks = kinds.split(",")
    return f" AND seg.src IN (SELECT id FROM src WHERE kind IN ({','.join('?' * len(ks))}))", ks



def cmd_ayah(ref: str, kinds: str | None, src: str | None, chars: int) -> None:
    con = connect()
    s, a = (int(x) for x in ref.split(":"))
    sql = "SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=?"
    args: list = [s, a, a]
    k_sql, k_args = kinds_filter(kinds)
    sql += k_sql
    args += k_args
    if src:
        ids = src.split(",")
        sql += f" AND src IN ({','.join('?' * len(ids))})"
        args += ids
    for r in con.execute(sql + " ORDER BY src, a", args):
        show(r, chars)



def cmd_search(q: str, a) -> None:
    con = connect()
    words = norm(q).split()
    fq = " ".join(f'"{w}"' + ("" if a.exact else "*") for w in words)
    sql = ("SELECT seg.seg,seg.src,seg.s,seg.a,seg.a_end,seg.head,seg.text,seg.extra FROM f JOIN seg ON seg.id=f.rowid "
           "WHERE f MATCH ?")
    args: list = [fq]
    if a.src:
        ids = a.src.split(",")
        sql += f" AND seg.src IN ({','.join('?' * len(ids))})"
        args += ids
    k_sql, k_args = kinds_filter(a.kind)
    sql += k_sql
    args += k_args
    if a.surah:
        sql += " AND seg.s=?"
        args.append(a.surah)
    if a.sahih:
        sql += " AND json_extract(seg.extra,'$.sahih')=1"
    rows = con.execute(sql + " ORDER BY rank LIMIT ?", args + [a.n]).fetchall()
    print(f"{len(rows)} shown (limit {a.n}) for {fq}")
    for r in rows:
        show(r, a.chars)



def cmd_sources(kind: str | None) -> None:
    for m in sources():
        if kind and m.get("kind") != kind:
            continue
        print(f"{m['id']:22} {m.get('kind', ''):12} {m.get('access', ''):7} {str(m.get('segments', '-')):>8}  "
              f"{m.get('author', '') or ''} — {m.get('title', '')}  [{m.get('coverage', '')}]")



def seed(source_root=None):
    """Copy eligible cached sources once; the upstream corpus is strictly read-only."""
    if running_calls():
        raise ValueError('Bible page calls are active')
    source_root = source_root or PG/'enrichment/corpus'
    paths = sorted(source_root.glob('*/source.json')) + sorted(source_root.glob('*/*/source.json'))
    copied=[]
    CORPUS.mkdir(parents=True,exist_ok=True)
    for path in paths:
        if 'raw' in path.relative_to(source_root).parts: continue
        meta=json.loads(path.read_text())
        if meta.get('kind') not in ('intertext','quran','modern','reference'): continue
        dst=CORPUS/meta['id']
        if dst.exists(): continue
        dst.mkdir()
        for name in ('source.json','segments.jsonl','raw'):
            src=path.parent/name
            if src.is_dir(): shutil.copytree(src,dst/name)
            elif src.is_file(): shutil.copyfile(src,dst/name)
        copied.append(meta['id'])
    print('Bible-owned sources copied: '+', '.join(copied))
    return copied


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--intertext',action='store_true',help='compatibility flag; this index is always intertext')
    sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('seed')
    sub.add_parser('build')
    p=sub.add_parser('sources'); p.add_argument('--kind')
    p=sub.add_parser('get'); p.add_argument('loc',nargs='+'); p.add_argument('--from',dest='start',type=int,default=0)
    p=sub.add_parser('ayah'); p.add_argument('ref'); p.add_argument('--src'); p.add_argument('--kind')
    p=sub.add_parser('search'); p.add_argument('q'); p.add_argument('--src'); p.add_argument('--kind')
    p.add_argument('--surah',type=int); p.add_argument('--n',type=int,default=10); p.add_argument('--exact',action='store_true')
    p.set_defaults(sahih=False)
    for name in ('get','ayah','search'):
        p=sub.choices[name]; p.add_argument('--chars',type=int,default=0 if name=='get' else 600)
        p.add_argument('--limit',type=int,default=9000)
    a=ap.parse_args()
    global CALL_LIMIT,PREVIEW
    CALL_LIMIT=getattr(a,'limit',9000); PREVIEW=a.cmd=='search'
    if a.cmd=='seed': seed()
    elif a.cmd=='build': build()
    elif a.cmd=='sources': cmd_sources(a.kind)
    else:
        sys.stdout=_Counter(sys.stdout)
        if a.cmd=='get': cmd_get(a.loc,a.chars,a.start)
        elif a.cmd=='ayah': cmd_ayah(a.ref,a.kind,a.src,a.chars)
        else: cmd_search(a.q,a)
        close_call()

if __name__=='__main__': main()
