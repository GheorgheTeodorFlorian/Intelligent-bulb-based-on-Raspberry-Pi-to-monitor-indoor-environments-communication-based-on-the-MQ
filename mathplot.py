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
def tempGet():
    sql = "SELECT Temperature FROM sensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        dev_x.append(x[0])
    
    
def timeGet():
    sql = "SELECT Time FROM sensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        dev_time.append(x[0])


def lightGet():
    sql = "SELECT LightLevel FROM sensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        dev_y.append(x[0])

def dateGet():
    sql = "SELECT Date FROM sensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        dev_date.append(x[0])
    
        
    
lightGet()
tempGet()
dateGet()
timeGet()


dev_datetime = [x + " " + y for x, y in zip(dev_date, dev_time)]
dev_datetime = [datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in dev_datetime]


dev_x = [ int(x) for x in dev_x]
dev_y = [ int(x) for x in dev_y]

plt.plot(dev_datetime,dev_x,label = "temp")    
plt.plot(dev_datetime,dev_y,label = 'light')
myFmt = mdates.DateFormatter('%d/%m \n %H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("LightLevel")
plt.title("Light and Temperature")
plt.show()


