#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from robot.api import logger
from appium import webdriver
from time import sleep
import os
import threading
import multiprocessing

__mtime__ = '2017/8/7'


def getProjectRootPath():
    """get rootpath of project
    """
    rootpath = os.getcwd().split('\libs')[0]
    return rootpath

def getDeviceList():
    p = subprocess.Popen("adb devices", stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
    outter,err = p.communicate()
    devicesIds = []
    outter =  outter.split("\r\n")[1:]
    for one in outter:
        if one:
            one = one.split('\tdevice')[0]
            devicesIds.append(one)
    p.wait()
    return devicesIds

def getCapabilities():
    devicelist = getDeviceList()
    apppath = getProjectRootPath() + r"\app\WhaleyVR.apk"
    port = 4721
    bootstrapport = 4722
    dict = {}
    for one in range(len(devicelist)):
        udid = devicelist[one]
        port += 2
        bootstrapport = bootstrapport + 2
        if udid == 'ea08a98e':
            devicename = 'MI5'
        elif udid == '8d5cd6c0':
            devicename = 'vivo_x9i'
        elif udid == '6221231716B0904714':
            devicename =  '360'
        elif udid == '5e321b32':
            devicename = 'SamsungGalaxy7'
        elif udid == 'VGYP7T6P99999999':
            devicename = 'oppo_r9tm'
        elif udid == 'GWY0217115007494':
            devicename = 'HUAWEI_Meta9'
        else:
            devicename = 'noknowdevice'
        try:
            desired_caps = {
                'platformName':'Android',
                'deviceName' :devicename,
                'app' : apppath,
                'appPackage' : 'com.snailvr.manager',
                'appActivity' : 'com.whaley.vr.module.launcher.activitys.SplashActivity',
                'unicodeKeyborad' : True,
                'resetKeyborad' : True,
                'noRest' : True,
                'commandTimeout': 60,
                'autoGrantPermissions':True,
                'sessonOverride': True
            }
        except UnboundLocalError:
            print   'devicename not found'
        remote_server = 'http://127.0.0.1:%s/wd/hub' % port
        if udid not in dict:
            dict[udid] = {'remote_server':remote_server,'desired_caps':desired_caps,'port':port,'bootstrapport':bootstrapport,'udid':udid,'deviceName':devicename}
        else:
            dict[udid].append({'remote_server':remote_server,'desired_caps':desired_caps,'port':port,'bootstrapport':bootstrapport,'udid':udid,'deviceName':devicename})
    return dict

def start_servers(port,bootstrapport,udid):
    cmd = r'node C:\Users\admin\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\build\lib\main.js -a 127.0.0.1 -p %s -bp %s -U %s --session-override'%(port,bootstrapport,udid)
    subprocess.Popen(cmd,shell=True)

def kill_node():
    port = 4723
    for one in range(len(getDeviceList())):
        cmd = 'netstat -ano|findstr "%s"'%port
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out,err=p.communicate()
        if out:
            out = out.split('\r\n')[0].split(' ')[-1]
            kill = 'taskkill /pid %s /F'%out
            subprocess.Popen(kill,shell=True)
        port += 2
        continue

def install_alert(udid):
    """create function using for dealing with alert during install the app
    """
    watcherpath = getProjectRootPath() + r"\libs\UIWatcher.jar"
    cmd1 = "adb -s %s push "%udid + watcherpath + " data/local/tmp"
    push = subprocess.Popen(cmd1,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    cmd2 = "adb -s %s shell uiautomator runtest UIWatcher.jar -c com.whaleytest.UiWatchers"%udid
    run = subprocess.Popen(cmd2,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outter, err = push.communicate()
    outter1, err1 = run.communicate()
    # logger.console(outter)
    print outter1
    sleep(5)
    # logger.console(outter1)

def multi_servers_start():
    dict = getCapabilities()
    for one in dict:
        port = dict[one]['port']
        bootstrapport = dict[one]['bootstrapport']
        udid = dict[one]['udid']
        thread = threading.Thread(target=start_servers(port,bootstrapport,udid))
        thread.start()
