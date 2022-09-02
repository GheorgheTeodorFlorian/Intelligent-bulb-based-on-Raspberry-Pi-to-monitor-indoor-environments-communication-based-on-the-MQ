from matplotlib import pyplot as plt
import sqlite3
from datetime import datetime
import matplotlib.dates as mdates


conn = sqlite3.connect('information.db')
cursor = conn.cursor()
dev_x=[]
dev_y=[]
dev_date=[]
dev_time=[]

example =' WHERE Date = "2022-08-28"'


def tempGet():
    sql = "SELECT Temperature FROM sensorData" + example
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        print(x)
        dev_x.append(x[0])
    
tempGet()
print(dev_x)