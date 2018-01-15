#!/bin/bash


help(){
    echo "USAGE: $0 date"
    echo "ex: $0 2017-12-01"
    echo "date: today yesterday"
}
if [ $# -lt 1 ]; then
    help
    exit 
fi

datestr=""

if [ "$1" = "today" ]; then
   datestr=""
else
   if [ "$1" = "yesterday" ]; then
	str=`date -d yesterday "+%Y-%m-%d"`
	datestr=".$str"
   else
	datestr=".$1"
   fi
fi


servertype="cbserver"


dirs=/data/bak/gameServer/logs

echo $datestr


daycount=`ssh ${servertype} "cd ${dirs};cat  gamedata.log$datestr|grep "\"leave_main\"" |cut -d '\"' -f 20| sort -u | wc -l;"`

gameuser=`ssh ${servertype} "cd ${dirs};cat  gamedata.log$datestr|grep "\"end_game\"" | cut -d '\"' -f 20| sort -u |wc -l "`

gamecount=`ssh ${servertype} "cd ${dirs};cat  gamedata.log$datestr|grep "\"end_game\"" | wc -l "`

let gcount=$gamecount/6

echo "dayNum:$daycount"
echo "gameuser:$gameuser"
echo "gamecount:$gcount"

