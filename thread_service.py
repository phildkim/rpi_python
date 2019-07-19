#!/usr/bin/python
import time
import threading
from time import sleep
from config import temp_ini

# Thread class
class ThreadCount(threading.Thread):
    def __init__(self, interval=1):
        threading.Thread.__init__(self)
        self.interval = interval
        self.value = 0
        self.alive = False
    def run(self):
        self.alive = True
        is_run = True
        print("\n\t\tSENDING ALERT EMAIL AT:\n\t\t%s" % time.strftime('%H:%M:%S', time.localtime()))
        while self.alive:
            time.sleep(self.interval)
            self.value += self.interval
            if (float(self.value) >= temp_ini['second']):
                self.alive = False
                is_run = False
        print("\n\t\tTHREAD TIME COMPLETE AT:\n\t\t%s" % time.strftime('%H:%M:%S', time.localtime()))
        return is_run
