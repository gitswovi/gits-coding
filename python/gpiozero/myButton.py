from gpiozero import Button

btn = Button(19)

while True:
    if btn.is_pressed:
        print("button is pressed")
    else:
        print("nothing")