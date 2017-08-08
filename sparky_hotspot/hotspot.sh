#!/bin/bash

case "$1" in
'start')
MODULE=$(basename $(readlink /sys/class/net/wlan0/device/driver/module))
ARCH=`/usr/bin/dpkg --print-architecture`

if [ $MODULE = "wlan_8192eu" -a $ARCH = "armhf" ] ; then
  echo "Launching Hostapd Edimax"
/usr/sbin/hostapd-edimax /etc/hostapd/hostapd-edimax.conf
elif [ $MODULE = "wlan_8192cu" -a $ARCH = "armhf" ] ; then
  echo "Launching Hostapd Edimax"
/usr/sbin/hostapd-edimax /etc/hostapd/hostapd-edimax.conf
else
  echo "Launching Ordinary Hostapd"
/usr/sbin/hostapd /etc/hostapd/hostapd.conf
fi
;;
'stop')

echo "Killing Hostapd"
/usr/bin/sudo /usr/bin/killall hostapd

echo "Killing Dhcpd"
/usr/bin/sudo /usr/bin/killall dhcpd
;;
esac
