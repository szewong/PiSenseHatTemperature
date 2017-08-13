import icons
import time
import os
from sense_hat import SenseHat
sense = SenseHat()

for file in os.listdir("./img"):
    if file.endswith(".png"):
		sense.set_pixels(icons.get_pixel_array(file))
		time.sleep(1)


sense.clear()
