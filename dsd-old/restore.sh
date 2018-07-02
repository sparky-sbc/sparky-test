#!/bin/sh
sudo wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-old/snd-usb-audio.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usb-audio.ko
sudo wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-old/snd-usbmidi-lib.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usbmidi-lib.ko
sleep 3
sudo sync

