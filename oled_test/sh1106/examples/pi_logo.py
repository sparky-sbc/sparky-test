#!/usr/bin/env python

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageDraw, Image

device = sh1106(port=2, address=0x3c)
#device = ssd1306(port=2, address=0x3d)

with canvas(device) as draw:
    logo = Image.open('/usr/src/sh1106/examples/images/pi_logo.png')
    draw.bitmap((32, 0), logo, fill=1)
