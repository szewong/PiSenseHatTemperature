import icons
import time
from sense_hat import SenseHat
sense = SenseHat()


sense.set_pixels(icons.get_pixel_array("sprite_0.png"))
time.sleep(1)
sense.set_pixels(icons.get_pixel_array("sprite_1.png"))
time.sleep(1)
sense.set_pixels(icons.get_pixel_array("sprite_2.png"))
time.sleep(1)
sense.set_pixels(icons.get_pixel_array("sprite_3.png"))
time.sleep(1)
sense.set_pixels(icons.get_pixel_array("sprite_4.png"))
time.sleep(1)
sense.set_pixels(icons.get_pixel_array("sprite_5.png"))
time.sleep(1)