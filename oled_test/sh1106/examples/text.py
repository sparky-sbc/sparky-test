#!/usr/bin/env python
# Ported from:
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
font = ImageFont.load_default()
device = sh1106(port=2, address=0x3C)

with canvas(device) as draw:
    padding = 8 
    shape_width = 400
    top = padding
    bottom = device.height - padding - 1
    x = padding + 2
    # Load default font.
    font = ImageFont.load_default()


#ip = '192.168.0.72'

    # Alternatively load a TTF font.
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    # font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write two lines of text.
#draw.text((x + 20, top),'IP ADDRESS', font=font, fill=255)
draw.text((x + 15, top+20), '192.168.0.72' , font=font, fill=255)

