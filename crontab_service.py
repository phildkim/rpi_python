#!/usr/bin/python
import os
from crontab import CronTab

# START CRONTAB FOR DAILY REPORT
cron = CronTab(user='pi')
job = cron.new(command='/usr/bin/python /home/pi/RaspberryPi/src/call_daily_report.py')
job.minute.every(5)
#job.hour.every(22)
cron.write()
for j in cron:
    print('\t' + str(j))

# START PROGRAM
os.system('cd ~/RaspberryPi/src; /usr/bin/python /home/pi/RaspberryPi/src/temperature_sensor.py')
