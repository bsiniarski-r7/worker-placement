#!/bin/bash

now="$(date +'%d-%m-%Y')"

echo "Stage 1/3: Downloading laliste output files"
sudo ./download-laliste.sh $1 $2 $3

echo "Stage 2/3: Extracting tokens"
sudo python ./extract-tokens.py $now

echo "Stage 3/3: Removing duplicates"
sudo python ./extract-tokens.py $now
