import json
from flask import Flask,request,render_template
import os
import time
app = Flask(__name__)

def getTime(timestr):
    process = os.popen('cat data/'+timestr+'.log|grep date |awk \'{print $2}\'|sed \'s/$/,/g\'|awk \'{printf("%s",$0);}\'')
    data  = process.read()
    process.close()
    return data

def getServerMem(timestr,name):
    process = os.popen('cat data/'+timestr+'.log|grep '+name+' |awk \'{print $3}\'|sed \'s/$/,/g\'|awk \'{printf("%s",$0);}\'')
    data  = process.read()
    process.close()
    return data

def getServerCpu(timestr,name):
    process = os.popen('cat data/'+timestr+'.log|grep '+name+' |awk \'{print $2}\'|sed \'s/$/,/g\'|awk \'{printf("%s",$0);}\'')
    data  = process.read()
    process.close()
    return data

def getOnline(timestr):
    process = os.popen('tail -n7 data/'+timestr+'.log|grep online |awk \'{print $2}\'')
    data  = process.read()
    process.close()
    return data

@app.route('/info.do',methods=['GET'])
def GetInfo():

    timestr = time.strftime("%Y-%m-%d", time.localtime())
    tt  = getTime(timestr)
    cur = getOnline(timestr)
    name = ["mapserver","loginserver","baseserver","dbserver","connectserver"]
    mem=[]
    cpu=[]

    for index,value in enumerate(name):
        mem.append(getServerMem(timestr,value))
    
    for index,value in enumerate(name):
        cpu.append(getServerCpu(timestr,value))

    return render_template('mon.html',timedata=tt,online=cur,mapdata=mem[0],logindata=mem[1],basedata=mem[2],dbdata=mem[3],connectdata=mem[4],\
                                        mapdata_cpu=cpu[0],logindata_cpu=cpu[1],basedata_cpu=cpu[2],dbdata_cpu=cpu[3],connectdata_cpu=cpu[4])


app.run(host='0.0.0.0',port=8888,debug=True)