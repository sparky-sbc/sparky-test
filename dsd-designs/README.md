This Includes updated usb audio drivers of USBridge dtd 28th June 2018.

the following native DSD support added , tested feedbacks to be get from usres.

- Designs patch added for DSD on MPD-5 dac

- new Ids added Mytek Manhatten , LH labs 1V5 2V0 ,HD-AVP/AVA IDA-8.

- irDAC-ii included for native DSD. To be get feedback from users.


*************************************
update procedure on dietpi/volumio

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-designs/snd-usb-audio.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usb-audio.ko

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-designs/snd-usbmidi-lib.ko -O /lib/modules/3.10.38/kernel/sound/usb/snd-usbmidi-lib.ko

sync

reboot


or

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-designs/install.sh

sh install.sh
