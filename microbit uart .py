import serial



#this file has the purpose of reiceving messeges from the microbit i used it for testing purposes

port = "COM5"
baud = 9600

ser = serial.Serial(port,baud,timeout=1)


while True:
    x = ser.readline()
    
    x=x.decode('utf8')
    x=x.split(" ")
    if len(x) == 2:
        temperature = x[0]
        lightlevel = x[1]
        print("Temperature:" + temperature +"\n"+"Light Level:" + lightlevel)
    