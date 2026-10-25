#!/usr/bin/env python3
"""Validate content/: schema, answer indexes, drills, diagrams, and weak-spot/fix coverage.

Usage: python3 scripts/check.py            (checks every built section)
       python3 scripts/check.py vpc hybrid (checks these sections, built or not)
Exits 1 on any error so CI and the Claude hook can block bad content.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, "content")
errors = []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def load(name):
    with open(os.path.join(C, name)) as f:
        return json.load(f)


manifest = load("manifest.json")
weak = {w["id"]: w for w in load("weakspots.json")}
fixes = {f["id"]: f for f in load("corrections.json")}
known_sections = {s["id"] for s in manifest["sections"]}
for w in weak.values():
    if w["section"] not in known_sections: err("weakspots.json", f"{w['id']} has unknown section {w['section']}")
for f in fixes.values():
    if f["section"] not in known_sections: err("corrections.json", f"{f['id']} has unknown section {f['section']}")

wanted = sys.argv[1:]
targets = [s for s in manifest["sections"] if (s["id"] in wanted if wanted else s.get("built"))]
targets += [s for s in manifest.get("extras", []) if not wanted or s["id"] in wanted]
seen_ids = set()

for s in targets:
    sid, path = s["id"], s.get("file", f"content/{s['id']}.json")
    if not os.path.exists(os.path.join(ROOT, path)):
        err(sid, f"missing {path}"); continue
    sec = json.load(open(os.path.join(ROOT, path)))
    if sec.get("id") != sid: err(sid, f"file id is {sec.get('id')}")

    for b in sec.get("notes", []):
        t = b.get("type")
        if t not in ("h2", "p", "diagram", "table", "traps", "exam"): err(sid, f"unknown block type {t}")
        if t == "diagram" and not os.path.exists(os.path.join(ROOT, b["src"])): err(sid, f"missing diagram {b['src']}")
        if t == "table":
            n = len(b["head"])
            for r in b["rows"]:
                if len(r) != n: err(sid, f"table row has {len(r)} cells, head has {n}: {r[0][:40]}")
        if t == "h2" and b.get("weak") and b["weak"] not in weak: err(sid, f"h2 tags unknown weak spot {b['weak']}")

    qs = sec.get("questions", [])
    if len(qs) < 10: err(sid, f"only {len(qs)} questions (want 10-20+)")
    for q in qs:
        qid = q.get("id", "?")
        if qid in seen_ids: err(sid, f"duplicate question id {qid}")
        seen_ids.add(qid)
        opts, ans = q.get("options", []), q.get("answer", [])
        if len(opts) < 2: err(qid, "fewer than 2 options")
        if not ans or any(not isinstance(a, int) or a < 0 or a >= len(opts) for a in ans): err(qid, f"bad answer {ans}")
        if len(set(ans)) != len(ans): err(qid, "repeated answer index")
        if q.get("multi") and len(ans) < 2: err(qid, "multi but one answer")
        if not q.get("multi") and len(ans) != 1: err(qid, "several answers but not multi")
        for o in opts:
            if not o.get("t") or not o.get("why"): err(qid, "option missing text or why")
        if q.get("weak") and q["weak"] not in weak: err(qid, f"unknown weak {q['weak']}")
        if q.get("fix") and q["fix"] not in fixes: err(qid, f"unknown fix {q['fix']}")

    for w in weak.values():
        if w["section"] == sid and not any(q.get("weak") == w["id"] for q in qs): err(sid, f"weak spot {w['id']} has no question")
    for f in fixes.values():
        if f["section"] == sid and not any(q.get("fix") == f["id"] for q in qs): err(sid, f"fix {f['id']} has no question")

    for d in sec.get("drills", []):
        did, t = d.get("id", "?"), d.get("type")
        if t == "thisorthat":
            for it in d["items"]:
                if it.get("ans") not in ("a", "b"): err(did, f"bad ans in {it.get('t')}")
        elif t == "match":
            if len(d["pairs"]) < 3 or any(len(p) != 2 for p in d["pairs"]): err(did, "pairs must be [term, meaning], 3+")
        elif t == "buckets":
            for it in d["items"]:
                if not (0 <= it.get("b", -1) < len(d["buckets"])): err(did, f"bad bucket for {it.get('t')}")
        elif t == "keyword":
            for it in d["items"]:
                if not (0 <= it.get("key", -1) < len(it["parts"])): err(did, "key out of range")
        else:
            err(did, f"unknown drill type {t}")

for e in errors: print("ERROR", e)
print(f"checked {len(targets)} section(s): {len(errors)} error(s)")
sys.exit(1 if errors else 0)
