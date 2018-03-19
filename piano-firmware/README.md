# piano-firmware
Allo Piano DAC 2.1 DSP firmware files (VERSION 1.2)

update procedure on dietpi/volumio

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/piano-firmware/piano-firmware.tar

tar -xvf piano-firmware.tar -C /lib/

sync

reboot
