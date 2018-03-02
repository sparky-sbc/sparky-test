added 720p supported sparky kernel.dtb and u-boot-dtb.img
usbridge support included.

example given for dietpi OS. can apply on other OS.

do ssh login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky_720p_dtb/sparky_720p_dtb.tar

tar -xvf sparky_720p_dtb.tar

cp kernel.dtb /boot/

dd if=u-boot-dtb.img of=/dev/mmcblk0 bs=512 seek=6144

sync

reboot



