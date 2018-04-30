#!/bin/bash

#This script will download laliste file from a specific set of workers and save it into "laliste-data" folder
export AWS_PROFILE=awsaml-086403773823
export AWS_DEFAULT_PROFILE=awsaml-086403773823

now="$(date +'%d-%m-%Y')"

echo "Downloading laliste output from $now"

for ((i=$2;i<=$3;i++))
do
echo "Saving laliste output from worker$i to laliste-data/$now-data/worker$i-$1"

if [ ! -d ../laliste-data/$now-data ]; then
  mkdir -p ../laliste-data/$now-data
fi

aws s3api get-object --bucket logentries-listings --key /worker$i-$1 ../laliste-data/$now-data/worker$i-$1

done
exit 0
