"""Ayah commentary (r13 reading) runs for the orchestrator.
  rstep.py next K        -> build --spawn the next K ayat in queue order (skips done/started); prints SPAWN lines
  rstep.py finish N:A    -> finish, postcheck, commit+push; prints STOP on any warning/failure
  rstep.py queue         -> what is left
"""
import glob, json, os, re, subprocess, sys

R = "/Volumes/aro/projects/prose_generation"
V = f"{R}/_commentary/v16"
SP = os.path.dirname(os.path.abspath(__file__))
ORDER = list(range(88, 100)) + [101, 102, 104, 105, 106, 108, 109, 110, 111, 112, 113, 114, 59]
AYAT = {59: 24, 88: 26, 89: 30, 90: 20, 91: 15, 92: 21, 93: 11, 94: 8, 95: 8, 96: 19, 97: 5, 98: 8, 99: 8, 101: 11, 102: 8,
        104: 9, 105: 5, 106: 4, 108: 3, 109: 6, 110: 3, 111: 5, 112: 4, 113: 5, 114: 6}


def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=R, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr)


def dirs(s):
    m = [d for d in glob.glob(f"{V}/out/s{s:03d}/surah.map3.*tool") if d.endswith(("map3.nohft.tool", "map3.nochannels.hftbundle.tool"))]
    if len(m) != 1:
        return None, None
    im = f"{V}/out/s{s:03d}/images.r13.{os.path.basename(m[0])[6:]}.tool"
    if not os.path.exists(f"{im}/images.md") or not os.path.exists(f"{im}/ledger.md"):
        return m[0], None
    return m[0], im


def rdir(s, a, im):
    return f"{V}/out/{s}_{a}/DM.r13.{os.path.basename(im)}.tool"


def queue():
    q = []
    for s in ORDER:
        m, im = dirs(s)
        for a in range(1, AYAT[s] + 1):
            if im is None:
                q.append((s, a, None))
                continue
            d = rdir(s, a, im)
            if not os.path.exists(f"{d}/started.json") and not os.path.exists(f"{d}/run.log.json"):
                q.append((s, a, d))
    return q


TEMPLATE = None


def template_ok(d):
    t = open(f"{V}/out/s096/surah.map3.nohft.tool/spawn.md", encoding="utf-8").read().replace(
        f"{V}/out/s096/surah.map3.nohft.tool", "DIR")
    x = open(f"{d}/spawn.md", encoding="utf-8").read().replace(d, "DIR")
    return x == t


def nxt(k):
    n = 0
    for s, a, d in queue():
        if n >= k:
            break
        if d is None:
            print(f"WAIT: S{s} surah commentary not finished; {s}:{a} not buildable yet")
            break
        m, im = dirs(s)
        rel_m = os.path.relpath(f"{m}/map.md", V)
        rel_i = os.path.relpath(f"{im}/images.md", V)
        rc, out = sh(f"python3 -B _commentary/v16/packets.py writer --ayah {s}:{a} --brief r13 --tool --map {rel_m} "
                     f"--images {rel_i} --spawn")
        out = "\n".join(l for l in out.splitlines() if not l.startswith("NOTE: no HFT records"))
        print(out)
        if rc != 0 or "BLOCKED" in out or not os.path.exists(f"{d}/spawn.md"):
            print(f"STOP: build failed for {s}:{a}")
            break
        print(("SPAWN " if template_ok(d) else "SPAWN-TEXT-DIFFERS ") + f"{s}:{a} {d}/spawn.md")
        n += 1


def finish(ref):
    s, a = (int(x) for x in ref.split(":"))
    m, im = dirs(s)
    d = rdir(s, a, im)
    rel = os.path.relpath(d, V)
    rc, out = sh(f"python3 -B _commentary/v16/packets.py finish --run {rel}")
    out = "\n".join(l for l in out.splitlines() if not l.startswith("NOTE: no HFT records"))
    print(out)
    bad = rc != 0 or re.search(r"WARNING: (tool use outside|unexpected commands|no subagent)|BLOCKED|Traceback|partial|status error", out)
    _, pc = sh(f"python3 {SP}/postcheck.py {rel}")
    pc = "\n".join(l for l in pc.splitlines() if "missing.py " not in l and not l.startswith("  ledger:"))
    print(pc)
    rows = [json.loads(l) for l in open(f"{V}/out/ledger.jsonl")]
    row = [r for r in rows if r.get("ref") == ref and r.get("arm") == "DM"][-1]
    summ = f"{row.get('status')}, check {row.get('check')} {row.get('check_findings') or ''}".strip()
    sh(f"git add {os.path.relpath(d, R)} _commentary/v16/out/ledger.jsonl")
    rc2, o2 = sh(f"git commit -q -m '{ref} ayah commentary (r13): {summ}' && git push -q")
    print(f"committed {ref}: {summ}" + ("" if rc2 == 0 else f" (git: {o2.strip()[:200]})"))
    if bad:
        print(f"STOP: {ref} needs attention")


def cycle(ref):
    """finish ref + build next, printing only one line (or STOP lines)."""
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        if ref != "-":
            finish(ref)
        nxt(1)
    out = buf.getvalue()
    keep = [l for l in out.splitlines() if l.startswith(("STOP", "WAIT", "SPAWN-TEXT-DIFFERS", "BLOCKED"))]
    sp = [l.split()[1] + " " + os.path.dirname(l.split()[2]) for l in out.splitlines() if l.startswith("SPAWN ")]
    print("\n".join(keep + (["NEXT " + sp[0]] if sp else [])) or "no next")


# ---- ayah augment (augment9): acycle N:A finishes, commits, builds the next; one line out
AORDER = sorted(set(ORDER + [100, 103, 107]) - {59}) + [59]
SOFT = "_commentary/v16/work/orchestrator/augment_soft.txt"


def rdirs(s):
    """finished-reading run dirs of S<s>, by ayah"""
    out = {}
    for d in glob.glob(f"{V}/out/{s}_*/DM.r13.images.r13.map3.*.tool.tool.tool"):
        a = int(d.split("/")[-2].split("_")[1])
        if os.path.exists(f"{d}/{s}_{a}.reading.tr.md"):
            out[a] = d
    return dict(sorted(out.items()))


def aqueue():
    q = []
    for s in AORDER:
        for a, d in rdirs(s).items():
            ad = f"{d}/augment.augment9.opus"
            if not os.path.exists(ad):
                q.append((s, a, d))
    return q


def anext():
    for s, a, d in aqueue():
        rc, out = sh(f"python3 -B _commentary/v16/augment.py {os.path.relpath(d, V)} --spawn")
        ad = f"{d}/augment.augment9.opus"
        if rc != 0 or "BLOCKED" in out or "WARNING" in out or not os.path.exists(f"{ad}/spawn.md"):
            print(out)
            print(f"STOP: augment build failed for {s}:{a}")
            return
        print(("NEXT " if template_ok(ad) else "SPAWN-TEXT-DIFFERS ") + f"{s}:{a} {ad}")
        return
    print("no next")


HARD = re.compile(r"Traceback|WARNING: status|WARNING: ran outside|WARNING: the command audit|refused|"
                  r"no subagent|tool use outside|unexpected commands|already finished|not an agent-spawned")


def afinish(ref):
    s, a = (int(x) for x in ref.split(":"))
    d = rdirs(s)[a]
    ad = f"{d}/augment.augment9.opus"
    rc, out = sh(f"python3 -B _commentary/v16/augment.py {os.path.relpath(d, V)} --finish")
    rows = [json.loads(l) for l in open(f"{V}/out/ledger.jsonl")]
    r1 = ([r for r in rows if r.get("ref") == ref and r.get("arm") == "augment"] or [{}])[-1]
    r2 = ([r for r in rows if r.get("ref") == ref and r.get("arm") == "augment-applied"] or [{}])[-1]
    summ = f"{r1.get('status')}, {r2.get('applied')}/{r2.get('insertions')} applied, check {r2.get('check')}"
    warns = [l for l in out.splitlines() if l.startswith("WARNING")]
    if warns:
        with open(f"{R}/{SOFT}", "a", encoding="utf-8") as f:
            f.write(f"== {ref}\n" + "\n".join(warns) + "\n")
    sh(f"git add {os.path.relpath(ad, R)} _commentary/v16/out/ledger.jsonl")
    rc2, o2 = sh(f"git commit -q -m '{ref} augment9: {summ}' && git push -q")
    if rc2 != 0:
        print(f"STOP: git for {ref}: {o2.strip()[:200]}")
    benign = 'WARNING: tool use outside the run\'s rule (treat the run as contaminated): ToolSearch {"query": "select:SendMessage"'
    hard = "\n".join(l for l in out.splitlines() if not l.startswith(benign))
    if rc != 0 or r1.get("status") != "ok" or HARD.search(hard):
        print(out[-3000:])
        print(f"STOP: {ref} augment needs attention ({summ})")


def acycle(ref):
    if ref != "-":
        afinish(ref)
    anext()


if __name__ == "__main__":
    if sys.argv[1] == "acycle":
        acycle(sys.argv[2])
    elif sys.argv[1] == "aqueue":
        q = aqueue(); print(len(q), "left;", ", ".join(f"{s}:{a}" for s, a, _ in q[:12]))
    elif sys.argv[1] == "cycle":
        cycle(sys.argv[2])
    elif sys.argv[1] == "next":
        nxt(int(sys.argv[2]))
    elif sys.argv[1] == "finish":
        finish(sys.argv[2])
    else:
        q = queue()
        print(len(q), "left;", ", ".join(f"{s}:{a}" for s, a, _ in q[:12]), "...")
