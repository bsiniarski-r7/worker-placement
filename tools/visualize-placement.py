from os import listdir
from os.path import isfile, join
import re
import os
import subprocess
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time


date = sys.argv[1]



while True:

    '''VISUALIZE THE NUMBER OF WORKERS ON WHICH A FILE IS PLACE ON A GIVEN DATE'''
    x_axis = []
    y_axis = []

    if not os.path.exists(os.path.dirname('../results/placement-%s' % date)):
        print ("Missing placements file")
    else:

        with open('../results/placement-%s' % date, "r") as outp:
            line = outp.readline()
            count = 0
            while line:
                line = outp.readline().strip("\n")

                #Convert comma separated string to array
                results = line.split(",")

                if len(results) != 1:
                    #   zip(ii,y[ii]) print results[0]
                    #print results[1]

                    results[0] = str(results[0])
                    results[1] = int(results[1])
                    x_axis.append(results[0])
                    y_axis.append(results[1])

                    count = count + 1


            a = np.array(y_axis)



            unique_elements, counts_elements = np.unique(a, return_counts=True)
            print(np.asarray((unique_elements, counts_elements)))

            plt.bar(unique_elements, counts_elements)
            plt.title('Number of samples: %s | Data from %s' % (count+1,date))
            plt.xticks(unique_elements)


            plt.show()



            outp.close()






#'7443-932f-4444-b986-f80976ff81b9/180425', 13, 29, 'worker208-10', 'worker213-10', 'worker217-10', 'worker216-10', 'worker206-10', 'worker202-10', 'worker215-10', 'worker205-10', 'worker211-10', 'worker201-10', 'worker210-10', 'worker200-10', 'worker214-10'
