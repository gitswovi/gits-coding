#!/bin/python3

# From https://pi-top-pi-top-python-sdk.readthedocs-hosted.com/en/latest/api_pma/components.html#led

# import libraries
from pitop.pma import LED
from time import sleep

led = LED("D4")

for i in range(5):
    led.on()
    print(led.is_lit)
    sleep(1)
    led.off()
    print(led.is_lit)
    sleep(1)

print(led.value)  # Returns 1 is the led is on or 0 if the led is off
sleep(2)


# Blink in the background:
#blink(on_time=1, off_time=1, n=None, background=True)
#Make the device turn on and off repeatedly.
#Parameters:	
#on_time (float) – Number of seconds on. Defaults to 1 second.
#off_time (float) – Number of seconds off. Defaults to 1 second.
#n (int or None) – Number of times to blink; None (the default) means forever.
#background (bool) – If True (the default), start a background thread to continue blinking and return immediately.
#If False, only return when the blink is finished (warning: the default value of n will result in this method never returning).

#led.blink()
led.blink(1,1,10,True)
print ("Still blinking isn't it?")
print (led.value)  # Returns 1 is the led is on or 0 if the led is off
print ("LED pin: ")
print (led.pin)
sleep(2)