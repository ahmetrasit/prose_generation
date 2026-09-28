#!/usr/bin/env python3
"""v15 runner: Luna through `codex exec`, Opus through `claude -p` (both on the subscriptions).

Rules kept here, not by habit:
- a completed unit is never rerun;
- a failed unit is not retried automatically; `--repair` allows one further attempt, logged;
- every call is logged in out/ledger.jsonl (time, unit, model, status, seconds, cost where reported);
- an Opus call starts only when its estimate is below gate.usd_per_call and keeps the ayah within
  gate.usd_per_ayah; once started it runs to the end, whatever it then costs. The gate is Opus-only by
  design: Luna runs on the flat Codex subscription and reports tokens, not dollars (logged as usage);
- a CLI usage error that never reached a model (non-zero exit, no output, under a minute, or a usage
  message on stderr) is logged as cli_error and does not block the unit; anything else is a failed run;
- agents run from a fresh temp directory in safe mode (no CLAUDE.md, memory, skills or hooks)
  and may read only v15/data.

  luna frames|loanwords|profiles|all [--limit N] [--parallel P] [--only JOB]   pending Luna jobs (all kinds share one pool)
  window --surah S [--ayah A]      Opus window reading      -> out/sNNN/window_lo-hi/window.json
  discover --ref S:A               Opus ayah reading        -> out/sNNN/S_A/record.json
  evidence --ref S:A               Luna evidence notes      -> out/sNNN/S_A/evidence.json
  write --ref S:A                  Opus Turkish commentary  -> out/sNNN/S_A/commentary.tr.md
  surah --surah S                  Opus surah commentary    -> out/sNNN/surah.tr.md
  status --surahs 1,100            what exists for a scope
Add --dry to see what would run (prompt size, command) without calling any model.
"""
import argparse
import concurrent.futures as cf
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

import build
import lib
from lib import CFG, DATA, OUT

LEDGER = os.path.join(OUT, 'ledger.jsonl')


# ------------------------------------------------------------------ ledger and guards

def log(entry):
    os.makedirs(OUT, exist_ok=True)
    entry = {'time': time.strftime('%Y-%m-%dT%H:%M:%S'), **entry}
    with open(LEDGER, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def ledger():
    if not os.path.exists(LEDGER):
        return []
    with open(LEDGER, encoding='utf-8') as f:
        return [json.loads(l) for l in f if l.strip()]


def may_run(unit, out_path, repair):
    if os.path.exists(out_path):
        print(f"skip {unit}: done ({os.path.relpath(out_path, lib.HERE)})")
        return False
    # a CLI usage error never reached a model, so it is not a failed run
    failed = [e for e in ledger() if e.get('unit') == unit and e.get('status') not in ('ok', 'cli_error')]
    if failed and not repair:
        print(f"skip {unit}: failed before ({failed[-1].get('status')}); not retried. Use --repair once if wanted.")
        return False
    if repair and any(e.get('repair') for e in failed):
        print(f"skip {unit}: its one repair attempt is already used")
        return False
    return True


def spent(ayah):
    return sum(e.get('cost_usd') or 0 for e in ledger() if e.get('ayah') == ayah)


def estimate(step, chars):
    """Pre-call estimate: the dearest earlier call of the same step, scaled up by prompt size;
    config defaults until the ledger has a reported cost for the step."""
    hist = [e for e in ledger() if e.get('step') == step and e.get('cost_usd') and e.get('prompt_chars')]
    if not hist:
        p, m = CFG['pricing'], CFG['estimate_model']
        tokens_in = chars / m['chars_per_token'] + m['cli_overhead_tokens']
        usd = (tokens_in * p['opus_in_per_mtok'] * p['cache_write_multiplier']
               + m['tool_rounds'][step] * tokens_in * p['opus_cache_read_per_mtok']
               + m['expected_output_tokens'][step] * p['opus_out_per_mtok']) / 1e6
        return usd, 'price-based default'

    worst = max(hist, key=lambda e: e['cost_usd'])
    return worst['cost_usd'] * max(1.0, chars / worst['prompt_chars']), f'ledger ({len(hist)} runs)'


def gate_ok(unit, step, chars, ayah):
    est, basis = estimate(step, chars)
    if est >= CFG['gate']['usd_per_call']:
        print(f"stop {unit}: estimate ${est:.2f} ({basis}) is not below the ${CFG['gate']['usd_per_call']:.2f} call gate")
        return False, est
    if ayah and spent(ayah) + est > CFG['gate']['usd_per_ayah']:
        print(f"stop {unit}: {ayah} has spent ${spent(ayah):.2f}; with this call's estimate ${est:.2f} "
              f"it would pass the ${CFG['gate']['usd_per_ayah']:.2f} ayah gate")
        return False, est
    return True, est


def fill(template, **kw):
    for k, v in kw.items():
        template = template.replace('{' + k + '}', str(v))
    return template


def prompt(name):
    with open(os.path.join(lib.PROMPTS, name), encoding='utf-8') as f:
        return f.read()


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def parse_json_text(text):
    t = text.strip()
    t = re.sub(r'^```(?:json)?\s*|\s*```$', '', t)
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        m = re.search(r'\{.*\}', t, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                return None
    return None


# ------------------------------------------------------------------ model calls

def call_opus(unit, step, text, out_path, schema=None, tools=True, ayah=None, dry=False, repair=False):
    if not may_run(unit, out_path, repair):
        return None
    m = CFG['models']['opus']
    cmd = ['claude', '-p', '--model', m['model'], '--effort', m['effort'], '--output-format', 'json',
           '--safe-mode', '--no-session-persistence', '--permission-mode', 'dontAsk']
    if tools:
        cmd += ['--tools', 'Read', 'Grep', 'Glob', '--allowedTools', 'Read', 'Grep', 'Glob', '--add-dir', DATA]
    else:
        cmd += ['--tools', '']
    if schema:
        cmd += ['--json-schema', json.dumps(lib.read_json(os.path.join(lib.SCHEMAS, schema)))]
    ok, est = gate_ok(unit, step, len(text), ayah)
    if dry:
        shown = [c if len(c) < 120 else c[:60] + '…' for c in cmd]
        print(f"[dry] {unit}: prompt {len(text):,} chars (~{len(text) // 3:,} tokens), estimate ${est:.2f} -> "
              f"{os.path.relpath(out_path, lib.HERE)}\n      {' '.join(shown)}")
        return None
    if not ok:
        return None
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    lib.write_text(out_path + '.prompt.md', text)
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix='v15_opus_') as cwd:
        try:
            p = subprocess.run(cmd, input=text, capture_output=True, text=True, cwd=cwd,
                               timeout=CFG.get('timeout_s', 5400))
            raw, err, code = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired:
            raw, err, code = '', 'timeout', None
    lib.write_text(out_path + '.raw.json', raw + ('\n\n[stderr]\n' + err if err else ''))
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        obj = None
    cost = obj.get('total_cost_usd') if isinstance(obj, dict) else None
    status = 'ok'
    if obj is None and is_cli_error(code, raw, err, time.time() - t0):
        status = 'cli_error'
    elif not isinstance(obj, dict) or obj.get('is_error'):
        status = 'error'
    elif schema:
        data = obj.get('structured_output')
        if data is None and isinstance(obj.get('result'), str):
            data = parse_json_text(obj['result'])
        if data is None:
            status = 'no_json'
        else:
            lib.write_json(out_path, data)
    else:
        if not (obj.get('result') or '').strip():
            status = 'no_text'
        else:
            lib.write_text(out_path, obj['result'].strip() + '\n')
    log({'unit': unit, 'step': step, 'ayah': ayah, 'model': m['model'], 'effort': m['effort'], 'status': status,
         'seconds': round(time.time() - t0), 'cost_usd': cost, 'estimate_usd': round(est, 2),
         'prompt_chars': len(text), 'repair': repair,
         'out': os.path.relpath(out_path, lib.HERE)})
    print(f"{unit}: {status} in {round(time.time() - t0)}s" + (f", ${cost:.2f}" if cost else ''))
    return status


USAGE_ERROR = re.compile(r'unexpected argument|unrecognized|unknown option|invalid value|^Usage:|error: .*argument',
                         re.I | re.M)


def is_cli_error(code, output, err, seconds):
    """True only when the CLI itself refused the call, so no model ran."""
    if code in (0, None) or output.strip():
        return False
    return seconds < 60 or bool(USAGE_ERROR.search(err or ''))


def call_luna(unit, text, out_path, schema, ayah=None, dry=False, repair=False):
    if not may_run(unit, out_path, repair):
        return None
    m = CFG['models']['luna']
    base = ['codex', 'exec', '-m', m['model'], '-c', f'model_reasoning_effort="{m["effort"]}"',
            '--disable', 'skill_search', '--skip-git-repo-check', '--ephemeral', '-s', 'read-only',
            '--output-schema', os.path.join(lib.SCHEMAS, schema), '--json']
    if dry:
        print(f"[dry] {unit}: prompt {len(text):,} chars (~{len(text) // 3:,} tokens) -> "
              f"{os.path.relpath(out_path, lib.HERE)}\n      {' '.join(base)} -o <tmp>/last.json -C <tmp> -")
        return None
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix='v15_luna_') as cwd:
        last = os.path.join(cwd, 'last.json')   # fresh per call: a stale message can never be read
        try:
            p = subprocess.run(base + ['-o', last, '-C', cwd, '-'], input=text, capture_output=True, text=True,
                               timeout=CFG.get('timeout_s', 5400))
            events, err, code = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired:
            events, err, code = '', 'timeout', None
        data = parse_json_text(read(last)) if os.path.exists(last) else None
    usage = {}
    for line in events.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(ev, dict) and isinstance(ev.get('usage'), dict):
            usage = ev['usage']
    status = 'ok'
    if data is None:
        status = 'cli_error' if is_cli_error(code, events, err, time.time() - t0) else 'no_json'
        lib.write_text(out_path + '.failed.log', events[-20000:] + '\n\n[stderr]\n' + err[-5000:])
    else:
        lib.write_json(out_path, data)
    log({'unit': unit, 'step': unit.split(':')[1], 'ayah': ayah, 'model': m['model'], 'effort': m['effort'],
         'status': status, 'seconds': round(time.time() - t0), 'usage': usage, 'prompt_chars': len(text),
         'repair': repair,
         'out': os.path.relpath(out_path, lib.HERE)})
    print(f"{unit}: {status} in {round(time.time() - t0)}s")
    return status


# ------------------------------------------------------------------ steps

def luna_jobs(kind, limit=None, parallel=1, dry=False, repair=False, only=None):
    """Pending jobs of one kind, or of every kind ('all') in one pool of `parallel` slots."""
    kinds = ['frames', 'loanwords', 'profiles'] if kind == 'all' else [kind]
    jobs = []
    for jp in sorted(p for k in kinds for p in glob.glob(os.path.join(DATA, k, 'jobs', '*', 'job.json'))):
        if only and os.path.basename(os.path.dirname(jp)) != only:
            continue
        job = lib.read_json(jp)
        out = os.path.join(lib.HERE, job['out'])
        if os.path.exists(out):
            continue
        jd = os.path.dirname(jp)
        text = prompt(job['prompt']) + '\n' + read(os.path.join(jd, 'input.md'))
        for extra in job.get('extra', []):
            text += f"\n\n## {os.path.basename(extra)}\n\n" + read(os.path.join(lib.HERE, extra))
        jobs.append((f"luna:{job['kind']}:{os.path.basename(jd)}", text, out, job['schema']))
    if limit:
        jobs = jobs[:limit]
    print(f"{kind}: {len(jobs)} pending job(s)" + (' (dry)' if dry else ''))
    if dry:
        for u, t, o, s in jobs[:3]:
            call_luna(u, t, o, s, dry=True)
        if jobs:
            print(f"      … total prompt chars {sum(len(t) for _, t, _, _ in jobs):,}")
        return
    with cf.ThreadPoolExecutor(max_workers=max(1, parallel)) as ex:
        list(ex.map(lambda j: call_luna(j[0], j[1], j[2], j[3], repair=repair), jobs))


def ensure_base(s):
    if not os.path.exists(os.path.join(DATA, 'words.tsv')):
        sys.exit('base tables missing: run `python3 build.py base` first')
    build.build_pull([s])


def step_window(s, only=None, dry=False, repair=False):
    ensure_base(s)
    for lo, hi, label in lib.windows_of_surah(s):
        if only and not (lo <= only <= hi):
            continue
        build.build_window(s, lo)
        packet = read(os.path.join(build.window_dir(s, lo, hi), 'packet.md'))
        text = fill(prompt('opus_window.md'), max_images=CFG['prose']['max_images_per_ayah']) + '\n' + packet
        call_opus(f'opus:window:{s}:{lo}-{hi}', 'window', text,
                  os.path.join(build.out_window_dir(s, lo, hi), 'window.json'), schema='window.schema.json',
                  dry=dry, repair=repair)


def step_discover(ref, dry=False, repair=False):
    s, a = [int(x) for x in ref.split(':')]
    ensure_base(s)
    build.build_ayah(s, a)
    packet = read(os.path.join(build.ayah_dir(s, a), 'discover.md'))
    text = fill(prompt('opus_discover.md'), ref=ref, radius=CFG['windows']['local_radius'],
                kwic_max=CFG['concordance']['kwic_max_uses']) + '\n' + packet
    call_opus(f'opus:discover:{ref}', 'discover', text, os.path.join(build.out_ayah_dir(s, a), 'record.json'),
              schema='record.schema.json', ayah=ref, dry=dry, repair=repair)


def step_evidence(ref, dry=False, repair=False):
    s, a = [int(x) for x in ref.split(':')]
    if not os.path.exists(os.path.join(build.out_ayah_dir(s, a), 'record.json')):
        sys.exit(f"{ref}: no record yet (run discover first)")
    ensure_base(s)
    build.build_evidence(s, a)
    text = prompt('luna_evidence.md') + '\n' + read(os.path.join(build.ayah_dir(s, a), 'evidence.md'))
    call_luna(f'luna:evidence:{ref}', text, os.path.join(build.out_ayah_dir(s, a), 'evidence.json'),
              'evidence.schema.json', ayah=ref, dry=dry, repair=repair)


def step_write(ref, dry=False, repair=False):
    s, a = [int(x) for x in ref.split(':')]
    o = build.out_ayah_dir(s, a)
    for need in ('record.json', 'evidence.json'):
        if not os.path.exists(os.path.join(o, need)):
            sys.exit(f"{ref}: {need} missing")
    build.build_write(s, a)
    text = fill(prompt('opus_write.md'), ref=ref, target=CFG['prose']['ayah_words_target'],
                cap=CFG['prose']['ayah_words_cap'], max_images=CFG['prose']['max_images_per_ayah']) \
        + '\n' + read(os.path.join(build.ayah_dir(s, a), 'write.md'))
    call_opus(f'opus:write:{ref}', 'write', text, os.path.join(o, 'commentary.tr.md'), tools=False,
              ayah=ref, dry=dry, repair=repair)


def step_surah(s, dry=False, repair=False):
    build.build_surah(s)
    text = fill(prompt('opus_surah.md'), surah=s) + '\n' + read(os.path.join(lib.WORK, f's{s:03d}', 'surah.md'))
    call_opus(f'opus:surah:{s}', 'surah', text, os.path.join(OUT, f's{s:03d}', 'surah.tr.md'), tools=False,
              dry=dry, repair=repair)


def status(surahs):
    for s in surahs:
        wins = lib.windows_of_surah(s)
        print(f"S{s}: {lib.surah_len(s)} ayat, {len(wins)} window(s)")
        for lo, hi, _ in wins:
            w = os.path.exists(os.path.join(build.out_window_dir(s, lo, hi), 'window.json'))
            print(f"  window {lo}-{hi}: {'done' if w else '-'}")
        for a in range(1, lib.surah_len(s) + 1):
            o = build.out_ayah_dir(s, a)
            marks = ''.join('x' if os.path.exists(os.path.join(o, f)) else '.'
                            for f in ('record.json', 'evidence.json', 'commentary.tr.md'))
            if marks != '...':
                print(f"  {s}:{a} record/evidence/commentary {marks}  spent ${spent(f'{s}:{a}'):.2f}")
        print(f"  surah commentary: {'done' if os.path.exists(os.path.join(OUT, f's{s:03d}', 'surah.tr.md')) else '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd')
    ap.add_argument('kind', nargs='?')
    ap.add_argument('--ref')
    ap.add_argument('--surah', type=int)
    ap.add_argument('--ayah', type=int)
    ap.add_argument('--surahs')
    ap.add_argument('--limit', type=int)
    ap.add_argument('--parallel', type=int, default=CFG['jobs'].get('luna_parallel', 1))
    ap.add_argument('--dry', action='store_true')
    ap.add_argument('--repair', action='store_true')
    ap.add_argument('--only', help='luna: run just this job id')
    x = ap.parse_args()
    if x.cmd == 'luna':
        luna_jobs(x.kind, x.limit, x.parallel, x.dry, x.repair, x.only)
    elif x.cmd == 'window':
        step_window(x.surah, x.ayah, x.dry, x.repair)
    elif x.cmd == 'discover':
        step_discover(x.ref, x.dry, x.repair)
    elif x.cmd == 'evidence':
        step_evidence(x.ref, x.dry, x.repair)
    elif x.cmd == 'write':
        step_write(x.ref, x.dry, x.repair)
    elif x.cmd == 'surah':
        step_surah(x.surah, x.dry, x.repair)
    elif x.cmd == 'status':
        status(build.parse_surahs(x.surahs))
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
