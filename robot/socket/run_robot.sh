#!/bin/bash


if [ $# -lt 1 ]; then
    echo "error.. please input robot num"
    exit 1
fi

myvar=$1
rm -f message.log
rm -f run.pid


for i in `seq $myvar`  
do  
     nohup python robot.py > message.log 2>&1 & echo $! >> run.pid
     sleep 10
done  
