#!/bin/bash

#This script downloads single file produced by laliste from each short term worker

echo download initiated

aws s3api get-object --bucket logentries-listings --key /worker200-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker200-16
echo 200 finished
aws s3api get-object --bucket logentries-listings --key /worker201-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker201-16
echo 201 finished
aws s3api get-object --bucket logentries-listings --key /worker202-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker202-16
echo 202 finished
aws s3api get-object --bucket logentries-listings --key /worker203-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker203-16
echo 203 finished
aws s3api get-object --bucket logentries-listings --key /worker204-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker204-16
echo 204 finished
aws s3api get-object --bucket logentries-listings --key /worker205-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker205-16
echo 205 finished
aws s3api get-object --bucket logentries-listings --key /worker206-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker206-16
echo 206 finished
aws s3api get-object --bucket logentries-listings --key /worker207-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker207-16
echo 207 finished
aws s3api get-object --bucket logentries-listings --key /worker208-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker208-16
echo 208 finished
aws s3api get-object --bucket logentries-listings --key /worker209-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker209-16
echo 209 finished
aws s3api get-object --bucket logentries-listings --key /worker210-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker210-16
echo 210 finished
aws s3api get-object --bucket logentries-listings --key /worker211-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker211-16
echo 211 finished
aws s3api get-object --bucket logentries-listings --key /worker212-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker212-16
echo 212 finished
aws s3api get-object --bucket logentries-listings --key /worker213-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker213-16
echo 213 finished
aws s3api get-object --bucket logentries-listings --key /worker214-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker214-16
echo 214 finished
aws s3api get-object --bucket logentries-listings --key /worker215-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker215-16
echo 215 finished
aws s3api get-object --bucket logentries-listings --key /worker216-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker216-16
echo 216 finished
aws s3api get-object --bucket logentries-listings --key /worker217-16 ~/Desktop/worker_placement_real_data/data-10-02-2018/worker217-16
echo all finished
