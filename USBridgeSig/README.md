

Allo Introducing new product USBridgeSig: 

USBridgeSig is with RaspberryPi CM3+ Lite Module. The CM3+ Compute Module contains the guts of a Raspberry Pi 3 Model B+ (the BCM2837 processor and 1GB RAM)

Interfaces : 3 x USB 2.0 Host ports, HDMI , 1 Gigabit Ethernet Port (AX88179)

MicroSD card for OS (8GB or above) , Power input - 5V/3A 


******************************************************

USBridgeSig having ASIX AX88179 Gigabit Etherenet Port. Asix Driver need to update  for USB audio streaming applications.

Updated Files are ax88179_178a.c , ax88179_178a.h and copy to linux source tree for compilation.

./Linux/drivers/net/usb/ax88179_178a.c

./Linux/drivers/net/usb/ax88179_178a.h

Updated Driver Source available on below links. 


https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/USBridgeSig/ax88179.tar


from linux :

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/USBridgeSig/ax88179.tar
