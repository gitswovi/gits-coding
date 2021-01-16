#!/usr/bin/env python3


# inspire by https://github.com/gitswovi/SunFounder_Super_Kit_V3.0_for_Raspberry_Pi/blob/master/Python/02_8Led.py
# gits just tiwcked,added buttons..

#import libraries
from gpiozero import LED, Button
from time import sleep
from random import randint
#from sys import version_info
#import sys

myLEDPins = [6, 13, 19, 26, 12, 16, 20, 21]
myLEDs = []
myReversed = []
myBtnPins = [17, 18, 27, 22, 23]
myBtns = []
#totalLEDs = len(myLEDPins)
#totalBtns = len(myBtnPins)
mode = -1
totalmodes = 8

# Define a function to print message at the beginning
def initMessage():
    print ("========================================")
    print ("                 8 LEDs                ")
    print ("     ------------------------------    ")
    print ("     Red LED0 connect to GPIO",myLEDPins[0])
    print ("     Red LED1 connect to GPIO", myLEDPins[1])
    print ("     Yellow LED2 connect to GPIO", myLEDPins[2])
    print ("     Yellow LED3 connect to GPIO", myLEDPins[3])
    print ("     Green LED4 connect to GPIO", myLEDPins[4])
    print ("     Green LED5 connect to GPIO", myLEDPins[5])
    print ("     Blue LED6 connect to GPIO", myLEDPins[6])
    print ("     Blue LED7 connect to GPIO", myLEDPins[7])
    print (" ")
    print ("     Red Button connect to GPIO", myBtnPins[0])
    print ("     Yellow Button connect to GPIO", myBtnPins[1])
    print ("     Green Button connect to GPIO", myBtnPins[2])
    print ("     Blue Button connect to GPIO", myBtnPins[3])
    print ("     Big button connect to GPIO", myBtnPins[4])
    print (" ")
    print ("                             gits wovi")
    print ("========================================\n")
    print ("Program is running...")
    print ("Please press Ctrl+C to end the program...")

def turnAllOn (Yes=True):
     # Turn on or off all LEDs:
    for led in myLEDs:
        if Yes:
            led.on()
        else:
            led.off()

def swMode():
    global mode

    mode = (mode + 1) % totalmodes
    print ("switching to mode", mode)

def setup():
    # Create LEDs:
    for pin in myLEDPins:
        myLEDs.append(LED(pin))
    myReversed = reversed(myLEDs)

    # Turn off all LEDs:
    turnAllOn()

    # Create Buttons:
    for pin in myBtnPins:
        myBtns.append(Button(pin))

    # Change mode when Big button pushed.
    myBtns[0].when_pressed = swMode

    # Print a message:
    initMessage()

def destroy():
     # Turn off all LEDs:
    turnAllOn(False)

    print ("\ngits end...")


def flowLeftRight(mylist = myLEDs,by = 1,sec = 0.1, keepOn = True):
    
    # Flow from Left to Right:
    for led in mylist:
        led.toggle()
        sleep(sec)
        if keepOn:
            led.on()

def flowRightLeft(by = 1,sec = 0.1,keepOn = True):
    
    flowLeftRight (reversed(myLEDs),by,sec,keepOn)

def wave(by = 1,sec = 0.1,keepOn = True):
    
    flowLeftRight(myLEDs,by,sec, keepOn)
    sleep(0.2)
    #flowRightLeft(by,sec, keepOn)
    #turnAllOn()
    flowLeftRight (reversed(myLEDs),by,sec,keepOn)

def flow (m = 0):
    if m == 0:
        wave(1,0.1,True)
    elif m == 1:
        wave (1,0.1,False)
    elif m == 2:
        flowLeftRight()
    elif mode == 3:
        flowLeftRight(myLEDs,1,0.1,False)
    elif m == 4:
        flowRightLeft()
    elif m == 5:
        flowRightLeft(1,0.1,False)
    elif m == 6:
        # all modes
        wave(1,0.1,True)
        # Icheck if mode changed after every set:
        if m==6:
            wave (1,0.1,False)
        if m==6:
            flowLeftRight()
        if m==6:
            flowRightLeft()
        if m==6:
            flowLeftRight(myLEDs,1,0.1,False)
        if m==6:
            flowRightLeft(1,0.1,False)
    elif m == 7:
        #random
        x = randint(0,totalmodes-3) # minus all and random
        print ("random mode ",x)
        flow(x)


setup()

# Turn all LEDs on.
turnAllOn()

print ("Press Big button to begin\n")

myBtns[0].wait_for_press()

# flow
while True:
    flow(mode)
    sleep(0.2)


destroy()