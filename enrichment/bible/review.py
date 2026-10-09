#!/usr/bin/env python3
"""Mechanical classification of a Bible page author's tool calls that fall outside the original call grammar, and
the operator review that lets `enrich.py finish` accept them. Never calls a model.

Kinds (each with strict, mechanical rules; anything else stays unclassified and fails finish):
  read        a read-only shell command, Read, Grep or Glob whose every path is an allowed input: the call
              directory, the pack, the frozen Bible inputs, the corpus, SCHEMA cards, prompts or the Bible tool
              sources (python only as `python3 -I -c` with safe modules and no writes)
  own_output  Read of a file the harness persisted for one of the agent's own earlier calls, announced by name in
              an earlier tool result of the same transcript
  helper      a helper script the agent wrote (Write/Edit in this transcript) and ran with `python3 -I`; its
              content is rebuilt from the transcript's Write/Edit inputs and its literal and argv paths must be
              allowed inputs or the call directory; writing such a script into the session scratchpad
  own_edit    `sed -i` on the agent's own call-directory files, or `mkdir` of the call directory or scratchpad

Auto-allowed for authors from 2026-10-09 (the widened grammar): read, own_output, own_edit inside the call
directory, and helper scripts that live inside the call directory. Helpers in the scratchpad need this review.

  review.py classify --surah S --target S:A              print the classification of every call outside the old rules
  review.py write --surah S --target S:A --reviewer TEXT write operator-review.json (refused if any call is
                                                          unclassified) and copy helper contents into helpers/
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PG = HERE.parents[1]
sys.path.insert(0, str(PG))

SCRATCH = re.compile(r'^/(?:private/)?tmp/claude-\d+/[^/]+/[^/]+/scratchpad(?:/|$)')
TOOL_RESULTS = re.compile(r'^' + re.escape(str(Path.home() / '.claude/projects')) + r'/[^/]+/[^/]+/tool-results/[\w.-]+\.txt$')
READ_PROGS = {'cat', 'head', 'tail', 'ls', 'grep', 'egrep', 'wc', 'echo', 'sort', 'uniq', 'cut', 'nl', 'file', 'stat',
              'printf', 'true'}
SAFE_MODULES = {'json', 'csv', 'sys', 're', 'collections', 'itertools', 'math', 'statistics', 'unicodedata',
                'functools', 'textwrap', 'string', 'operator'}
WRITES = re.compile(r"\.write|open\([^)]*['\"][wax+]|unlink|rmtree|rename|replace\(|remove\(|mkdir|chmod|system\(|"
                    r"popen|exec\(|eval\(|__import__|compile\(")
SED_PRINT = re.compile(r'^\s*(?:(?:\d+|\$|/[^/]*/)(?:,(?:\d+|\$|/[^/]*/))?)?p\s*(?:;\s*(?:(?:\d+|\$|/[^/]*/)'
                       r'(?:,(?:\d+|\$|/[^/]*/))?)?p\s*)*$')
SEPARATORS = {';', '&&', '||', '|', '\n'}
# Bible tools an author may run without -I, with their read-only subcommands; write flags must point into the call dir
BIBLE_TOOLS = {'corpus.py': {'sources', 'get', 'ayah', 'search'}, 'hebrew.py': {'root', 'cognates', 'word', 'table'},
               'validate.py': None, 'verdicts.py': None, 'render.py': None}
WRITE_FLAGS = {'--out', '--report'}
GLOB = re.compile(r'[*?\[]')
SED_SUBST = re.compile(r'^(?:\d+(?:,\d+)?)?(?:s([^\w\s\\])(?:(?!\1).)*\1(?:(?!\1).)*\1[gI0-9]*|d)$')
# Allowed flags per read program: (combinable short letters, long flags, letters that take a value).
FLAGS = {
    'cat': ('nbsAvet', set(), ''), 'head': ('nqvc', set(), 'nc'), 'tail': ('nqvc', set(), 'nc'),
    'ls': ('la1hRtSrdF', set(), ''), 'wc': ('lwcm', set(), ''), 'nl': ('bnw', set(), 'bnw'),
    'grep': ('nivclLwxEFohHrABCme', {'--color=never'}, 'ABCme'), 'egrep': ('nivclLwxohHrABCme', set(), 'ABCme'),
    'sort': ('nrukVfbts', set(), 'kt'), 'uniq': ('cdui', set(), ''), 'cut': ('dfcb', {'--complement'}, 'dfcb'),
    'file': ('b', set(), ''), 'stat': ('', set(), ''),
}


def flags_ok(prog, args):
    """(ok, operands, pattern_given): every flag is in prog's allowlist; operands exclude flag values."""
    letters, longs, takes = FLAGS.get(prog, ('', set(), ''))
    ops, i, pattern = [], 0, False
    while i < len(args):
        t = args[i]
        if t == '--':
            ops += args[i + 1:]
            break
        if t.startswith('--'):
            if t not in longs:
                return False, [], False
        elif prog in ('head', 'tail') and t[1:].isdigit() and t.startswith('-'):
            pass                               # -40: a line count
        elif t.startswith('-') and len(t) > 1:
            body = t[1:]
            for j, c in enumerate(body):
                if c not in letters:
                    return False, [], False
                if c in takes:
                    pattern = pattern or c == 'e'
                    if j == len(body) - 1:
                        i += 1                 # the value is the next token
                    break                      # the rest of the token is the value
        else:
            ops.append(t)
        i += 1
    return True, ops, pattern
OLD_TAIL_TOOLS = {'corpus.py', 'hebrew.py', 'validate.py', 'render.py', 'verdicts.py'}


def call_hash(call: dict) -> str:
    return hashlib.sha256(json.dumps([call.get('name'), call.get('input')], ensure_ascii=False,
                                     sort_keys=True).encode()).hexdigest()


class Ctx:
    """What one call directory may read and write, from its started.json."""
    def __init__(self, d: Path):
        self.d = d.resolve()
        st = json.loads((d / 'started.json').read_text())
        self.pack = (HERE / 'work' / f"s{st['surah']:03d}" / 'pack').resolve()
        self.inputs = {(PG / p).resolve() for p in st.get('bible_inputs', {})}
        self.dirs_listable = {p.parent for p in self.inputs}

    def readable(self, p: Path) -> bool:
        p = p.resolve()
        if p == self.d or p.is_relative_to(self.d) or p.is_relative_to(self.pack) or p in self.inputs:
            return True
        if p.is_relative_to((HERE / 'corpus').resolve()) or p in self.dirs_listable:
            return True
        if p.parent == HERE and (p.suffix == '.py' or p.name.startswith('SCHEMA')):
            return True
        return p.is_relative_to((HERE / 'prompts').resolve())

    def cd_ok(self, p: Path) -> bool:
        """A directory the call may move into: the repository root, its own call directory, the pack, its inputs'
        directories or the Bible corpus."""
        p = p.resolve()
        return p == PG.resolve() or p in {q.resolve() for q in self.dirs_listable} or self.readable(p)

    def own(self, p: Path) -> bool:
        p = p.resolve()
        return p == self.d or p.is_relative_to(self.d)


def is_scratch(p: str) -> bool:
    return bool(SCRATCH.match(str(p)))


def path_args(tokens):
    """Tokens that name files: absolute, home-relative or repository paths."""
    return [t for t in tokens if t.startswith(('/', '~', 'enrichment/'))]


def resolve(t: str) -> Path:
    p = Path(t).expanduser()
    return p if p.is_absolute() else PG / p


def segments(cmd: str):
    """Shell command → list of argv segments, or None when it uses syntax beyond plain commands and pipes."""
    if '`' in cmd or '$(' in cmd or '<<' in cmd:
        return None
    q = None                                   # quote state: None, "'" or '"'
    for ch in cmd:
        if q == "'":
            if ch == "'":
                q = None
        elif q == '"':
            if ch == '"':
                q = None
            elif ch == '$':
                return None                    # expansion inside double quotes (a backslash there expands nothing)
        elif ch in "'\"":
            q = ch
        elif ch in '\n\r$\\':
            return None                        # an unquoted newline runs a second command; $ and backslash expand
    if q is not None:
        return None
    lx = shlex.shlex(cmd, posix=True, punctuation_chars=';&|<>')
    lx.whitespace_split = True
    try:
        toks = list(lx)
    except ValueError:
        return None
    segs, cur, i = [], [], 0
    while i < len(toks):
        t = toks[i]
        if t in SEPARATORS:
            segs.append(cur); cur = []
        elif t in ('>', '2>', '>>'):
            nxt = toks[i + 1] if i + 1 < len(toks) else ''
            if nxt != '/dev/null':
                return None
            i += 1
        elif t and set(t) <= set(';&|<>'):
            return None
        else:
            cur.append(t)
        i += 1
    segs.append(cur)
    return [s for s in segs if s]


def imports(code: str) -> set[str]:
    mods = set()
    for m in re.finditer(r'(?:^|[;\n])\s*import\s+([\w., ]+)', code):
        mods |= {x.strip().split('.')[0].split(' as ')[0].strip() for x in m[1].split(',')}
    mods |= {m[1].split('.')[0] for m in re.finditer(r'(?:^|[;\n])\s*from\s+([\w.]+)\s+import', code)}
    return {m for m in mods if m}


def literal_paths(code: str):
    """Path-like string literals. `NAME + '/x'` where NAME is assigned a literal path in the same code counts as that
    path joined with '/x' (a call-directory constant plus a file name); every other literal counts as written."""
    assigned = {m[1]: m[2] for m in re.finditer(r"""(?m)^\s*(\w+)\s*=\s*['"]((?:/|~/|enrichment/)[^'"\n]*)['"]\s*$""", code)}
    out, joined = [], set()
    for m in re.finditer(r"""\b(\w+)\s*\+\s*['"](/[^'"\n]*)['"]""", code):
        if m[1] in assigned:
            out.append(assigned[m[1]].rstrip('/') + m[2]); joined.add(m.start(2) - 1)
    out += [m[1] for m in re.finditer(r"""['"]((?:/|~/|enrichment/)[^'"\n]*)['"]""", code) if m.start() not in joined]
    return out


def classify_python(seg, ctx: Ctx, scripts: dict):
    """(kind, reason, auto) for a `python3 ...` segment, or (None, reason, False)."""
    args = seg[1:]
    tool = next((resolve(x) for x in args if x.endswith('.py')), None)
    if tool and tool.parent.resolve() == HERE and tool.name in OLD_TAIL_TOOLS and '--help' in args:
        return 'read', f'help text of the Bible tool {tool.name}', True
    isolated = bool(args) and args[0] == '-I'
    if isolated:
        args = args[1:]
    elif not (args and args[0] == '-c'):
        return None, 'a python script run without -I', False
    if args and args[0] == '-c':
        if len(args) < 2:
            return None, 'python -c without code', False
        code, argv = args[1], args[2:]
        bad = imports(code) - SAFE_MODULES
        if bad or WRITES.search(code):
            return None, f'inline python with unsafe modules or writes: {sorted(bad)}', False
        paths = literal_paths(code) + path_args(argv)
        out = [p for p in paths if not ctx.readable(resolve(p))]
        return ((None, f'inline python names {out}', False) if out else
                ('read', 'inline python reading allowed inputs' + ('' if isolated else ' (without -I)'), True))
    if not args:
        return None, 'python without a script', False
    script, argv = resolve(args[0]), args[1:]
    content = scripts.get(str(script))
    if content is None:
        return None, f'script {script} was not written in this transcript (or an Edit did not apply)', False
    bad = imports(content) - SAFE_MODULES
    if bad or re.search(r'system\(|popen|subprocess|socket|urllib|requests|rmtree|__import__|exec\(|eval\(', content):
        return None, f'helper {script.name} uses unsafe modules or calls: {sorted(bad)}', False
    paths = literal_paths(content) + path_args(argv)
    out = [p for p in paths if not (ctx.readable(resolve(p)) or ctx.own(resolve(p)))]
    if out:
        return None, f'helper {script.name} names paths outside the inputs and call directory: {out}', False
    return 'helper', f'helper {script.name} on allowed inputs and the call directory', ctx.own(script)


def path_like(t: str, cwd: Path) -> bool:
    return '/' in t or t.startswith(('.', '~')) or bool(GLOB.search(t)) or (cwd / t).exists()


def arg_paths(args, cwd: Path, skip_first=False):
    """Every path-like argument (also `--flag=value` values), resolved against cwd, plus the write targets
    (values of --out/--report). Returns (paths, writes, bad) where bad lists glob arguments."""
    paths, writes, bad, first, i = [], [], [], skip_first, 0
    while i < len(args):
        t = args[i]
        if t.startswith('-'):
            flag, eq, val = t.partition('=')
            if flag in WRITE_FLAGS:
                v = val if eq else (args[i + 1] if i + 1 < len(args) else '')
                if not eq:
                    i += 1
                writes.append((cwd / Path(v).expanduser()) if v else Path('/'))
            elif eq and path_like(val, cwd):
                (bad if GLOB.search(val) else paths).append(val if GLOB.search(val) else cwd / Path(val).expanduser())
        elif first:
            first = False                      # a grep pattern or sed script, not a path
        elif path_like(t, cwd):
            (bad if GLOB.search(t) else paths).append(t if GLOB.search(t) else cwd / Path(t).expanduser())
        i += 1
    return paths, writes, bad


def classify_shell(cmd: str, ctx: Ctx, scripts: dict, announced=frozenset()):
    segs = segments(cmd)
    if segs is None:
        return None, 'shell syntax beyond plain commands and pipes', False
    kinds, reasons, auto, cwd = [], [], True, PG
    ok_read = lambda q: ctx.readable(q) or (TOOL_RESULTS.match(str(q.resolve())) and str(q.resolve()) in announced)
    for seg in segs:
        prog = Path(seg[0]).name
        if prog == 'cd':
            tgt = (cwd / Path(seg[1]).expanduser()).resolve() if len(seg) > 1 else None
            own_out_dir = tgt is not None and any(Path(x).parent == tgt for x in announced)
            if tgt is None or not (ctx.cd_ok(tgt) or own_out_dir):
                return None, f'cd outside the allowed directories: {seg[1:2]}', False
            cwd = tgt
            kinds.append('read'); reasons.append('cd into the repository root or an allowed directory')
            continue
        if prog in ('python', 'python3') or re.fullmatch(r'python3\.\d+', prog):
            tool = next((t for t in seg[1:] if t.endswith('.py')), None)
            tpath = (cwd / tool).resolve() if tool else None
            if tpath and tpath.parent == HERE.resolve() and tpath.name in BIBLE_TOOLS and seg[1] == tool:
                rest = seg[2:]
                subs = BIBLE_TOOLS[tpath.name]
                if set(rest) & {'--help', '-h'} and all(t.startswith('-') or t in (subs or ()) for t in rest):
                    kinds.append('read'); reasons.append(f'help text of the Bible tool {tpath.name}')
                    continue
                if subs is not None:
                    pos = [t for t in rest if not t.startswith('-')]
                    if not pos or pos[0] not in subs:
                        return None, f'Bible tool {tpath.name} subcommand {pos[:1]} is not a read', False
                paths, writes, bad = arg_paths(rest, cwd)
                badp = [str(q) for q in paths if not (ok_read(q) or ctx.own(q))] + [str(q) for q in writes if not ctx.own(q)]
                if bad or badp:
                    return None, f'Bible tool {tpath.name} names paths outside the inputs and call directory: {bad + badp}', False
                k, r, a = 'helper', f'Bible tool {tpath.name} on allowed inputs, writing only in the call directory', True
            else:
                if cwd != PG:
                    rel_ok = [t for t in seg[1:] if not t.startswith('-') and t.endswith('.py') and not t.startswith('/')]
                    if rel_ok:
                        return None, 'a relative python script after cd', False
                k, r, a = classify_python(seg, ctx, scripts)
                if k is not None and cwd != PG and '-c' in seg:
                    code = seg[seg.index('-c') + 1] if seg.index('-c') + 1 < len(seg) else ''
                    for m in re.finditer(r"""open\(\s*['"]([^'"]+)['"]""", code):
                        q = cwd / m[1]
                        if not ok_read(q):
                            return None, f'inline python after cd opens {m[1]} outside the allowed inputs', False
        elif prog == 'sed':
            args = seg[1:]
            inplace = args[:1] == ['-i']
            rest = [t for t in (args[1:] if inplace else args) if t not in ('-n', '-E', '-r')]
            if not rest or any(t.startswith('-') for t in rest):
                return None, f'sed flags beyond -i/-n/-E: {args[:4]}', False
            script, files = rest[0], rest[1:]
            if not files or any(GLOB.search(t) for t in files):
                return None, f'sed operands that are not plain files: {files}', False
            fpaths = [(cwd / Path(t).expanduser()) for t in files]
            if inplace:
                k, r, a = (('own_edit', 'sed -i plain substitution on own call-directory files', True)
                           if SED_SUBST.match(script) and all(ctx.own(q) for q in fpaths)
                           else (None, f'sed -i that is not a plain substitution on own files: {args[:4]}', False))
            else:
                k, r, a = (('read', 'print-only sed on allowed inputs', True)
                           if SED_PRINT.match(script) and all(ok_read(q) for q in fpaths)
                           else (None, f'sed that is not print-only on allowed inputs: {args[:4]}', False))
        elif prog == 'mkdir':
            paths, _, bad = arg_paths(seg[1:], cwd)
            ok = paths and not bad and all(ctx.own(q) or is_scratch(str(q)) for q in paths)
            k, r, a = (('own_edit', 'mkdir of the call directory or scratchpad', all(ctx.own(q) for q in paths))
                       if ok else (None, f'mkdir outside the call directory/scratchpad: {paths}', False))
        elif prog in READ_PROGS:
            if prog in ('echo', 'printf', 'true'):
                k, r, a = 'read', f'{prog}', True
            else:
                fine, ops, pattern = flags_ok(prog, seg[1:])
                if not fine:
                    return None, f'{prog} with a flag outside its read-only allowlist: {seg[1:5]}', False
                if prog in ('grep', 'egrep') and not pattern:
                    ops = ops[1:]              # the first operand is the pattern
                if prog == 'uniq' and len(ops) > 1:
                    return None, 'uniq with an output operand', False
                if any(GLOB.search(t) for t in ops):
                    return None, f'{prog} with a glob operand: {ops}', False
                badp = [t for t in ops if not ok_read(cwd / Path(t).expanduser())]
                k, r, a = ((None, f'{prog} names paths outside the allowed inputs: {badp}', False) if badp
                           else ('read', f'read-only {prog} on allowed inputs', True))
        else:
            k, r, a = None, f'command {prog} is not a read, helper or own edit', False
        if k is None:
            return None, r, False
        kinds.append(k); reasons.append(r); auto = auto and a
    order = ['helper', 'own_edit', 'read']
    return next(k for k in order if k in kinds), '; '.join(dict.fromkeys(reasons)), auto


def classify(call: dict, ctx: Ctx, scripts: dict, announced: set):
    """(kind, reason, auto) of one tool call; kind None means unclassifiable."""
    name, inp = call.get('name'), call.get('input') or {}
    if name == 'Bash':
        return classify_shell(str(inp.get('command', '')), ctx, scripts, announced)
    raw = inp.get('file_path') or inp.get('path') or inp.get('notebook_path')
    if name in ('Read', 'Grep', 'Glob'):
        if raw and TOOL_RESULTS.match(str(raw)):
            return (('own_output', 'harness-persisted output of an earlier call, announced in this transcript', True)
                    if str(raw) in announced else (None, f'persisted output {raw} not announced earlier', False))
        if raw and ctx.readable(resolve(str(raw))):
            return 'read', f'{name} of an allowed input', True
        return None, f'{name} outside the allowed inputs: {raw}', False
    if name in ('Write', 'Edit', 'MultiEdit') and raw:
        p = str(resolve(str(raw)))
        if Path(p).name in ('operator-review.json',):
            return None, 'the author may not write the operator review', False
        if is_scratch(p) and p.endswith('.py'):
            return 'helper', 'helper script written to the session scratchpad', False
        return None, f'{name} outside the call directory: {p}', False
    return None, f'tool {name} outside the Bible call rules', False


def walk(d: Path, calls: list[dict]):
    """Classification of every call in order, with helper scripts rebuilt from Write/Edit inputs as they ran."""
    ctx, scripts, announced, rows, used = Ctx(d), {}, set(), [], {}
    for i, c in enumerate(calls):
        k, r, a = classify(c, ctx, scripts, announced)
        rows.append(dict(index=i, call_id=c.get('id'), name=c.get('name'), hash=call_hash(c), kind=k, reason=r, auto=a))
        if c.get('name') == 'Bash' and k == 'helper':
            for seg in segments(str((c.get('input') or {}).get('command', ''))) or []:
                if Path(seg[0]).name.startswith('python') and len(seg) > 2 and seg[2] != '-c':
                    p = str(resolve(seg[2]))
                    if p in scripts:
                        used.setdefault(p, []).append((i, scripts[p]))
        inp = c.get('input') or {}
        if not c.get('is_error'):
            if c.get('name') == 'Write' and inp.get('file_path'):
                scripts[str(resolve(inp['file_path']))] = inp.get('content', '')
            elif c.get('name') == 'Edit' and inp.get('file_path'):
                p = str(resolve(inp['file_path']))
                old, new = inp.get('old_string', ''), inp.get('new_string', '')
                if p in scripts and old in scripts[p]:
                    scripts[p] = scripts[p].replace(old, new) if inp.get('replace_all') else scripts[p].replace(old, new, 1)
                elif p in scripts:
                    scripts.pop(p)  # the Edit cannot be replayed: the script is no longer known
        res = c.get('result')
        if isinstance(res, str):
            announced |= set(re.findall(re.escape(str(Path.home() / '.claude/projects')) + r'/[^\s"\']+\.txt', res))
    return rows, used


def flagged(d: Path, calls: list[dict]) -> list[dict]:
    """Calls outside the original grammar (agentrun's rules before 2026-10-09), classified."""
    from enrichment.bible import agentrun as AR
    rows, _ = walk(d, calls)
    return [r for r, c in zip(rows, calls) if not AR.old_rule_allows(d, c)]


def write(d: Path, calls: list[dict], reviewer: str, transcript: str) -> dict:
    if (d / 'operator-review.json').exists():
        raise ValueError('operator-review.json exists; never overwrite a review')
    if not reviewer.strip():
        raise ValueError('name the reviewer')
    rows, used = walk(d, calls)
    from enrichment.bible import agentrun as AR
    flags = [r for r, c in zip(rows, calls) if not AR.old_rule_allows(d, c)]
    bad = [r for r in flags if r['kind'] is None]
    if bad:
        raise ValueError('unclassifiable calls: ' + '; '.join(f"{r['call_id']} {r['reason']}" for r in bad))
    helpers = d / 'helpers'
    copies = []
    for path, runs in used.items():
        for i, content in runs:
            name = f'call{i:03d}_{Path(path).name}'
            dst = helpers / name
            helpers.mkdir(exist_ok=True)
            if dst.exists() and dst.read_text() != content:
                raise ValueError(f'{dst} exists with other content')
            dst.write_text(content)
            copies.append(dict(call_index=i, source=path, copy=str(dst.relative_to(d)),
                               sha256=hashlib.sha256(content.encode()).hexdigest()))
    review = dict(policy='bible-page-operator-review-v1', reviewer=reviewer, transcript=transcript,
                  transcript_sha256=hashlib.sha256(Path(transcript).read_bytes()).hexdigest(),
                  calls=[{k: r[k] for k in ('index', 'call_id', 'name', 'hash', 'kind', 'reason', 'auto')} for r in flags],
                  helper_copies=copies)
    (d / 'operator-review.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n')
    return review


def covered(d: Path, calls: list[dict]) -> tuple[set[int], list[str]]:
    """Indexes of calls the operator review covers (exact hash and kind), and problems with the review itself."""
    f = d / 'operator-review.json'
    if not f.exists():
        return set(), []
    rev = json.loads(f.read_text())
    problems, ok = [], set()
    for c in rev.get('helper_copies', []):
        p = d / c['copy']
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != c['sha256']:
            problems.append(f"helper copy {c['copy']} missing or changed")
    rows, _ = walk(d, calls)
    for r in rev.get('calls', []):
        i = r.get('index')
        if not isinstance(i, int) or i >= len(rows) or rows[i]['hash'] != r.get('hash') or rows[i]['kind'] != r.get('kind') \
                or r.get('kind') is None:
            problems.append(f"review entry {r.get('call_id')} does not match the transcript call")
            continue
        ok.add(i)
    return ok, problems


def main():
    from enrichment.bible import agentrun as AR, enrich as E
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('phase', choices=('classify', 'write'))
    ap.add_argument('--surah', type=int, required=True)
    ap.add_argument('--target', required=True)
    ap.add_argument('--attempt', type=int, default=1)
    ap.add_argument('--reviewer', default='')
    a = ap.parse_args()
    d = E.call_dir(a.surah, a.target, a.attempt)
    ts = AR.transcripts(d)
    if len(ts) != 1:
        raise SystemExit(f'expected one transcript, found {len(ts)}')
    calls = AR.parse(ts[0])['tool_calls']
    if a.phase == 'classify':
        rows = flagged(d, calls)
        for r in rows:
            print(f"{r['index']:3d} {r['name']:5} {r['kind'] or 'UNCLASSIFIED':10} auto={r['auto']!s:5} {r['reason'][:150]}")
        print(f"{len(rows)} calls outside the original grammar; unclassified: {sum(r['kind'] is None for r in rows)}")
        return
    rev = write(d, calls, a.reviewer, str(ts[0]))
    print(f"operator-review.json: {len(rev['calls'])} calls, {len(rev['helper_copies'])} helper copies")


if __name__ == '__main__':
    main()
