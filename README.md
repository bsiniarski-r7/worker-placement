# worker-placement
by Bart Siniarski

Set of tools and scripts to understand the placement of files on short term workers (w200 - w217). In order to find placement you need to do the following:

1. run download-worker-data.sh to download laliste outputs
2. run extract-tokens.py to extract tokens from downloaded files
3. run remove-duplicates to further clean data
4. populate file named <i>test-population</i> with token you want to search for. You can get those tokens from laliste-tokens folder created after step 2.
5. run find-placement.py to find placement of logs from <i>test-population</i> file on all of the workers


# Tools:
## download-worker-data.sh

This tool is used to download TODAY's laliste output in a raw format - as it is stored on the short term workers. The copy is saved locally into a folder named "laliste-data". Laliste produces a new file every hour, hence we are letting you specify the time of the day and the number of workers to download.

<b>Run with sudo:</b>
<pre>
download-laliste.sh <b>time</b> <b>worker_start</b> <b>worker_end</b>
</pre>

If you are getting AWS errors, you need to change AWS_PROFILE and AWS_DEFAULT_PROFILE inside of the bash script to match your profile:

export AWS_PROFILE=awsaml-0123456789
export AWS_DEFAULT_PROFILE=awsaml-0123456789

<b>Notice: Each laliste output file is approximately 1.5GB, so be aware of your memory.</b>

<b>Example 1: Get laliste output from 2pm today from all workers [200,201,202...215,216,217]</b>

<pre>
download-worker-data.sh 14 200 217
</pre>

<b>Example 2: Get laliste output from 10am today from workers [202,203,204,205]</b>

<pre>
download-worker-data.sh 10 202 205
</pre>

Valid date arguments:   AM and PM hours using 24-hours format i.e. 15 for 3pm

## extract-tokens.py
Extract only those tokens that contain the .log extension from a specific laliste-data directory

<b>To run:</b>
Assuming that <b>29-04-2018-data</b> folder exists and is populated with laliste outputs, you can do:

<pre>python extract-tokens.py <b>29-04-2018</b></pre>

This will create a folder called laliste-tokens with files containing tokens only. Each file should be significantly smaller compared to original laliste outputs. For example 1.5Gb is reduced to approximately 50MB

## remove-duplicates.py
Tokens may be duplicated. For example a log set may be split into 3 files on a single worker just like this:

log/65/65/7443-932f-4444-b986-f80976ff81b9/180428-000000-000.indexer118.log

log/65/65/7443-932f-4444-b986-f80976ff81b9/180428-000000-000.indexer100.log

log/65/65/7443-932f-4444-b986-f80976ff81b9/180428-000000-000.indexer104.log

We are only interested to find out where the following is placed, and not in how many files it is split to:

log/65/65/7443-932f-4444-b986-f80976ff81b9/180428

<b>To run:</b>
<pre>python remove-duplicates.py <b>29-04-2018</b></pre>

## find-placement.py
Finally, you can use this script to find placement of logs.

1. Firstly, you need to populate a file called 'test-population' with logs that you wish to search for. This file is created by remove-duplicates.py script at the end of execution, so you don't have to do it manually.

2. Then run:
<pre>python find-placement.py <b>29-04-2018</b></pre>

3. Results will be saved in results folder in a file named "placement"


## Sample output

![alt text](link "Sample output for 20,000 samples)

![alt text](link "Sample output for 100,000 samples)
