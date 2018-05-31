using sparky_gpio command  out 0 or 1 to any selected gpio pin on sparky 40 pin connector.

refer https://github.com/sparkysbc/sparky_linux_images/blob/master/GPIO_Details_sparky.pdf


ssh login

cd /usr/src

wget https://github.com/sparky-sbc/sparky-test/blob/master/sparky_gpio/sparky_gpio

chmod +x sparky_gpio

cp sparky_gpio /usr/sbin


usage :

please enter sparky_gpio <gpio number> <direction out or in > <value 0 or 1 >
