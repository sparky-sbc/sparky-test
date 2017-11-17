this drivers for sparky generic dac support.

pc5102a cadec and dac support.

cd /usr/src/

root@volumio-sparky:/usr/src#wget https://raw.githubusercontent.com/sparky-sbc/sparky-test/master/sparky-gen-dac/allo-hifi-dac.tar

root@volumio-sparky:/usr/src#tar -xvf allo-hifi-dac.tar

root@volumio-sparky:/usr/src#sh install.sh

***********************************

example:

cat /etc/modules

# /etc/modules: kernel modules to load at boot time.
# at boot time, one per line. Lines beginning with "#" are ignored.

snd-soc-pcm5102a

snd-soc-allo-hifi-dac

********************************************************
aplay -l

card 1: HifiDAC [HifiDAC], device 0: HifiDAC pcm5102a-hifi-0 []

  Subdevices: 1/1

  Subdevice #0: subdevice #0

