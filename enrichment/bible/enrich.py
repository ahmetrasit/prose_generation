#!/usr/bin/env python3
"""Independent Bible enrichment: prepare, spawn, finish and merge frozen pages."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import sys
import time
from pathlib import Path
V2 = Path(__file__).resolve().parent
PG = V2.parents[1]
sys.path.insert(0, str(PG))
from enrichment.bible import agentrun as AR, render as R, validate as VAL
from enrichment.bible import discovery as DISC, verdicts as VERDICTS
WORK = V2 / 'work'
OUT = V2 / 'out'
ISLAMIC_OUT = PG / 'enrichment/v2/out'  # read-only accepted layer
PROMPTS = V2 / 'prompts'
LEDGER = WORK / 'ledger.jsonl'
ERRATA = V2 / 'errata.jsonl'
BRIEF = 'ehlikitap'
MODE = 'agent'
EFFORT = 'high'
DEFAULT_MODEL = 'opus'
MODELS = {'opus': ('agent', 'claude-opus-5-5')}
GELENEK = {'zengin':'islami', 'ehlikitap':'ehlikitap'}


def wd(s: int) -> Path:
    return WORK / f"s{s:03d}"



def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()



def log(row: dict) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")



def rel(p: Path) -> str:
    return str(p.relative_to(PG)) if p.is_relative_to(PG) else str(p)



def tag(target: str) -> str:
    return target.replace(":", "_")



def call_dir(s: int, target: str, attempt: int = 1, model: str = DEFAULT_MODEL, effort: str = EFFORT) -> Path:
    name = f"ehlikitap.{tag(target)}.{model}.{effort}"
    return wd(s) / (name if attempt == 1 else f"{name}.a{attempt}")



def page_name(s: int, target: str) -> str:
    stem = "surah" if target == "surah" else tag(target)
    return f"{stem}.md" if BRIEF == "zengin" else f"{stem}.{BRIEF}.md"  # the Bible pass has its own page beside the Islamic one



def discovery_list(s: int, target: str) -> Path | None:
    """An explicitly selected, completed Bible discovery handoff."""
    root = wd(s) / 'discovery'
    selection = root / 'selected.json'
    if not selection.exists():
        return None
    entry = json.loads(selection.read_text()).get(target)
    if not entry:
        return None
    path = (root / entry).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f'invalid discovery selection for {target}: {entry}')
    return path



def file_hash(path: Path) -> str:
    return VAL.C.sha256(path)



def bible_inputs(s: int, target: str) -> dict:
    """Preflight and freeze the exact discovery, prefetch and intertext index."""
    discovery = discovery_list(s, target)
    if discovery is None:
        raise ValueError('no selected Bible discovery; prepare, finish, merge and prefetch discovery first')
    manifest = discovery.with_suffix('.json')
    meta = json.loads(manifest.read_text())
    _, base, info = R.target_page(s, target)
    if meta.get('status') != 'ok' or meta.get('tsv_sha256') != file_hash(discovery):
        raise ValueError('Bible discovery is incomplete or changed since merge')
    if meta.get('target') != target:
        raise ValueError('Bible discovery handoff belongs to a different target')
    if meta.get('base_sha256') != sha(base):
        raise ValueError('Bible discovery used a different frozen base')
    prefetch = discovery.parent / 'prefetch.json'
    fetched = json.loads(prefetch.read_text())
    if fetched.get('lists', {}).get(discovery.name) != file_hash(discovery) or not fetched.get('complete'):
        raise ValueError('Bible discovery has no completed matching prefetch report')
    index = VAL.C.INDEX_INTERTEXT
    index_manifest = index.with_suffix('.manifest.json')
    indexed = json.loads(index_manifest.read_text())
    if indexed.get('index_sha256') != file_hash(index):
        raise ValueError('intertext index differs from its build manifest')
    files = [discovery, manifest, prefetch, wd(s)/'discovery/selected.json', index, index_manifest,
             *DISC.verify_handoff(discovery,s,target)]
    if not {'WLC', 'SBLGNT', 'QURAN'}.issubset(indexed.get('source_hashes', {})):
        raise ValueError('the Bible index requires WLC, SBLGNT and QURAN')
    if not indexed.get('metadata_hashes'):
        raise ValueError('rebuild the Bible index to freeze source metadata')
    for field, filename in (('source_hashes', 'segments.jsonl'), ('metadata_hashes', 'source.json')):
        for sid, digest in indexed[field].items():
            path = VAL.C.CORPUS / sid / filename
            if file_hash(path) != digest:
                raise ValueError(f'rebuild the Bible index: {sid}/{filename} changed')
            files.append(path)
    for sid, digest in fetched.get('source_hashes', {}).items():
        if indexed.get('source_hashes', {}).get(sid) != digest:
            raise ValueError(f'intertext index must be rebuilt after prefetch of {sid}')
    if indexed.get('format') != 'intertext-2':
        raise ValueError('rebuild the intertext index with repaired WLC and segment traditions')
    pack = wd(s) / 'pack'
    pack_meta = json.loads((pack / 'pack.json').read_text())
    for filename, digest in pack_meta['files'].items():
        path = pack / filename
        if file_hash(path) != digest:
            raise ValueError(f'Bible pack input changed: {filename}')
        files.append(path)
    return {rel(p): file_hash(p) for p in files}



def verify_bible_inputs(started: dict) -> None:
    saved = started.get('bible_inputs')
    if not saved:
        raise ValueError('Bible call lacks its discovery/index input hashes; build a fresh call')
    for path, digest in saved.items():
        if not (PG / path).is_file() or file_hash(PG / path) != digest:
            raise ValueError(f'Bible input changed since the call: {path}')



def accepted(s: int, target: str) -> bool:
    return (OUT / f"s{s:03d}" / page_name(s, target)).exists()



def blocked(d: Path) -> bool:
    return (d / "started.json").exists() or (d / "run.log.json").exists()



def targets(s: int) -> list[str]:
    """The surah page and every ayah page that has a base."""
    base = json.loads((wd(s) / "pack" / "base.json").read_text(encoding="utf-8"))
    return ["surah"] + [ref for ref, info in base["ayat"].items() if info]



def select(s: int, spec: str) -> list[str]:
    """--target: surah | S:A | ayat | all."""
    if spec == "all":
        return targets(s)
    if spec == "ayat":
        return targets(s)[1:]
    if spec == "surah":
        return ["surah"]
    if ":" not in spec or spec.split(":")[0] != str(s) or not spec.split(":")[1].isdigit():
        raise SystemExit(f"--target {spec!r}: expected surah, ayat, all or {s}:A")
    return [spec]



def missing_ayat(s: int) -> list[str]:
    """Ayat of the surah with no ayah base (v16 augment9 not run): no ayah page until the pack is rebuilt."""
    base = json.loads((wd(s) / "pack" / "base.json").read_text(encoding="utf-8"))
    return [ref for ref, info in base["ayat"].items() if not info]



def base_words(s: int, target: str) -> int | None:
    try:
        return len(R.target_page(s, target)[1].split())
    except (OSError, SystemExit, KeyError, ValueError):
        return None



def estimate(s: int, target: str, model: str, effort: str) -> str:
    """USD estimate for a Claude call from the ledger: past calls of the same model, effort and page kind, scaled by
    the base's word count (the surah pages ran $0.67–0.98 per 1k base words with Opus high)."""
    if MODELS[model][0] != "agent":
        return "subscription (no USD)"
    kind = ("surah" if target == "surah" else "ayah") + ("" if MODE == "agent" else "-" + MODE)
    rates, failed, bad = [], [], 0
    for line in (LEDGER.read_text(encoding="utf-8").splitlines() if LEDGER.exists() else []):
        try:
            r = json.loads(line)
        except json.JSONDecodeError:  # e.g. a row being appended right now
            bad += 1
            continue
        if r.get('brief', 'zengin') != BRIEF:
            continue
        if not (r.get("cost_usd") and (r.get("model"), r.get("effort")) == (model, effort)
                and ("surah" if r.get("target") == "surah" else "ayah") + ("" if r.get("mode", "agent") == "agent" else "-" + r["mode"]) == kind):
            continue
        if r.get("status") != "ok":
            failed.append(r["cost_usd"])
            continue
        w = r.get("base_words") or base_words(r["surah"], r["target"])
        if w:
            rates.append(r["cost_usd"] / w * 1000)
    w = base_words(s, target)
    notes = ([f"{len(failed)} failed calls of this kind cost ${sum(failed):.2f} in all"] if failed else []) + \
            ([f"{bad} unreadable ledger lines skipped"] if bad else [])
    tail = f"; {'; '.join(notes)}" if notes else ""
    if not rates or not w:
        return f"no calibration yet for {model}:{effort} {kind} pages (base {w or '?'} words){tail}"
    lo, hi = min(rates), max(rates)
    return f"${lo * w / 1000:.1f}–{hi * w / 1000:.1f} (base {w:,} words; {len(rates)} past calls){tail}"



def header(s: int, target: str, d: Path, runner: str = "codex") -> str:
    pack = wd(s) / "pack"
    n = json.loads((pack / "pack.json").read_text(encoding="utf-8"))["ayat"]
    name = R.target_page(s, target)[0]
    card = 'SCHEMA_BIBLE_CARD.md' if BRIEF == 'ehlikitap' else 'SCHEMA_CARD.md'
    for path in (pack / 'numbered' / name, V2 / card):
        if not path.is_file():
            raise ValueError(f'missing page input: {path}')
    py = "python3"
    if target == "surah":
        what = f"the surah page of S{s} (base PACK/numbered/surah.md; all ayat 1–{n})"
    else:
        what = (f"the ayah page of {target} (base PACK/numbered/{name}; Arabic text in PACK/quran.json); "
                f"every record's ayet must include {target}")
    return "\n".join([
        "# Job", "",
        f"- Surah: {s} (ayat 1–{n}); ids use S{s:03d}",
        f"- Target: {target} — {what}",
        f"- Workspace root: {PG}", f"- PACK: {pack}",
        f"- Your call directory (write only here): {d}",
        f"- Schema card: {V2 / card} (read it once; the full reference is {V2 / 'SCHEMA.md'})",
        f"- Corpus tool: {py} {V2 / 'corpus.py'}",
        f"- Validator: {py} {V2 / 'validate.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'}" + (" --pass ehlikitap" if BRIEF == "ehlikitap" else ""),
        f"- Renderer (preview): {py} {V2 / 'render.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'} --out {d / 'preview'}",
        f"- Verdict draft check: {py} {V2 / 'verdicts.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'} --draft --report {d / 'verdicts.draft.json'}",
        f"- Hebrew root and cognate tool: {py} {V2 / 'hebrew.py'} root ROOT | cognates 'ARABIC ROOT' | word WLC:Book.C.V",
        "- Deliverables: annotations.jsonl, verdicts.jsonl, gaps.json and root_verdicts.jsonl in your call directory.",
    ] + ([f"- Pass: ehlikitap (the Tevrat and İncil layers; brief ehlikitap.md); corpus tool: {py} "
          f"{V2 / 'corpus.py'} --intertext (the flag before the subcommand)",
          "- Prefetch: read prefetch.json beside the selected discovery list; record its gaps in your gaps.json.",
          "- Review: read the .merged.json beside the discovery TSV. It preserves wording findings, repeats, repairs and provenance.",
          "- Discovery list: " + (str(discovery_list(s, target)) if discovery_list(s, target) else
                                  "none (build only; discovery and prefetch are required before spawn)")]
         if BRIEF == "ehlikitap" else [])) + "\n"



def finish(s: int, target: str, d: Path, trial: bool = False, started: dict | None = None) -> dict:
    """Check the records, drop the failing ones, render, check the page, accept (unless trial). Nothing goes back to
    the agent. started: the call's started row; if the pack (base or any input) changed since the call, the page is
    never accepted, and the accepted record names the dictionary the call saw."""
    ann = d / "annotations.jsonl"
    if not ann.exists():
        return {"check": "no annotations.jsonl", "ok": False}
    started = started or {}
    if BRIEF == 'ehlikitap':
        try:
            verify_bible_inputs(started)
        except (OSError, ValueError) as e:
            return {'check': str(e), 'ok': False}
    dst = OUT / f"s{s:03d}" / page_name(s, target)
    if not trial and dst.exists():  # before anything is rendered or written
        return {"check": f"{rel(dst)} exists (never overwrite)", "ok": False}
    now = R.target_page(s, target)[2]["sha256"]
    if started.get("base_sha256") and now != started["base_sha256"]:
        return {"check": f"base changed since the call ({started['base_sha256'][:12]} -> {now[:12]}): never "
                         f"accepted; run a new attempt on the new base", "ok": False}
    pack_now = hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest()
    if started.get("pack_sha256") and pack_now != started["pack_sha256"]:
        return {"check": "the pack was rebuilt since the call (pack.json differs): the page's inputs are no longer "
                         "the ones the call saw; never accepted; run a new attempt", "ok": False}
    try:
        recs = R.load(ann)
    except SystemExit as e:
        return {"check": f"annotations.jsonl unreadable: {e}", "ok": False}
    kept, dropped, warnings = VAL.check_records(s, target, recs, GELENEK[BRIEF])
    page_dir = d / "page"
    if page_dir.exists():
        shutil.rmtree(page_dir)
    page, placement = R.render(s, target, kept, page_dir)
    name, base, info = R.target_page(s, target)
    page_errors = VAL.check_page(page, base, kept) + placement
    check = {"surah": s, "target": target, "records": len(recs), "kept": len(kept), "dropped": dropped,
             "warnings": warnings, "page_errors": page_errors}
    (d / "check.json").write_text(json.dumps(check, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts = {"kept": len(kept), "dropped": len(dropped), "warnings": len(warnings)}
    if dropped and not kept:
        return {'check': 'all records failed validation (see check.json)', 'ok': False, **counts}
    if not recs and BRIEF == 'ehlikitap':
        gaps = d / 'gaps.json'
        reason = json.loads(gaps.read_text()).get('no_findings_reason') if gaps.exists() else None
        if not isinstance(reason, str) or not reason.strip():
            return {'check': 'empty Bible page requires gaps.json no_findings_reason', 'ok': False, **counts}
    try:
        verdict_report=VERDICTS.check(d,discovery_list(s,target),base,kept)
    except (OSError,ValueError,KeyError,TypeError) as exc:
        verdict_report=dict(ok=False,errors=[str(exc)])
    DISC.save(d/'verdict_report.json',verdict_report)
    if not verdict_report['ok']:
        return {'check':'incomplete/invalid Bible verdicts (see verdict_report.json)', 'ok':False,
                'verdict_errors':verdict_report['errors'],**counts}
    if page_errors:
        return {"check": f"page errors: {len(page_errors)} (see check.json)", "ok": False, **counts}
    if trial:
        return {"check": "ok (trial: page in the call directory only)", "ok": True, **counts}
    dictionary = started.get("dictionary") or json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8")).get("dictionary")
    errata = [r for r in kept if r.get("tur") == "duzeltme"]
    logged = set()
    for line in (ERRATA.read_text(encoding="utf-8").splitlines() if ERRATA.exists() else []):
        try:
            x = json.loads(line)
        except json.JSONDecodeError:
            continue  # a hand-edited line; never rewritten here
        logged.add((x.get("surah"), x.get("target"), x.get("id"), x.get("taban")))
    with ERRATA.open("a", encoding="utf-8") as f:  # before the page: an accepted page never lacks its errata
        for r in errata:
            if (s, target, r["id"], r.get("taban")) in logged:  # a failed earlier accept already logged it
                print(f"NOTE: {r['id']} already in errata.jsonl (an earlier accept of this page); not repeated",
                      flush=True)
                continue
            f.write(json.dumps({"surah": s, "target": target, "base": info["path"], "id": r["id"], "taban": r.get("taban"),
                                "hata": r.get("hata"), "metin": r.get("metin"), "kaynak": r.get("kaynak")},
                               ensure_ascii=False) + "\n")
    dst.parent.mkdir(parents=True, exist_ok=True)
    snapshot = dst.with_suffix('.annotations.jsonl')
    payload = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in kept)
    # A previous interrupted accept may have written the identical snapshot only.
    if snapshot.exists() and snapshot.read_text() != payload:
        return {'check': f'{rel(snapshot)} differs from this result; never overwrite', 'ok': False, **counts}
    if not snapshot.exists():
        with snapshot.open('x', encoding='utf-8') as f:
            f.write(payload)
    evidence_snapshots={}
    for filename in ('verdicts.jsonl','gaps.json','verdict_report.json','root_verdicts.jsonl'):
        if filename=='root_verdicts.jsonl' and not (d/filename).exists():
            continue  # calls prepared before the Semitic root table (2026-10-09)
        frozen=dst.with_suffix('.'+filename)
        content=(d/filename).read_bytes()
        if frozen.exists() and frozen.read_bytes()!=content:
            return {'check':f'{rel(frozen)} differs from this result; never overwrite','ok':False,**counts}
        if not frozen.exists():
            with frozen.open('xb') as f: f.write(content)
        evidence_snapshots[filename]=dict(path=rel(frozen),sha256=file_hash(frozen))
    with open(page, "rb") as src, open(dst, "xb") as out:  # exclusive: never overwrite, even in a race
        out.write(src.read())
    rec = {"surah": s, "target": target, "accepted_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "page_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "base": info,
           "dictionary": dictionary, "annotations": rel(ann),
           "accepted_annotations": rel(snapshot), "annotations_sha256": file_hash(snapshot),
           "verdict_artifacts": evidence_snapshots,
           "bible_inputs": started.get('bible_inputs'),
           "kept": len(kept), "dropped": [x["id"] for x in dropped]}
    dst.with_suffix(".json").write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"check": "ok", "ok": True, **counts, "errata": len(errata)}



def unread_sources(s: int, target: str, d: Path) -> list[str]:
    """Sources with segments tied to the ayah that the agent never named in a tool call (Read path, command) and
    that its corpus extract (mode dosya2) did not show: the page's silent skips, now recorded (meal, translation
    and Qur'an-text sources excepted: they reach the agent through the pack)."""
    if target == "surah":
        return []
    import sqlite3
    from enrichment.bible import corpus as C
    index = C.INDEX_INTERTEXT if BRIEF == 'ehlikitap' else C.INDEX
    con = sqlite3.connect(f"file:{index}?mode=ro", uri=True)
    a = int(target.split(":")[1])
    srcs = {r[0] for r in con.execute("SELECT DISTINCT seg.src FROM seg JOIN src ON src.id=seg.src WHERE seg.s=? AND "
                                       "seg.a<=? AND coalesce(seg.a_end, seg.a)>=? AND src.kind NOT IN "
                                       "('meal','translation','quran')", (s, a, a))}
    if BRIEF == 'ehlikitap':
        path = discovery_list(s, target)
        if path:
            report = json.loads((path.parent / 'prefetch.json').read_text())
            srcs |= {loc.split(':')[0] for item in report['candidates']
                     for loc in item.get('locators', []) + item.get('related', [])}
    con.close()
    seen = ""
    tc = d / "tool_calls.json"
    if tc.exists():
        seen += " ".join(json.dumps(c.get("input"), ensure_ascii=False) for c in json.loads(tc.read_text(encoding="utf-8")))
    ex = d / "extract.json"
    if ex.exists():
        rec = json.loads(ex.read_text(encoding="utf-8"))
        listed = {x.split(":")[0] for x in rec.get("segments_listed_only", [])}
        seen += " " + " ".join(f"{x}:" for x in srcs - listed)  # every source with something shown in the extract
    return sorted(x for x in srcs if f"{x}:" not in seen and f"{x}," not in seen and f"{x} " not in seen)



def merged_registry(texts: list[str]) -> str:
    """Preserve the source descriptions frozen in the accepted pages."""
    sources = {}
    for text in texts:
        section = text.rsplit('\n## Kaynak kayıtları', 1)
        if len(section) != 2:
            raise ValueError('accepted page has no source registry')
        for line in section[1].splitlines():
            if not line.strip():
                continue
            match = re.fullmatch(r'- \*\*([^*]+)\*\* — (.*)', line)
            if not match:
                raise ValueError('unrecognized accepted source registry line')
            sid, description = match.groups()
            desc, _, refs = description.partition('. Atıflar: ')
            entry = sources.setdefault(sid, {'descriptions': [], 'refs': []})
            if desc not in entry['descriptions']:
                entry['descriptions'].append(desc)
            for ref in refs.split(', ') if refs else []:
                if ref not in entry['refs']:
                    entry['refs'].append(ref)
    lines = ['## Kaynak kayıtları', '']
    for sid, entry in sorted(sources.items()):
        line = f'- **{sid}** — ' + ' / '.join(entry['descriptions'])
        if entry['refs']:
            line += '. Atıflar: ' + ', '.join(entry['refs'])
        lines.append(line)
    return '\n'.join(lines) + '\n'


def merge_page(s: int, target: str) -> bool:
    """out/sNNN/<page>.merged.md from the accepted Islamic page and the accepted Bible page (whichever exist): the
    kept records of both, rendered into the frozen base; the Islamic records get gelenek islami. Never overwrites
    an accepted page; the merged file is rewritten each time."""
    stem = "surah" if target == "surah" else tag(target)
    recs, parts, provenance, originals = [], [], {}, []
    name, base, info = R.target_page(s, target)
    metas = {m['id']: m for m in VAL.C.sources()}
    try:
        for brief in ('zengin', 'ehlikitap'):
            filename = f'{stem}.md' if brief == 'zengin' else f'{stem}.ehlikitap.md'
            page = (ISLAMIC_OUT if brief == 'zengin' else OUT) / f's{s:03d}' / filename
            rec_path = page.with_suffix('.json')
            if not rec_path.exists() and not page.exists():
                continue
            rec = json.loads(rec_path.read_text())
            if file_hash(page) != rec['page_sha256']:
                raise ValueError(f'{filename}: accepted page has changed')
            if brief=='ehlikitap':
                for artifact in rec.get('verdict_artifacts',{}).values():
                    if file_hash(PG/artifact['path']) != artifact['sha256']:
                        raise ValueError(f'{filename}: accepted verdict/gap evidence changed')
            if rec['base']['sha256'] != info['sha256']:
                raise ValueError(f'{filename}: accepted base differs from the current frozen base')
            original = page.read_text()
            originals.append(original)
            if rec.get('accepted_annotations'):
                ann = PG / rec['accepted_annotations']
                if file_hash(ann) != rec.get('annotations_sha256'):
                    raise ValueError(f'{filename}: accepted annotation snapshot has changed')
                rs = R.load(ann)
            else:
                # Historical Islamic pages have only the accepted Markdown/hash.
                # Recover records only when their complete rendered layout matches it.
                rs, seen = [], set()
                for r in R.load(PG / rec['annotations']):
                    if brief == 'zengin':
                        r.setdefault('gelenek', 'islami')
                    line = VAL.B.tag_line(r)
                    if line in original.splitlines() and line not in seen:
                        rs.append(r)
                        seen.add(line)
            if len(rs) != rec['kept']:
                raise ValueError(f'{filename}: accepted record count differs')
            rebuilt, errors = R.render_page(base, rs, original.split('\n\n')[0], None, metas)
            if errors or rebuilt.split('\n## Kaynak kayıtları')[0] != original.split('\n## Kaynak kayıtları')[0]:
                raise ValueError(f'{filename}: records do not reproduce the accepted page')
            valid, dropped, _ = VAL.check_records(s, target, rs, 'ehlikitap') if brief == 'ehlikitap' else (rs, [], [])
            if dropped:
                raise ValueError(f'{filename}: invalid accepted records: {dropped}')
            recs.extend(valid)
            parts.append(f'{brief} {len(rs)}')
            provenance[brief] = {'page': rel(page), 'page_sha256': file_hash(page),
                                 'manifest_sha256': file_hash(rec_path)}
        ids = [r['id'] for r in recs]
        if len(ids) != len(set(ids)):
            raise ValueError('duplicate IDs across the accepted layers')
        registry = merged_registry(originals) if parts else ''
    except (OSError, KeyError, ValueError, SystemExit) as exc:
        print(f'WARNING: S{s} {target} merge: {exc}', flush=True)
        return False
    if not parts:
        print(f"WARNING: S{s} {target}: no accepted page of either pass; nothing merged", flush=True)
        return False
    head = (f"<!-- schema:zenginlestirme {VAL.B.SCHEMA['version']}; target:{'S' + str(s) if target == 'surah' else target}; "
            f"base:{info['path']} sha256:{info['sha256']}; merged:{time.strftime('%Y-%m-%d')}; layers: {', '.join(parts)} -->")
    text, errors = R.render_page(base, recs, head, None if target == "surah" else R.AYAH_SECTION, metas)
    text = text.rsplit('\n## Kaynak kayıtları', 1)[0] + '\n' + registry
    if errors:
        for e in errors:
            print(f"WARNING: S{s} {target} merge: {e}", flush=True)
        return False
    dst = OUT / f"s{s:03d}" / f"{stem}.merged.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_suffix('.md.tmp')
    tmp.write_text(text, encoding='utf-8')
    page_errors = VAL.check_page(tmp, base, recs)
    if page_errors:
        tmp.unlink()
        print(f'WARNING: S{s} {target} merge: {page_errors}', flush=True)
        return False
    tmp.replace(dst)
    dst.with_suffix('.json').write_text(json.dumps({'base': info, 'layers': provenance,
        'partial': len(parts) < 2, 'page_sha256': file_hash(dst)}, indent=2) + '\n')
    print(json.dumps({"surah": s, "target": target, "merged": rel(dst), "layers": parts,
                      'partial': len(parts) < 2}, ensure_ascii=False), flush=True)
    return True



def target_roots(s,target):
    """The Arabic roots of a page's frozen text (dictionary labels; for the surah page also the images' members)."""
    ts=DISC.targets_of(s)
    if target=='surah':
        return sorted({r for t in ts if t['target'].startswith('sec') for r in DISC.target_roots(t)})
    t=next((t for t in ts if t['target']==target),None)
    if t is None: raise ValueError(f'{target}: not a target of the S{s} pack')
    return DISC.target_roots(t)


def root_section(roots):
    from enrichment.bible import hebrew
    table=hebrew.table(roots) if roots else '(The frozen text cites no Arabic root.)'
    return ('# Semitic root table of this page\n\nThe Arabic roots this page cites, with the Hebrew and Biblical Aramaic '
            'roots that correspond to them by regular sound correspondences and exist in the lexicon (hebrew.py). Each '
            'root needs one line in root_verdicts.jsonl (Step 3b).\n\n'+table)


def build_prompt(s,target,d,roots=None):
    parts=[header(s,target,d,'agent'),(PROMPTS/'common.md').read_text(),(PROMPTS/'ehlikitap.md').read_text()]
    if roots is not None: parts.append(root_section(roots))
    return '\n\n'.join(parts)


def spawn_target(s,target,attempt=1,revise=False):
    """revise: a new attempt (>1) on an ACCEPTED page, finished with --trial and compared; `supersede` then archives
    the accepted page and accepts the revision (user, 2026-10-09: re-author S103 after the relevance rule)."""
    d=call_dir(s,target,attempt)
    if blocked(d) or (accepted(s,target) and not revise):
        raise ValueError(f'{target}: already started or accepted; never rerun (a revision: --revise --attempt N)')
    if revise and attempt<2:
        raise ValueError('--revise needs --attempt 2 or more (attempt 1 is the accepted call)')
    inputs=bible_inputs(s,target)
    from enrichment.bible import hebrew
    if not hebrew.INDEX.exists(): raise ValueError('build the Hebrew root index first: hebrew.py build')
    inputs[rel(hebrew.INDEX)]=file_hash(hebrew.INDEX)
    roots=target_roots(s,target)
    prompt=build_prompt(s,target,d,roots)
    _,base,info=R.target_page(s,target)
    row=dict(surah=s,target=target,brief=BRIEF,attempt=attempt,model='opus',model_id=MODELS['opus'][1],effort=EFFORT,
             base_sha256=info['sha256'],base_words=len(base.split()),pack_sha256=file_hash(wd(s)/'pack/pack.json'),
             bible_inputs=inputs,estimate=estimate(s,target,'opus',EFFORT),semitic_roots=roots)
    AR.prepare(d,prompt,row,'enrich','annotations.jsonl',lookup=False)
    return {'status':'prepared','surah':s,'target':target,'dir':rel(d),'spawn':rel(d/'spawn.md')}


def supersede_target(s,target,d):
    """Accept a revision that finished ok with --trial: the accepted page's files move to
    out/sNNN/superseded/<stem>.<date>/ (kept, listed in the run log), then the revision is finished for real."""
    log=d/'run.log.json'
    if not log.exists(): raise ValueError(f'{d}: not finished; finish it with --trial first')
    row=json.loads(log.read_text())
    if row.get('status')!='ok' or 'trial' not in str(row.get('check','')):
        raise ValueError(f'{d}: only a revision finished ok with --trial can supersede (status {row.get("status")}, check {row.get("check")})')
    out=OUT/f's{s:03d}'; stem=page_name(s,target)[:-3]           # e.g. 103_1.ehlikitap
    old=sorted(out.glob(stem+'.*'))
    if not old: raise ValueError(f'no accepted page {stem} to supersede')
    arch=out/'superseded'/f'{stem}.{time.strftime("%Y%m%d-%H%M%S")}'
    arch.mkdir(parents=True)
    for f in old: f.rename(arch/f.name)
    kept=d/'run.log.trial.json'
    with kept.open('xb') as f: f.write(log.read_bytes())
    log.unlink()
    print(f'NOTE: {target}: {len(old)} accepted file(s) moved to {rel(arch)}')
    return finish_target(s,target,d,False,reaudit_of=kept.name)


def reaudit_target(s,target,d,trial=False):
    """Finish again after a failed finish, with no model call: the failed run log is kept as run.log.failed-N.json
    (never overwritten), then the transcript, the operator review (review.py) and the records are checked anew."""
    log=d/'run.log.json'
    if not log.exists(): raise ValueError(f'{d}: not finished yet; use finish')
    row=json.loads(log.read_text())
    if row.get('status')!='error': raise ValueError(f'{d}: only a failed finish can be re-audited (status {row.get("status")})')
    n=1
    while (d/f'run.log.failed-{n}.json').exists(): n+=1
    kept=d/f'run.log.failed-{n}.json'
    with kept.open('xb') as f: f.write(log.read_bytes())
    log.unlink()
    return finish_target(s,target,d,trial,reaudit_of=kept.name)


def finish_target(s,target,d,trial=False,reaudit_of=None):
    if (d/'run.log.json').exists(): raise ValueError(f'{d}: already finished')
    row=json.loads((d/'started.json').read_text())
    if row.get('runner')!='agent': raise ValueError('expected a native page-agent call')
    if (row.get('surah'), row.get('target')) != (s, target):
        raise ValueError('call target differs from the requested page')
    result=AR.finish(d,'annotations.jsonl')
    row.update(cost_usd=result.get('total_cost_usd'),cost_basis=result.get('cost_basis'),transcript=result.get('transcript'),
               usage=result.get('usage'),stop_reason=result.get('stop_reason'),
               allowed_beyond_original_grammar=result.get('allowed_beyond_original_grammar'),
               tool_use_outside_rule=result.get('tool_use_outside_rule'))
    if (d/'operator-review.json').exists(): row['operator_review_sha256']=file_hash(d/'operator-review.json')
    if reaudit_of: row['reaudit_of']=reaudit_of
    try:
        if result.get('is_error') or not result.get('completed'):
            checked={'ok':False,'check':result.get('error') or 'agent did not complete'}
        else:
            checked=finish(s,target,d,trial,row)
        row.update(status='ok' if checked.pop('ok') else 'error',**checked)
    except (Exception,SystemExit) as exc:
        row.update(status='error',check=str(exc))
    row['seconds']=round(time.time()-time.mktime(time.strptime(row['started'],'%Y-%m-%dT%H:%M:%S')))
    (d/'run.log.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
    log(row)
    return row


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cmd',choices=('status','build','spawn','finish','reaudit','supersede','merge'))
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--target',help='surah, S:A, ayat or all')
    ap.add_argument('--attempt',type=int,default=1)
    ap.add_argument('--trial',action='store_true',help='finish in the call directory only')
    ap.add_argument('--revise',action='store_true',help='spawn a new attempt on an accepted page (then finish --trial, compare, supersede)')
    a=ap.parse_args()
    if a.cmd=='status':
        for d in sorted(wd(a.surah).glob('ehlikitap*')):
            p=d/'run.log.json'
            state=json.loads(p.read_text()).get('status') if p.exists() else 'started' if blocked(d) else 'prepared'
            print(f'{d.name}: {state}')
        return
    if not a.target: ap.error('--target is required')
    failed=0
    for target in select(a.surah,a.target):
        d=call_dir(a.surah,target,a.attempt)
        try:
            if a.cmd=='build':
                try: roots=target_roots(a.surah,target)
                except (OSError,ValueError,KeyError) as exc: roots=None; print(f'NOTE: {target}: no root table ({exc})')
                prompt=build_prompt(a.surah,target,d,roots)
                issue=None
                try: bible_inputs(a.surah,target)
                except (OSError,ValueError,KeyError) as exc: issue=str(exc)
                print(json.dumps(dict(target=target,prompt_chars=len(prompt),estimate=estimate(a.surah,target,'opus',EFFORT),
                                      ready=issue is None,preflight=issue,call_dir=rel(d)),ensure_ascii=False))
            elif a.cmd=='spawn': print(json.dumps(spawn_target(a.surah,target,a.attempt,a.revise),ensure_ascii=False))
            elif a.cmd=='supersede':
                result=supersede_target(a.surah,target,d)
                print(json.dumps(result,ensure_ascii=False)); failed+=result['status']!='ok'
            elif a.cmd in ('finish','reaudit'):
                result=(finish_target if a.cmd=='finish' else reaudit_target)(a.surah,target,d,a.trial)
                print(json.dumps(result,ensure_ascii=False)); failed+=result['status']!='ok'
            else: failed+=not merge_page(a.surah,target)
        except (Exception,SystemExit) as exc:
            failed+=1; print(f'WARNING: S{a.surah} {target}: {exc}')
    if failed: raise SystemExit(1)

if __name__=='__main__': main()
