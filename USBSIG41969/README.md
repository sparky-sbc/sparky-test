USBridgeSig RPI 4.19.69 kernel driver for tesing

download all .tar.gz files from below links , then execute commands on board

cd /

https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/USBSIG41969/modules.tar.gz

https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/USBSIG41969/boot.tar.gz

https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/USBSIG41969/firmware.tar.gz

cd /

sudo rm -rf lib/modules lib/firmware

sudo tar xfz ./modules.tar.gz

sudo tar xfz ./firmware.tar.gz

sudo tar xfz ./boot.tar.gz

sudo sync

