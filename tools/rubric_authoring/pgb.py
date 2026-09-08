"""PhyGenBench physical_laws audit.  g(...) per group, o(...) per-item override, save()."""
import json, os

ROOT = '/home/jovyan/chy/physical_judge'
SRC  = json.load(open(os.path.join(ROOT, 'prompts', 'PhyGenBench.json')))
OUT  = os.path.join(ROOT, 'audit', 'phygenbench', '_audit.json')
VERDICTS = ('ok', 'rewrite', 'exclude')
FLAGS = ('low-visibility', 'premise-implausible', 'outcome-uncertain', 'duplicate',
         'non-visual', 'caption-law-conflict', 'object-mismatch', 'mechanism-mislabelled')
A = {}


def g(ids, verdict, law, obs, issue=None, flags=None):
    """Record one analysis shared by `ids` (indices into PhyGenBench.json)."""
    assert verdict in VERDICTS, verdict
    for f in (flags or ()):
        assert f in FLAGS, f
    for i in ids:
        assert i not in A, f'{i} already audited'
        s = SRC[i]
        r = {'id': i, 'caption': s['caption'], 'main_category': s['main_category'],
             'sub_category': s['sub_category'], 'law_original': s['physical_laws'],
             'verdict': verdict, 'law_corrected': law, 'observables': list(obs)}
        if issue: r['issue'] = issue
        if flags: r['flags'] = list(flags)
        A[i] = r


def o(i, add=None, **kw):
    """Override or extend one item's record."""
    r = A[i]
    for f in kw.get('flags', ()):
        assert f in FLAGS, f
    if 'verdict' in kw: assert kw['verdict'] in VERDICTS
    r.update(kw)
    if add: r['observables'] = r['observables'] + list(add)


def save():
    recs = [A[i] for i in sorted(A)]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(recs, open(OUT, 'w'), ensure_ascii=False, indent=2)
    import collections
    c = collections.Counter(r['verdict'] for r in recs)
    print(f'{len(recs)}/{len(SRC)} audited  ' + '  '.join(f'{k}={c[k]}' for k in VERDICTS))
    miss = [i for i in range(len(SRC)) if i not in A]
    if miss: print('NOT YET AUDITED:', miss)
