import sqlite3
import matplotlib.pyplot as plt
import datetime

conn = sqlite3.connect('timeTracking.db')
c = conn.cursor()


plt.figure(figsize=(8,8))

labels = []
values = []

with conn:
    c.execute("select taskname from tasks")
    result = c.fetchall()
    for r in result:
        labels.append(str(r[0]))

    print(labels)
    for i in labels:
        total_seconds = 0
        c.execute("select sum(total_hours) from taskDetails where taskname = ?", (i,))
        result = c.fetchone()
        total_seconds += result[0]*3600
        c.execute("select sum(total_minutes) from taskDetails where taskname = ?", (i,))
        result = c.fetchone()
        total_seconds += result[0]*60
        c.execute("select sum(total_seconds) from taskDetails where taskname = ?", (i,))
        result = c.fetchone()
        total_seconds += result[0]

        values.append(total_seconds)
        
    print(values)

plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.show()
