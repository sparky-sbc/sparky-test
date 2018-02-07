This Includes updated usb audio drivers of USBridge dtd 7th feb 2018.

the following native DSD support added , tested feedbacks to be get from usres.

QUAD Artera

Pro-Ject Pre Box S2 Digital

Matrix Audio Quattro II 

Topping D30 (XMOS)

WaveIO USB Audio 2.0

Soekris dac1101

Engineered Electronics Stereo

*************************************
update procedure on dietpi/volumio

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/pro-ject-s2/snd-usb-audio.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usb-audio.ko

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/pro-ject-s2/snd-usbmidi-lib.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usbmidi-lib.ko

sync

reboot




