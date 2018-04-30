from os import listdir
from os.path import isfile, join
import re
import os
import subprocess
import sys

date = sys.argv[1]

original = [o for o in listdir(('../laliste-tokens/%s-tokens') % date)]
original = sorted(original)

print original


for o in original:
    print "Removing duplicates from " + str(o)
    with open('../laliste-tokens/%s-tokens/%s' % (date,o), "r") as fobj:


        if not os.path.exists(os.path.dirname('../laliste-tokens-grouped/%s-grouped/%s' % (date,o))):
            try:
                os.makedirs(os.path.dirname('../laliste-tokens-grouped/%s-grouped/%s' % (date,o)))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise


        with open('../laliste-tokens-grouped/%s-grouped/%s' % (date,o), "w") as outp:
            lines_seen = set() # holds lines already seen
            for line in fobj:
                if line not in lines_seen: # not a duplicate
                    outp.write(line)
                    lines_seen.add(line)
            outp.close()

if not os.path.exists('../test_population'):
    f = file('../test_population')
else:
    f = file('../test_population')
