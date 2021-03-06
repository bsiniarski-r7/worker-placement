from os import listdir
from os.path import isfile, join
import re
import os
import subprocess
import sys

'''Extract only those tokens that contain the .log extension from a specific laliste-data directory'''

date = sys.argv[1]

#Find all files in directory. This directory should contain files generated by laliste.
files = [f for f in listdir(('../laliste-data/%s-data') % date)]

#Sort list of files
files = sorted(files)

print files

if not files:
    print "WARN: laliste-data folder is empty or does not exist"
else:
    for f in files:
        print "Analyzing " + str(f)
        #Open each file and create a shorter version of each file containing log tokens only
        with open('../laliste-data/%s-data/%s' % (date, f), "r") as fobj:
            text = fobj.read()
            output = re.findall(r'.{10}(.{39}).*\.log', text)
            out_str = "\n".join(output)

        if not os.path.exists(os.path.dirname('../laliste-tokens/%s-tokens/%s' % (date,f))):
            try:
                os.makedirs(os.path.dirname('../laliste-tokens/%s-tokens/%s' % (date,f)))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open('../laliste-tokens/%s-tokens/%s' % (date,f), "w") as outp:
            outp.write(out_str)
