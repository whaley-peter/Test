#!/usr/bin/env python
# -*- coding: utf-8 -*-
import adb_helper
import sys
import platform
import socket

reload(sys)
sys.setdefaultencoding('utf-8')

__mtime__ = '2017/8/21'

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
    if udid == 'ea08a98e':
        devicename = 'MI5'
    elif udid == '8d5cd6c0':
        devicename = 'vivo_x9i'
    elif udid == '6221231716B0904714':
        devicename = '360'
    elif udid == '5e321b32':
        devicename = 'SamsungGalaxy7'
    elif udid == 'VGYP7T6P99999999':
        devicename = 'oppo_r9tm'
    elif udid == 'GWY0217115007494':
        devicename = 'HUAWEI_Meta9'
    else:
        devicename = 'noknowdevice'
    return devicename

def get_ip():
    iplist = socket.gethostbyname_ex(socket.gethostname())
    ip = iplist[2][0]
    # ip = '127.0.0.1'
    return ip


if __name__ == '__main__':
    b = get_devices()
    print b
    print platform.system()
