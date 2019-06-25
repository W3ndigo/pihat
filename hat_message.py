#!/usr/bin/env python
# This script will show scrolling message on the Pi Hat

from sense_hat import SenseHat
sense=SenseHat()

# Will send text Hello World to the show_message() functon
sense.show_message("william")
