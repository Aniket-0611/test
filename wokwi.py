from machine import Pin
from time import sleep


green = Pin(4, Pin.OUT)
yellow = Pin(5, Pin.OUT)
red = Pin(2, Pin.OUT)


button = Pin(15, Pin.IN, Pin.PULL_UP)


green.off()
yellow.off()
red.off()

cycle_count = 0

def all_off():
    green.off()
    yellow.off()
    red.off()

while True:

    
    if button.value() == 0:
        print("EMERGENCY")

        green.on()
        yellow.off()
        red.off()
        sleep(5)

       
        print("RED")
        green.off()
        yellow.off()
        red.on()
        sleep(2)

    
    print("ALL OFF")
    all_off()
    sleep(1)

    
    print("GREEN")
    green.on()
    yellow.off()
    red.off()
    sleep(5)

    
    if button.value() == 0:
        continue

    
    print("YELLOW")
    green.off()
    yellow.on()
    red.off()
    sleep(2)

    if button.value() == 0:
        continue

   
    print("RED")
    green.off()
    yellow.off()
    red.on()
    sleep(5)

    
