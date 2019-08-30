import sqlite3

conn = sqlite3.connect('timeTracking.db')

c = conn.cursor()

c.execute(""" create table tasks (
            taskname text primary key
        )""")

c.execute(""" create table taskDetails (
            taskname text,
            start_time text,
            end_time text,
            total_time text,
            total_hours integer,
            total_minutes integer,
            total_seconds integer
        )""")

conn.commit()

conn.close()
