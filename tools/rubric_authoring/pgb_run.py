import os, sys
import pgb
HERE = os.path.dirname(os.path.abspath(__file__))
for m in sys.argv[1:]:
    exec(open(os.path.join(HERE, f'pgb_{m}.py')).read(), {'g': pgb.g, 'o': pgb.o})
pgb.save()
