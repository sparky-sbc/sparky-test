#!/usr/bin/env python
import threading
import time
import sys
import socket
import fcntl
import struct
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
import subprocess
cmd = "mpc current"
cmd1 = "mpc volume"
out = ""
out1 = ""
TEXT = ''
ifname = ''
device = sh1106(port=2, address=0x3C)
shape_width = 220
padding = 8
top = padding
bottom = device.height - padding - 1
x = padding + 2
#font = ImageFont.load_default()
#font = ImageFont.load_default().font
#font = ImageFont.truetype("Volter__28Goldfish_29.ttf",12)
font = ImageFont.load_default().font
font = ImageFont.truetype("Verdana.ttf",12)

line1=""
line2=""
line3=""
line4=""
def display():
	global line1, line2, line3, line4
	with canvas(device) as draw:
		rndfont=12
		draw.text((x, top), line1, font=font, fill=255)
		draw.text((x, top+14), line2, font=font, fill=255)
		draw.text((x+10, top+30), line4, font=font, fill=255)
		draw.text((x, top+40), line3, font=font, fill=255)

def readtrack():
	global out
	p = subprocess.Popen(cmd, shell="True", stdout=subprocess.PIPE)
	if True:
		out = p.stdout.read()
def volume():
        global out1
        p = subprocess.Popen(cmd1, shell="True", stdout=subprocess.PIPE)
        if True:
                out1 = p.stdout.read()

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

# Write two lines of text.

def looper(): 
	global line1, line2, line3, line4
	readtrack()
	line1=out[0:16]
	line2=out[16:36]
        volume()
        line4=out1[0:11] 
	display()
	threading.Timer(2, looper).start()
looper()

line3=ifname + ':' + TEXT
display()

