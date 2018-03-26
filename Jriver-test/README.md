This steps for installing JRiver manually on sparky

on dietpi OS do ssh login , configure Mate or LXDE desktop, Auto login on Desktop , Install Media Center

wget -q "http://dist.jriver.com/mediacenter@jriver.com.gpg.key" -O- | sudo apt-key add -

sudo wget http://dist.jriver.com/latest/mediacenter/mediacenter23native.list -O /etc/apt/sources.list.d/mediacenter23.list

sudo apt-get update

sudo apt-get install mediacenter23



or

cd /usr/src/

wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/Jriver-test/install.sh

sh install.sh



