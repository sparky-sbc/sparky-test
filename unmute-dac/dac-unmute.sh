#!/bin/sh
for x in `amixer controls  | grep layback` ; do amixer cset "${x}" on ; done
sudo alsactl store
exit 0

