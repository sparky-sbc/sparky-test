some of the dacs going to mute state  on os update/error states.

to unmute , do ssh login , run alsamixer command select the device , unmute using m , 00 for unmute , mm for mute state.


or execute below lines.

for x in `amixer controls  | grep layback` ; do amixer cset "${x}" on ; done

alsactl store


  
