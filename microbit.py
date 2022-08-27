# Add your Python code here. E.g.
from microbit import *

on = Image("99999:"
            "99999:"
             "99999:"
             "99999:"
             "99999")
             
onMidLight = Image("55555:"
                "55555:"
                "55555:"
                "55555:"
                "55555")             
             
             
off = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00000")
             
uart.init()



while True:
    if uart.any():
        msg = uart.read()
        msg_str = msg.decode("utf-8")
        
        if len(msg_str) == 1:
            if msg_str == "1":
                if display.read_light_level() < 127:
                    display.show(on)
                elif display.read_light_level() > 127:
                    display.show(onMidLight)
                
            elif msg_str == "0":
                display.show(off)
                
    uart.write(str(temperature())+" "+str(display.read_light_level()))
    sleep(2000)
    
    if temperature() > 65:
        print("Temperature exceeds normal parameters breaking loop")
        display.scroll("Temperature exceeds normal parameters breaking loop")
        break


#display.show(Image.ALL_CLOCKS, loop=True, delay=100)