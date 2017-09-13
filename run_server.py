#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mutil_test import get_info
from mutil_test import manage_server
import sys
import time
import os
import subprocess
reload(sys)
sys.setdefaultencoding('utf-8')

ip=get_info.get_ip()
arglist=sys.argv

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

if "-p" in arglist:
    aport=int(arglist[arglist.index('-p')+1])
    iport=int(arglist[arglist.index('-p')+1])
else:
    aport=4723
    iport=14723

if "-sp" in arglist:
    bport=int(arglist[arglist.index('-sp')+1])
    wport=int(arglist[arglist.index('-sp')+1])
else:
    bport=5723
    wport=8101


def start_server():
    global aport
    global bport
    global wport
    global iport
    global ip
    global plat

    result = manage_server.kill_port(aport)
    manage_server.kill_port(bport)
    currentpath = sys.path[0]

    run_appium = 'appium -a {0} -p {1} -bp {2}'.format(ip,aport,bport)
    aport += 1
    bport += 1
    if result == 1:
        # os.system(run_appium)
        subprocess.Popen(run_appium, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        print "error:================"
    else:
        pass

devicelist = get_info.get_devices()

if devicelist==[]:
     print "NO Android Device Connect The PC!"

else:
    for div in devicelist:
        start_server()

time.sleep(3)