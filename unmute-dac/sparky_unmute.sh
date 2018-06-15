#!/bin/bash
for x in `amixer controls | grep layback`
do

    amixer cset "${x}" 100% &> /dev/null

done
alsactl store &> /dev/null
