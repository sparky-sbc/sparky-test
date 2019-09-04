USBridgeSig RPI 4.19.69 kernel driver for tesing

download all .tar.gz files and execute below commands on board.

cd /

sudo rm -rf lib/modules lib/firmware

sudo tar xfz ./modules.tar.gz

sudo tar xfz ./firmware.tar.gz

sudo tar xfz ./boot.tar.gz

sudo sync

