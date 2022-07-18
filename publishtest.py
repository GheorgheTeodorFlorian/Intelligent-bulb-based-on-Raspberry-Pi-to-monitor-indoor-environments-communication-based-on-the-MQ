import paho.mqtt.client as mqtt
import time
import serial
from termcolor import colored

broker = "broker.emqx.io"
client = mqtt.Client("tester")
client.connect(broker,1883)
test = input()
while True:
    
    client.publish("setlight0",test)