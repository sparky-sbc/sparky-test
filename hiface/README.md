This is for testing hiface dacs on sparky. dtd 27092017
this build on 3.10.38 kernel.

on volumio Image:
ssh login with volumio
volumio@volumio:~$ su
Password:
root@volumio:/home/volumio# cd /usr/src/
root@volumio:/usr/src# wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/hiface/hiface.tar
root@volumio:/usr/src# ls
hiface.tar
root@volumio:/usr/src# tar -xvf hiface.tar
install.sh
snd-usb-hiface.ko
root@volumio:/usr/src# ls
hiface.tar  install.sh  snd-usb-hiface.ko
root@volumio:/usr/src# sh install.sh
root@volumio:/usr/src# lsmod
Module                  Size  Used by
snd_usb_hiface          8678  0
.........................................

