import paho.mqtt.client as mqtt
import time
import serial
from termcolor import colored



def on_message(client,userdata, message):
    print(str(message.payload.decode("utf-8")))

broker = "broker.emqx.io"
client = mqtt.Client("tester")
client.connect(broker,1883)
client.subscribe("000666000")
client.loop_start()
client.on_message = on_message



while True:
    client.publish("000666000","hello")
    time.sleep(500)
    pass
   


   
    
    
    
    