#!/bin/bash

#This script downloads single file produced by laliste from each short term worker



echo "My argument is $1"

for i in {200..217}
do
echo "Downloading from worker $i"
#aws s3api get-object --bucket logentries-listings --key /worker$i-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker200-16

done
exit 0
