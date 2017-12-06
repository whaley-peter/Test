#!/usr/bin/env python
# -*- coding: utf-8 -*-
import adb_helper
import sys
import platform
import socket
import subprocess
reload(sys)
sys.setdefaultencoding('utf-8')

__mtime__ = '2017/8/21'

def connectDevice():
    try:
        deviveinfo = subprocess.check_output("adb devices").split("\r\n")
        if deviveinfo[1]=='':
            return False
        else:
            return True
    except Exception,e:
        print "Device Connect Fail: ",e

def get_devices():
    ADB = adb_helper.AdbHelper()
    devices = []
    output = ADB.getConnectDevices()
    for line in output:
        if line['state'] in ['device','device\r']:
            dev=line['uuid']
            devices.append(dev)
    devices.reverse()
    return devices

def get_devicename(udid):
    try:
        if connectDevice():
            dict = {}
            devicesInfo = subprocess.check_output('adb devices -l').split('\r\n')[1:-2]

            for deviceInfo in devicesInfo:
                deviceId = deviceInfo.split('device product')[0].rstrip()
                deviceName = deviceInfo.split('model:')[1].split(' ')[0]
                dict[deviceId]=deviceName

            if udid in dict.keys():
                Name =  dict[udid]
                return Name
            else:
                print "can't find the device by given udid, please check"
        else:
            print "No device is connectted"
    except Exception,e:
        print "Get Android version:",e

def get_ip():
    iplist = socket.gethostbyname_ex(socket.gethostname())
    ip = iplist[2][0]
    # ip = '127.0.0.1'
    return ip


if __name__ == '__main__':
    b = get_devicename("VGYP7T6P99999999")
    print b
