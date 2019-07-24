### To run the program:
```shell
$ python crontab_service.py
```
#### In crontab_service.py:
```python
job = cron.new(command='/usr/bin/python /home/pi/RaspberryPi/src/call_daily_report.py')
job.hour.every(22)  # job will execute call_daily_report.py 
# call_daily_report.py will execute daily_report.py which sends email at 10:00 pm everyday.
```
