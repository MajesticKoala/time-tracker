import logging
import sys
from AppKit import NSWorkspace
import time
from datetime import datetime
import sqlite3

running = True
last_window_name = ""

conn = sqlite3.connect('timeTracking.db')
c = conn.cursor()

while running:
    active_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])

    if active_window_name != last_window_name:
        # Window has been changed
        end_time = datetime.now()
        if last_window_name:
            total_time = end_time - start_time
            total_hour = end_time.hour - start_time.hour
            total_minute = end_time.minute - start_time.minute
            total_second = end_time.second - start_time.second
            with conn:
                c.execute("select * from tasks where taskname = ?", (last_window_name,))
                if c.fetchone():
                    c.execute("insert into taskDetails values (?, ?, ?, ?, ?, ?, ?)", (last_window_name, str(start_time), str(end_time), str(total_time), total_hour, total_minute, total_second))
                else:
                    c.execute("insert into tasks values (?)", (last_window_name,))
                    c.execute("insert into taskDetails values (?, ?, ?, ?, ?, ?, ?)", (last_window_name, str(start_time), str(end_time), str(total_time), total_hour, total_minute, total_second))

        start_time = end_time
        last_window_name = active_window_name
    else:
        pass

    time.sleep(1)

