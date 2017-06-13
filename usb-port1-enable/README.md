this contains the sparky kernel.dtb , 

	-on this allo 12 key IR remote code added (june 2017) 
	-and USB-port1 enabled	(june 2017)
	- default display HDMI-auto,1280x800 default.

to update this file on board

login on sparky volumio or dietpi image booted board.

root@volumio:~/ cd /home/
root@volumio:/home# wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/usb-port1-enable/kernel.dtb
Saving to: 'kernel.dtb'

kernel.dtb                                100%[=======================================================================================>]  33.43K   114KB/s   in 0.3s


root@volumio:/home# cp /boot/kernel.dtb /boot/kernel.dtb_bkp
root@volumio:/home# cp kernel.dtb /boot/kernel.dtb
root@volumio:/home# reboot

