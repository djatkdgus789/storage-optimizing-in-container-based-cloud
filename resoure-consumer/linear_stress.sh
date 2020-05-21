#!/bin/bash

#for var in `seq 0 180 1800`;do 
#	time=1800-$var
#	curl --data "millicores=30&durationSec=$time" http://10.111.135.103:8080/ConsumeCPU
#	sleep 180
#done 




var=0
time=1800
while (( "${var}" <= 1800 )); do
    echo "${var}"

	curl --data "millicores=30&durationSec=$time" http://10.111.135.103:8080/ConsumeCPU
	sleep 180

	    (( var = "${var}" + 180 )) # 숫자와 변수의 연산은 (())가 필요합니다.
		(( time = 1800 - "${var}"))
		done
