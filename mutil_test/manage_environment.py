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



if __name__ == "__main__":
    kill_uiautomator("VGYP7T6P99999999")
