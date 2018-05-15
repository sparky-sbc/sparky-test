shairport binary file with version number on sparky USBridge

v159 uses - 3.1.3 vesrion

v6.3 uses 3.1.7 version.

dietpi latest versions observed shairport disconnection with 3.1.7 version , so replace with 3.1.3 version for testing - dtd 15 may 2018 


 
steps:

ssh login and follow below steps.

root@DietPi:/usr/src# dietpi-services stop

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dietpi-shairport-v/3.1.3/shairport-sync -O /usr/local/bin/shairport-sync

or for 3.1.7

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dietpi-shairport-v/3.1.7/shairport-sync -O /usr/local/bin/shairport-sync

root@DietPi:/usr/src# chmod 755 /usr/local/bin/shairport-sync

root@DietPi:/usr/src# dietpi-services start

*******************************************************************************************

