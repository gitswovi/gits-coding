#!/bin/python3

# From https://pi-top-pi-top-python-sdk.readthedocs-hosted.com/en/latest/api_miniscreen/oled.html

#import libraries
from pitop.miniscreen import OLED
from pitop.miniscreen.buttons import CancelButton
from time import sleep

oled = OLED()
cancel_button = CancelButton()

oled.draw_multiline_text("Press cancel to exit!", font_size=22)

while not cancel_button.is_pressed:
    sleep(0.1)

oled.draw_multiline_text("Bye!")
sleep(2)