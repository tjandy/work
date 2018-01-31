import json
from flask import Flask,request,render_template
import os
import time
app = Flask(__name__)

def getTime(timestr,interval):
    process = os.popen('cat data/'+timestr+'.log|grep date |awk \'{print $2}\'|sed \'s/$/,/g\'|awk \'{printf("%s",$0);}\'')
    data  = process.read()
    process.close()
    return data

def getServerMem(timestr,name,interval):
    process = os.popen('cat data/'+timestr+'.log|grep -w '+name+' |awk \'{print $3}\'|sed \'s/$/,/g\'|awk \'{printf("%s",$0);}\'')
    data  = process.read()
    process.close()
    return data

def getServerCpu(timestr,name,interval):
    process = os.popen('cat data/'+timestr+'.log|grep -w '+name+' |awk \'{print $2}\'|sed \'s/$/,/g\'|awk \'{printf("%s",$0);}\'')
    data  = process.read()
    process.close()
    return data

def getOnline(timestr):
    process = os.popen('tail -n7 data/'+timestr+'.log|grep online |awk \'{print $2}\'')
    data  = process.read()
    process.close()
    return data

def tojson(name,data):
    return {'name':name,'data':data}


@app.route('/info.do',methods=['GET'])
def GetInfo():
    curtime=time.localtime()

    timestr = time.strftime("%Y-%m-%d", curtime)

    interval = time.strftime("%H:%M",curtime)

    tt  = getTime(timestr,interval)
    cur = getOnline(timestr)
    name = ["mapserver","mapserver2","loginserver","baseserver","dbserver","connectserver"]
    mem=[]
    cpu=[]

    for index,value in enumerate(name):
        mem.append(getServerMem(timestr,value,interval))
    
    for value in name:
        cpu.append(getServerCpu(timestr,value,interval))
    
    memdata=[]
    for index,value in enumerate(name):
	memdata.append(tojson(value,mem[index]))
    cpudata=[]
    for index,value in enumerate(name):
        cpudata.append(tojson(value,cpu[index]))
    return render_template('mon.html',timedata=tt,online=cur,memdata=memdata,cpudata=cpudata)


@app.route('/cpu.do',methods=['GET'])
def GetCpuInfo():

    curtime=time.localtime()

    timestr = time.strftime("%Y-%m-%d", curtime)

    interval = time.strftime("%H:%M",curtime)

    tt  = getTime(timestr,interval)
    cur = getOnline(timestr)
    name = ["mapserver","mapserver2","loginserver","baseserver","dbserver","connectserver"]
    cpu=[]

    for value in name:
        cpu.append(getServerCpu(timestr,value,interval))

    cpudata=[]
    for index,value in enumerate(name):
        cpudata.append(tojson(value,cpu[index]))
    return render_template('mon.html',timedata=tt,online=cur,cpudata=cpudata)

@app.route('/mem.do',methods=['GET'])
def GetMemInfo():
    
    curtime=time.localtime()

    timestr = time.strftime("%Y-%m-%d", curtime)

    interval = time.strftime("%H:%M",curtime)

    tt  = getTime(timestr,interval)
    cur = getOnline(timestr)
    name = ["mapserver","mapserver2","loginserver","baseserver","dbserver","connectserver"]
    mem=[]

    for value in name:
        mem.append(getServerMem(timestr,value,interval))

    data=[]
    for index,value in enumerate(name):
        data.append(tojson(value,mem[index]))
    return render_template('mon.html',timedata=tt,online=cur,memdata=data)

app.run(host='0.0.0.0',port=8888,debug=True)
