#!/bin/python3

# From https://pi-top-pi-top-python-sdk.readthedocs-hosted.com/en/latest/api_miniscreen/oled.html

#import libraries
from pitop.miniscreen import OLED
from pitop.miniscreen.buttons import CancelButton
from PIL import Image, ImageSequence
from time import sleep

# Note: When you create a OLED object in your program, the mini-screen on the pi-top [4] will clear and is then controlled by your code.
# You will not be able to access the system menu on the mini-screen until your program exits, at which point the system menu is automatically
# restored. If you need to provide yourself with a method of being able to exit, it is recommended that you check for a press event on the
# ‘cancel’ button.
oled = OLED()

# Writing text to the OLED:
oled.draw_multiline_text("Hello, world!")

sleep(2)

# Image provided by 'pt-project-files'
rocket = Image.open("/usr/share/pt-project-files/images/rocket.gif")

# Showing an image on the OLED:
# oled.draw_image_file(rocket)

# Loop a GIF on the OLED:
#while True:
#    for frame in ImageSequence.Iterator(rocket):
#        oled.draw_image(frame)

# Displaying an GIF once:
oled.play_animated_image(rocket)

sleep(2)

# Using cancel button:
cancel_button = CancelButton()
oled.draw_multiline_text("Press cancel to exit!", font_size=22)
while not cancel_button.is_pressed:
    sleep(0.1)
oled.draw_multiline_text("Bye!")

sleep(2)