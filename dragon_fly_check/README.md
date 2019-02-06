this files for checking dragonfly usb dac with sparky USBridge 17_nov_17

usb_audio_sparky.tar  - included dragonfly patch.

*******************************************

-updated on 30-nov 2017

uImage  changes

1) updated with aotg.aotg1_speed=1 parameter to change usb 1.1 , 0 for high speed. This only for connecting USB 1.1 audio dac with USBridge.

2) updated with aotg.urb_fix=1  , default value 0 fir testing up to pcm 32/192k files , 1 for test DSD files DSD256 continous mode to avoid dac disconnection on HQplayer.

these 2 parameters can be appended to the end of /boot/uenv.txt  (/Dietpi/uEnv.txt for dietpi , volumio /boot/uenv.txt)

all SBC drivers updated - 3.10.38.bz2 - added Sabaj Da2, Da3 DSD support  - 1 dec 2017

sound/usb/snd-usb-audio.ko, sound/usb/snd-usbmidi-lib.ko updated dsd native for Matrix Audio X-SPDIF 2 -11 Dec 2017

usb drivers updated same as in dsd-marantz folder.
************************************************************

11 dec update -  based on feedback

20 & 22 dec update - based on feedback regarding bootup hanging with dragon fly , taken care this , with urb_fix=1 setting also work now.

*****************



