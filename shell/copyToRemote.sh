#!/bin/bash


help(){
    echo "USAGE: $0 versionNum servertype"
    echo "servetype : test/patch"
}
if [ $# -lt 1 ]; then
    help
    exit 
fi
url="patch.xxxx.com"
servertype="patchserver"


if [ "$2" = "test" ]; then
   servertype="testserver"
   url="testpatch.xxxx.com"
else
   if [ "$2" != "patch" ]; then
	echo "wrong servertype !!!"
        help
	exit
   fi
fi


dirs=/data/httpServer/werewolf

version=$1

if [ ! -d "${dirs}/${1}" ]; then 
    echo "${dirs}/${1}"
    echo "version not find!!!!!"
    exit 
fi


echo "start copy to ${servertype}"

scp -r ${dirs}/${1} ${servertype}:${dirs}

echo "copy end"
echo "start change update.json"

ssh ${servertype} "cd /data/httpServer/ ;echo '{\"update_url\": \"http://${url}/werewolf/${version}\", \"code_url\": \"http://${url}/werewolf/${version}/game_code_${version}.zip\"}' > werewolf_update.json"

echo "change end "


