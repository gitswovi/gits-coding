#!/usr/bin/env python3


# From https://github.com/gitswovi/SunFounder_Super_Kit_V3.0_for_Raspberry_Pi/blob/master/Python/02_buttonControlLed.py
# gits moved to use gpiozero and changed a number of things

#import libraries
from gpiozero import LED, Button
#from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
#from sys import version_info
import sys

#### What's this for?
if sys.version_info.major == 3:
    raw_input = input

# Set #17 as LED pin
led1 = LED(17)  # local pin
# Set #18 as button pin
btn1 = Button(18) # local pin
# Set #19 as button pin
btn2 = Button(19) # local pin

# Define a function to print message at the beginning
def print_message():
    print ("========================================")
    print ("|          Button control LED          |")
    print ("|    ------------------------------    |")
    print ("|         LED connect to", led1.pin, "       |")
    print ("|        Button connect to", btn1.pin, "     |")
    print ("|        Button connect to", btn2.pin, "     |")
    print ("|                                      |")
    print ("| Press any button to turn on/off LED. |")
    print ("|                                      |")
    print ("|                            gits wovi |")
    print ("========================================\n")
    print ("Program is running...")
    raw_input ("Press Enter to begin then press any button\n")
    print ("Please press Ctrl+C to end the program...")

# Define a setup function for some setup
def setup():
    #global led1
    #global btn1
    #global btn2
    
    # I turn on the LED:
    led1.on()
    
    # Callback function to swLed
    btn1.when_pressed = swLed
    btn2.when_pressed = swLed

# Define a callback function for button callback
def swLed(ev=None):
    # global led1
    # Switch led status(on-->off; off-->on)
    if (btn1.is_active and btn2.is_active):
        destroy()
        sys.exit("Exit, two buttons pressed.")
    else:
        led1.toggle()
    if (not led1.is_lit):
        print ("LED OFF...")
    else:
        print("...LED ON")

# Define a main function for main process
def main():
    # Print messages
    print_message()
    setup()
    while True:
        # Don't do anything.
        sleep (1)

# Define a destroy function for clean up everything after
# the script finished
def destroy():
    #global led1
    # Turn off LED
    led1.off()
    print ("LED status is ", led1.is_active)
    # How do I release resources?
    #GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
    #destroy()
    
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        print (" KB interrupt")
        destroy()
        sys.exit("Exit, Ctrl+C pressed")
    finally:
        print("end destroy")
        destroy()
