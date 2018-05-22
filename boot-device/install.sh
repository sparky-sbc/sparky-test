#!/bin/sh
wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/boot-device/bootloader.bin
sleep 2
sudo dd if=/usr/src/bootloader.bin of=/dev/mmcblk0 bs=512 seek=4097
sudo sync
exit 0
