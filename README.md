# worker-placement
by Bart Siniarski

Set of tools and scripts to understand the placement of files on short term workers (w200 - 217)

# Tools:
## download-worker-data.sh

This tool is used to download TODAY's laliste output in a raw format - as it is stored on the short term workers. The copy is saved locally into a folder named "laliste-data". Laliste produces a new file every hour, hence we are letting you specify the time of the day and the number of workers to download.

**Run with sudo:**
<pre>
download-laliste.sh <b>time</b> worker_start worker_end
</pre>

If you are getting AWS errors, you need to change AWS_PROFILE and AWS_DEFAULT_PROFILE inside of the bash script to match your profile:

export AWS_PROFILE=awsaml-0123456789
export AWS_DEFAULT_PROFILE=awsaml-0123456789

**Example 1: Get laliste output from 2pm today from all workers [200,201,202...215,216,217] **
```
download-worker-data.sh 14 200 217
```

**Example 2: Get laliste output from 10am today from workers [202,203,204,205] **
```
download-worker-data.sh 10 202 205
```

Valid date arguments:   AM and PM hours using 24-hours format i.e. 15 for 3pm
