#!/bin/sh
wget wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky_dsi_dtb/sparky_dsi_touch.tar
sleep 2 
sudo mkdir /usr/src/sparky_lcd
sudo tar -xvf sparky_dsi_touch.tar -C /usr/src/sparky_lcd
sudo cp /usr/src/sparky_lcd/kernel.dtb /boot/kernel.dtb
sudo cp /usr/src/sparky_lcd/boot_logo.bmp.gz /boot/boot_logo.bmp.gz
sudo cp /usr/src/sparky_lcd/ctp_ft5x06.ko /lib/modules/3.10.38/kernel/drivers/input/touchscreen/FT5406/ctp_ft5x06.ko
sudo dd if=/usr/src/sparky_lcd/u-boot-dtb.img of=/dev/mmcblk0 bs=512 seek=6144
sudo rm -rf /usr/src/sparky_lcd/
sudo sync

