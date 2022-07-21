import time
import serial

#this file has the purpose of sending a messege to the microbit with the uart protocol i used it for testing purposes and to simplify the concept

port = "COM3"
baud = 9600

ser = serial.Serial(port,baud,timeout=1)

while True:
    test = input()
    ser.write(test.encode("utf-8"))
    time.sleep(2)