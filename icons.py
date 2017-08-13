from PIL import Image
import os

g = (0,255,0)
r = (255,0,0)
b = (0,0,255)
d = (0,0,0)


wifi = [
d,d,d,d,d,d,d,d,
d,d,b,b,b,b,d,d,
d,b,d,d,d,d,b,d,
b,d,d,d,d,d,d,b,
d,d,d,b,b,d,d,d,
d,d,b,d,d,b,d,d,
d,d,d,d,d,d,d,d,
d,d,d,b,b,d,d,d
]

no_wifi = [
r,d,d,d,d,d,d,r,
d,r,g,g,g,g,r,d,
d,g,r,d,d,r,g,d,
g,d,d,r,r,d,d,g,
d,d,r,g,g,r,d,d,
d,r,g,d,d,g,r,d,
r,d,d,d,d,d,d,r,
d,d,d,g,g,d,d,d
]

#code from 
# https://www.raspberrypi.org/magpi/pixel-art-on-sense-hat/

# Open image file
image_file = os.path.join(
os.sep,"/home","pi","PiHAT","img","sprite_0.png")
img = Image.open(image_file)
 
# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())
 
# Get the 64 pixels you need
pixel_width = 6
image_width = pixel_width*8
png_file = []
start_pixel = 0
while start_pixel < (image_width*64):
    png_file.extend(image_pixels[start_pixel:(
start_pixel+image_width):pixel_width])
    start_pixel += (image_width*pixel_width)
