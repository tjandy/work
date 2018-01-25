安装说明：

1、安装python2.7环境

2、通过pip安装flask

3、启动监控脚本 
   nohup sh getUserOnline.sh &

4、启动flask
   nohup python2.7 index.py &


注意：

1、目前查询是根据进程名，所以暂不支持多个同名进程的信息查询
如果需要修改进程名，可以看index.py

2、templates\mon.html 中可改页面刷新时间

3、getUserOnline.sh 中可改监控信息获取频率

4、暂不支持跨天