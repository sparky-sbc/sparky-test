#!/bin/sh
for x in `amixer controls  | grep layback` ; do amixer cset "${x}" 100% ; done
sudo alsactl store
exit 0

