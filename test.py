import serial

port = "COM3"
baud = 9600

ser = serial.Serial(port,baud,timeout=1)


while True:
    x = ser.readline()
    
    x=str(x)
    print(x)