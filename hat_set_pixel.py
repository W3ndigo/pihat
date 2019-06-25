#!/usr/bin/env python
# This script will display colors for individual picti\ures
from sense_hat import SenseHat
sense = SenseHat()
import time

green = (0, 255, 0)
white = (255, 255, 255)
black = (32, 32, 32)

sense.set_pixel(0, 0, (white))
sense.set_pixel(0, 1, (green))
sense.set_pixel(0, 2, (green))
sense.set_pixel(0, 3, (green))
sense.set_pixel(0, 4, (white))
sense.set_pixel(0, 5, (white))
sense.set_pixel(0, 6, (white))
sense.set_pixel(0, 7, (green))
#////////////////////////////////////////2
sense.set_pixel(1, 0, (green))
sense.set_pixel(1, 1, (green))
sense.set_pixel(1, 2, (black))
sense.set_pixel(1, 3, (black))
sense.set_pixel(1, 4, (green))
sense.set_pixel(1, 5, (green))
sense.set_pixel(1, 6, (white))
sense.set_pixel(1, 7, (green))
#////////////////////////////////////////3
sense.set_pixel(2, 0, (green))
sense.set_pixel(2, 1, (green))
sense.set_pixel(2, 2, (black))
sense.set_pixel(2, 3, (black))
sense.set_pixel(2, 4, (white))
sense.set_pixel(2, 5, (black))
sense.set_pixel(2, 6, (black))
sense.set_pixel(2, 7, (black))
#////////////////////////////////////////4
sense.set_pixel(3, 0, (green))
sense.set_pixel(3, 1, (green))
sense.set_pixel(3, 2, (green))
sense.set_pixel(3, 3, (green))
sense.set_pixel(3, 4, (black))
sense.set_pixel(3, 5, (black))
sense.set_pixel(3, 6, (black))
sense.set_pixel(3, 7, (green))
#////////////////////////////////////////5
sense.set_pixel(4, 0, (white))
sense.set_pixel(4, 1, (green))
sense.set_pixel(4, 2, (green))
sense.set_pixel(4, 3, (green))
sense.set_pixel(4, 4, (black))
sense.set_pixel(4, 5, (black))
sense.set_pixel(4, 6, (black))
sense.set_pixel(4, 7, (white))
#////////////////////////////////////////6
sense.set_pixel(5, 0, (green))
sense.set_pixel(5, 1, (green))
sense.set_pixel(5, 2, (black))
sense.set_pixel(5, 3, (black))
sense.set_pixel(5, 4, (white))
sense.set_pixel(5, 5, (black))
sense.set_pixel(5, 6, (black))
sense.set_pixel(5, 7, (black))
#////////////////////////////////////////7
sense.set_pixel(6, 0, (green))
sense.set_pixel(6, 1, (green))
sense.set_pixel(6, 2, (black))
sense.set_pixel(6, 3, (black))
sense.set_pixel(6, 4, (green))
sense.set_pixel(6, 5, (green))
sense.set_pixel(6, 6, (green))
sense.set_pixel(6, 7, (green))
#///////////////////////////////////////8
sense.set_pixel(7, 0, (green))
sense.set_pixel(7, 1, (white))
sense.set_pixel(7, 2, (white))
sense.set_pixel(7, 3, (green))
sense.set_pixel(7, 4, (green))
sense.set_pixel(7, 5, (white))
sense.set_pixel(7, 6, (green))
sense.set_pixel(7, 7, (green))

time.sleep(10)



sense.clear()

