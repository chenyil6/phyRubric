"""Shared helpers for the phyworldbench rubric batches.  add(...) then flush().

Captions are pulled from prompts/phyworldbench.json by id, so they are never retyped.
SRC[i] also carries the benchmark's own physics_prompt / key_standards, which are the
authoring cross-check (write our own items first, then diff) -- never copied verbatim.

KS[i] is key_standards normalised to a flat list of strings. 11 of the 315 records wrap
their standards in a dict -- {'standards': [...]} on 22, 45, 76, 85, 93, 121, 212, 223,
262, 294 and {'remaining_standards': [...]} on 226 -- while the other 304 ship a bare
list. Reading those 11 naively yields the dict's key, i.e. the bare string 'standards',
which looks like an unfilled placeholder. Always cross-check against KS[i], never
against SRC[i]['key_standards'].
"""
import ast
import json, os, sys
sys.path.insert(0, '/home/jovyan/chy/physical_judge/rubrics')
from emit import emit

DS = 'phyworldbench'
ROOT = '/home/jovyan/chy/physical_judge'
SRC = {e['id']: e for e in
       json.load(open(os.path.join(ROOT, 'prompts', 'phyworldbench.json')))}
CAPS = {i: e['caption'] for i, e in SRC.items()}


def _standards(ks):
    """key_standards -> flat list of strings, unwrapping the dict form and str repr."""
    if isinstance(ks, str):
        try:
            ks = ast.literal_eval(ks)
        except (ValueError, SyntaxError):
            return [ks]
    if isinstance(ks, dict):                       # {'standards': [...]} on 11 records
        ks = [s for v in ks.values() for s in (v if isinstance(v, list) else [v])]
    return [s for s in ks if isinstance(s, str) and s.strip()]


KS = {i: _standards(e['key_standards']) for i, e in SRC.items()}
B = []


def S(*t):
    return [{'id': f'S{i+1}', 'weight': w, 'check': c} for i, (w, c) in enumerate(t)]


def P(*t):
    out = []
    for i, x in enumerate(t):
        d = {'id': f'P{i+1}', 'severity': x[0], 'expect': x[1], 'fail': x[2]}
        if len(x) > 3:
            d['precondition'] = x[3]
        out.append(d)
    return out


def add(mechanism, i, shape, sa, pc, note=None):
    d = {'id': i, 'caption': CAPS[i], 'shape': shape, 'sa': sa, 'pc': pc}
    if note:
        d['note'] = note
    B.append((mechanism, d))


def flush():
    seen = [r['id'] for _, r in B]
    assert len(seen) == len(set(seen)), 'duplicate id in batch'
    for m in sorted({m for m, _ in B}):
        emit([r for g, r in B if g == m], m, dataset=DS)
