import paho.mqtt.client as mqtt
import time
import serial
import sqlite3
from datetime import date
from datetime import datetime

setthelight = " "

conn = sqlite3.connect('information.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS sensorData (LightLevel text,Temperature text,Date text,Time text)""")



def on_message(client,userdata, message):
    global setthelight
    
    if len(str(message.payload.decode("utf-8"))) == 1:
        setthelight = str(message.payload.decode("utf-8"))
        print(setthelight)
        
        


port = "COM3"
baud = 9600

ser = serial.Serial(port,baud,timeout=1)

broker = "broker.emqx.io"
client = mqtt.Client("Temperature")
client.connect(broker,1883)

temperature = 0
lightlevel = 0
log = 0 
client2 = mqtt.Client("set_lights")
client2.connect(broker,1883)

print("Connection made.")



while True:
    try:
        client2.loop_start()
        x = ser.readline()
      
        x=x.decode('utf8')
        x=x.split(" ")
        client2.subscribe("temperature0")
        client2.on_message = on_message
        
       
        if len(setthelight) == 1:
            ser.write(setthelight.encode("utf-8"))
            
        
        if len(x) == 2:
            temperature = x[0]
            lightlevel = x[1]
            print("///////////////////////"+ "\n" + "LOG: " + str(log) + "\n" + "Information received."+ "\n" +"Temperature:" + temperature +"\n"+"Light Level:" + lightlevel)
            client.publish("temperature0",temperature)
            client.publish("light0",lightlevel)
            textlog = str(log)
            texttemp= str(temperature)
            textlightlevel= str(lightlevel)
            ddate = str(date.today())
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c.execute("INSERT INTO sensorData VALUES (?,?,?,?)",(textlightlevel,texttemp,ddate,current_time))
            conn.commit()
            
            log+=1
            
        
        
        
    except Exception as e:
        print("An error has occured:", e)
        
    
    
    
    
