# worker-placement

# Tools

## download-worker-data.sh
This tool is used to download TODAY's laliste output in a raw format, as it is stored on the short term workers. The copy is saved locally. You can specify the time of the day and the number of workers to download.

**Run with sudo:**
```
download-worker-data.sh time worker_start worker_end
```
**Example 1: Get laliste output from today at 2pm from all workers [200,201,202...215,216,217] **
```
download-worker-data.sh 14 200 217
```

**Example 2: Get laliste output from today at 10am from workers [202,203,204,205] **
```
download-worker-data.sh 10 202 205
```

Valid date arguments:   AM and PM hours using 24-hours format i.e. 15 for 3pm
