#!/bin/bash

#PS=$(ps -ef | sed -nE "s/pi\s+([0-9]+).*python3\stest_inc\.py$/\1/p")
PS=$(ps -ef | sed -nE "s/pi\s+([0-9]+).*python3\stest_wrk\.py$/\1/p")

#echo $PS

if [ -z "$PS" ] 
then
	echo "apple" > /dev/null
else
	VOL=$(kill -USR1 $PS)
	echo $VOL
fi

