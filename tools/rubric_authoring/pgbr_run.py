import os, sys
import pgbadd
HERE = os.path.dirname(os.path.abspath(__file__))
G = {'add': pgbadd.add, 'S': pgbadd.S, 'P': pgbadd.P}
for m in sys.argv[1:]:
    exec(open(os.path.join(HERE, f'pgbr_{m}.py')).read(), dict(G))
pgbadd.flush()
