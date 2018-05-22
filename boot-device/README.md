On sparky boot device priority can be change by reloading the bootloader.bin

this folder contains the bootloader.bin for first priority on uSD card.

by default volumio boots from eMMC first, dietpi OS boots uSD card first.

ssh login 

cd /usr/src/

download the install script.

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/boot-device/install.sh

sh install.sh

