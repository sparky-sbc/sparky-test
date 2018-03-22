This includes Sparky DSI display supporting kernel.dtb and u-boot-dtb.img 

(to check with sparky LCD display and touch screen on dietpi install Mate desktop and run below commands )

ssh login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky_dsi_dtb/kernel.dtb

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky_dsi_dtb/u-boot-dtb.img

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky_dsi_dtb/ctp_ft5x06.ko

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky_dsi_dtb/boot_logo.bmp.gz

dd if=u-boot-dtb.img of=/dev/mmcblk0 bs=512 seek=6144

cp kernel.dtb /boot/

cp boot_logo.bmp.gz /boot/

cp ctp_ft5x06.ko /lib/modules/3.10.38/kernel/drivers/input/touchscreen/FT5406/ctp_ft5x06.ko

sync

reboot
