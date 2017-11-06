#!/bin/sh
ver=$(uname -r)
ver_match=0
#echo "$ver"
if [ "$ver" = "3.10.38" ]; then
  echo "kernel version is '$ver'"
sudo rm -rf /lib/modules/$ver/kernel/drivers/net/wireless/rtl8812au
sudo cp -pr rtl8812au/ /lib/modules/$ver/kernel/drivers/net/wireless/
sudo cp rtl8812au/wlan_8812au.conf /etc/modprobe.d/
ver_match=1
fi
if [ "$ver_match" = "1" ]; then
  echo "kernel matching"
cd /lib/modules/$ver/kernel/drivers/net/wireless/rtl8812au/
sudo sh load.sh
else
 echo "kernel version not matching"
fi
exit 0

