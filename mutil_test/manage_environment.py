#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from time import sleep
from robot.api import logger
from eles.globaleles import getProjectRootPath
import get_info
import shutil
import os
__mtime__ = '2017/9/18'


def logcat(udid=None, testcasename=None):
    kill_logcat(udid)
    devicename = get_info.get_devicename(udid)
    path = getProjectRootPath().split("\libs")[0]
    if udid == None:
        dir = "{0}/LogOutput/Temp".format(getProjectRootPath().split("\libs")[0])
    else:
        dir = "{0}/LogOutput/Temp_{1}".format(getProjectRootPath().split("\libs")[0], devicename)
    if os.path.isdir(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    try:
        if udid == None and testcasename == None:
            logcat = r'adb logcat "| grep com.snailvr.manager" >{0}/LogOutput/Temp/TestLog_%date:~0,4%%date:~5,2%%date:~8,2%0%time:~1,1%%time:~3,2%%time:~6,2%.txt'.format(
                path)
            subprocess.Popen(logcat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        elif udid != None and testcasename != None:
            logcat = 'adb -s {0} logcat "| grep com.snailvr.manager" >{1}/LogOutput/Temp_{2}/{2}_{3}_%date:~0,4%%date:~5,2%%date:~8,2%0%time:~1,1%%time:~3,2%%time:~6,2%.txt'.format(
                udid, path, devicename, testcasename)
            subprocess.Popen(logcat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    except Exception, e:
        print "exception:", e

def kill_logcat(udid=None):
    if udid == None:
        cmd = "adb shell ps |find " + r'"logcat"'
    else:
        cmd = "adb -s {0} shell ps |find ".format(udid) + r'"logcat"'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out,err = p.communicate()
    while out:
        lines = out.split("\r\n")
        for line in lines:
            if line:
                pid = line.split()[1]
                if udid == None:
                    kill = "adb shell kill " + pid
                else:
                    kill = "adb -s {0} shell kill ".format(udid) + pid
                os.system(kill)
        break

def kill_uiautomator(udid=None):
    """kill uiautomator after test
    for mutil test,you must put the udid Variables

    :param udid:
    :return:
    Example:
    | kill uiautomator |
    | kill uiautomator | ${udid} |
    """
    if udid == None:
        cmd = "adb shell ps |find " + r'"uiautomator"'
    else:
        cmd = "adb -s {0} shell ps |find ".format(udid) + r'"uiautomator"'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    if out:
        a = out.split(" ")[5]
        if udid == None:
            kill = "adb shell kill " + a
        else:
            kill = "adb -s {0} shell kill ".format(udid) + a
        killinfo = subprocess.Popen(kill, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        killout, killerr = killinfo.communicate()
        if killout:
            logger.console(killout)
        else:
            logger.console(killerr)

def install_alert(udid=None):
    watcherpath = getProjectRootPath() + r"\libs\UIWatcher.jar"
    if udid==None:
        cmd1 = "adb push " + watcherpath + " data/local/tmp"
        cmd2 = u"adb shell uiautomator runtest UIWatcher.jar -c com.whaleytest.UiWatchers"
    else:
        cmd1 = 'adb -s {0} push '.format(udid) + watcherpath + " data/local/tmp"
        cmd2 = u"adb -s {0} shell uiautomator runtest UIWatcher.jar -c com.whaleytest.UiWatchers".format(udid)

    push = subprocess.Popen(cmd1,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    run = subprocess.Popen(cmd2,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outter, err = push.communicate()
    outter1, err1 = run.communicate()
    logger.console(outter)
    logger.console(outter1)

if __name__ == "__main__":
    # kill_uiautomator("VGYP7T6P99999999")
    logcat()
    kill_logcat()