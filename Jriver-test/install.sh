#!/bin/sh
wget -q "http://dist.jriver.com/mediacenter@jriver.com.gpg.key" -O- | sudo apt-key add -
sudo wget http://dist.jriver.com/latest/mediacenter/mediacenter23native.list -O /etc/apt/sources.list.d/mediacenter23.list
sudo apt-get update
sudo apt-get install mediacenter23
exit 0
