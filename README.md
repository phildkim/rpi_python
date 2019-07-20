---------------------------------------------------------------------------------------
[To run the program: ]
$ python crontab_service.py
---------------------------------------------------------------------------------------
[In the crontab_service.py, the crontab job is set to send email at 10pm everyday
and also runs your main program. If you quit your main program it will remove crontab,
so always run this file.]
---------------------------------------------------------------------------------------
[To change configuration/settings: ]
$ python config.py
---------------------------------------------------------------------------------------
[In the config.py, GLOBAL CONSTANT TEMPERATURE VARIABLES is settings for temperature 
max, min and seconds to wait after alert. Make sure to use floating point and not 
whole number. Ex: _MAX_TEMPERATURE = 90.0]
[In the config.py, GLOBAL CONSTANT SMTP VARIABLES is settings for smtp service. 
If you want to add more receipants, just include comma after email (nospaces).
Ex: 'philipkim337@gmail.com,philipdanielkim@gmail.com']
--------------------------------------------------------------------------------------
[Main program: temperature_sensor.py]
[Daily email (22:00): daily_report.py]
[SMTP class: smtp_service.py]
[MySQL class: mariadb_service.py]
[Thread class: thread_service.py]
[Crontab: call_daily_report.py, crontab_service.py]
[Directory: csv file directory. Files will be removed daily.]
---------------------------------------------------------------------------------------
