6th April 2018 - added Topping D50 dsd support and DAC 8 DSD test (Altset 1 enabled for DSD fir checking)

*************************************
update procedure on dietpi/volumio

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd_dac8/snd-usb-audio.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usb-audio.ko

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd_dac8/snd-usbmidi-lib.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usbmidi-lib.ko`

sync

reboot




