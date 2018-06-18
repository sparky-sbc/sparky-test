#!/bin/sh
ver=$(uname -r)
ver_match=0
#echo "$ver"
if [ "$ver" = "4.14.42-v7+" ]; then
  echo "kernel version is '$ver'"
wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/rpi-41442-8192eu/8192eu.ko -O /lib/modules/4.14.42-v7+/kernel/drivers/net/wireless/8192eu.ko
ver_match=1
fi
if [ "$ver" = "4.14.49-v7+" ]; then
  echo "kernel version is '$ver'"
wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/rpi-41449-8192eu/8192eu.ko -O /lib/modules/4.14.49-v7+/kernel/drivers/net/wireless/8192eu.ko
ver_match=1
fi
if [ "$ver_match" = "1" ]; then
  echo "kernel matching"

#sudo rmmod rtl8xxxu.ko
#echo blacklist rtl8xxxu > /etc/modprobe.d/blacklist-rtl8xxxu.conf
sudo insmod /lib/modules/$ver/kernel/drivers/net/wireless/8192eu.ko
sudo depmod -a
else
 echo "kernel version not matching"
fi
exit 0

