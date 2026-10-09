#!/usr/bin/env python3
"""Run prepared Bible discovery readers through `codex exec` from a Claude Code orchestrator (no Codex parent).

Same two-turn protocol as discovery_native.py, in the same files: start → turn 1 (`codex exec`) → snapshot →
the fixed follow-up as turn 2 in the same session (`codex exec resume`) → audit → policy review → finish. The run log
also records the API-equivalent cost of the whole session (codexrun.RATES).

  discovery_exec.py run --surah S --run-tag TAG [--targets 103:1,surah] [--parallel 50]
  discovery_exec.py cost --surah S --run-tag TAG       expected cost before a run, actual after

Each phase is done once: a finished phase is skipped, a turn whose stream exists is never started again (a dead
turn is printed as a WARNING; it needs a fresh attempt). The policy review finishes a session only when its tool
calls stayed inside the session's call directory (reads of prompt/package, writes of list.tsv/followup.tsv) with no
network, scripts or other files; anything else is printed and the session is left for the operator.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import shlex
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from enrichment.bible import codexrun as X, discovery as D, discovery_native as N  # noqa: E402

# Expected cost per reader session (both turns), from the S87 Luna sessions (~1.0M input tokens, ~90% cached,
# ~50k output) priced at codexrun.RATES; Sol high is assumed to read about the same.
EXPECTED = {'luna': 0.05, 'sol': 1.00}
NETWORK = re.compile(r'\b(curl|wget|ssh|scp|nc|git|rsync)\s')


def task_name(s, tag, target, model):
    return re.sub(r'[^a-z0-9_]', '_', f'bible_s{s:03d}_{tag}_{target}_{model}'.lower())


JS_STRING = re.compile(r'"(?:[^"\\\n]|\\.)*"' + r"|'(?:[^'\\\n]|\\.)*'" + r'|`(?:[^`\\]|\\.)*`')
# absolute paths under a filesystem root (a sed address like /pattern/d is not a path)
ABS_PATH = re.compile(r'(?<![\w.])/(?:Users|Volumes|private|tmp|var|etc|home|opt|usr|dev|System|Library|bin|sbin|root)'
                      r'(?:/[A-Za-z0-9_.@+-]*)+')
STREAMS = re.compile(r'^/dev/(null|stdin|stdout|stderr|fd/\d+)$')
SCRATCH = ('/tmp/', '/private/tmp/', '/var/folders/')
TOOLS = {'exec_command', 'apply_patch'}
OPERATIONAL = {'clock__curr_time', 'wait'}   # reading the clock, waiting on a running command: noted, not research


JS_ESC = re.compile(r'\\(u\{[0-9a-fA-F]+\}|u[0-9a-fA-F]{4}|x[0-9a-fA-F]{2}|.)', re.S)
JS_SIMPLE = {'n': '\n', 't': '\t', 'r': '\r', 'b': '\b', 'f': '\f', 'v': '\v', '0': '\0'}


def unquote(lit):
    """The value of a JavaScript string literal (quotes or backticks), escapes decoded."""
    def esc(m):
        e = m[1]
        if e.startswith('u{'):
            return chr(int(e[2:-1], 16))
        if e[0] in 'ux' and len(e) > 1:
            return chr(int(e[1:], 16))
        return JS_SIMPLE.get(e, e)
    return JS_ESC.sub(esc, lit[1:-1])


def code_of(call):
    """(code text, tool names) of one native call; plain function calls are wrapped as code too."""
    name, args = call.get('name', '').split('.')[-1], call.get('arguments') or ''
    if name == 'exec':
        return args, set(re.findall(r'tools\.(\w+)', args))
    if name == 'exec_command':
        try:
            return json.dumps(json.loads(args).get('cmd', '')), {'exec_command'}
        except ValueError:
            return args, {'exec_command'}
    if name == 'apply_patch':
        return json.dumps(args), {'apply_patch'}
    return args, {name}


REL_PATH = re.compile(r'(?<![\w/.])enrichment/[A-Za-z0-9_./@+-]+')
VAR = re.compile(r'\b(?:const|let|var)\s+(\w+)\s*=\s*("(?:[^"\\\n]|\\.)*"|\'(?:[^\'\\\n]|\\.)*\')')
NET_CMDS = {'curl', 'wget', 'ssh', 'scp', 'nc', 'git', 'rsync', 'ftp', 'telnet'}
MODEL_CMDS = {'codex', 'claude', 'node', 'npx', 'deno'}
SCRIPT_CMDS = {'python', 'python3', 'bash', 'sh', 'zsh', 'perl', 'ruby'}
UNSAFE_CODE = re.compile(r'\b(urllib|requests|socket|subprocess|os\.system|os\.popen|http\.client|shutil\.rmtree)\b')


def strings_of(code):
    """String literals of a call's JavaScript, with ${name} filled from string constants declared in it."""
    env = {m[1]: unquote(m[2]) for m in VAR.finditer(code)}
    out = []
    for m in JS_STRING.finditer(code):
        s = unquote(m[0])
        out.append(re.sub(r'\$\{(\w+)\}', lambda v: env.get(v[1], v[0]), s))
    return out


HEREDOC = re.compile(r"([^\n]*)<<-?\s*['\"]?(\w+)['\"]?[^\n]*\n(.*?)\n\2\b", re.S)


def drop_data_heredocs(s):
    """Remove heredoc bodies that are data (`cat > list.tsv <<EOF`); keep those fed to an interpreter (code)."""
    def keep(m):
        head = m[1].strip().split()[0].rsplit('/', 1)[-1] if m[1].strip() else ''
        return m[0] if head in SCRIPT_CMDS else m[1] + '<<' + m[2] + ' [data]'
    return HEREDOC.sub(keep, s)


def policy(d, calls):
    """(violations, notes) for a reader's tool calls. Readers may wrap the two tools in their own JavaScript, so the
    review looks at what the code can reach: the tools it calls, every file its strings name (absolute paths and
    repository paths, which must be the reader's own prompt, package or TSVs, or the workspace root as a workdir),
    the files its patches write (only list.tsv/followup.tsv), and the commands it runs (no network, no model or
    repository scripts; a local script that only touches the reader's own files is recorded as a note)."""
    bad, notes = [], []
    own = {d / 'prompt.md', d / 'package.md', d / 'list.tsv', d / 'followup.tsv', d, X.ROOT.resolve()}
    for c in calls:
        code, tools = code_of(c)
        where = f"turn {c.get('phase')} {c.get('call_id')}"
        if tools - TOOLS - OPERATIONAL:
            bad.append(f"{where}: tool outside the reader rules: {', '.join(sorted(tools - TOOLS - OPERATIONAL))}")
        if tools & OPERATIONAL:
            notes.append(f"{where}: operational tool {', '.join(sorted(tools & OPERATIONAL))}")
        lits = strings_of(code)
        patches = [x for x in lits if '*** Begin Patch' in x]
        for x in patches:
            for m in re.finditer(r'\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)', x):
                q = Path(m[1].strip())
                q = (q if q.is_absolute() else X.ROOT / q).resolve()
                if q not in {d / 'list.tsv', d / 'followup.tsv'}:
                    bad.append(f'{where}: patch writes {q}')
        rest = '\n'.join(drop_data_heredocs(x) for x in lits if '*** Begin Patch' not in x)
        named = [Path(m[0]).resolve() for m in ABS_PATH.finditer(rest)]
        named += [(X.ROOT / m[0].rstrip('.')).resolve() for m in REL_PATH.finditer(rest)]
        for q in dict.fromkeys(named):
            if q in own or STREAMS.match(str(q)):
                continue
            if str(q).startswith(SCRATCH):
                notes.append(f'{where}: scratch file in the system temp directory: {q}')
            else:
                bad.append(f'{where}: names {q}')
        if re.search(r'https?://', rest):
            bad.append(f'{where}: names a URL')
        heads = {seg.strip().split()[0].rsplit('/', 1)[-1] for seg in re.split(r'[\n;|&]+', rest)
                 if seg.strip() and re.match(r'[A-Za-z_./-]', seg.strip())}
        if heads & NET_CMDS:
            bad.append(f"{where}: network or repository command: {', '.join(sorted(heads & NET_CMDS))}")
        if heads & MODEL_CMDS:
            bad.append(f"{where}: model or agent command: {', '.join(sorted(heads & MODEL_CMDS))}")
        if heads & SCRIPT_CMDS:
            if UNSAFE_CODE.search(rest):
                bad.append(f'{where}: script with network/process access: {rest[:200]}')
            else:
                notes.append(f'{where}: local script on its own files ({", ".join(sorted(heads & SCRIPT_CMDS))})')
        if c.get('phase') == 2 and 'followup.tsv' not in code:
            notes.append(f'{where}: follow-up turn call not about followup.tsv: {code[:160]}')
    return bad, notes


def one(s, tag, target, model):
    d = D.tdir(s, target, tag) / model
    lock = d / 'exec.lock'
    if not (d / 'prompt.md').exists():
        return f'{target} {model}: WARNING not prepared'
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        pid = lock.read_text().strip()
        try:
            os.kill(int(pid), 0)
            return f'{target} {model}: NOTE another runner (pid {pid}) is working on this session; skipped'
        except (ValueError, ProcessLookupError):
            lock.unlink()
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    try:
        return run_session(s, tag, target, model, d)
    finally:
        lock.unlink(missing_ok=True)


def run_session(s, tag, target, model, d):
    a = SimpleNamespace(surah=s, target=target, run_tag=tag, model=model, task=task_name(s, tag, target, model),
                        reviewed=False, protocol_finding=[], phase='start')
    say = lambda m: f'{target} {model}: {m}'  # noqa: E731
    if (d / 'run.log.json').exists():
        return say('already finished, skipped')
    if not (d / 'prompt.md').exists():
        return say('WARNING not prepared')
    start = json.loads((d / 'started.json').read_text()) if (d / 'started.json').exists() else None
    if start is None:
        N.run_phase(a, runner='codex-exec')
        start = json.loads((d / 'started.json').read_text())
    elif start.get('runner') != 'codex-exec':
        return say(f"WARNING started by runner {start.get('runner')}; not continued here")
    model_id, effort = start['model'], start['effort']
    if not (d / 'turn1.stream.jsonl').exists():
        r = X.turn(d, 1, (d / 'spawn.md').read_text(), model_id, effort)
        if not (r['completed'] and r['thread_id']):
            return say(f"WARNING turn 1 failed (rc {r['returncode']}): {r['stderr'][-300:]}")
        D.save(d / 'session.json', {'agent_path': start['agent_path'], 'agent_id': r['thread_id'],
                                    'transcript': str(X.rollout(r['thread_id'])), 'runner': 'codex-exec'})
    if not (d / 'session.json').exists():
        return say('WARNING turn 1 started earlier but never completed (no session.json); needs a fresh attempt')
    session = json.loads((d / 'session.json').read_text())
    if not (d / 'turn1.json').exists():
        a.phase = 'snapshot'
        N.run_phase(a, runner='codex-exec')
    if not (d / 'turn2.stream.jsonl').exists():
        r = X.turn(d, 2, (d / 'followup.txt').read_text(), model_id, effort, thread=session['agent_id'])
        if not r['completed'] or r.get('error'):
            return say(f"WARNING turn 2 failed (rc {r['returncode']}): {r.get('error') or r['stderr'][-300:]}")
    a.phase = 'audit'
    calls = N.run_phase(a, runner='codex-exec')
    bad, notes = policy(d, calls)
    D.save(d / 'policy_review.json', {'violations': bad, 'notes': notes, 'calls': len(calls),
                                      'reviewer': 'discovery_exec.policy (automatic) for the Claude Code orchestrator'})
    if bad:
        return say('WARNING policy review found violations; not finished:\n  ' + '\n  '.join(bad))
    c = X.cost(Path(session['transcript']))
    a.phase, a.reviewed = 'finish', True
    try:
        row = N.run_phase(a, runner='codex-exec', extra={**c, 'cost_basis': 'API-equivalent at codexrun.RATES '
                                                          '(Codex subscription; usage counts)', 'policy_notes': notes})
    except SystemExit:
        row = json.loads((d / 'run.log.json').read_text())
        return say(f"WARNING finished with status {row['status']}: {row.get('protocol_findings')} "
                   f"{row.get('consolidation_error') or ''}")
    extra = f"; NOTE {len(notes)} policy note(s): " + ' | '.join(notes) if notes else ''
    return say(f"ok, {row['turn1_rows']} + {row['turn2']['rows_added']} rows, ${c['usd_equivalent']:.3f}{extra}")


def jobs(s, tag, targets):
    ts = D.targets_of(s)
    if targets:
        want = set(targets.split(','))
        ts = [t for t in ts if t['target'] in want or ('surah' in want and t['target'].startswith('sec'))]
    return [(t['target'], m) for t in ts for m in D.readers(s, tag)
            if (D.tdir(s, t['target'], tag) / m / 'prompt.md').exists()]


def cost(s, tag, targets):
    js = jobs(s, tag, targets)
    exp = sum(EXPECTED.get(m, 0) for _, m in js)
    act, done = 0.0, 0
    for target, m in js:
        f = D.tdir(s, target, tag) / m / 'run.log.json'
        if f.exists():
            act += json.loads(f.read_text()).get('usd_equivalent') or 0
            done += 1
    print(f'S{s} {tag}: {len(js)} reader sessions; expected ≈ ${exp:.2f} API-equivalent; '
          f'finished {done}, actual ${act:.2f}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('phase', choices=('run', 'cost'))
    ap.add_argument('--surah', type=int, required=True)
    ap.add_argument('--run-tag', required=True)
    ap.add_argument('--targets')
    ap.add_argument('--parallel', type=int, default=7)
    a = ap.parse_args()
    if a.phase == 'cost':
        return cost(a.surah, a.run_tag, a.targets)
    js = jobs(a.surah, a.run_tag, a.targets)
    cost(a.surah, a.run_tag, a.targets)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as pool:
        futs = {pool.submit(one, a.surah, a.run_tag, t, m): (t, m) for t, m in js}
        for f in concurrent.futures.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:  # recorded, never silent
                t, m = futs[f]
                print(f'{t} {m}: WARNING {type(e).__name__}: {e}', flush=True)
    cost(a.surah, a.run_tag, a.targets)


if __name__ == '__main__':
    main()
