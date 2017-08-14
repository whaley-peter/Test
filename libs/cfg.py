#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/7'
from launchManagerment import getProjectRootPath
apppath = getProjectRootPath()+ r"\app\WhaleyVR.apk"

desired_caps = {
    'platformName':'Android',
    'platformVersion' : '6.0',
    'deviceName' :'test',
    'udid':'6221231716B0904714',
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


remote_server = 'http://localhost:4723/wd/hub'

username = '18616512272'
password = 'a123456'
