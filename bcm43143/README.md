this driver buid for testing RPI official Wi-FI module on sparky 3.10.38 kernel ( not tested)

steps
*********
ssh login to sparky 

cd /usr/src/

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/bcm43143/brcm_wlan.tar

tar -xvf brcm_wlan.tar

cd brcm_wlan

./install.sh


