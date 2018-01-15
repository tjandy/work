#!/bin/sh


export JAVA_HOME=/data/soft/jdk1.8.0_111
export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin

JVM_ARGS=" -Xmx3000m -Xms3000m -verbose:gc -Xloggc:logs/gc.log -XX:CMSInitiatingOccupancyFraction=80 -XX:+UseCMSCompactAtFullCollection -XX:MaxTenuringThreshold=10 -XX:MaxPermSize=512M -XX:SurvivorRatio=3 -XX:NewRatio=2 -XX:+PrintGCDateStamps -XX:+PrintGCDetails -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -Dfile.encoding=utf-8 "

GAME_PATH=/data/gameServer
GAMELIB_PATH=$GAME_PATH/lib

pid=`ps axu|grep java|grep -v grep|awk '{print $2}'`  
dat=`date '+%Y-%m-%d %H:%M:%S'` 

echo $dat
echo $pid

if [ -n "$pid" ];  then
	echo ====shutdown====
	kill -9 $pid
	sleep 1
fi

echo ====start====

cd $GAME_PATH

echo `pwd`

echo $JVM_ARGS

java $JVM_ARGS -Djava.ext.dirs=.:./lib -cp wolf-1.0.jar com.happyslime.wolf.Start &

	
sleep 5
	
newpid=`ps axu|grep java|grep -v grep|awk '{print $2}'`

echo ==== new_pid:$newpid ====


