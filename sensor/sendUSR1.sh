#!/bin/bash

PS=$(ps -ef | sed -nE "s/pi\s+([0-9]+).*test_inc\.py$/\1/p")

#echo $PS

if [ -z "$PS" ] 
then
	echo "apple" > /dev/null
else
	kill -USR1 $PS
fi

