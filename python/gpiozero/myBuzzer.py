#!/usr/bin/env python3


# gits controlled a buzzer and LED with a button

# import libraries
from gpiozero import LED, Button, Buzzer
from time import sleep

# variables
led1 = LED (17)
btn1 = Button (18)
#my buzzer operates differently, it is activated (sounds) when low
#so based on https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer
bzz1 = Buzzer (22,False, False)

# setup
led1.off()
bzz1.off()

def myAlarm ():
    if btn1.is_active:
        print ("pressed...")
        bzz1.on()
        led1.on()
    else:
        print ("released...")
        bzz1.off()
        led1.off()

btn1.when_pressed = myAlarm
btn1.when_released = myAlarm
    
print ("Press Ctrl+C to exit")
while True:
    sleep(1)


