#!/bin/bash

for i in `ps aux|grep robot.py|awk '{print $2}'`  
do  
      kill -9  $i
done  
