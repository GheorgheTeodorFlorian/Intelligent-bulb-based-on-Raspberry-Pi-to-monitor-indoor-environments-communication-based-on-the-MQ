import paho.mqtt.client as mqtt
import time
import serial
from termcolor import colored

broker = "broker.emqx.io"
client = mqtt.Client("tester")
client.connect(broker,1883)

while True:
    test = input()
    client.publish("setlight0",test)