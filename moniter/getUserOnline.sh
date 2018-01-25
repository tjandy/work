#!/bin/bash  
  


tofile(){

	echo $1 >> data/$DATE.log
}


getinfo(){

	pid=`ps aux|grep $1|grep -v grep|awk '{print $2}'`
	
	mem=`cat /proc/$pid/status | grep VmRSS | cut -d ':' -f 2|sed 's/[ \t]//g'|sed 's/kB//g'`
	
	cpu=`top -b -n 1 -p $pid  2>&1 | awk -v pid=$pid '{if ($1 == pid)print $9}'`
	 
	tofile "$1	$cpu	$mem"	
}

while true
do

DATE=`date -d today '+%Y-%m-%d'`
TIME="\"`date -d today '+%H:%M'`\""


str=`(sleep 1;echo getStatus;sleep 1; echo quit;sleep 1) | telnet   127.0.0.1 8659 `
online=`echo ${str} |grep  "200 OK" |cut -d ',' -f4| cut -d ' ' -f 1 `

tofile "date	$TIME"
tofile "online	$online"
getinfo mapserver
getinfo loginserver
getinfo baseserver
getinfo dbserver
getinfo connectserver

sleep 1m

done
