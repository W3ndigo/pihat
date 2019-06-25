#!/usr/bin/env python
#display random colored letters

from sense_hat import SenseHat
sense = SenseHat()
import time
import random

#assign random integer between 0 ad 255 to a variable
r = random.randint(0,255)
x = random.randint(0,255)
y = random.randint(0,255)
print("the random number is..."), r, "(this time)"




sense.show_letter("H", (r, x, y))
time.sleep(1)
sense.show_letter("i", (x, r, y))
time.sleep(1)
sense.show_letter("!", (x, y, r))

time.sleep(1)
sense.clear()
