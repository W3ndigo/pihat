#1/usr/bin/env python3
from sense_hat import SenseHat

sense = SenseHat()
#clears all LEDs that may have been left on.

print("clearing LEDs")

sense.clear()
