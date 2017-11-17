#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

from __future__ import unicode_literals


search_terms = ['python']

import os
import sys
import time
from PIL import ImageFont

try:
    from Queue import Queue
except ImportError:
    from queue import Queue

from demo_opts import get_device
from luma.core.render import canvas
from luma.core.virtual import viewport


try:
    import tweepy
except ImportError:
    print("The tweepy library was not found. Run 'sudo -H pip install tweepy' to install it.")
    sys.exit()


def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)


def scroll_message(status, font=None, speed=1):
    author = u"@{0}".format(status.author.screen_name)
    full_text = u"{0}  {1}".format(author, status.text).replace("\n", " ")
    x = device.width

    # First measure the text size
    with canvas(device) as draw:
        w, h = draw.textsize(full_text, font)

    virtual = viewport(device, width=max(device.width, w + x + x), height=max(h, device.height))
    with canvas(virtual) as draw:
        draw.text((x, 0), full_text, font=font, fill="white")
        draw.text((x, 0), author, font=font, fill="yellow")

    i = 0
    while i < x + w:
        virtual.set_position((i, 0))
        i += speed
        time.sleep(0.025)


class listener(tweepy.StreamListener):

    def __init__(self, queue):
        super(listener, self).__init__()
        self.queue = queue

    def on_status(self, status):
        self.queue.put(status)


device = get_device()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
queue = Queue()

if device.height >= 16:
    font = make_font("code2000.ttf", 12)
else:
    font = make_font("pixelmix.ttf", 8)

try:
    stream = tweepy.Stream(auth=api.auth, listener=listener(queue))
    stream.filter(track=search_terms, async=True)

    try:
        while True:
            status = queue.get()
            scroll_message(status, font=font)
    except KeyboardInterrupt:
        pass

finally:
    stream.disconnect()