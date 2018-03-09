#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mutil_test import get_info
from mutil_test import manage_server
import sys
import time
import os
import subprocess
import multiprocessing


reload(sys)
sys.setdefaultencoding('utf-8')
#获取IP地址
ip=get_info.get_ip()

#获取用户输入参数
arglist=sys.argv

#run方法用于调用外部程序
def run(arg):
    # subprocess.Popen(str(arg), stdout=open(logpath,"w"), stderr=subprocess.PIPE, shell=True)
    subprocess.Popen(str(arg),shell=True)
    # os.system(str(arg))

if '-h' in arglist:
    outstr = '''
    how to use it
    -h  help
    -n the num of starting appium server
    -p server port
    -sp decond server port
    '''
    print outstr
    sys.exit(0)

# if "-n" in arglist:
#     num=arglist[arglist.index('-n')+1]
# else:
#     num=0

#如果用户有输入port参数，则采用用户输入的参数，如果没有则采用默认的端口4723
if "-p" in arglist:
    aport=int(arglist[arglist.index('-p')+1])
    iport=int(arglist[arglist.index('-p')+1])
else:
    aport=4723
    iport=14723

#如果用户有输入bpport参数，则采用用户输入的参数，如果没有则采用默认的端口5723
if "-sp" in arglist:
    bport=int(arglist[arglist.index('-sp')+1])
    wport=int(arglist[arglist.index('-sp')+1])
else:
    bport=5723
    wport=8101

#通过多进程，启动多个appium服务
def start_server():
    global aport
    global bport
    global wport
    global iport
    global ip
    global plat
    #获取连接的设备数
    devicelist = get_info.get_devices()
    lprocess = []
    if devicelist == []:
        print "NO Android Device Connect The PC!"
    else:
        #确定设备数，然后启动对应数量的appium服务
        for div in devicelist:
            #杀掉port以及bpport端口
            result = manage_server.kill_port(aport)
            manage_server.kill_port(bport)
            run_appium = 'appium -a {0} -p {1} -bp {2}'.format(ip,aport,bport)
            aport += 1
            bport += 1
            if result == 1:
                p = multiprocessing.Process(target=run, args=(run_appium,))
                #将线程保存到列表
                lprocess.append(p)
            else:
                print "the appium server still running,skip"

    return lprocess

if __name__ == '__main__':
    process = start_server()
    if process:
        #启动进程
        for p in process:
            p.daemon = True
            p.start()

    time.sleep(3)