# worker-placement
by Bart Siniarski

Set of tools and scripts to understand the placement of files on short term workers (w200 - w217)

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
Assuming that <b>29-04-2018-data</b> folder exists and is populated with laliste date, you can do:

<pre>python extract-tokens <b>29-04-2018</b></pre>

This will create a folder called laliste-tokens and with files containing tokens only. Each file should be significantly smaller compared to original laliste outputs. For example 1.5Gb is reduced to approximately 50MB
