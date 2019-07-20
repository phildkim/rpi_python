#!/usr/bin/python
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# GLOBAL CONSTANT TEMPERATURE VARIABLES
_SECONDS = 60.0
_MAX_TEMPERATURE = 90.0
_MIN_TEMPERATURE = 60.0
_DEGREE = u'\xb0F'.encode('utf8')

# GLOBAL CONSTANT SMTP VARIABLES
_RECEIPANT = 'philipkim337@gmail.com'

password = {
    'pw': '2539Excellent',         
}

temp_ini = { 
    'degree': _DEGREE,
    'max': _MAX_TEMPERATURE,
    'min': _MIN_TEMPERATURE,
    'second': _SECONDS,
}

mariadb_ini = {
    'host': 'localhost',
    'user': 'hydropi_usr',
    'password': '2539Excellent',
    'database': 'temperature_db',
    'charset': 'utf8',
    'use_unicode': 'True',
}

smtp_ini = {
    'sender': 'hydrosensor2019@gmail.com',
    'receipant': _RECEIPANT,
    'server': 'smtp.gmail.com',
    'port': '587',
    'tls': 'yes',
    'login': 'hydrosensor2019@gmail.com',
    'subject': 'DS18B20 Sensor(RTD) from RaspberryPi',
}

# Print information
def print_info(info, status, delay_time, temp_msg, running):
    degree_msg = temp_msg[0:temp_msg.find('$')]
    date_msg = temp_msg[temp_msg.find('\n') + 1:len(temp_msg)]
    status_msg = status[7:len(status)]
    max_temp_msg = str(_MAX_TEMPERATURE) + _DEGREE
    min_temp_msg = str(_MIN_TEMPERATURE) + _DEGREE
    count_msg = date_msg[24:len(date_msg) - 4]
    os.system('clear')
    print ("\n\n\t|-----------------------------------------------|\n"
        "\t|            HYDRO RASPBERRYPI %s              |\n"
        "\t|-----------------------------------------------|\n"
        "\t|   DEVICE: DS18B20 Temperature Sensor(%s)     |\n"
        "\t|                                               |\n"
        "\t|   STATUS: %s\tUPDATES: %0.2f sec       |\n"
        "\t|                                               |\n"
        "\t|   MAX TEMP: %s\tMIN TEMP: %s        |\n"
        "\t|                                               |\n"
        "\t|   %s       |\n"
        "\t|                                               |\n"
        "\t|   %s               |\n"
        "\t|                                               |\n"
        "\t|                                               |\n"
        "\t| \t    PRESS 'Ctrl + C' TO QUIT.           |\n"
        "\t|-----------------------------------------------|\n"
        "\t   \t     TIME: %s                   \n"
        % (running, info, status_msg, delay_time, max_temp_msg,
            min_temp_msg, date_msg, degree_msg, count_msg))
