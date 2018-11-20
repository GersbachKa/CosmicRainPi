#!/bin/bash
#Must edit to run on startup: add "sudo /boot/blinkingIP.sh &" to /etc/rc.local


echo none > /sys/class/leds/led0/trigger #Allow the use of the LED
on="echo 1 > /sys/class/leds/led0/brightness"
off="echo 0 > /sys/class/leds/led0/brightness"

function separate {
    string=$1
    separator="."

    tmp=${string//"$separator"/$'\2'}
    IFS=$'\2' read -a arr <<< "$tmp"
    for substr in "${arr[@]}" ; do
        bignumber $substr
        sleep 3
    done
}
function bignumber {
    s=$1
    for ((i=0; i<${#s}; i++)) ; do
        blink ${s:i:1}
        sleep 2
    done
}
function blink {
    n=$1
    if (( $n == 0 ))
    then
        blinklong
    else
        for ((j=$n; j>0; j--)) ; do
            eval "$on"
            sleep .2
            eval "$off"
	    sleep .2
        done
    fi
}
function blinklong {
    eval "$on"
    sleep 1
    eval "$off"
    sleep .2
}

sleep 1
eval "$on"
sleep 10
eval "$off"
sleep 5

ipI=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1') #Get the IP address
separate $ipI

sleep 2

echo mmc0 >/sys/class/leds/led0/trigger #Removes the use of the LED
