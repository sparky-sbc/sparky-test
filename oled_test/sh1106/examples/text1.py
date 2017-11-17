#!/usr/bin/env python
import sys
import socket
import fcntl
import struct
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
import subprocess
cmd = "mpc current"
TEXT = ''
ifname = ''
device = sh1106(port=2, address=0x3C)
with canvas(device) as draw:
    shape_width = 220
    padding = 16 
    top = padding
    bottom = device.height - padding - 1
    x = padding + 2

font = ImageFont.load_default()

p = subprocess.Popen(cmd, shell="True", stdout=subprocess.PIPE)
if True:
	out = p.stdout.read()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

try:
    TEXT = get_ip_address('wlan0') # WiFi address of WiFi adapter. NOT ETHERNET
    ifname="Wlan0"
except IOError:
   try:
       TEXT = get_ip_address('eth0') # WiFi address of Ethernet cable. NOT ADAPTER
       ifname="Eth0"
   except IOError:
       TEXT = ('NO INTERNET!')

with canvas(device) as draw:
    shape_width = 220
    padding = 8
    top = padding
    bottom = device.height - padding - 1
    x = padding + 2
    # Write two lines of text.
    draw.text((x, top), out[0:19], font=font, fill=255)
    draw.text((x, top+10), out[19:40], font=font, fill=255)
    draw.text((x, top+40), ifname + ':' + TEXT, font=font, fill=255)

