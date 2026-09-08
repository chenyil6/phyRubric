"""Shared helpers for the phygenbench rubric batches.  add(...) then flush().

Captions are pulled from prompts/PhyGenBench.json by index, so they are never retyped.
"""
import json, os, sys
sys.path.insert(0, '/home/jovyan/chy/physical_judge/rubrics')
from emit import emit

DS = 'phygenbench'
ROOT = '/home/jovyan/chy/physical_judge'
CAPS = [e['caption'] for e in json.load(open(os.path.join(ROOT, 'prompts', 'PhyGenBench.json')))]
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
