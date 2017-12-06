#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import socket
import get_info
import os

#检查appium 服务是否开启
def check_appium(ip,port):
    flag = 1
    checktime = 0
    while(flag and checktime < 10):
        try:
            r = requests.get(url='http://{0}:{1}/favicon.ico'.format(ip,port))
            if r.status_code == 200:
                print  'the appium reponse code is {0}'.format(r.status_code)
                flag=0
                return 1
            else:
                checktime += 1
                print 'the appium reponse code is {0}'.format(r.status_code)
                print 'the reponse code is not 200, ti would be somthing wrong,please check if , time:{0}'.format(checktime)
                time.sleep(3)
        except:
            checktime += 1
            print "appium server is not start by {0}:{1},try to check again now ,time:{2}".format(ip,port, checktime)
            time.sleep(3)
    if checktime == 10:
        return 0

#检查appium服务是否在运行中
def check_running(ip,port):
    try:
        r = requests.get(url='http://{0}:{1}/favicon.ico'.format(ip,port))
        if r.status_code == 200 or r.status_code == 304:
            return 1
        else:
            print "the appium respone code is {0}".format(r.status_code)
            return 0
    except:
        return 0

#检查当前端口是否已经连接
def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        return True
    except:
        return False

#如果端口被占用，则杀掉进程
def kill_port(port):
    ip = get_info.get_ip()
    if IsOpen(ip,port) == True:
        cmd = "netstat -ano|findstr {0}:{1}".format(ip, port)
        plist = os.popen(cmd).readlines()
        plisttmp = plist[0].split(" ")
        # print plisttmp
        plists = plisttmp[-1].split("\n")
        # print plists[0]
        try:
            if check_running(ip, port) == 0:
                os.popen("taskkill /pid {0} -t -f".format(plists[0]))
                print "kill proess:{0} succuess which is used port:{1}".format(plists[0], port)
                return 1
            else:
                print "the appium server by port:{0} still running,skip".format(port)
                return 0
        except:
            print "kill proess fail"
            return 0
    else:
        if port > 5000:
            print "bootstrap port:{0} was not use".format(port)
        else:
            print "appium port:{0} was not use".format(port)
        return 1

if __name__ == "__main__":
    # check_appium('127.0.0.1','4723')
    ip = get_info.get_ip()
    print check_running(ip,'4723')