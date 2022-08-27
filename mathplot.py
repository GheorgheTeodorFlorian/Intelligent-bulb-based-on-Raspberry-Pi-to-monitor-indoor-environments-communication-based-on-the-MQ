from matplotlib import pyplot as plt
import sqlite3

conn = sqlite3.connect('information.db')
cursor = conn.cursor()
dev_x=[]
dev_y=[]
dev_date=[]

def tempGet():
    sql = "SELECT Temperature FROM sensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        dev_x.append(x[0])
    
    
    

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

plt.plot(dev_date,dev_x,label = "temp")    
plt.plot(dev_date,dev_y,label = 'light')
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("LightLevel")
plt.title("Light and Temperature")
plt.show()


