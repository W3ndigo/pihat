#!/usr/bin/env python
# Script will define colours for message on Pi
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values for color definition
yellow = (255, 0, 0)
blue = (105,105, 105)

speed = 0.05

message = "Hello World"

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
