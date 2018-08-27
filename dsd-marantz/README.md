This Includes updated usb audio drivers of USBridge dtd 6th march 2018.

the following native DSD support added , tested feedbacks to be get from usres.

 Denon DA-300USB, Marantz HD-DAC1,  Marantz SA-14S1, TEAC UD-501/UD-503/NT-503
 
 Esoteric D-05X, T+A DAC8DSD-V2.0, MP1000E-V2.0, MP2000R-V2.0, MP2500R-V2.0, MP3100HV-V2.0

T+A USB HD Audio 1, T+A USB HD Audio 2 ,COMBO384 ids added 

6th April 2018 - added Topping D50 dsd support

30th april added XMOS 20b1:3078

14th may 18 added T+A dac8 patch

28th June-18 : Designs patch added for DSD on MPD-5 dac , new Ids added Mytek Manhatten , LH labs 1V5 2V0 ,HD-AVP/AVA IDA-8.

29th June-18 :  irDAC-ii included for native DSD - Waiting for user feedback)

16th July-18   included for native DSD Mytek Brooklyn DAC+

27th Aug-18 DSD Native : Pro-Ject Box DAC , AQUA , IFI Pro iDSD  

*************************************
update procedure on dietpi and volumio OS for USBridge DSD native support.

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-marantz/snd-usb-audio.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usb-audio.ko

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-marantz/snd-usbmidi-lib.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usbmidi-lib.ko

sync

reboot

or

sh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-marantz/install.sh

sh install.sh

reboot


