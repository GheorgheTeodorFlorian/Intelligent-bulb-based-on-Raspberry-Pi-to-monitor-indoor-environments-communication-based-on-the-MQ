# Add your Python code here. E.g.
from microbit import *

while True:
    msg = uart.read()
    msg_str = str(msg, 'UTF-8')
    if len(msg_str) == 1:
        print("it worked!!!!!!!!")
    uart.write(str(temperature())+" "+str(display.read_light_level()))
    sleep(2000)