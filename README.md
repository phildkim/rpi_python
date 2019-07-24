### To run the program:
```shell
$ python crontab_service.py 
```
#### In crontab_service.py:
```python
job = cron.new(command='/usr/bin/python /home/pi/RaspberryPi/src/call_daily_report.py')
job.hour.every(22)  # job will execute call_daily_report.py at 22:00 
```
#### In call_daily_report.py:
```python
os.system('cd ~/RaspberryPi/src; /usr/bin/python /home/pi/RaspberryPi/src/daily_report.py')
# This file will execute daily_report.py
```
#### In daily_report.py:
```python
def main():
    write_csv_file()  # creates csv file in the src/daily_report directory
    send_email()      # sends email using gmail smtp service
    remove_mariadb()  # drops the tables from mysql
    create_mariadb()  # creates new tables for mysql
    return
```
#### In temperature_sensor.py:
```python
# Main loop, will stop the loop if you press 'Control + c' and press '1', otherwise any other key to continue.
while is_running:
        try:
            print_device = str(sensor_device.query("R")) + config.temp_ini['degree']
            # This check_temperature function checks temperature every 10 seconds
            temp_msg = check_temperature(print_device)
            config.print_info(device_info, device_status, delay_time, temp_msg, " ON")
            # If temp_msg returns 'NORMAL' then it will insert into MySQL.
            if temp_msg[0:6] == "NORMAL":
                insert_mariadb(print_device)
            # If the temp_msg is NOT normal, then it will send an alert email.
            else:
                insert_mariadb(print_device)
                insert_mariadb('ALERT')
                write_csv_file()
                send_email(temp_msg, 'ALERT REPORT')
                # This while loop will count number of seconds to pause the sensor.
                while is_thread:
                    is_thread = thread.run()
        except KeyboardInterrupt:
```
#### In config.py:
```python
# GLOBAL CONSTANT TEMPERATURE VARIABLES (decimals)
_SECONDS = 60.0                     # Seconds to wait when alert is signaled
_MAX_TEMPERATURE = 90.0             # Maximum temperature for alert
_MIN_TEMPERATURE = 60.0             # Minimum temperature for alert

# GLOBAL CONSTANT SMTP VARIABLES
_RECEIPANT = 'youremail@gmail.com'  # For multiple emails: 'abc1@gmail.com,abc2@gmail.com' (comma no space)
```
