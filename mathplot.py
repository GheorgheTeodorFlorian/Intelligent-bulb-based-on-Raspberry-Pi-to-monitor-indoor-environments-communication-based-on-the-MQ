from matplotlib import pyplot as plt
import sqlite3
from datetime import datetime
import matplotlib.dates as mdates


conn = sqlite3.connect('information.db')
cursor = conn.cursor()

example =' WHERE Date = "                                                       "'

def tempGet(data):
    dev_x=[]
    dev_y=[]
    dev_date=[]
    dev_time=[]
    sql = 'SELECT Temperature,Time,LightLevel,Date FROM sensorData '
    if data != "":
        sql += 'WHERE Date = "' +  data + '"' 
    cursor.execute(sql)
    rows = cursor.fetchall()

    for x in rows:
        dev_x.append(x[0])
        dev_y.append(x[2])
        dev_date.append(x[3])
        dev_time.append(x[1])
    return dev_x,dev_y,dev_date,dev_time
   
    
        
           
        
def setup(date):
    



    
    dev_x,dev_y,dev_date,dev_time = tempGet(date)


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


        
    
