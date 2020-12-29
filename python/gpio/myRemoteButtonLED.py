#!/bin/python3

# From https://magpi.raspberrypi.org/articles/remote-control-gpio-raspberry-pi-gpio-zero

#import libraries
import gpiozero
from gpiozero import LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

btn = Button(2) # local RPi.GPIO pin

# change change the default pin factory on the fly:
gpiozero.Device.pin_factory = PiGPIOFactory('192.168.64.1')
remoteLED = LED(17) # remote pin

remoteLED.source = button.values

pause()