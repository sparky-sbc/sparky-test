

Allo Introducing new product USBridgeSig: 

USBridgeSig is with RaspberryPi CM3+ Lite Module. The CM3+ Compute Module contains the guts of a Raspberry Pi 3 Model B+ (the BCM2837 processor and 1GB RAM)

Interfaces : 3 x USB 2.0 Host ports, HDMI , 1 Gigabit Ethernet Port (AX88179)

MicroSD card for OS (8GB or above) , Power input - 5V/3A 


******************************************************

USBridgeSig having ASIX AX88179 Gigabit Etherenet Port. Asix Driver (version 1.4) need to update  for USB audio streaming applications.

Updated Files are ax88179_178a.c , ax88179_178a.h and copy to linux source tree for compilation.

./Linux/drivers/net/usb/ax88179_178a.c

./Linux/drivers/net/usb/ax88179_178a.h

Updated Driver Source available on below links. 


https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/UsbridgeSig/ax88179.tar


from linux :

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/UsbridgeSig/ax88179.tar



**************
updated version check using modinfo : run below command , result will be v0.1.4

modinfo ax88179_178a | grep version

version:        v0.1.4


info : Pull Request  submited on Raspberrypi Linux kernel repository

https://github.com/raspberrypi/linux/pull/2999


***************** WIFI Modules driver installation on Raspbian******

thanks to https://www.raspberrypi.org/forums/viewtopic.php?t=194859

ssh  or terminal login using OS credentials 

sudo wget http://3.230.113.73:9011/Allocom/USBridgeSig/install-wifi -O /usr/bin/install-wifi

sudo chmod +x /usr/bin/install-wifi

for help

sudo install-wifi -h

sudo install-wifi


****************install ASIX updated driver on Raspbian 4.19.50-v7+ onwards**************

ssh  or terminal login using OS credentials

cd /usr/src

sudo wget http://3.230.113.73:9011/Allocom/USBridgeSig/install.sh

sh install.sh



