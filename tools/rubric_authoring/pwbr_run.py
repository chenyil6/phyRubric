"""Run one or more phyworldbench rubric chunks in a single process, then write.

    python3 pwbr_run.py kinematics interaction ...

All chunks must run in one process because pwbadd.B is in-memory.
"""
import os, sys, pwbadd
HERE = os.path.dirname(os.path.abspath(__file__))
G = {k: getattr(pwbadd, k) for k in ('S', 'P', 'add', 'SRC', 'CAPS', 'KS')}
for name in sys.argv[1:]:
    exec(open(os.path.join(HERE, f'pwbr_{name}.py')).read(), dict(G))
pwbadd.flush()
