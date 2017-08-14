#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pexpect,sys,os.path,subprocess
from robot.api import logger
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
    rootpath = getProjectRootPath()
    with open(rootpath,"w") as f:
        outter = outter.decode('cp936').decode('utf-8')
        outter =  outter.split("\r\n")[1:]
        for one in outter:
            if one:
                one = one.split('\tdevice')[0]
                f.write(one + ',')
                devicesIds.append(one)
    p.wait()
    return devicesIds






