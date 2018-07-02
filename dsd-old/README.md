This is for restore the previous version USBridge drivers

last update 14th may 18
*************************************
update procedure on dietpi/volumio

ssh root login

cd /usr/src

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/dsd-old/restore.sh 

sh restore.sh

sync

reboot




