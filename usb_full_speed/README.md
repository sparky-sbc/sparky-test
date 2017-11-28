This uImage for sparky , testing USBridge on full speed mode dt : 22/nov/2017

Dietp OS:

root@DietPi:~# cd /usr/src/

root@DietPi:/usr/src# mkdir bkp

root@DietPi:/usr/src# cp /boot/uImage bkp/

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/usb_full_speed/uImage

root@DietPi:/usr/src#cp uImage /boot/

to set USbridge 1.1 mode edit /DietPi/uEnv.txt , add aotg.aotg1_speed=1  at the end of the line.

root@DietPi:/usr/src# cat /DietPi/uEnv.txt

uenvcmd=setenv os_type linux;

bootargs=earlyprintk clk_ignore_unused selinux=0 scandelay console=tty0 loglevel=1 real_rootflag=rw root=/dev/mmcblk0p2 rootwait init=/lib/systemd/systemd aotg1.aotg_speed=1

