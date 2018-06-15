On RPI latest version Kernel observed connectios dromps with RTL8xxxU driver for RTL8192EU module.

dowload this module for 4.14.42 kernel

ssh login 

cd /usr/src/ 

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/rpi-41442-8192eu/8192eu.ko -O /lib/modules/4.14.42-v7+/kernel/drivers/net/wirless/8192eu.ko

depmod -a

modprobe 8192eu

configure Wi-Fi
