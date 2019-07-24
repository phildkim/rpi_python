### To run the program:
```shell
$ python crontab_service.py
```
#### In crontab_service.py:
```python
job = cron.new(command='/usr/bin/python /home/pi/RaspberryPi/src/call_daily_report.py')
job.hour.every(22)  # job will execute call_daily_report.py at 22:00 
```
