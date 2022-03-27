#!/bin/bash

PS=$(ps -ef | sed -nE "s/pi\s+([0-9]+).*python3\sread_sensor\.py$/\1/p")

if [ -z "$PS" ] 
then
	echo "apple" > /dev/null
else
	VOL=$(kill -USR1 $PS)
	echo $VOL
fi

