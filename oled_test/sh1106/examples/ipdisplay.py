#!/usr/bin/env python
import netifaces as ni
# Ported from:
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py

from oled.device import ssd1306, sh1106
from oled.render import canvas
import sys
import socket
import fcntl
import struct
from PIL import ImageFont
from PIL import ImageFont
TEXT = ''
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


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

try:
    TEXT = get_ip_address('wlan0') # WiFi address of WiFi adapter. NOT ETHERNET
    ifname="wlan0"
    
    print ifname
    print TEXT
except IOError:
    try:
        TEXT = get_ip_address('eth0') # WiFi address of Ethernet cable. NOT ADAPTER

        ifname="eth0"
        print ifname
        print TEXT
    except IOError:
        TEXT = ('NO INTERNET!')


    draw.text((x + 20, top),    'IP ADDRESS',  font=font, fill=255)
    draw.text((x + 15, top+20), 'TEXT', font=font, fill=255)
