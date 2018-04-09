This Includes updated usb audio drivers of USBridge dtd 6th march 2018.

the following native DSD support added , tested feedbacks to be get from usres.

 Denon DA-300USB
 
 Marantz HD-DAC1
 
 Marantz SA-14S1 

 TEAC UD-501/UD-503/NT-503
 
 Esoteric D-05X

T+A DAC8DSD-V2.0, MP1000E-V2.0, MP2000R-V2.0, MP2500R-V2.0, MP3100HV-V2.0

T+A USB HD Audio 1

T+A USB HD Audio 2 

COMBO384 ids added 

6th April 2018 - added Topper D50 dsd support

*************************************
update procedure on dietpi/volumio

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-marantz/snd-usb-audio.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usb-audio.ko

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-marantz/snd-usbmidi-lib.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usbmidi-lib.ko

sync

reboot




