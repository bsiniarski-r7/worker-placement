from os import listdir
from os.path import isfile, join
import re
import os
import subprocess
import sys

date = sys.argv[1]


#Find all files in directory. This directory should contain files generated by laliste.
tokens = [t for t in listdir(('../laliste-tokens-grouped/%s-grouped') % date)]


if not os.path.exists(os.path.dirname('../results/placement')):
    try:
        os.makedirs(os.path.dirname('../results/placement'))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise


with open('../results/placement', "a") as outp:

    #total_selected is a number of log files in test population
    total_selected = 0
    #total_count is a sum of all placements which will be used to get an average later
    total_count = 0
    #We find if a token exists only in our test worker or if it exists in other workers too
    for line in open('../test_population'):
        print "Matching " + str(total_selected)
        total_selected = total_selected + 1
        count = 0
        token_placement = []

        for t in tokens:
            if line in open('../laliste-tokens-grouped/%s-grouped/%s' % (date, t)).read():
                #We just found a token in another file
                count = count + 1
                token_placement.append(t)

        total_count = total_count + count

        #The structure is as follows : [token, count, workers...]
        #token_placement.insert(0, line.strip('\n'))
        #token_placement.insert(1, count)

        #The structure is now updated to : [token, date, count, workers 1...n]
        token_placement.insert(0, line.strip('\n'))
        token_placement.insert(1, count)

        formatted_date = str(date).replace("'", "").split("-")
        formatted_date = formatted_date[0]

        token_placement.insert(2, int(formatted_date))

        outp.write(str(token_placement)[1 : -1] + "\n")


    outp.write("Total number of files searched = " + str(total_selected)+ "\n")
    outp.write("Average placement count per files = " + str(float(total_count)/float(total_selected))+ "\n")
